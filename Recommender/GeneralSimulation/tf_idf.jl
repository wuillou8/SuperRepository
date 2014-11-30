#=======================================
        Make tfidf Dict
=======================================#

function createPathsDict()
    # create dictionary over stemmed words/paths.
    _dict = Set{String}()
    for k in keys(SectorPLW.access)
        for i in getpath(SectorPLW,k)
            [ push!(_dict,tm) for tm in getpath(SectorPLW,k) ]
        end
    end
    for k in keys(SectorLWTL.access)
        for i in getpath(SectorLWTL,k)
            [ push!(_dict,tm) for tm in getpath(SectorLWTL,k) ]
        end
    end
    num = 0
    _dict = {i => num+=1 for i in _dict}
    convert(Dict{String,Int64},_dict)
end

function createKWRDSDDicts()
    num = 0
    dictPLW = { k => num =num+1  for k in keys(SectorPLW.access)}
    num = 0
    dictLWTL = { k => num =num+1  for k in keys(SectorLWTL.access)}
    dictPLW, dictLWTL  
end

function vectoriseTFIDF(_dict::Dict{String,Int64},_path::Array{String,1})
# create TF_IDF
    tfidfvec = zeros(_dict.count)
    for i in _path
        #println(dict[i])
        tfidfvec[_dict[i]] += 1
    end
    tfidfvec/norm(tfidfvec)
end

function similarityTFIDF(_dict::Dict{String,Int64},_path1::Array{String,1},_path2::Array{String,1})
    _v1 = vectoriseTFIDF(_dict,_path1)
    _v2 = vectoriseTFIDF(_dict,_path2)
    dot(_v1,_v2)
end

#approx... dont use it yet
function makeIDF(_dict::Dict{String,Int64}) #,feeds::Array{String,1})
    idfvec = zeros(_dict.count)
    N = 0
    for k in keys(SectorPLW.access)
    N+=1
    for i in getpathPLW(SectorPLW,k)
        [ (idfvec[dict[tm]] += 1) for tm in getpathPLW(SectorPLW,k) ]
    end
    end
    for k in keys(SectorLWTL.access)
    N+=1
    for i in getpathLWTL(SectorLWTL,k)
        [ (idfvec[dict[tm]] += 1) for tm in getpathLWTL(SectorLWTL,k) ]
    end
    end
    map(x->log(N/x),idfvec)
end


# similarity matrix between LWTL and PLW. The similarity is based on 
# the paths trough which content is simulated.
function createSimMatrix()
    matrTF_IDF = Array(Float64, SectorLWTL.access.count, SectorPLW.access.count)
    for nb1 = 1:SectorLWTL.access.count
        for nb2 = 1:SectorPLW.access.count
            path1 = getpath(SectorLWTL,nb1)
            path2 = getpath(SectorPLW,nb2)
            matrTF_IDF[nb1,nb2] = similarityTFIDF(dictPATHS,path1,path2)
        end
    end
    matrTF_IDF
end

# Similarity matrix between LWTL and PLW taxonomy nodes.
function correlation(kwLWTL::String,kwPLW::String)
    try
        matrTF_IDF[ SectorLWTL.access[kwLWTL], SectorPLW.access[kwPLW] ]
    catch error
        println("One of the keywords not detected in the taxonomy tree") 
    end
end
