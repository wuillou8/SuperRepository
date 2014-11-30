abstract Model

#=====================================
    Bayesian Model For Entities
=====================================#

# Old Bernoulli
type BernoulliNB <: Model
    Voc::Array{String,1}
    Nc::Int64
    Nc_::Int64
    prior::Float64
    prior_::Float64
    probvec::Array{Float64,1}
    probvec_::Array{Float64,1}

    function BernoulliNB( Voc::Array{String,1},Nc::Int64,Nc_::Int64,
                          prior::Float64, prior_::Float64,
                          probvec::Array{Float64,1}, probvec_::Array{Float64,1})
        new(Voc,Nc,Nc_,prior,prior_,probvec,probvec_)
    end

    function BernoulliNB(trainUsage::DataFrame,trainNews::News)
        usedEnts, newsEnts = GetEntities(trainUsage, trainNews)
        usedNews = countmap(usedEnts)
        generalNews = countmap(newsEnts)
        Voc = unique(newsEnts)

        Ndocs = length(unique(trainNews.news))
        Nc = length(unique(trainUsage[:Custom1]))
        Nc_ = Ndocs - Nc
        prior, prior_ = Nc/Ndocs, Nc_/Ndocs

        probvec, probvec_ = TrainBernoulliNB(usedNews,generalNews, Voc, Nc, Nc_)

        new(Voc,Nc,Nc_,prior,prior_,probvec,probvec_)
    end

    function BernoulliNB(trainUsage::DataFrame,trainNews::News, __CutOff::Int64)
        usedEnts, newsEnts = GetEntities(trainUsage, trainNews)

        usedNews = countmap(usedEnts)
        generalNews = countmap(newsEnts)

        arr = String[]
        for k in keys(generalNews)
            if generalNews[k] >= __CutOff
            push!(arr,k)
            end
        end

        arr2 = String[]
        for k in keys(usedNews)
            if k in arr
                push!(arr2,k)
            end
        end

        generalNews = convert(Dict{String,Int64},{ k => generalNews[k] for k in arr })
        usedNews = convert(Dict{String,Int64},{ k => usedNews[k] for k in arr2 })
        Voc = unique(arr)

        Ndocs = length(unique(trainNews.news))
        Nc = length(unique(trainUsage[:Custom1]))
        Nc_ = Ndocs - Nc
        prior, prior_ = Nc/Ndocs, Nc_/Ndocs

        probvec, probvec_ = TrainBernoulliNB(usedNews,generalNews, Voc, Nc, Nc_)

        new(Voc,Nc,Nc_,prior,prior_,probvec,probvec_)
    end
end


function TrainBernoulliNB(usedNews::Dict{String,Int64},generalNews::Dict{String,Int64},
    Voc::Array{String,1}, Nc::Int64, Nc_::Int64)
    L = length(Voc)
    probvec = zeros(L)
    probvec_ = zeros(L)

    # entities used
    for i in 1:L
        wd = Voc[i]
        if wd in keys(usedNews)
            Nct = usedNews[wd]
        else
            Nct = 0 #Laplace smoothing
        end
        probvec[i] = (Nct + 1)/(Nc + 2)
    end

    # entities unused
    #=
    for i in 1:L
        wd = Voc[i]
        if wd in keys(generalNews)
            Nct = generalNews[wd] - usedNews[wd]
        else
            Nct = 0
        end
        probvec_[i] = (Nct + 1)/(Nc_ + 2) # Laplace smoothing + 1
    end
    =#

    probvec, probvec_
end

function ApplyBernoulliNB(modelNB::BernoulliNB, news::News, id::String)
    L = length(modelNB.Voc)
    new = getguid(news,id)
    ents= String[]
    for ent in map(x->x["value"], new.entities)
        push!(ents,ent)
    end

    score = log(modelNB.prior)
    for i = 1:L
        wd = modelNB.Voc[i]
        if wd in ents #keys(voc)
            score += log(modelNB.probvec[i])
            #println(probvec[i]," ", score)
        else
            score += log(1.-modelNB.probvec[i])
        end
    end
    score
end


#===
function ApplyBernoulliNB2(modelNB::BernoulliNB, news::News, id::String)
    L = length(modelNB.Voc)
    new = getguid(news,id) # pass a New element instead
    ents= String[]
    for ent in map(x->x["value"], new.entities) # externalise
        push!(ents,ent)
    end

    score = log(modelNB.prior)
    for ent in ents
      tmp = 0
      try
        tmp += log(modelNB.probvec[i])
      catch
        pass
      end
      score += tmp

    for i = 1:L
        wd = modelNB.Voc[i]
      if wd in ents #keys(voc) # use try catch
        score += log(modelNB.probvec[i])
            #println(probvec[i]," ", score)
        #else
        #    score += log(1.-probvec[i])
      end
    end
    score
end
===#

