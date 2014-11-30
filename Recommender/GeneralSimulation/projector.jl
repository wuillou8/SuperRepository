#============================================
        PROJECTORS
============================================#

type recPLW
    rec::Dict{String,Float64}
end

type recLWTL
    rec::Dict{String,Float64}
end


initReceiver( obj::DetectPLW ) = convert(Dict{String,Float64}, { k => 0. for k in keys(obj.access)})
initReceiver( obj::DetectLWTL ) = convert(Dict{String,Float64}, { k => 0. for k in keys(obj.access)})

reduce_(rec::Dict{String,Float64}, threshold::Float64) = 
                    { i => rec[i] for i in filter( x-> rec[x] >= threshold ,keys(rec)) }
reduce_( rec::Dict{String,Float64}, NbMax::Int64 ) = 
        map(x -> x[2], sort([ (rec[k],k) for k in keys(rec) ], rev=true)[1:min(end,NbMax)])
reduce_( rec::Dict{Any,Any}, NbMax::Int64 ) = 
                    map(x -> x[2], sort([ (rec[k],k) for k in keys(rec) ], rev=true)[1:min(end,NbMax)])
reduce_(rec::Dict{String,Float64}, threshold::Float64, NbMax::Int64 ) = reduce_( reduce_(rec, threshold), NbMax )


# PROJECTORs
function ProjDomain(profi::ProfilePLW, threshold::Float64, thresholdNumb::Int64 = 20)
    rec = recPLW(initReceiver( SectorPLW ))
    for k in keys(profi.coords)
        ProjPath(rec, k)
    end
    reduce_(rec.rec,threshold, thresholdNumb)
    #rec.rec = reduce_(rec.rec,threshold)
    #reduce_(rec.rec,thresholdNumb)
end

function ProjDomain(profi::ProfileLWTL, threshold::Float64, thresholdNumb::Int64 = 20)
    rec = recLWTL(initReceiver( SectorLWTL ))
    for k in keys(profi.coords)
        ProjPath(rec, k)
    end
    reduce_(rec.rec,threshold, thresholdNumb)
    #rec.rec = reduce_(rec.rec,threshold)
    #reduce_(rec.rec,thresholdNumb)
end

# function normalising the projection within a sector
# cut off in summed up. Thershold based on similarity or Nb of elements
function Profilefilter(profi::ProfilePLW, simthres::Float64 = -.1, thresholdNb::Int64 = 20) 
    dom = ProjDomain(profi, simthres, thresholdNb )
    clls =  userCell[]
    n =  0

    for k in dom
        cell = SectorPLW.cellsk[k]
        push!(clls, userCell(cell.key,cell.weight,cell.path,cell.BT) )
        n += 1
    end

    cells =  { i => clls[i] for i = 1:thresholdNb }
    coords  = { clls[i].key::String => i for i =1:n }
    profi.cells = cells
    profi.coords = coords
    profi
end

# function normalising the projection within a sector
# cut off in summed up. Thershold based on similarity or Nb of elements
function Profilefilter(profi::ProfileLWTL, simthres::Float64 = -.1, thresholdNb::Int64 = 20) 
    dom = ProjDomain(profi, simthres, thresholdNb )
    clls =  userCell[]
    n =  0

    for k in dom
        cell = SectorLWTL.cellsk[k]
        push!( clls, userCell(cell.key,cell.weight,cell.path,cell.BT) )
        n += 1
    end

    cells =  { i => clls[i] for i = 1:thresholdNb }
    coords  = { clls[i].key::String => i for i =1:n }
    profi.cells = cells
    profi.coords = coords
    profi
end

#PROJECTORs across domains
function ProjDomainLWTLtoPLW(profi::ProfileLWTL, threshold::Float64, N::Int64)
    rec = recPLW(initReceiver( SectorPLW ))
    for k in keys(profi.coords)
        ProjPathLWTLtoPLW(rec, k)
    end
    tmp = reduce_(rec.rec,threshold, N)
    ProfilePLW(profi.domain,tmp) 
end

#PROJECTORs across domains
function ProjDomainPLWtoLWTL(profi::ProfilePLW, threshold::Float64, N::Int64)
    rec = recLWTL(initReceiver( SectorLWTL ))
    for k in keys(profi.coords)
        ProjPathPLWtoLWTL(rec, k)
    end
    tmp = reduce_(rec.rec,threshold, N)
    ProfileLWTL(profi.domain,tmp) 
end

#ProjPaths
function ProjPath(rec::recPLW, piv::String)
    pivotpath = getpath(SectorPLW,piv)
    for k in keys(rec.rec)
        path2 = getpath(SectorPLW,k)
        sim = similarityTFIDF(dictPATHS,pivotpath,path2)
        rec.rec[k] += sim
    end
end

function ProjPath(rec::recLWTL, piv::String)
    pivotpath = getpath(SectorLWTL,piv)
    for k in keys(rec.rec)
        path2 = getpath(SectorLWTL,k)
        sim = similarityTFIDF(dictPATHS,pivotpath,path2)
        rec.rec[k] += sim
    end
end

function ProjPathLWTLtoPLW(rec::recPLW, piv::String)
    pivotpath = getpath(SectorLWTL,piv)
    for k in keys(rec.rec)
        path = getpath(SectorPLW,k)
        sim = similarityTFIDF(dictPATHS,pivotpath,path)
        rec.rec[k] += sim
    end
end

function ProjPathPLWtoLWTL(rec::recLWTL, piv::String)
    pivotpath = getpath(SectorPLW,piv)
    for k in keys(rec.rec)
        path = getpath(SectorLWTL,k)
        sim = similarityTFIDF(dictPATHS,pivotpath,path)
        rec.rec[k] += sim
    end
end
