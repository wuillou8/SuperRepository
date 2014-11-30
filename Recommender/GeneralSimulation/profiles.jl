#=====================================
       Profiles for Projections
=====================================#


type userCell
    key::String
    weight::Float64
    #coord::Int64
    path::Array{String,1}
    BT::Array{String,1}
end 

#SectorPLW
function spanDomainPLW(domain::String)
    cells, n::Int64 = userCell[], 0
    cell = SectorPLW.cells[SectorPLW.access[domain]]
    push!(cells, userCell(cell.key,cell.weight,cell.path,cell.BT))
    for i = 1:SectorPLW.cells.count
        cell::jRecPLW = SectorPLW.cells[i]
        if (domain[5:end] in cell.BT)
            push!(cells, userCell(cell.key,cell.weight,cell.path,cell.BT))
            n += 1
        end
    end
    cells, n
end

type ProfilePLW
    domain::String
    cells::Dict{Int64,userCell}
    coords::Dict{String,Int64}

    function ProfilePLW(domain::String)
        cellstmp, n = spanDomainPLW(domain)
        cells::Dict{Int64,userCell} =  { i => cellstmp[i] for i = 1:n }
        coords::Dict{String,Int64} = { cellstmp[i].key::String => i for i =1:n }
        new(domain,cells,coords)
    end

    function ProfilePLW(domain::String, strs::Array{ASCIIString,1})
        num::Int64 = mapreduce(1,+,strs)
        clls = userCell[]
        for i = 1:num
            cell = SectorPLW.cells[SectorPLW.access[strs[i]]]
            push!(clls, userCell(cell.key,cell.weight,cell.path,cell.BT))
        end
        cells::Dict{Int64,userCell} =  { i => clls[i] for i = 1:num }
        coords::Dict{String,Int64} = { clls[i].key::String => i for i =1:num }
        new(domain,cells,coords)
    end
end

function spanDRecurs(domain::String, cells = userCell[])
    try
        cell = SectorLWTL.cells[SectorLWTL.access[domain]]
    catch 
        return cells
    end
    cell = SectorLWTL.cells[SectorLWTL.access[domain]]
    push!(cells, userCell(cell.key,cell.weight,cell.path,cell.BT))
    for k in cell.NT
        cells = spanDRecurs("LWTL "*k,cells)
    end
    cells
end


type ProfileLWTL
    domain::String
    cells::Dict{Int64,userCell}    
    coords::Dict{String,Int64}
    function ProfileLWTL(domain::String)
        cellstmp = spanDRecurs(domain)
        num::Int64 = mapreduce(1,+,cellstmp) # get array size
        cells::Dict{Int64,userCell} = { i => cellstmp[i] for i = 1:num }
        coords::Dict{String,Int64} = { cellstmp[i].key::String => i for i =1:num }
        new(domain,cells,coords)
    end

    function ProfileLWTL(domain::String, strs::Array{ASCIIString,1})
        num::Int64 = mapreduce(1,+,strs)
        clls = userCell[]
        for i = 1:num
            cell = SectorLWTL.cells[SectorLWTL.access[strs[i]]]
            push!(clls, userCell(cell.key,cell.weight,cell.path,cell.BT))
        end
        cells::Dict{Int64,userCell} =  { i => clls[i] for i = 1:num }
        coords::Dict{String,Int64} = { clls[i].key::String => i for i =1:num }
        new(domain,cells,coords)
    end

end

getpath(obj::ProfilePLW, idx::Int64) = obj.cells[idx].path
getpath(obj::ProfilePLW, key::String) = getpath(obj::ProfilePLW, obj.coords[key])
getpath(obj::ProfileLWTL, idx::Int64) = obj.cells[idx].path
getpath(obj::ProfileLWTL, key::String) = getpath(obj::ProfileLWTL0, obj.coords[key])
