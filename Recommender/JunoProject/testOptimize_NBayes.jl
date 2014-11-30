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
include("displayjuno.jl")

# IO parameters
__usageClusterparams = ["France", "Germany", "Switzerland", "Japan", "Hong Kong", "China", "Turkey", "Nigeria"]
Cutoffs = [ 50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
#__newsClusterparams = ["everything"]

__clustUsage = "France"
__clustNews = "everything"
__display_YorN = "no"

for __clustUsage in [__usageClusterparams[1]]
cntry = __clustUsage
# read news and usage train/test samples
t1 = time()
# training sets
trainUsage = readtable("pseudoDBASE/trainUsage"*__clustUsage*".csv" )
newspath = "pseudoDBASE/trainNews"*__clustNews*".json"
trainNews = News(JSON.parsefile(newspath)["news"])
# testing sets
testUsage = readtable("pseudoDBASE/testUsage"*__clustUsage*".csv" )
newspath = "pseudoDBASE/testNews"*__clustNews*".json"
testNews = News(JSON.parsefile(newspath)["news"])
t2 = time()
println("load time: ",t2-t1)




# Run optimisation
t1 = time()
#Cutoffs = [ 50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
rocaucs = Float64[]
    for __cut in Cutoffs
        t1 = time()

        modelNB = BernoulliNB(trainUsage, trainNews, __cut)

        scores = Float64[]
        for new in testNews.news
            push!(scores, ApplyBernoulliNB(modelNB,testNews,new.guid))
        end

        precs1, recalls1, specifs1, f1s1 = Float64[], Float64[], Float64[], Float64[]
        for i in 1:3:100
            prec, recall, specif, f1 = EvaluatePerfo(testNews, testUsage, "naivebayes", scores, i)
            push!(precs1,prec), push!(recalls1,recall), push!(specifs1,specif), push!(f1s1,f1)
        end

        auc = trapz(1.-specifs1,recalls1)/(maximum(1.-specifs1)*maximum(recalls1))
        push!(rocaucs, (auc)) #/(maximum(1.-specifs1)*maximum(recalls1)))
        t2 = time()
        println("ROC AUC: ",auc)
        println("$__cut comput time: ",t2 - t1)
    end
    Nmax = findNMax(rocaucs,1)
    println("----*-*-*---*Max for $__clustUsage: ", rocaucs[Nmax][1])

    ProcessPlot(rocaucs,Cutoffs,cntry,Nmax)
    # rerun model
    modelNB = BernoulliNB(trainUsage, trainNews, __cut)
    scores = Float64[]
    for new in testNews.news
            push!(scores, ApplyBernoulliNB(modelNB,testNews,new.guid))
    end

    plotPrecRandVSNBtest(testNews, testUsage, scores, cntry)
    PlotFullRocAUC(testNews, testUsage, scores, cntry)
end

#===
modelNB = BernoulliNB(trainUsage, trainNews, __cutOff)
t2 = time()
println("train time: ",t2-t1)

out = open("pseudoDBASE/currentNaiveBayesModel.json","w+")
JSON.print(out, modelNB)
close(out)
===#
