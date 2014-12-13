using JSON
using Dates
using Lazy
using StatsBase


include("utilities.jl")
include("classes.jl")
include("models.jl")
include("recommender.jl")
include("perfomeasures.jl")
include("tests.jl")




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
    
    # pass data    
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
    #println("Model pseudo loaded ",__TH.Recommenders[1])
    #__model = modelsFactory(__TH.Recommenders[1], "data")
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
__recommSizes = 
              [ 1, 3, 5, 7, 10, 20, 40, 80, 120, 200]

for __model in __models
#__model = __models[1]


   __perfs, __mrr_meas, __mrr_rand, __random = 
                                TestPerfos( __model, 
                                            testusersIds, testnewsIds,
                                            trainbedata, testbedata,
                                            __recommSizes )

__perfs |> println
__mrr_meas |> println 
__mrr_rand |> println 
__random |> println
"***********fin 1 " |> println 
end

exit()
# Plot
if __TH.Plotting # == true
    using PyPlot
    include("display.jl")

    if "perfs" in __TH.Metrics
        plotPerf(__perfs,__random,__recommSizes,__TH.Recommenders[1])
    end
    if "rankings" in __TH.Metrics
        plotMeanRecRank(__mrr_meas,__mrr_rand,__recommSizes,__TH.Recommenders[1])
    end
end

println(__TH.Recommenders[2])
