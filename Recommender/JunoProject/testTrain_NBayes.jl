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
__clustNews = "everything"
__cutOff = 200


# read news and usage train samples
t1 = time()
trainUsage = readtable("pseudoDBASE/trainUsage"*__clustUsage*".csv" )
newspath = "pseudoDBASE/trainNews"*__clustNews*".json"
trainNews = News(JSON.parsefile(newspath)["news"])
t2 = time()
println("load time: ",t2-t1)

t1 = time()
modelNB = BernoulliNB(trainUsage, trainNews, __cutOff)
t2 = time()
println("train time: ",t2-t1)

out = open("pseudoDBASE/currentNaiveBayesModel.json","w+")
JSON.print(out, modelNB)
close(out)
