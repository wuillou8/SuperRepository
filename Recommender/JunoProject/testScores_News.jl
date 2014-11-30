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
__modelpath = "currentNaiveBayesModel"
__clustNewspath1 = "testNews"
__clustNewspath2 = "everything"

# load model and news list
t1 = time()
modelpath = "pseudoDBASE/"*__modelpath*".json"
modelNB = JSON.parsefile(modelpath)
modelNB = BernoulliNB(convert(Array{String,1},modelNB["Voc"]),
                    modelNB["Nc"], modelNB["Nc_"],
                    modelNB["prior"], modelNB["prior_"],
                    convert(Array{Float64,1},modelNB["probvec"]), convert(Array{Float64,1},modelNB["probvec_"]))

newspath = "pseudoDBASE/"*__clustNewspath1*__clustNewspath2*".json"
testNews = News(JSON.parsefile(newspath)["news"])
t2 = time()
println("loading: ", t2-t1)

# Makes scores
t1 = time()
scores = Float64[]
for new in testNews.news
    push!(scores, ApplyBernoulliNB(modelNB,testNews,new.guid))
end
t2 = time()
println("compute scores: ",t2 - t1)

t1 = time()
writecsv("pseudoDBASE/scores.csv", scores)
t2 = time()
println("print scores: ",t2 - t1)
