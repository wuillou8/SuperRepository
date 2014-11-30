#============================================
        PRACTICAL LAW
============================================#

function readkeysPLW(PLWpath = "PRACTICAL_LAW/pl_taxonomy_no=,tolower.txt")
    listPL = readdlm(PLWpath,'\t')
    tmp = listPL[1,1]
    keyPLW = String[]
    btPLW = Array{String,1}[]
    for i in 1:size(listPL)[1]
        if listPL[i] == ""
            push!(keyPLW,"PLW "*tmp*" "*listPL[i,2])
            push!(btPLW,[tmp])
        else
            tmp = listPL[i,1]
            push!(keyPLW,"PLW "*listPL[i,1])
            push!(btPLW,[listPL[i,1]])
        end
    end
    keyPLW, btPLW
end

function readpathPLW(PLWpath = "PRACTICAL_LAW/pl_taxonomy_no=,tolower.txt")
    listPL = readdlm(PLWpath,'\t')
    tmp = listPL[1,1]
    ftreePL = Array{String,1}[]
    for i in 1:size(listPL)[1]
        if listPL[i] == ""
            push!(ftreePL,[listPL[i,2]," ",tmp])
        else
            tmp = listPL[i,1]
            push!(ftreePL,[listPL[i,1]," "])
        end
    end
    ftreePL
end

function readdepthPLW(PLWpath = "PRACTICAL_LAW/pl_taxonomy_no=,tolower.txt")
    listPL = readdlm(PLWpath,'\t')
    depthPL = Int64[]
    for i in 1:size(listPL)[1]
        listPL[i] == "" ? push!(depthPL,2) : push!(depthPL,1)
    end
    depthPL
end

function cleanstemtoken(dat::Array{Array{String,1},1})
    @>> dat begin
        map(y->mapreduce(x->x*" ",*,y))
        map(x->nltk.word_tokenize(x))
        map(y->filter(x->!(x in [",","''","``","{","}","'s","'",":","`","~","&","<",">"]),y))
        filter(x->nostopwrd(x,stopwds))
        map(y->map(x-> pycall(snowball["stem"], PyAny, x),y))
    end
end

function makeDicjRec(jrecs::Array{jRecPLW,1}, num::Int64 = 0)
# create dictionary for the Lawtel jRec
    N_PLW=438
    dictk::Dict{String,jRecPLW} = { jrecs[i].key => jrecs[i] for i = 1:N_PLW}
    dict::Dict{Int64,jRecPLW} = { i => jrecs[i] for i = 1:N_PLW}
    dictcoords::Dict{String,Int64} = { jrecs[i].key::String => i for i = 1:N_PLW}    
    return dictk, dict, dictcoords
end

#    make PLW DETECTOR
function MakeDetectPLW()
    N_PLW=438
    keysPLW, btPLW = readkeysPLW()
    pathsPLW = convert(Array{Array{String,1},1},cleanstemtoken(readpathPLW())) 
    depthPLW = readdepthPLW()

    jrecs = jRecPLW[]
    for i = 1:N_PLW
        push!(jrecs,jRecPLW(keysPLW[i],pathsPLW[i],depthPLW[i], btPLW[i]))
    end

    makeDicjRec(jrecs)
end
