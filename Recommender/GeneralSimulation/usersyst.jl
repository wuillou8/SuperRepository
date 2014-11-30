
#user with specific preference for simulation

type User
    userid::ASCIIString
    prefs::Array{String,1} 
    # for now the basket/history is a dataframe, should become connected to the database
    history::DataFrame
    User(userid::ASCIIString, prefs::Array{String,1}) = 
    new(userid,prefs)
end

#=
type User
    userid::ASCIIString
    prefs::Array{ASCIIString,1}
    history::DataFrame # for now the basket/history is a dataframe
    User(userid::ASCIIString, prefs::Array{ASCIIString,1}) = #, initT::Int64) = 
                                new(userid,prefs) #, DataFrame( T = [initT for i in prefs], Items = prefs ))
end
=#

# btw, the current schema for user interactions with content is: 
# timestamp, source_entity, source_id, target_entity, target_id, action, value

type System 
    converthist::DataFrame # for now the basket/history is a dataframe
    generalhist::DataFrame
end


function PrefdictIntoUser (prefdict)
    tmp = ASCIIString[]
    [ push!(tmp,str) for str in keys(prefdict) ];
end

function getProgPrefs(prof::ProfilePLW)
    pcoords = keys(prof.coords)
    convert(Array{ASCIIString,1},[ push!(tmp,str) for str in ucoords ][1])
end

#=
     Functions initiating users for the simulations, based on the taxonnomy nodes selected by the 
     profiles generations and projections.
     The User used for simulations has an Id "name", preferences and a consumption or rating history that is 
     filled initially based on his preferences(ColdSolved==true) or randomly (ColdSolved==false). 
=#

function gInitUser(str::ASCIIString,  profiLWTL::ProfileLWTL,  
                profiPLW::ProfilePLW, Time::Int64, ColdSolved::Bool = true)
    prefsLWTL = PrefdictIntoUser(profiLWTL.coords)[1]
    prefsPLW = PrefdictIntoUser(profiPLW.coords)[1]
    usr = User( str, convert(Array{String,1}, [prefsLWTL, prefsPLW] ) )

    if ColdSolved
        usr.history = DataFrame( T = [ Time for i in [prefsLWTL, prefsPLW] ], Items = [prefsLWTL, prefsPLW] )
    else # random start
        println("random")
        tmpLWTL = map( x->SectorLWTL.cells[rand(1:SectorLWTL.cells.count)].key, prefsLWTL )
        tmpPLW = map( x->SectorPLW.cells[rand(1:SectorLWTL.cells.count)].key, prefsPLW ) 
        prefs = convert( Array{ASCIIString,1}, [tmpLWTL,tmpPLW] )
        usr.history = DataFrame( T = [ Time for i in prefs ], Items = prefs )
    end
    usr
end


function gInitUser(str::ASCIIString,  profiLWTL::ProfileLWTL, Time::Int64, ColdSolved::Bool = true)
    prefs = [ PrefdictIntoUser(profiLWTL.coords)[1] ]
    usr = User( str, convert(Array{String,1}, prefs) )
    if ColdSolved
        usr.history = DataFrame( T = [ Time for i in prefs ], Items = prefs )
    else # random start
        prefs = convert( Array{String,1}, map( x->SectorLWTL.cells[rand(1:SectorLWTL.cells.count)].key, prefs ) )
        usr.history = DataFrame( T = [ Time for i in prefs ], Items = prefs )
    end
    usr
end

function gInitUser(str::ASCIIString,  profiPLW::ProfilePLW, Time::Int64, ColdSolved::Bool = true)
    prefs = [ PrefdictIntoUser(profiPLW.coords)[1] ]
    usr = User( str, convert(Array{String,1}, prefs) )
    if ColdSolved
        usr.history = DataFrame( T = [ Time for i in prefs ], Items = prefs )
        else # random start
        prefs = convert( Array{ASCIIString,1}, map( x->SectorPLW.cells[rand(1:SectorPLW.cells.count)].key, prefs ) )
        usr.history = DataFrame( T = [ Time for i in prefs ], Items = prefs )
    end
    usr
end
