using JSON
using Dates
using Lazy
using StatsBase
using Dates
using PyPlot


include("utilities.jl")
include("classes.jl")
include("models.jl")
include("recommender.jl")
include("perfomeasures.jl")
include("tests.jl")
include("display.jl")







# read data passed from backend
    __backenddatapath = "DataBase/bedata.json"
    bedata = BEData( JSON.parsefile(__backenddatapath) )

# instantiate test harness
    __TH = createTest("testfile.txt")

# split data into train/test sets
    trainbedata = BEData(getInTs(bedata,__TH.T1,__TH.T2))
    testbedata = BEData(getInTs(bedata,__TH.T2,__TH.T3))

# filter out test UsersId and NewsId 
# create hash table
    testusersIds = getsourceIds(testbedata,"user")
    testnewsIds = gettargetIds(testbedata,"article")
    hashtestUsage = 
            { Id => convert(Array{String,1}, getUsageIds(testbedata, Id)) for Id in testusersIds }


# send event for training
    # print modelname to be trained
    __traindatapath = "DataBase/datafortraining.json"
    out = open(__traindatapath,"w+")
    JSON.print( out, trainbedata)
    close(out)

# trainer also need testing events for personalisation
# identifying user without usage that are dealt with by a global model.
    __testdatapath = "DataBase/datafortesting.json"
    out = open(__testdatapath,"w+")
    JSON.print(out,testbedata)
    close(out)


# launch model trainings
    for i = 1:length(__TH.Recommenders)
        model = __TH.Recommenders[i]
        "model $i trained: $model" |> println
        run(`time julia trainModel.jl $model Random $i`)
    end


# load trained model(s)
    __models = MODEL[]
    for i = 1:length(__TH.Recommenders)
        __modelName = __TH.Recommenders[i]

        # load/instantiate/append model
        "DataBase/trainedmodel$__modelName$i.json" |> 
                   JSON.parsefile |> (_ -> modelsFactory(_,  __modelName)) |>
                                (_ -> begin 
                                          push!(__models,_)
                                          "model $__modelName loaded" |> println
                                      end )
    end

# Test Harness Core 
# recomm list intervals for tests/plots
    __recommSizes = [ 1, 3, 5, 7, 10, 20, 40, 80, 120, 200]

    __perfs, __perfs_ranks, __randoms = Vector{Perfo}[], PerfoRank[], Vector{Float64}[]
    __outresults = OUTPUTRES[]


testusersIds = __models[1].modelP.persoIds

   for __model in __models
    
       __perf, __perf_rank, __random = 
                            TestPerfos( __model, testusersIds, testnewsIds, 
                                                 trainbedata, testbedata, __recommSizes )
       # build results
       push!(__perfs, __perf)
       push!(__perfs_ranks, __perf_rank)
       push!(__randoms, __random)          
       push!(__outresults, 
               OutputRes(strftime(time()), __TH, __model, [Intervals(__recommSizes), __perf, __perf_rank]) ) 
    end

# Print out result file
    __resupath = "DataBase/testresufile.json"
    out = open(__resupath,"w+")
    JSON.print( out, __outresults)
    close(out)

# Plot
    #println(__TH.Plotting)
    Nmodel = length(__TH.Recommenders)
    if __TH.Plotting # == true

        if "perfs" in __TH.Metrics
            Nmodel > 1 ? plotPerf2(__perfs,__randoms,__recommSizes,__TH.Recommenders) :
                                 plotPerf1(__perfs[1],__randoms[1],__recommSizes,__TH.Recommenders[1])
        end
        if "rankings" in __TH.Metrics
            Nmodel > 1 ? plotMeanRecRank2(__perfs_ranks,__recommSizes,__TH.Recommenders) :
                                 plotMeanRecRank1(__perfs_ranks[1].__mrr_meas,__perfs_ranks[1].__mrr_rand,__recommSizes,__TH.Recommenders[1])
        end
    end

#plotPerf1(::Array{Perfo,1}, ::Array{Float64,1}, ::Array{Int64,1}, ::Array{String,1})






