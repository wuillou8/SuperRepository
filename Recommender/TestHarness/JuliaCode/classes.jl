# Recommendation class
immutable Recommendation
    reclist::Vector{String}
    Recommendation(vec::Vector{String}) = new(vec)
    Recommendation(obj::Dict{String,Any}) = new( obj["reclist"] )
end

#=========================================================
        CLUSTER MODELS
        simulates the clustering for the computations
        possibly also the parallelisation ~±.
=========================================================#

abstract Clusters

immutable Countries <: Clusters
    labels::Array{String,1}
end

immutable Channels <: Clusters
    labels::Array{String,1}
end

#=========================================================
        Classical Perfo Evaluation
=========================================================#

-

####################################################################
#                 Output File                                      #
####################################################################

abstract OUTPUTRES
#===
type OutputRes{model <: MODEL} <: OUTPUTRES
    # creation time
    testdate::ASCIIString
    # query::
    testHarn::testHarness
    # model with parameteres
    testmodel::model
    # testresults (different performances can be appended)
    testres::Vector{PERFO}
end
===#

#=== currently in display
type OutputRes{model <: MODEL} <: OUTPUTRES
    # creation time
    testdate::ASCIIString
    # query::
    testHarn::testHarness
    # model with parameteres
    testmodel::model
    # testresults (different performances can be appended)
    testres::Vector{PERFO}
end
===#

###################################################################
#                TEST HARNESS                                     #
###################################################################

function getMetrics(var::String)
   var |> ( _->
            _ == "all" ? ["perfs","rankings"] :
            _ == "perfs" ? ["perfs"] :
            _ == "rankings" ? ["rankings"] :
            println("testHarness::getmetrics var must be in all perfs, rankings") )
end

type testHarness
    T1::DateTime
    T2::DateTime
    T3::DateTime
    Recommenders::Array{String,1}
    Scorings::Array{String,1}
    Plotting::Bool
    Metrics::Array{String,1}
end

function createTest(__testfilename::String)
    T1, T2, T3 = DateTime(), DateTime(), DateTime()
    Recommenders = String[]
    Submodels = String[]
    Scorings = String[]
    Plotting = Bool
    Metrics = String[]

    iofile = readdlm(__testfilename)
    for i = 1:length(iofile[1:end,1])
        _type = iofile[i,1]
        _var = iofile[i,2]
        _type |> ( _ ->
                   _ == "T1=" ? T1 = DateTime(_var) :
                   _ == "T2=" ? T2 = DateTime(_var) :
                   _ == "T3=" ? T3 = DateTime(_var) :
                   _ == "Recommender=" ? push!(Recommenders, _var) :
                   _ == "Submodel=" ? push!(Submodels, _var) :
                   _ == "Scoring=" ? push!(Scorings, _var) :
                   _ == "Metrics=" ? Metrics = getMetrics(_var) :
                   _ == "Plotting=" ? ( _var == "yes" ? Plotting = true : Plotting = false ) :
                          " pass "
                  )
       #==
        @switch _type begin
            "T1="; T1 = DateTime(_var)
            "T2="; T2 = DateTime(_var)
            "T3="; T3 = DateTime(_var)
            "Recommender=" ; push!(Recommenders, _var)
            "Submodel=" ;  push!(Submodels, _var)
            "Scoring=" ; push!(Scorings, _var)
            "Metrics=" ; Metrics = getMetrics(_var)
            "Plotting=" ; _var == "yes" ? Plotting = true : Plotting = false
                " pass "
        end
        ==#
    end
    testHarness(T1,T2,T3,Recommenders,Scorings,Plotting,Metrics)
end

####################################################################
#                 Backend Format                                   #
####################################################################

# Data Usage as in Backend format
immutable DataUsage
    source_entity_type::String #(ie, user),
    target_entity_type::String #(ie, document_keyword),
    source_entity_id::String #(ie, device_id),
    target_entity_id::String #(ie, "nasa"),
    action::String #(ie, "view", "rate"),
    value::String #(ie, null, [1-5]),
    time::Int64 #(UTC timestamp),
    DataUsage(source_entity_type::String,target_entity_type::String,source_entity_id::String,target_entity_id::String,action::String,value::String,time::Int64) =
                new(source_entity_type,target_entity_type,source_entity_id,target_entity_id,action,value,time)
    function DataUsage(jsonfile::Dict{String,Any})
        source_entity_type = jsonfile["source_entity_type"]
        target_entity_type = jsonfile["target_entity_type"]
        source_entity_id = jsonfile["source_entity_id"]
        target_entity_id = jsonfile["target_entity_id"]
        action = jsonfile["action"]
        value = jsonfile["value"]
        time = jsonfile["time"]
        new(source_entity_type, target_entity_type,
                    source_entity_id, target_entity_id, action, value, time)
    end
end

type BEData
    Usage::Array{DataUsage,1}
    #Hashtable ?
    # constructor
    BEData(Usage::Array{DataUsage,1}) = new(Usage)
    function BEData(IObedata::Dict{String,Any})
        Usage = IObedata["Usage"] |>
                             (_ -> map(x -> DataUsage(x), _))
        new(Usage)
    end

    function BEData(myiostream::IOStream)
        __bedata = DataUsage[]

        while !eof(STDIN)
            sent_type, tent_type, sent_id, tent_id, action, value, time =
            readline(STDIN) |> JSON.parse |>
              ( _ -> begin
                        _["source_entity_type"],
                        _["target_entity_type"],
                        _["source_entity_id"],
                        _["target_entity_id"],
                        _["action"],
                        _["value"],
                        _["time"]
                      end )
            push!(__bedata, DataUsage(sent_type, tent_type, sent_id, tent_id, action, value, time))
        end
        new(__bedata)
    end
end

# getters for BEData
getAllarticleIds(bedata::BEData) = filter(x -> x.target_entity_type == "article", bedata.Usage) |>
                        (_ -> map(x -> x.source_entity_id, _))

getAllEnts(bedata::BEData) = filter(x -> x.target_entity_type == "entity", bedata.Usage) |>
                        (_ -> map(x -> x.value, _)) |>
                        unique |>
                        StatsBase.countmap

getSId(bedata::BEData, __myId::String) =
                        filter(x -> x.source_entity_id == __myId, bedata.Usage)
getTId(bedata::BEData, __myId::String) =
                        filter(x -> x.target_entity_id == __myId, bedata.Usage)

getEntType(bedata::BEData, __myEnt::String) =
                        filter(x -> (x.target_entity_type == "entity") & (x.source_entity_id == __myEnt), bedata.Usage)

getEntType(bedata::BEData, __myEnt::String) =
                        filter(x -> (x.target_entity_type == "entity") & (x.value == __myEnt), bedata.Usage)

getUnderT(bedata::BEData, __Time::DateTime) =
                        filter(x -> x.time < datetime2unix(__Time), bedata.Usage)

getOverT(bedata::BEData, __Time::DateTime) =
                        filter(x -> x.time > datetime2unix(__Time), bedata.Usage)

getInTs(bedata::BEData, __T1::DateTime, __T2::DateTime) =
                        filter(x -> (x.time > datetime2unix(__T1)) & (x.time <= datetime2unix(__T2)), bedata.Usage)

getUsageIds(bedata::BEData,userId::String) = getSId(bedata,userId) |>
                        (_ -> filter(x -> x.target_entity_type == "article",_)) |>
                        (_ -> map(x->x.target_entity_id,_))

getsourceIds(bedata::BEData, __type::String) = bedata.Usage |>
            (_ -> filter(x -> x.source_entity_type == __type, _)) |>
            (_ -> map(x -> x.source_entity_id, _)) |>
            unique |>
            (_ -> convert(Array{String,1}, _))

gettargetIds(bedata::BEData, __type::String) = bedata.Usage |>
            (_ -> filter(x -> x.target_entity_type == __type, _)) |>
            (_ -> map(x -> x.target_entity_id, _)) |>
            unique |>
            (_ -> convert(Array{String,1}, _))

# get entities
getEntssourceMap(bedata::BEData,userId::String) =  filter(x -> x.source_entity_id == userId, bedata.Usage) |>
                                (_ -> filter(x -> x.target_entity_type == "entity", _)) |>
                                (_ -> map(x -> x.value, _)) |>
                                unique |>
                                StatsBase.countmap

getEntstargetMap(bedata::BEData,targId::String) =  filter(x -> x.target_entity_id == targId, bedata.Usage) |>
                                (_ -> filter(x -> x.target_entity_type == "entity", _)) |>
                                (_ -> map(x -> x.value, _)) |>
                                unique |>
                                StatsBase.countmap
