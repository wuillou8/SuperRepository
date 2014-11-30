# ƒunctionalities 
stopwds = readcsv("DATA/stopwords.csv")

cnt(str) = 1+sizeof(filter(x->x=='<',str))/2 


function getDicLWTL(idx::Int64, path = "DATA/taxorandalfullpaths.csv")
    l, N, quickarr = readcsv(path), 20401, String[]
    if idx == 8
        for i=2:N
            push!(quickarr,"LWTL "*l[i,idx])
        end
    elseif idx == 4
        for i=2:N
            push!(quickarr,[l[i,idx]])
        end  
    else
        for i=2:N
            push!(quickarr,l[i,idx])
        end
    end
    quickarr
end

function cleanfilt(val::String)
    @>> val begin # lazy package
        nltk.word_tokenize()
        filter(x->!(x in [",","''","``","{","}","'s","'",":","`","~","&","<",">"]))
        filter(x->!(x in stopwds))
        map(x-> pycall(snowball["stem"], PyAny, x))   
    end
end

function makeDicjRec(jrecs::Array{jRecLWTL,1},num::Int64 = 0)
# create dictionary for the Lawtel jRec
    N_LWTL=20400
    dictk::Dict{String,jRecLWTL} = { jrecs[i].key => jrecs[i] for i = 1:N_LWTL}    
    dict::Dict{Int64,jRecLWTL} = {i => jrecs[i] for i = 1:N_LWTL}
    num = 0
    dictcoords::Dict{String,Int64} = {rec.key::String => num+=1 for rec in jrecs}    
    return dictk, dict, dictcoords
end

function makeDicCorrRec(jrecs::Array{jRecLWTL,1},num::Int64 = 0)
# create dictionary for the Lawtel jRec
    N_LWTL=110
    dictk::Dict{String,jRecLWTL} = { jrecs[i].key => jrecs[i] for i = 1:N_LWTL}    
    dict::Dict{Int64,jRecLWTL} = {i => jrecs[i] for i = 1:N_LWTL}
    num = 0
    dictcoords::Dict{String,Int64} = {rec.key::String => num+=1 for rec in jrecs}    
    return dictk, dict, dictcoords
end

type jRecord
#= Local helper class, because working out Lawtel Taxo is a mess =#
    name::String
    SC::Array{String,1}
    BT::Array{String,1}
    NT::Array{String,1}
    RT::Array{String,1}
    PT::Array{String,1}
    UF::Array{String,1}
    path::Array{String,1}
    function jRecord(line)
        name = line[1]
        SC,BT,NT,RT,PT,UF = String[], String[], String[], String[], String[], String[]
        for x in filter(x->x!="" ,line[2:end])
            l = x[1:3]
            @switch l begin 
                "sc:"; push!(SC,x[4:end])   
                "bt:"; push!(BT,x[4:end])
                "nt:"; push!(NT,x[4:end])
                "rt:"; push!(RT,x[4:end])
                "pt:"; push!(PT,x[4:end])
                "uf:"; push!(UF,x[4:end])
                "we dont care"
            end
        end
        new(name,SC,BT,NT,RT,PT,UF,[]) 
    end
end

function readLWTLtoRecords(LWTLpath = "LAWTEL/taxasciitolower.csv", buildpath = "no") 
#=  read in LWTL
    the path building is done by brute force, generating all the paths and subpasses, 
    therefore taking a lot of time. =#
    
    #try
    listLTL = readcsv(LWTLpath, String)
    #catch e
    #    jp("readLWTLtoRecords::error reading LAWTEL file")
    #    exit(0)
    #end
    
    jrecords = jRecord[]
    lsSC, lsUF, lsBT = Set{String}(), Set{String}(), Set{String}()
    for i = 1:size(listLTL)[1]
        push!(jrecords,jRecord(listLTL[i,1:end]))
        [ push!(lsSC,tmp) for tmp in jrecords[i].SC ]
        [ push!(lsUF,tmp) for tmp in jrecords[i].UF ]
        [ push!(lsBT,tmp) for tmp in jrecords[i].BT ]
    end
   # paths generation
   buildpath == "yes" ?  buildtaxopaths(jrecords,lsSC) : "taxo path not built"
   jrecords
end

function MakeDetectLWTL() 
    # dirty way for now 
    N_LWTL=20400
    
    lstkeys = getDicLWTL(1)
    lstpaths = convert(Array{Array{String,1},1},map(x-> cleanfilt(x),getDicLWTL(8)))
    lstdepth = convert(Array{Int64,1},map(x-> cnt(x),getDicLWTL(8)))
    
    jrecsLWTL2 = readLWTLtoRecords()
    jrecsLWTL = jRecLWTL[]
    for i =1:N_LWTL
        push!(jrecsLWTL,jRecLWTL("LWTL "*lstkeys[i],lstpaths[i],lstdepth[i],jrecsLWTL2[i].NT, jrecsLWTL2[i].BT)) 
    end
    
    makeDicjRec(jrecsLWTL)
end


