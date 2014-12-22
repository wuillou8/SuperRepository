using JSON
using Dates #Time
#using Lazy #, StatsBase

include("JuliaCode/classes.jl")
include("JuliaCode/models.jl")


# readin which model//settings
	__model = ARGS[1]
	__submodel = ARGS[2]
  #__modelNb = ARGS[3]

# read in event for training
	__traindatapath = "DataBase/data4train.json"
  STDIN = open(__traindatapath)
	train_bedata = BEData( STDIN )
	__testdatapath = "DataBase/data4test.json"
	STDIN = open(__testdatapath)
  test_bedata = BEData( STDIN )




# filter out test UsersId and NewsId
# create hash table
	testnewsIds = gettargetIds(test_bedata,"article")
	testusersIds = getsourceIds(test_bedata,"user")

# instantiate and train models:
# here we have PersoSimple
	__myModel = __model |>
                (_ -> _ == "Random" ? RandomModel() :
                      _ == "PersoSimple" ? PersoModel(train_bedata, test_bedata) :
                      _ == "PersoNaiveBayes" ? PersoBernoulliNB(train_bedata, test_bedata) :
                       "trainModel.jl:: model::$_ not recognised"  )

                #====
                @switch __model begin
                        "Random" ; RandomModel()
                        "PersoSimple" ; PersoModel(train_bedata, test_bedata)
                        "PersoNaiveBayes" ;  PersoBernoulliNB(train_bedata, test_bedata)
                        #    ...
                             "trainModel.jl:: model::$__model not recognised" |> println
		                 exit()
                end
                ====#

# train
	train(__myModel, __submodel)

# store trained model
	__trainmodelpath = "DataBase/trainedmodel$__model.json"
	out = open(__trainmodelpath,"w+")
	JSON.print(out,__myModel)
	close(out)
