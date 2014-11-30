#=========================================================
        CLUSTER MODEL
        simulates the clustering for the computations
        possibly also the parallelisation ~±.
=========================================================#

abstract Clusters

immutable Countries <: Clusters
    labels::Array{String,1}
end

immutable Channels <: Clusters
    labels::Array{String,1}
end

#=========================================================
        Classical Perfo Evaluation
=========================================================#

type Perfo
  tp::Int64
  fp::Int64
  tn::Int64
  fn::Int64
end

function addPerfo(perf::Perfo,tp,fp,tn,fn)
  perf.tp += tp
  perf.fp += fp
  perf.tn += tn
  perf.fn += fn
end

Precis(perf::Perfo) = perf.tp/(perf.tp+perf.fp)
Recall(perf::Perfo) = perf.tp/(perf.tp + perf.fn)
Specif(perf::Perfo) = 1.-perf.fp/(perf.fp + perf.tn)
F1(perf::Perfo) = 2*Precis(perf)*Recall(perf)/(Precis(perf)+Recall(perf))

#========================================================
        NEWS Class
========================================================#

myfil(entities::Array{Any,1}) =
            filter( x->!( x["type"] in ["organization-score","person-score" ] ), entities)

type New
    date::DateTime
    guid::String
    entities::Array{Any,1}
    function New(new::Dict{String,Any})
        date = DateTime(new["date"])
        guid = lowercase(new["guid"])
        entities = new["entities"] #myfil(new["entities"])
        new(date,guid,entities)
    end
    function New(new::Dict{String,Any}, date::String)
        date = DateTime(date)
        guid = lowercase(new["guid"])
        entities = new["entities"] #myfil(new["entities"])
        new(date,guid,entities)
    end
end

function MakeguidTable(news::Array{New,1})
  n = 0
  guidTable = convert(Dict{String, Int64},{ new.guid => n+=1 for new in news })
end

type News
    news::Array{New,1}
    hashtable::Dict{String,Int64}

    function News(nws::Array{Any,1})
        news = New[]
        for new in nws
            push!(news,New(new))
        end
        hashtable = MakeguidTable(news)
        new(news,hashtable)
    end
    function News(news::Array{New,1})
        hashtable = MakeguidTable(news)
        new(news,hashtable)
    end
    function News(nws::Array{Any,1}, df::DataFrame)
        news = New[]
        dates = df[:myDates]
        n, N = length(nws), length(dates)
        if n != N
            println("Wrong size, problem in IO!!!", n, " vs ", N )
        end
        for i = 1:n #new in nws
            new, date = nws[i], dates[i]
            push!(news,New(new,date))
        end
        hashtable = MakeguidTable(news)
        new(news,hashtable)
    end
end

# getter: new <- guid
getguid(mynews::News,str::String) = mynews.news[mynews.hashtable[str]];
# is in guid?
isinguid(mynews::News,str::String) = str in keys(mynews.hashtable)


#===
guids = String[]
for new in MyNews.news
    push!(guids,new.guid)
end

typesNews = String[]
for new in MyNews.news
    for ent in map(x->x["type"], new.entities)
        push!(typesNews,ent)
    end
end

typesNews = countmap(typesNews)
===#
