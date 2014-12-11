#==========================================
        Perfo. Measure
==========================================#


# function measuring INFORMATION RETRIEVAL metrics
# listnews: it the list of news
# listReco: the recommendation list
# idUser: used Id
# output: perf::Perfo
function perfoMeasOpt(listNews::Array{String,1}, listReco::Array{String,1}, idUsed::String)
    L_listNews = length(listNews)
    L_listReco = length(listReco)
    
    perf = Perfo(0,0,0,0)    
    if idUsed in listReco
        perf.tp = 1
        perf.fp = L_listReco - 1
        perf.fn = 0
        perf.tn = L_listNews - L_listReco - 1
    else
        perf.tp = 0
        perf.fp = L_listReco
        perf.fn = 1
        perf.tn = L_listNews - L_listReco - 1
    end
    perf
    
end

# mean reciprocal rank measure: MRR
# http://en.wikipedia.org/wiki/Mean_reciprocal_rank
# MRR = 1/Q_i sum_i=1^Q 1./rank_i, whereas i is summed over the objects.
# utility function for MRR
function get_Rank(recoList, use)
    for n = 1:length(recoList)
        if use == recoList[n]
            return n
        end
    end
    1_000_000_000_000_000
end

# MRR comput.
function MRR_Meas(recoList, usage)
    [ sum( map(_use_ -> 1./get_Rank(recoList,_use_), usage) ), length(usage) ]
end

# evaluate random value/ benchmark
function MRR_Meas(newslist::Array{String,1}, N::Int64)
    L = length(newslist)
    sm = sum([ 1./i for i = 1:N ])
    sm / L
end
