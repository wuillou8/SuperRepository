using HttpServer, Logging
using Requests
using JSON
using Dates
#using Lazy
using StatsBase, Dates
using PyPlot

include("JuliaCode/classes.jl")
include("JuliaCode/utilities.jl")
include("JuliaCode/models.jl")
#include("__globalFun.jl")
include("__globalModel.jl")
include("JuliaCode/recommender.jl")
include("JuliaCode/perfomeasures.jl")
include("JuliaCode/tests.jl")
include("JuliaCode/display.jl")

function printresult(resp::Response)
    resp |> (_ -> begin
                      _.status,
                      _.headers,
                      _.data,
                      _.finished
                   end ) |> println
end

# instantiate test harness
    __TH = createTest("testfile.txt")


jair = get("http://localhost:8000/retrain")
printresult(jair)
jair = get("http://localhost:8000/testStat/")
printresult(jair)
jair = get("http://localhost:8000/retrain/PersoSimple/")
printresult(jair)
jair = get("http://localhost:8000/testStat/")
printresult(jair)
jair = get("http://localhost:8000/retrain/PersoSimple/")
printresult(jair)
jair = get("http://localhost:8000/testStat/")

printresult(jair)
jair = get("http://localhost:8000/retrain/PersoSimpleNaiveBayes/")
printresult(jair)
jair = get("http://localhost:8000/testStat/")
printresult(jair)
jair = get("http://localhost:8000/retrain/PredictionIO/")
printresult(jair)
jair = get("http://localhost:8000/testStat/")
printresult(jair)
