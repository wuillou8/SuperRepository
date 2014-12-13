using JSON
using Dates #Time
using Lazy, StatsBase

include("classes.jl")
include("models.jl")


# readin which model//settings
	__model = ARGS[1]; #"Random" 
	__submodel = ARGS[2]; #"Random"
        __modelNb = ARGS[3]

# read in event for training
	__traindatapath = "DataBase/datafortraining.json"
	train_bedata = BEData( JSON.parsefile(__traindatapath) )
	__testdatapath = "DataBase/datafortesting.json"
	test_bedata = BEData( JSON.parsefile(__testdatapath) )

# filter out test UsersId and NewsId 
# create hash table
	testnewsIds = gettargetIds(test_bedata,"article")
	testusersIds = getsourceIds(test_bedata,"user")

# instantiate and train models:
# here we have PersoSimple
	# if PersoSimple
	if __model == "Random"
	__myModel = 
 		RandomModel()
	elseif __model == "PersoSimple"
	__myModel = 
		PersoModel(train_bedata, test_bedata)
		#if modelToTrain2 == "Random"
		#	__myModel.globModel = RandomModel()
		#end
	else 
		"trainModel.jl:: model::$__model not recognised" |> println
		exit()
	end
	# 	...

# train 
	train(__myModel, __submodel)

# store trained model
	__trainmodelpath = "DataBase/trainedmodel$__model$__modelNb.json"
	out = open(__trainmodelpath,"w+")
	JSON.print(out,__myModel)
	close(out)


#"model trained: $__model  $__submodel" |> println
