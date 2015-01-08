
function appendtofile( filepath::String, str::String )
    # append mode
    FILE = open(filepath, "a")
    write(FILE, str)
    close(FILE)
end

function cleanfile(filepath::String)
    # "refresh" file (delete file elements)
    FILE = open(filepath, "w+")
    close(FILE)
end

# readin which model//settings
function trainModel(__modelName::String = "Random", __submodel::String = "Random")
    "building model: $__modelName // $__submodel" |> println
    # read in events for training
    # test events needed for the "local models"
test_bedata = getDataUsage("DataBase/data4test.json")
    # read in event for training
  train_bedata = getDataUsage("DataBase/data4train.json")
    # filter out test UsersId and NewsId
    # create hash table
	  testnewsIds = gettargetIds(test_bedata,"article")
	  testusersIds = getsourceIds(test_bedata,"user")


 # __myModel =  PersoBernoulliNB(train_bedata, test_bedata)
    # instantiate and train models:
    # here we have PersoSimple
    __myModel = __modelName |>
                (_ -> _ == "Random" ? RandomModel() :
                      _ == "PersoSimple" ? PersoModel(train_bedata, test_bedata) :
                      _ == "PersoNaiveBayes" ? PersoBernoulliNB(train_bedata, test_bedata) :
                      _ == "PredictionIO" ? PredictionIO() :
                       "trainModel.jl:: model::$_ not recognised"  )

    # train
	  train(__myModel, __submodel)

    # store trained model
	      __trainmodelpath = "DataBase/trainedmodel$__modelName.json"
	      out = open(__trainmodelpath,"w+")
	      JSON.print(out,__myModel)
	      close(out)
        __myIds = Ids(train_bedata, test_bedata)

    return __myModel, train_bedata, test_bedata, __myIds
  end


 function loadmodel(__modelName::String = "Random")
    # load/instantiate/append model
    println("DBG1")
    __model = "DataBase/trainedmodel$__modelName.json" |>
                                        JSON.parsefile |> (_ -> modelsFactory(_,  __modelName))

    return __model
  end

  function loaddata(__traindatapath::String = "DataBase/data4train_short.json", __testdatapath::String = "DataBase/data4test_short.json")
      "load data: traindata: $__traindatapath // testdata: $__testdatapath" |> println
      # read in events for training
	    train_bedata = getDataUsage("DataBase/data4train_short.json")
      # test events needed for the "local models"
      test_bedata = getDataUsage("DataBase/data4test_short.json")
      # make Ids element
      ids = Ids(train_bedata, test_bedata)

      return train_bedata, test_bedata, ids
  end

  function recommend(gm::GlobalModel, __userId::String = "")

      __userId = "987d1a033896bb4214b0586e64f6805ee8e80564"
      recommenderList( gm, __userId )
  end



