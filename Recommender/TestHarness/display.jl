


function plotPerf(__perfs::Array{Perfo,1}, __random, __xaxis, __modellabel::String, __plotlabel::String = "")    
    # prepare for plotting
    precis = map(x->x.Precis,__perfs) 
    recalls = map(x->x.Recall,__perfs)
    specifs = map(x->x.Specif,__perfs) 
    f1s = map(x->x.F1,__perfs)
    
    #####################
    #       PLOTS       #
    #####################

    close("all")
    xlim([0,__xaxis[end]+1])
    title("Performance Comparison: Recall")
    xlabel("Recomm List size")
    ylabel("Recall (tp/tp+fn)")
    plot(__xaxis,recalls,"go")
    plot(__xaxis,__random)
    legend(["model","random performance"], "upper left")
    savefig("FIGS/"*__modellabel*"Recallall_"*__plotlabel*".png")

    close("all")
    lim = 9
    xlim([0,__xaxis[lim]+1])
    title("Performance Comparison: Recall // close In")
    xlabel("Recomm List size")
    ylabel("Recall (tp/tp+fn)")
    plot(__xaxis[1:lim],recalls[1:lim],"go")
    plot(__xaxis[1:lim],__random[1:lim])
    legend(["model","random performance"], "upper left")
    savefig("FIGS/"*__modellabel*"Recallclosein_"*__plotlabel*".png")

    close("all")
    xlim([0,__xaxis[end]+1])
    title("Performance Comparison: Precision")
    xlabel("Recomm List size")
    ylabel("Precision (tp/tp+fp)")
    plot(__xaxis,precis,"go")     
    savefig("FIGS/"*__modellabel*"Precision_"*__plotlabel*".png")

    close("all")
    xlim([0.,1.])
    ylim([0.,1.])
    plot(precis,recalls,"go")
    plot(precis,recalls)
    title("Performance Comparison: Recall(Precision)")
    xlabel("Precision")
    ylabel("Recall")
    savefig("FIGS/"*__modellabel*"RecallPrecision_"*__plotlabel*".png")

    close("all")
    xlim([0,__xaxis[end]+1])
    plot(__xaxis,specifs,"go")
    title("Performance Comparison: Specificity")
    xlabel("Recomm List size")
    ylabel("Specificity (1 - fp/fp+tn)")
    savefig("FIGS/"*__modellabel*"Specifs_"*__plotlabel*".png")

    close("all")
    xlim([0,__xaxis[end]+1])
    plot(__xaxis,f1s,"go")
    #legend(["random","NaiveBayes on Entities"], "upper left")
    title("Performance Comparison: F1")
    xlabel("Recomm List size")
    ylabel("F1 = 2*Precision*Recall/(Precision+Recall)")
    savefig("FIGS/"*__modellabel*"F1_"*__plotlabel*".png")
    
end

function plotMeanRecRank(__mrr_meas,__mrr_rand,__xaxis,__modellabel::String, __plotlabel::String = "") #__TH.Recommenders[1])
    close("all")
    xlim([0,__xaxis[end]+1])
    plot(__xaxis,__mrr_meas,"go")
    plot(__xaxis,__mrr_rand)
    legend(["random","random values"], "lower right")
    title("Performance Comparison: Mean reciprocal Rank Meas.")
    xlabel("Recomm List size")
    ylabel("MRR")
    savefig("FIGS/"*__modellabel*"MRR_"*__plotlabel*".png")
end
