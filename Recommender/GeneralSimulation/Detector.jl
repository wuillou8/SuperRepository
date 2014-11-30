
#=========================================
        Taxonomy "Cells" 
=========================================#

type jRecLWTL # basical record cell LAWTEL
    key::String
    weight::Float64 # depth in th tree
    path::Array{String,1}
    NT::Array{String,1} # narrower term or child sub-branches
    BT::Array{String,1}
    #=SC::Array{String,1}
    BT::Array{String,1}
    NT::Array{String,1}
    RT::Array{String,1}
    PT::Array{String,1}
    UF::Array{String,1}=#
    function jRecLWTL(key::String, path::Array{String,1}, depth::Int64, NT::Array{String,1}, BT::Array{String,1}) 
        weight::Float64 = 1.*depth
        new(key,weight,path,NT,BT)
    end
end

type jRecPLW # basical record cell Practical Law
    key::String
    weight::Float64
    path::Array{String,1}
    BT::Array{String,1}
        function jRecPLW(arg1::String, arg2::Array{String,1}, arg3::Int64, bt::Array{String,1})
        key::String = arg1
        path::Array{String,1} = arg2
        weight::Float64 = 1.*arg3
        BT = bt
    new(key,weight,path,BT)
    end
end

#======================================
    Detector
======================================#

type DetectLWTL
    cellsk::Dict{String,jRecLWTL}
    cells::Dict{Int64,jRecLWTL} # taxocell
    access::Dict{String,Int64}
end

type DetectPLW
    cellsk::Dict{String,jRecPLW}
    cells::Dict{Int64,jRecPLW}
    access::Dict{String,Int64}
end

type Detect
    secLWTL::DetectLWTL
    secPLW::DetectPLW
    function Detect(secLWTL::DetectLWTL,secPLW::DetectPLW)
        new(secLWTL,secPLW)
    end
end

#SectorLWTL = DetectLWTL(detectLWTL, coordsLWTL)
#SectorPLW = DetectPLW(detectPLW, coordsPLW)

getpath(obj::DetectLWTL,idx::Int64) =  obj.cells[idx].path
getpath(obj::DetectPLW,idx::Int64) = obj.cells[idx].path
getpath(obj::DetectLWTL,val::String) =  obj.cellsk[val].path
getpath(obj::DetectPLW,val::String) =  obj.cellsk[val].path
#getpath(obj::DetectLWTL,val::String) =  obj.cells[obj.access[val]].path
#getpath(obj::DetectPLW,val::String) = obj.cells[obj.access[val]].path

function getpath(obj::Detect,key::String)
    x = key[1:3]
    @switch x begin
    "LWT"; getpath(obj.secLWTL, key)
    "PLW"; getpath(obj.secPLW, key)
        println("Detect::getpath:: error, path not recognised"), exit(0)
    end
end


function getMainDomains(sector::DetectPLW)
    doms = String[]
    for i in 1:sector.access.count
        c = sector.cells[i]
        if (c.weight == 1.) & (sizeof(c.NT) > 0)
            push!(doms,c.key)
        end
    end
    doms
end

function getMainDomains(sector::DetectLWTL)
    doms = String[]
    for i in 1:sector.access.count
        c = sector.cells[i]
        if (c.weight == 1.) & (sizeof(c.NT) > 0)
            push!(doms,c.key)
        end
    end
    doms
end
