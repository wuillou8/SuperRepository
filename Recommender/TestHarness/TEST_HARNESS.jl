using JSON
using Dates #Time
using Lazy
using PyPlot


include("utilities.jl")
include("classes.jl")
include("model.jl")
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
    
    # pass data    
    __traindatapath = "DataBase/datafortraining.json"
    out = open(__traindatapath,"w+")
    JSON.print( out, trainbedata)
    close(out)

    # run model trainings
    for model in __TH.Recommenders 
        __TH.Recommenders |> println
        "model trained: $model" |> println
        run(`time julia trainModel.jl $model Random`)
    end

# for now we also store the testing events
    __testdatapath = "DataBase/datafortesting.json"
    out = open(__testdatapath,"w+")
    JSON.print(out,testbedata)
    close(out)

# send/load model(s) to train
    println("Model pseudo loaded ",__TH.Recommenders[1])
    __model = modelsFactory(__TH.Recommenders[1], "data")

# Test Harness Core 
# recomm list intervals for tests/plots
   __recommSizes = 
              [ 1, 3, 5, 7, 10, 20, 40, 80, 120, 200]
   __perfs, __mrr_meas, __mrr_rand, __random = 
                                TestPerfos(__model, testusersIds, __recommSizes)

# Plot
if __TH.Plotting # == true
    if "perfs" in __TH.Metrics
        plotPerf(__perfs,__random,__recommSizes,__TH.Recommenders[1])
    end
    if "rankings" in __TH.Metrics
        plotMeanRecRank(__mrr_meas,__mrr_rand,__recommSizes,__TH.Recommenders[1])
    end
end

println(__TH.Recommenders[2])
