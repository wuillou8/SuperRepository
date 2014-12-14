
abstract MODEL
# model's particular Parameters
abstract MODELparams
# models particular contexts'decompo/etc...
abstract MODELcontext

# idea of doing model factory as we actually load the model might be silly or to be 
# rather placed in the trainer script.
function modelsFactory(modelname::String, data::Any)
	@switch modelname begin
		"Random"; return RandomModel()
                # ... 
		"model::$modelname not implemented yet" |> println
	end
end

# make model from json dict
function modelsFactory(model::Dict{String,Any}, modelname::String)
	@switch modelname begin
		"Random"; return RandomModel() # nothing to be done :-)
		"PersoSimple"; return PersoModel(model)
                # ...
                "model::$modelname not implemented yet" |> println
	end
end


#==================================================================================
               GLOBAL MODELS
==================================================================================#

type RandomModel <: MODEL
    #myparams::String
    # reader from JSON file
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

###    FUNCTIONALITIES    ###
#      train
function train(myModel::PersoModel, mode::String, data = Any[])
    if mode == "Random"
        myModel.globModel = RandomModel()
        #elseif() train with data
    end
end
function train(myModel::RandomModel, mode::String, data = Any[])
    #if mode == "Random"
    #	myModel.globModel = RandomModel()
    #elseif() train with data
    #end
end

Merge!(usrprof::EntityFan, hashDict) = merge!(usrprof.Profile, hashDict)

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

