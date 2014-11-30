#===========================================
            PLOTS
===========================================#

# plot mini ROC AUC curve.
function ProcessPlot(rocaucs::Array{Float64,1}, Cutoffs::Array{Int64,1}, cntry::ASCIIString, Nmax::Array{Int64,1})
    close("all")
    maxy = rocaucs[Nmax]
    xlim([-1.,length(rocaucs)])
    plot(rocaucs,"go")
    axhline(maxy)
    max = Cutoffs[Nmax][1]

    legend(["Maximum at $max","$Cutoffs"], "lower right")
    title("mini ROC AUC (NB Entities): $cntry")
    xlabel("Nb Entities for Bayesian Model")
    ylabel("mini ROC AUC")

    savefig("FIGS/NaiveBayesian/rocOptimiz"*cntry*".png")
end


function plotPrecRandVSNBtest(testNews::News, testUsage::DataFrame, scores::Array{Float64,1}, cntry::String)

    Itsteps = 1:3:100
    precs, recalls, specifs, f1s = Float64[], Float64[], Float64[], Float64[]
    for i in Itsteps
        prec, recall, specif, f1 = EvaluatePerfo(testNews, testUsage, "naivebayes", scores, i)
        push!(precs,prec), push!(recalls,recall), push!(specifs,specif), push!(f1s,f1)
    end
    perfoRDM = Float64[]
    [ push!(perfoRDM,i/length(testNews.news)) for i in Itsteps ]

    xarr = [Itsteps]
    xlim([0,Itsteps.stop+1])

    close("all")
    plot(xarr,perfoRDM,"*")
    plot(xarr,recalls,"go")
    legend(["random","NaiveBayes on Entities"], "upper left")
    title("Performance Comparison: Recall")
    xlabel("Recomm List size")
    ylabel("Recall (tp/tp+fn)")
    savefig("FIGS/NaiveBayesian/plotOptimalRecall"*cntry*".png")

    close("all")
    xlim([0,Itsteps.stop+1])
    plot(xarr,perfoRDM,"*")
    plot(xarr,precs,"go")
    legend(["random","NaiveBayes on Entities"], "lower right")
    title("Performance Comparison: Precision")
    xlabel("Recomm List size")
    ylabel("Precision (tp/tp+fp)")
    savefig("FIGS/NaiveBayesian/plotOptimalPrec"*cntry*".png")

    close("all")
    xlim([0,Itsteps.stop+1])
    plot(xarr,perfoRDM,"*")
    plot(xarr,specifs,"go")
    legend(["random","NaiveBayes on Entities"], "upper left")
    title("Performance Comparison: Specificity")
    xlabel("Recomm List size")
    ylabel("Specificity (1 - fp/fp+tn)")
    savefig("FIGS/NaiveBayesian/plotOptimalSpec"*cntry*".png")

    close("all")
    xlim([0,Itsteps.stop+1])
    plot(xarr,perfoRDM,"*")
    plot(xarr,f1s,"go")
    legend(["random","NaiveBayes on Entities"], "upper left")
    title("Performance Comparison: F1")
    xlabel("Recomm List size")
    ylabel("F1 = 2*Precision*Recall/(Precision+Recall)")
    savefig("FIGS/NaiveBayesian/plotOptimalF1"*cntry*".png")

    close("all")
    xlim([0.,1.])
    ylim([0.,1.])
    plot(precs,recalls,"go")
    plot(precs,recalls)
    title("Performance Comparison: Recall(Precision)")
    xlabel("Precision")
    ylabel("Recall")
    savefig("FIGS/NaiveBayesian/plotOptimalPrecRec"*cntry*".png")
end

function PlotFullRocAUC(testNews::News, testUsage::DataFrame, scores::Array{Float64,1}, cntry::String)

    Itsteps1 = 1:5:length(scores)
    precs1, recalls1, specifs1, f1s1 = Float64[], Float64[], Float64[], Float64[]
    for i in Itsteps1
        prec, recall, specif, f1 = EvaluatePerfo(testNews, testUsage, "naivebayes", scores, i)
        push!(precs1,prec), push!(recalls1,recall), push!(specifs1,specif), push!(f1s1,f1)
    end
    auc = trapz(1.-specifs1,recalls1)
    close("all")
    xlim([0.,1.])
    ylim([0.,1.])
    plot(1.-specifs1,recalls1,"go")
    plot([0.,1.],[0.,1.])
    legend(["ROC AUC score: $auc"], "lower right")
    title("Performance Comparison: ROC AUC")
    xlabel("TPR (True Positive Rate)")
    ylabel("FPR (False Positive Rate)")
    savefig("FIGS/NaiveBayesian/plotOptimalRocAUC"*cntry*".png")

end
