
####################################################################
#                 Output File                                      #
####################################################################
#===
abstract OUTPUTRES
===#

# for each tests, the testharness parameters,
type OutputRes{model <: MODEL} <: OUTPUTRES
    # creation time
    testdate::ASCIIString
    # query::
    testHarn::testHarness
    # model with parameteres
    testmodel::model
    # testresults (different performances can be appended)
    testres::Vector{PERFO}
end


#####################################################################
#                 Output Plot                                       #
#####################################################################

function plotMeanRecRank1(__mrr_meas, __mrr_rand, __xaxis,__modellabel::String, __plotlabel::String = "")
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

function plotMeanRecRank2(__pr::Vector{PerfoRank}, __xaxis, __modellabel::Vector{String}, __plotlabel::String = "")
    close("all")
    xlim([0,__xaxis[end]+1])
    __pr |> (_ -> map(x -> plot(__xaxis,x.mrr_meas, "o"), _))
    __pr |> (_ -> map(x -> plot(__xaxis,x.mrr_rand,"k"), _))
    legend([__modellabel,"Random theoretical"], "lower right")
    title("Performance: Mean reciprocal Rank Measure")
    xlabel("Recomm List size")
    ylabel("MRR")
    savefig("FIGS/"*foldr(*,__modellabel)*__plotlabel*"MRR_"*__plotlabel*".png")
end

function plotMeanRecRank3(__pr::Vector{PerfoRank}, __xaxis, __modellabel::Vector{String}, __plotlabel::String = "")
    close("all")
    xlim([0,__xaxis[end]+1])
    __pr |> (_ -> map(x -> plot(__xaxis,x.mrr_meas, "o"), _))
    __pr |> (_ -> map(x -> plot(__xaxis,x.mrr_rand,"k"), _))
    legend([__modellabel,"Random theoretical"], "lower right")
    title("Performance: Mean reciprocal Rank Measure")
    xlabel("Recomm List size")
    ylabel("MRR")
    savefig("FIGSs/"*foldr(*,__modellabel)*__plotlabel*"MRR_"*__plotlabel*".png")
end

function plotPerf2(__perfs::Array{Vector{Perfo},1}, __randoms::Array{Vector{Float64},1}, __xaxis, __modellabel::Vector{String}, __plotlabel::String = "")
    # prepare for plotting
    precis = [ map( x -> x.Precis, _) for _ in __perfs ]
    recalls = [ map( x -> x.Recall, _) for _ in __perfs ]
    specifs = [ map(x -> x.Specif, _) for _ in __perfs ]
    f1s = [ map(x -> x.F1, _) for _ in __perfs ]

    #####################
    #       PLOTS       #
    #####################

    close("all")
    xlim([0,__xaxis[end]+1])
    title("Performance Comparison: Recall")
    xlabel("Recomm List size")
    ylabel("Recall (tp/tp+fn)")
    [ plot(__xaxis,_,"o") for _ in recalls ]
    [ plot(__xaxis,_) for _ in __randoms ]
    legend( __modellabel, "lower right" )
    savefig("FIGS/"*"Recallall_"*foldr(*,__modellabel)*__plotlabel*".png")

    close("all")
    lim = 6
    xlim([0,__xaxis[lim]+1])
    title("Performance Comparison: Recall // close In")
    xlabel("Recomm List size")
    ylabel("Recall (tp/tp+fn)")
    [ plot(__xaxis[1:lim],_[1:lim],"o") for _ in recalls]
    [ plot(__xaxis[1:lim],_[1:lim]) for _ in __randoms ]
    legend(__modellabel, "lower right" )
    savefig("FIGS/"*"Recallclosein_"*foldr(*,__modellabel)*__plotlabel*".png")

    close("all")
    xlim([0,__xaxis[end]+1])
    title("Performance Comparison: Precision")
    xlabel("Recomm List size")
    ylabel("Precision (tp/tp+fp)")
    map( x -> plot(__xaxis,x,"o"), f1s)
    legend( __modellabel, "lower right" )
    savefig("FIGS/"*"Precision_"*foldr(*,__modellabel)*__plotlabel*".png")

    close("all")
    xlim([0.,1.])
    ylim([0.,1.])
    [ plot(precis[i],recalls[i],"o") for i = 1:length(recalls) ]
    [ plot(precis[1],recalls[i]) for i = 1:length(recalls) ]
    title("Performance Comparison: Recall(Precision)")
    xlabel("Precision")
    ylabel("Recall")
    legend( __modellabel, "lower right" )
    savefig("FIGS/"*"RecallPrecision_"*foldr(*,__modellabel)*__plotlabel*".png")

    close("all")
    xlim([0,__xaxis[end]+1])
    map( x -> plot(__xaxis,x,"o"), specifs)
    title("Performance Comparison: Specificity")
    xlabel("Recomm List size")
    ylabel("Specificity (1 - fp/fp+tn)")
    legend( __modellabel, "lower right" )
    savefig("FIGS/"*"Specifs_"*foldr(*,__modellabel)*__plotlabel*".png")

    close("all")
    xlim([0,__xaxis[end]+1])
    #[ plot(__xaxis,_,"go") for _ in f1s ]
    map( x -> plot(__xaxis,x,"o"), f1s)
    title("Performance Comparison: F1")
    xlabel("Recomm List size")
    ylabel("F1 = 2*Precision*Recall/(Precision+Recall)")
    legend( __modellabel, "lower right" )
    savefig("FIGS/"*"F1_"*foldr(*,__modellabel)*__plotlabel*".png")

end


function plotPerf1(__perfs::Array{Perfo,1}, __random, __xaxis, __modellabel::String, __plotlabel::String = "")
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
    legend(["model","random performance"], "lower right")
    savefig("FIGS/"*__modellabel*"Recallall_"*__plotlabel*".png")

    close("all")
    lim = 6
    xlim([0,__xaxis[lim]+1])
    title("Performance Comparison: Recall // close In")
    xlabel("Recomm List size")
    ylabel("Recall (tp/tp+fn)")
    plot(__xaxis[1:lim],recalls[1:lim],"go")
    plot(__xaxis[1:lim],__random[1:lim])
    legend(["model","random performance"], "lower right")
    savefig("FIGS/"*__modellabel*"Recallclosein_"*__plotlabel*".png")

    close("all")
    xlim([0,__xaxis[end]+1])
    title("Performance Comparison: Precision")
    xlabel("Recomm List size")
    ylabel("Precision (tp/tp+fp)")
    plot(__xaxis,precis,"go")
    legend(["model","random performance"], "lower right")
    savefig("FIGS/"*__modellabel*"Precision_"*__plotlabel*".png")

    close("all")
    xlim([0.,1.])
    ylim([0.,1.])
    plot(precis,recalls,"go")
    plot(precis,recalls)
    title("Performance Comparison: Recall(Precision)")
    xlabel("Precision")
    ylabel("Recall")
    legend(["model","random performance"], "lower right")
    savefig("FIGS/"*__modellabel*"RecallPrecision_"*__plotlabel*".png")

    close("all")
    xlim([0,__xaxis[end]+1])
    plot(__xaxis,specifs,"go")
    title("Performance Comparison: Specificity")
    xlabel("Recomm List size")
    ylabel("Specificity (1 - fp/fp+tn)")
    legend(["model","random performance"], "lower right")
    savefig("FIGS/"*__modellabel*"Specifs_"*__plotlabel*".png")

    close("all")
    xlim([0,__xaxis[end]+1])
    plot(__xaxis,f1s,"go")
    title("Performance Comparison: F1")
    xlabel("Recomm List size")
    ylabel("F1 = 2*Precision*Recall/(Precision+Recall)")
    legend(["model","random performance"], "lower right")
    savefig("FIGS/"*__modellabel*"F1_"*__plotlabel*".png")
end

function plotPerf3(__perfs::Array{Vector{Perfo},1}, __randoms::Array{Vector{Float64},1}, __xaxis, __modellabel::Vector{String}, __plotlabel::String = "")

    # prepare for plotting
    precis = [ map( x -> x.Precis, _) for _ in __perfs ]
    recalls = [ map( x -> x.Recall, _) for _ in __perfs ]
    specifs = [ map(x -> x.Specif, _) for _ in __perfs ]
    f1s = [ map(x -> x.F1, _) for _ in __perfs ]

    #####################
    #       PLOTS       #
    #####################

    close("all")
    xlim([0,__xaxis[end]+1])
    title("Performance Comparison: Recall")
    xlabel("Recomm List size")
    ylabel("Recall (tp/tp+fn)")
    [ plot(__xaxis,_,"o") for _ in recalls ]
    [ plot(__xaxis,_) for _ in __randoms ]
    legend( __modellabel, "lower right" )
    savefig("FIGSs/"*"Recallall_"*foldr(*,__modellabel)*__plotlabel*".png")
#=====
    close("all")
    lim = 6
    xlim([0,__xaxis[lim]+1])
    title("Performance Comparison: Recall // close In")
    xlabel("Recomm List size")
    ylabel("Recall (tp/tp+fn)")
    [ plot(__xaxis[1:lim],_[1:lim],"o") for _ in recalls]
    [ plot(__xaxis[1:lim],_[1:lim]) for _ in __randoms ]
    legend(__modellabel, "lower right" )
    savefig("FIGSs/"*"Recallclosein_"*foldr(*,__modellabel)*__plotlabel*".png")

    close("all")
    xlim([0,__xaxis[end]+1])
    title("Performance Comparison: Precision")
    xlabel("Recomm List size")
    ylabel("Precision (tp/tp+fp)")
    map( x -> plot(__xaxis,x,"o"), f1s)
    legend( __modellabel, "lower right" )
    savefig("FIGSs/"*"Precision_"*foldr(*,__modellabel)*__plotlabel*".png")

    close("all")
    xlim([0.,1.])
    ylim([0.,1.])
    [ plot(precis[i],recalls[i],"o") for i = 1:length(recalls) ]
    [ plot(precis[1],recalls[i]) for i = 1:length(recalls) ]
    title("Performance Comparison: Recall(Precision)")
    xlabel("Precision")
    ylabel("Recall")
    legend( __modellabel, "lower right" )
    savefig("FIGSs/"*"RecallPrecision_"*foldr(*,__modellabel)*__plotlabel*".png")

    close("all")
    xlim([0,__xaxis[end]+1])
    map( x -> plot(__xaxis,x,"o"), specifs)
    title("Performance Comparison: Specificity")
    xlabel("Recomm List size")
    ylabel("Specificity (1 - fp/fp+tn)")
    legend( __modellabel, "lower right" )
    savefig("FIGSs/"*"Specifs_"*foldr(*,__modellabel)*__plotlabel*".png")

    close("all")
    xlim([0,__xaxis[end]+1])
    #[ plot(__xaxis,_,"go") for _ in f1s ]
    map( x -> plot(__xaxis,x,"o"), f1s)
    title("Performance Comparison: F1")
    xlabel("Recomm List size")
    ylabel("F1 = 2*Precision*Recall/(Precision+Recall)")
    legend( __modellabel, "lower right" )
    savefig("FIGSs/"*"F1_"*foldr(*,__modellabel)*__plotlabel*".png")
=====#
end


