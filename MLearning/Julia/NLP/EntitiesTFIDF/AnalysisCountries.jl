# packages and files
using DataArrays, RDatasets, DataFrames
using Requests
using PyPlot
using Lazy

# DataFramesMeta.jl is a functional package, helper for DataFrames operations. 
# packagecould be cloned, in that case the file was just
# taken from the internet and has to be in the same dir.
include("DataFramesMeta.jl")
using DataFramesMeta


# Initialises Stemmers, Lemmatizer, loading stopwords (they were taken from python nltk),
# as well as applying other cleaning operations.
using PyCall, Lazy
@pyimport nltk
@pyimport nltk.stem as nltk_stem

snowball = nltk_stem.SnowballStemmer("english")
wnl = nltk.WordNetLemmatizer()
stopwds = readcsv("DATA/stopwords.csv")

function chckifinstr(str, list) 
    for i in str
        if i in list
            return true
        end
    end
    false        
end  

# tokenize, remove stowords and clean strings (bag of words).
function myfilt(strings)
    @>> strings begin # lazy package
    nltk.word_tokenize()
    map(y->filter(x->x!='\'', y))
    filter(x->length(x)>1)
    filter(x->!(x in ["''"]))
    filter(x->!(x in stopwds))
    filter(x->!chckifinstr(x,
    [';',':','<','>','@','&','}','{',',','.','/','\\','+','-','=','(',')','?','[',']','*','!','^','$','#','|','~','`','�','Ϡ','_']))
    filter(x->!chckifinstr(x,['0','1','2','3','4','5','6','7','8','9']))
    map(x->pycall(wnl["lemmatize"], PyAny, x))
    end    
    
end

# Extract out lemmatized words
# runs for long minutes
function extractwords(df::DataFrame)
    N = size(df[:Custom2])[1]
    words = String[] 
    for i = 1:N 
        str = df[:Custom2][i]
        tr = myfilt(str)
        if length(tr) > 1
            [ push!(words, tmp) for tmp in tr ]
        end
    end  
    words
end

# TF-IDF methods
# two similarities methods are implemented. One that is basic vectorisation and another 
# using idf corrections. 
function vectTFIDF(_dict::Dict{String,Int64},_path::Array{String,1})
    tfidfvec = zeros(_dict.count)
    for i in _path
        tfidfvec[_dict[i]] += 1
    end
    tfidfvec/norm(tfidfvec)
end

function vectTFIDF(_dict::Dict{String,Int64},__idf::Dict{String,Float64},_path::Array{String,1})
    tfidfvec = zeros(_dict.count)
    for i in _path
        n = _dict[i]
        tfidfvec[n] += __idf[i]
    end
    tfidfvec/norm(tfidfvec)
end

function simTFIDF(_dict::Dict{String,Int64},_path1::Array{String,1},_path2::Array{String,1})
    _v1 = vectoriseTFIDF(_dict,_path1)
    _v2 = vectoriseTFIDF(_dict,_path2)
    dot(_v1,_v2)
end

function simTFIDF(_dict::Dict{String,Int64},__idf::Dict{String,Float64},
                                    _path1::Array{String,1},_path2::Array{String,1})
    _v1 = vectTFIDF(_dict,__idf,_path1)
    _v2 = vectTFIDF(_dict,__idf,_path2)
    dot(_v1,_v2)
end


#===================================
#	RUN
===================================#

# putting one file loaded from Bango. That is four days user activity. 
path = "DATA/Events_Report_363809_08_November_2014_10_53_35_519.csv"
df = DataFrames.readtable( path )


# Select countries: Threshold set to 5000 for the News read.
cntries = String[]
cntriesStat = Int64[]
for c in sort(unique(df[:Country]))
    tmp = @where(df, :Country .== c)
    n = size(tmp)[1]
    if n > 5000
        println(c, " ", n) #size(tmp)[1])
        push!(cntries,c)
        push!(cntriesStat,n)
    end
end

# extract words (Takes half an hour on the data above)
words = extractwords(df)

# create the word dictionary
Dic = countmap(words)
#create vectorised dictionary, with frequency and an idf vector
Ncntrs = length( unique(df[:Country]) )
idfvec = map(x->log(Ncntrs)/log(1+x),values(Dic))
m, n = 0, 0
idfDic = convert(Dict{String,Float64},{ k => idfvec[m=m+1] for k in keys(Dic) })
dic = convert(Dict{String,Int64}, { k => n=n+1 for k in keys(Dic) });

# preparation for similarity matrix construction
# takes approx twenty minutes to run.
wrdsvec = Array{String,1}[]
for c in cntries
    t1 =  time()
    dftmp = @where(df, :Country .== c)
    push!(wrdsvec, extractwords(dftmp))
    t2 = time()
    println(c, " ", t2 - t1)
end

# building up similarity matrix 
Ncntries = length(wrdsvec)
mat = zeros((Ncntries,Ncntries)) #Array{,2}
matidf = zeros((Ncountries,Ncountries)) 
for i = 1:Ncntries #length(cntries)
    for j = 1:i #length(cntries)
        mat[i,j] = simTFIDF(dic, wrdsvec[i], wrdsvec[j])
        println(cntries[i]," ",cntries[j]," ", simTFIDF(dic, wrdsvec[i], wrdsvec[j]))
        matidf[i,j] = simTFIDF(dic, idfDic, wrdsvec[i], wrdsvec[j])
        mat[j,i] = mat[i,j]
        matidf[j,i] = matidf[i,j]
    end
end

# apply classical multidimensional scaling: 
# http://multivariatestatsjl.readthedocs.org/en/latest/cmds.html
# http://en.wikipedia.org/wiki/Multidimensional_scaling
using MultivariateStats
D = gram2dmat(mat)
mds = classical_mds(D, 2)

D = gram2dmat(matidf)
mds_idf = classical_mds(D, 2)

#=======================
#	plotting
=======================#
# For great julia exampklpes with pyplot: https://gist.github.com/gizmaa/7214002

# PLot simple Vectorised, TF version:
lis = ["b*","go","r^","c<","m>","m*","bo","g^","r<","c>","c*","mo","b^","g<","r>","m8","ro","g>"]
plt.title("Reuters News: Countries with TF")
plt.xlabel("posX")
plt.ylabel("posY")

ax = axes()
ax[:set_xlim]([-0.3,1.5])
ax[:set_ylim]([-0.1,0.35])
for i = 1:Ncntries
    plt.plot(mds[1:end,i][1], mds[1:end,i][2], lis[i])
    plt.scatter(mds[1:end,i][1], mds[1:end,i][2], cntriesStat[i], alpha = 0.1)
end
lg = legend()
plt.legend(cntries) #,prop={"size":6})

# PLot TFIDF version:
lis = ["b*","go","r^","c<","m>","m*","bo","g^","r<","c>","c*","mo","b^","g<","r>","m8","ro","g>"]
plt.title("Reuters News: Countries with TFIDF")
plt.xlabel("posX")
plt.ylabel("posY")
ax = axes()
ax[:set_xlim]([0.75,1.05])
ax[:set_ylim]([-0.21,0.6])
for i = 1:Ncntries
    plt.plot(mds_idf[1:end,i][1], mds_idf[1:end,i][2], lis[i])
    plt.scatter(mds_idf[1:end,i][1], mds_idf[1:end,i][2], cntriesStat[i], alpha = 0.1)
end
plt.legend(cntries) #,prop={"size":6})
