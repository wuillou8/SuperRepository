#include("JuliaCode/utilities.jl")

abstract MODEL
# model's particular Parameters
abstract MODELparams
# models particular contexts'decompo/etc...
abstract MODELcontext

#===== MODEL ===========================================#

# select users for the local model:
# if they read more than Cutoff articles in the training period
function Users4LocalModel(train_bedata::BEData, test_bedata::BEData, __cutoff::Int64)
    __selectedIds, __unselectedIds = String[], String[]

    # select users in train/test sets
    testfullusersids = getAllarticleIds(test_bedata)
    trainfullusersids = getAllarticleIds(train_bedata)
    arry = Any[]
    for user in unique(testfullusersids)
        cnt1, cnt2  = 0, 0
        for use in trainfullusersids
            if use == user
                cnt1 += 1
            end
        end
        for use in testfullusersids
            if use == user
                cnt2 += 1
            end
        end
        push!(arry,[user,cnt1,cnt2]);
    end

    # selection users for Perso
    for _arr in arry
        if _arr[2] > __cutoff
            push!(__selectedIds,_arr[1])
        else
            push!(__unselectedIds,_arr[1])
        end
    end

    __selectedIds, __unselectedIds
end

#===
# idea of doing model factory as we actually load the model might be silly or to be
# rather placed in the trainer script.
function modelsFactory(modelname::String, data::Any)
	@switch modelname begin
		"Random"; return RandomModel()
                # ...
		"model::$modelname not implemented yet" |> println
	end
end
===#

# make model from json dict
function modelsFactory(model::Dict{String,Any}, modelname::String)
  #println(modelname)
  modelname |>
  ( _ ->
      _ == "Random" ? RandomModel() :
      _ == "PersoSimple" ? PersoModel(model) :
      _ == "PersoNaiveBayes" ? PersoBernoulliNB(model) :
      _ == "PredictionIO" ? PredictionIO(model) :
      ""   )
  #===
	@switch modelname begin
		"Random"; RandomModel() # nothing to be done :-)
		"PersoSimple"; PersoModel(model)
    "PersoNaiveBayes"; PersoBernoulliNB(model)
                # ...
                "model::$modelname not implemented yet" |> println
	end
  ===#
end

#==================================================================================
               GLOBAL MODELS
==================================================================================#

   # Ids class: the computation can be restricted to subset of ids.
type Ids
    testusersIds::Vector{String}
    testnewsIds::Vector{String}
    hashtestUsage::Dict{String,Array{String,1}}

    function Ids(trainbedata::BEData, testbedata::BEData)
        testusersIds = getsourceIds(testbedata,"user")
        testnewsIds = gettargetIds(testbedata,"article")
        hashtestUsage = convert( Dict{String,Vector{String}},
                     { Id => convert(Array{String,1}, getUsageIds(testbedata, Id)) for Id in testusersIds })
        new(testusersIds, testnewsIds, hashtestUsage)
    end
end

type RandomModel <: MODEL
    RandomModel(dict::Dict{String,Any}) = new()
    RandomModel() = new()
end

#==================================================================================
               LOCAL MODELS
==================================================================================#

immutable PersoModelparams <: MODELparams
    cutoff::Int64
    PersoModelparams(cutoff::Int64) = new(cutoff)
    PersoModelparams(pmpIOObj::Dict{String,Any}) = new(pmpIOObj["cutoff"])
end

immutable PersoModelcontext <: MODELcontext
    # ids in the perso model
    persoIds::Vector{String}
    # ids in the glob model
    globalIds::Vector{String}
    PersoModelcontext(persoIds::Vector{String},globalIds::Vector{String}) = new(persoIds, globalIds)
    PersoModelcontext(ctxtIOObj::Dict{String,Any}) = new(ctxtIOObj["persoIds"], ctxtIOObj["globalIds"])
   end

# Basical Personalisation model
type PersoModel <: MODEL

    # cutoff for separating user into global//perso
    modelP::PersoModelparams
    # context parameters users allocated to global//perso model
    context::PersoModelcontext
    # global model for cold start pbm (or __globalIds)
    globModel::MODEL
    # Std. Instantiater:
    # decompose the user set into train and test subsets, based on their usage.
    function PersoModel(trainbedata::BEData, testbedata::BEData, cutoff = 30)
        persoIds, globalIds = Users4LocalModel(trainbedata, testbedata, cutoff)
        new(PersoModelparams(cutoff), PersoModelcontext(persoIds, globalIds))
    end
    # Reader from file
    function PersoModel(pmodel::Dict{String,Any})
       mparams, mcontext, globModel = pmodel |>
              (_ -> begin
        		           _["modelP"],
        		           _["context"],
        		           _["globModel"]
	     	            end )
        new(PersoModelparams(mparams), PersoModelcontext(mcontext), RandomModel(globModel))
    end
end

# Trivial model based on preference footprints
type EntityFan
    Profile::Dict{String,Int64}
#==
    keys::Array{String,1}
    values::Array{Int64}
    function UserProfile(Profile::Dict{String,Int64})
        keys = keys(Profile)
        values = values(Profile)
        new(Profile,keys,values)
    end
==#
end

# Scoring function for EntityFan model
function scoreNew(usrprof::EntityFan, bedata::BEData, guid::String)
    newents = getEntstargetMap(bedata, guid) |> keys
    score = 0.
    for ent in newents
        if ent in keys(usrprof.Profile)
            score += usrprof.Profile[ent]
        end
    end

    if length(newents) > 0
        score/length(newents), score, length(newents)
    else
        0.,0, 0
    end
end

################################################################################################
#                          NAIVE BAYESIANs                                                     #
################################################################################################

type PersoBernoulliNBparams <: MODELparams
    cutoff::Int64
    PersoBernoulliNBparams(cutoff::Int64) = new(cutoff)
    PersoBernoulliNBparams(pmpIOObj::Dict{String,Any}) = new(pmpIOObj["cutoff"])
end

type PersoBernoulliNBcontext <: MODELcontext
    # ids in the perso model
    persoIds::Vector{String}
    # ids in the glob model
    globalIds::Vector{String}
    Ents::Dict{String,Int64}
    Voc::Vector{String}
    Ndocs::Int64
    PersoBernoulliNBcontext(persoIds::Vector{String},globalIds::Vector{String},Ents::Dict{String,Int64},Voc::Vector{String},Ndocs::Int64) =
              new(persoIds, globalIds, Ents, Voc, Ndocs)
    PersoBernoulliNBcontext(_::Dict{String,Any}) = new(_["persoIds"], _["globalIds"], _["Ents"], _["Voc"], _["Ndocs"])
end

# Old Bernoulli
type PersoBernoulliNB <: MODEL
    # cutoff for statistics
    modelP::PersoBernoulliNBparams
    # context parameters users allocated to global//perso model
    context::PersoBernoulliNBcontext
    # global model for cold start pbm (or __globalIds)
    globModel::MODEL

    function PersoBernoulliNB(trainbedata::BEData, testbedata::BEData)

       cutoff = 1
       Ents = getAllEnts(trainbedata)
       Voc = convert(Vector{String},[k for k in keys(Ents)])
       Ndocs = getAllarticleIds(trainbedata) |>
                                   unique |> length
       persoIds, globalIds = Users4LocalModel(trainbedata, testbedata, cutoff)
       new(PersoBernoulliNBparams(cutoff), PersoBernoulliNBcontext(persoIds, globalIds, Ents, Voc, Ndocs))
    end

    function PersoBernoulliNB(pmodel::Dict{String,Any})
       mparams, mcontext, globModel = pmodel |>
              (_ -> begin
        		            _["modelP"],
        		            _["context"],
        		            _["globModel"]
	     	             end )
        new(PersoBernoulliNBparams(mparams), PersoBernoulliNBcontext(mcontext), RandomModel(globModel))
    end
end

#EntityFan
#    Profile::Dict{String,Int64}
#    Ents::Dict{String,Int64}
#    Voc::Vector{String}
#    Ndocs::Int64

function TrainBernoulliNB(__modelNB::PersoBernoulliNB,__usermodel::EntityFan) #generalNews::Dict{String,Int64})

    usedNews = __usermodel.Profile
    Voc = __modelNB.context.Voc
    Ntot = length(Voc)
    Nc = values(usedNews) |> sum
    Nc_ = (1.-Nc/Ntot)*Ntot |> round |> (_ -> convert(Int64,_))

    prior, prior_ = Nc/Ntot, 1. - Nc/Ntot #(Ntot - Nc)/Ntot
    probvec, probvec_ = zeros(Ntot), zeros(Ntot)

    # !!!!!
    # Version based on the available vocabulary and not the
    # available nbs of documents as in the litterature, however, this
    # should be performing better in these settings.

    # entities used
    for i in 1:Ntot
        wd = Voc[i]
        if wd in keys(usedNews)
            Nct = usedNews[wd]
        else
            Nct = 0
        end
        # with Laplace smoothing
        probvec[i] = (Nct + 1)/(Nc + 2)
    end

    # entities unused
    for i in 1:Ntot
        wd = Voc[i]
        if wd in keys(usedNews)
            Nct = 0
        else
            Nct = 1
        end
        # With Laplace smoothing
        probvec_[i] = (Nct + 1)/(Nc_ + 2)
    end

    prior, probvec, prior_, probvec_
end

function applyBernoulliNB(__model::PersoBernoulliNB, Id::String, prior::Float64, probvec::Vector{Float64})
    # following Manning's book methods.
    L = length(__model.context.Voc)
    ents = getTId(testbedata, Id) |>
            (_ -> filter(x -> x.target_entity_type == "entity", _)) |>
            (_ -> map(x -> x.value, _)) |>
            unique

    score = log(prior)
    for i = 1:L
        wd = __model.context.Voc[i]
        if wd in ents
            score += log(probvec[i])
        else
            score += log(1.-probvec[i])
        end
    end

    score
end

################################################################################################
#                          PredictionIO                                                        #
################################################################################################

abstract PIOq

immutable PIOquery <: PIOq
    user::String
    num::Int64
end

type PredictionIOparams <: MODELparams
    access_key::ASCIIString
    url::ASCIIString #String
    threads::Int64
    qsize::Int64
    PredictionIOparams(access_key::ASCIIString,url::ASCIIString,threads::Int64,qsize::Int64) =
                                                                                           new(access_key,url,threads,qsize)
    PredictionIOparams(_::Dict{String,Any}) = new(_["persoIds"], _["globalIds"], _["Ents"], _["Voc"], _["Ndocs"])
end

type PredictionIOcontext <: MODELcontext
    # PIO method
    # appId::PIOquery
    #PredictionIOcontext() = new()
   end
   #==
   client = predictionio.EventClient(
    access_key=<ACCESS KEY>,
    url=<URL OF EVENTSERVER>,
    threads=5,
    qsize=500
    ) ===#

type PredictionIO <: MODEL
    modelP::PredictionIOparams
    context::PredictionIOcontext
    #appId::PIOquery
    PredictionIO() = new(PredictionIOparams("bla","bla",1,1), PredictionIOcontext())

    function PredictionIO(pmodel::Dict{String,Any})
        mparams, mcontext = pmodel |>
              (_ -> begin
        		            _["modelP"],
        		            _["context"]#,
        		            #_["globModel"]
	     	             end )
        new(PersoBernoulliNBparams(mparams), PersoBernoulliNBcontext(mcontext)) #, RandomModel(globModel))
    end
end

#===
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
===#

#==================================================================================
               MODEL FUNCTIONALITIES
==================================================================================#
#      train
function train(myModel::RandomModel, mode::String, data = Any[])
    #if mode == "Random"
    #	myModel.globModel = RandomModel()
    #elseif() train with data
    #end
end

function train(myModel::PersoModel, mode::String, data = Any[])
    if mode == "Random"
        myModel.globModel = RandomModel()
        #elseif() train with data
    end
end

function train(myModel::PersoBernoulliNB, mode::String, data = Any[])
    if mode == "Random"
        myModel.globModel = RandomModel()
        #elseif() train with data
    end
end

train(myModel::PredictionIO, mode::String, data = Any[]) = "" #myModel = myModel

Merge!(usrprof::EntityFan, hashDict) = merge!(usrprof.Profile, hashDict)



#===
function BernoulliNB(trainUsage::DataFrame, trainNews::News)
    getAllEnts(trainbedata), newsEnts = GetEntities(trainUsage, trainNews)
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
===#



#====

# Old Bernoulli
type BernoulliNB <: MODEL
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

    function BernoulliNB(trainUsage::DataFrame, trainNews::News)
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

    function BernoulliNB(trainUsage::DataFrame, trainNews::News, __CutOff::Int64)
        # Build up Bernoulli Naive Bayesian model.
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
    end
end
====#
