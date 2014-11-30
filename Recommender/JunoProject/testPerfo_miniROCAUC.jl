PATH = "/Users/jair/Desktop/PROJECTS/KALE/KaleAUTO/USERAnalysis/"

using DataFrames
using Lazy
using Dates
include("DataFramesMeta.jl")
using DataFramesMeta;

include("utilitiesjuno.jl")
include("classesjuno.jl")
include("testingjuno.jl")
include("modeljuno.jl")


# IO parameters
__clustUsage = "France"
__clustNewspath1 = "testNews"
__clustNewspath2 = "everything"
__scorepath = "scores"

# load model and news list
t1 = time()
# load test files
testUsage = readtable("pseudoDBASE/testUsage"*__clustUsage*".csv" )
testnewspath = "pseudoDBASE/"*__clustNewspath1*__clustNewspath2*".json"
testNews = News(JSON.parsefile(testnewspath)["news"])
# load scores
scorespath = "pseudoDBASE/"*__scorepath*".csv"
scores = readcsv(scorespath)[1:end,1]
t2 = time()
println("loading: ", t2-t1)

# evaluate perfo
t1 = time()
precs1, recalls1, specifs1, f1s1 = Float64[], Float64[], Float64[], Float64[]
for i in 1:3:100
    prec, recall, specif, f1 = EvaluatePerfo(testNews, testUsage, "naivebayes", scores, i)
    push!(precs1,prec), push!(recalls1,recall), push!(specifs1,specif), push!(f1s1,f1)
end

rocauc = trapz(1.-specifs1,recalls1)/(maximum(1.-specifs1)*maximum(recalls1))
t2 = time()
println("evaluation time: ",t2 - t1)

println("\n--*-*-ROC AUC measured:\n",rocauc)
