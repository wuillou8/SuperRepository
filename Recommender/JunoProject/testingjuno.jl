using DataArrays, RDatasets, DataFrames
using Requests
using PyPlot
using Lazy
using Dates
include("DataFramesMeta.jl")
using DataFramesMeta;

# Function decomposing data into test and train subsets:
# T1 < T2 < T3,
# train data: T1 -> T2,
# test data: t2 -> T3.
function PrepareDataForTest( dfusage::DataFrame, mynews::News, T1::DateTime, T2::DateTime, T3::DateTime )

    t1 = time()
    # filter operation don in two steps
    df = @> begin
            dfusage[[:Date,:AppUser_id,:EventName,:EventDetail,:EventValue,:Country,:Custom1]]
            @transform( TestTrain = map(x->getDateTime(x) < T2, :Date) )
            @transform( TestTrain2 = map(x->getDateTime(x) < T3, :Date) )
            @transform( DateJulia = map(x->getDateTime(x), :Date) )

        end
    trainUsage = @where(df, :TestTrain .== true)[[:DateJulia,:AppUser_id,:EventName,:EventDetail,:EventValue,:Country,:Custom1]]
    testUsage = @where(df, :TestTrain .== false) #, :TestTrain2 .== true)[[:DateJulia,:AppUser_id,:EventName,:EventDetail,:EventValue,:Country,:Custom1]];
    testUsage = @where(testUsage, :TestTrain2 .== true)[[:DateJulia,:AppUser_id,:EventName,:EventDetail,:EventValue,:Country,:Custom1]];
    t2 = time()
    println("run Usage Selection: ",t2 - t1)

    #T3 = maximum(testUsage[:DateJulia])
    # decompose news into two sets.
    t1 = time()
    trainNews = News(filter(x -> (DateTime(x.date) < T2), mynews.news))
    trainNews = News(filter(x -> (DateTime(x.date) >= T1), trainNews.news))
    testNews = News(filter(x -> (DateTime(x.date) >= T2), mynews.news))
    testNews = News(filter(x -> (DateTime(x.date) < T3), testNews.news))
    t2 = time()
    println("run News Selection: ",t2 - t1)

    println("News:: train dates, min: ", minimum(map(x -> DateTime(x.date), trainNews.news)), " max: ", maximum(map(x -> DateTime(x.date), trainNews.news)))
    println("Usage:: train dates, min: ", minimum(trainUsage[:DateJulia]), " max: ", maximum(trainUsage[:DateJulia]))
    println("News:: test dates, min: ", minimum(map(x -> DateTime(x.date), testNews.news)), " max: ", maximum(map(x -> DateTime(x.date), testNews.news)))
    println("Usage:: test dates, min: ", minimum(testUsage[:DateJulia]), " max: ", maximum(testUsage[:DateJulia]))

    trainUsage, testUsage, trainNews, testNews
end

function PrepareUsage4Test( dfusage::DataFrame, T1::DateTime, T2::DateTime, T3::DateTime )
        t1 = time()
    # filter operation done in two steps because bad docu of DataFrame and small brain...
    df = @> begin
            dfusage[[:Date,:AppUser_id,:EventName,:EventDetail,:EventValue,:Country,:Custom1]]
            @transform( TestTrain = map(x->getDateTime(x) < T2, :Date) )
            @transform( TestTrain2 = map(x->getDateTime(x) < T3, :Date) )
            @transform( DateJulia = map(x->getDateTime(x), :Date) )

        end
    trainUsage = @where(df, :TestTrain .== true)[[:DateJulia,:AppUser_id,:EventName,:EventDetail,:EventValue,:Country,:Custom1]]
    testUsage = @where(df, :TestTrain .== false)
    testUsage = @where(testUsage, :TestTrain2 .== true)[[:DateJulia,:AppUser_id,:EventName,:EventDetail,:EventValue,:Country,:Custom1]];
    t2 = time()
    println("run Usage Selection: ",t2 - t1)
    println("Usage:: train dates, min: ", minimum(trainUsage[:DateJulia]), " max: ", maximum(trainUsage[:DateJulia]))
    println("Usage:: test dates, min: ", minimum(testUsage[:DateJulia]), " max: ", maximum(testUsage[:DateJulia]))
    trainUsage, testUsage
end

function PrepareNews4Test( mynews::News, T1::DateTime, T2::DateTime, T3::DateTime )

    # decompose news into two sets.
    t1 = time()
    # T2+Day(1) allow to loose less data. some news where read before publication within the data...
    trainNews = News(filter(x -> (DateTime(x.date) < T2+Day(1)), mynews.news))
    trainNews = News(filter(x -> (DateTime(x.date) >= T1), trainNews.news))
    testNews = News(filter(x -> (DateTime(x.date) >= T2), mynews.news))
    testNews = News(filter(x -> (DateTime(x.date) < T3), testNews.news))
    t2 = time()
    println("run News Selection: ",t2 - t1)

    println("News:: train dates, min: ", minimum(map(x -> DateTime(x.date), trainNews.news)), " max: ", maximum(map(x -> DateTime(x.date), trainNews.news)))
    println("News:: test dates, min: ", minimum(map(x -> DateTime(x.date), testNews.news)), " max: ", maximum(map(x -> DateTime(x.date), testNews.news)))
    trainNews, testNews
end


# Prepare Usage data for test
function PrepareTest( mynews::News, cntry::String, T1::DateTime, T2::DateTime, T3::DateTime)

    # read usage data
    dfusage = readtable(PATH*"DATA/"*cntry*"traintest0717_1120.csv")

    # separate into train and test sets
    trainUsage, testUsage, trainNews, testNews = PrepareDataForTest( df, mynews, T1, T2, T3 )
    #PrepareUsage4Test( df, T1, T2, T3 )
    trainUsage, testUsage, trainNews, testNews
end

# Prepare Usage data for test
# this function decompose data usage into clusters.
function Prepare4Test(usage::DataFrame, cntrsModel::Countries, T1::DateTime, T2::DateTime, T3::DateTime)

    for cntry in cntrsModel.labels
        # Filter elements belonging to cluster entity.
        # Here this was done elsewhere and we just import the contry data
        # usage => there should be a model.
        dfusage = readtable(PATH*"DATA/"*cntry*"traintest0717_1120.csv")

        # separate into train and test sets. We might also want a cross validation set later
        trainUsage, testUsage = PrepareUsage4Test( dfusage, T1, T2, T3 )


        # Store the preprocessed set into the database. At this point files in the pseudoDB directory...
        writetable( "pseudoDBASE/trainUsage"*cntry*".csv", trainUsage)
        writetable( "pseudoDBASE/testUsage"*cntry*".csv", testUsage)
    end
end

# idem
function Prepare4Test(mynews::News, chanlModel::Channels, T1::DateTime, T2::DateTime, T3::DateTime)

    for chanl in chanlModel.labels
        # Filter elements belonging to cluster entity.
        # ... no model yet:
        mynews = mynews

        # separate into train and test sets. We might also want a cross validation set later
        trainNews, testNews = PrepareNews4Test( mynews, T1, T2, T3 )
        # Store the preprocessed set into the database. At this point files in the pseudoDB directory...
        out1, out2 = open("pseudoDBASE/trainNews"*chanl*".json","w+"), open("pseudoDBASE/testNews"*chanl*".json","w+")
        #trainNews = map(x -> Newprint(x), trainNews)
        #testNews = map(x -> Newprint(x), testNews)
        JSON.print(out1, trainNews)
        JSON.print(out2, testNews)
        close(out1)
        close(out2)
    end
end

# function extracting the entities from
# News and Usage training samples.
function GetEntities(trainUsage::DataFrame, trainNews::News)

    # get Entities from Usage
    t1 = time()
    usedEnts = String[]
    for id in unique(trainUsage[:Custom1])
        new = getguid(trainNews,id)
        for ent in map(x->x["value"], new.entities)
            push!(usedEnts,ent)
        end
    end
    t2 = time()
    t2 - t1
    println("Get Entities from Usage: ", t2 - t1)

    # get Entities from News
    t1 = time()
    newsEnts = String[]
    for new in unique(trainNews.news)
        for ent in map(x->x["value"], new.entities)
            push!(newsEnts,ent)
        end
    end
    t2 = time()
    println("Get Entities from News: ", t2 - t1)

    usedEnts, newsEnts
end

# function correcting the statistics for the fact that news ids are not p
# present within the news test sample.
function Correction(testNews::News, testUsage::DataFrame)
    idsNews = map(x->x.guid,testNews.news)
    t = 0
    for i in unique(testUsage[:Custom1])
        if i in idsNews
            t+=1
        end
    end
    length(unique(testUsage[:Custom1]))/t
end

# function collecting the scores.
# modelname specify which scores array is to be used
function EvaluatePerfo(testNews::News, testUsage::DataFrame, modelname::String, scores::Array{Float64,1}, Nrec::Int64)

    arr = Int64[]
    @switch modelname begin
        "random"; [ push!( arr,rand(1:length(testNews.news)) ) for i = 1:Nrec ]
        "naivebayes"; arr = findNMax( scores+1000, Nrec )
        "model not recognised"
    end

    recoList, pickList = String[], Int64[]
    [push!(recoList,testNews.news[i].guid) for i in arr ]

    idsNews = unique(map(x->x.guid,testNews.news)) #unique(testUsage[:Custom1])
    usage = countmap(testUsage[:Custom1])

    perf = Perfo(0,0,0,0)
    for id in idsNews
        if id in recoList
            if id in keys(usage)
                perf.tp += usage[id]
                #push!(pickList,1)
            else
                perf.fp += 1
                #push!(pickList,0)
            end
        else # not in recommendation list
            if id in keys(usage)
                perf.fn += usage[id]
                #push!(pickList,1)
            else
                perf.tn += 1
                #push!(pickList,0)
            end

      end
    end

    #println("arr ",length(arr))
    #println("uniqarr ",length(unique(arr)))
    check = 0
    for id in keys(usage)
        if usage[id] > 1
            check += usage[id] - 1
        end
    end

    #println( "Check: ", perf.tp+perf.tn+perf.fp+perf.fn, " =?= ", length(idsNews), " ", check)
    #+sum(values(usage))- length(keys(usage)) - 2*check , " ", check )

    Precis(perf) , Recall(perf), Specif(perf), F1(perf)
end
# function collecting the scores.
# modelname specify which scores array is to be used
function EvaluatePerfoSAVE(testNews::News, testUsage::DataFrame, modelname::String, scores::Array{Float64,1}, Nrec::Int64)

    arr = Int64[]
    @switch modelname begin
        "random"; [ push!( arr,rand(1:length(testNews.news)) ) for i = 1:Nrec ]
        "naivebayes"; arr = findNMax( scores+1000, Nrec )
        "model not recognised"
    end

    recoList, pickList = String[], Int64[]
    [push!(recoList,testNews.news[i].guid) for i in arr ]

    idsNews = map(x->x.guid,testNews.news) #unique(testUsage[:Custom1])
    usag = (unique(testUsage[:Custom1]))
    perf = Perfo(0,0,0,0)
    for id in testUsage[:Custom1]
      if id in idsNews
        if id in recoList
            perf.tp += 1
            push!(pickList,1)
        else
            perf.fn += 1
            push!(pickList,0)
        end
      end
    end


    #println(perf.tp+perf.fp, " VS ")
    # doing the correction this
    ##corr = Correction(testNews,testUsage)
    ##println("corr factor:  ",corr)
    ##perf.tp = int(corr*perf.tp)
    ##perf.fp = int(perf.fp/corr)
    Precis(perf)
end

# Evaluation of precision with ROC AUC
function EvaluateROC(testNews::News, testUsage::DataFrame, scores::Array{Float64,1})

    arr = Int64[]
    Nrec = length(scores)
    arr = findNMax( scores+1000, Nrec )

    recoList, pickList = String[], Int64[]
    [push!(recoList,testNews.news[i].guid) for i in arr ]

    idsNews = map(x->x.guid,testNews.news) #unique(testUsage[:Custom1])
    perf = Perfo(0,0,0,0)
    #for id in testUsage[:Custom1]
      #if id in idsNews
    usageIds =  unique(testUsage[:Custom1])
    for id in recoList
        if id in usageIds
            #perf.tp += 1
            push!(pickList,1)
        else
            #perf.fp += 1
            push!(pickList,0)
        end
    end
    #println(perf.tp+perf.fp, " VS ")
    # doing the correction this
    ##corr = Correction(testNews,testUsage)
    ##println("corr factor:  ",corr)
    ##perf.tp = int(corr*perf.tp)
    ##perf.fp = int(perf.fp/corr)
    scores, pickList
end

# create precision arrays for plotting.
function makePrecisions(testNews::News,testUsage::DataFrame,scores::Array{Float64,1})
    perfoNB = Float64[]
    for i = 1:1:200
        str = convert(String,"naivebayes")
        push!(perfoNB, EvaluatePerfo(testNews, testUsage, "naivebayes", scores, i)[1])
    end
    perfoRDM = Float64[]
    [ push!(perfoRDM,i/length(testNews.news)) for i in 1:1:200 ]
    perfoNB, perfoRDM
end

# plot
function plotPrecRandVSNB(testNews::News,testUsage::DataFrame,scores::Array{Float64,1}) #perfoNB::Array{Float64,1}, perfoRDM::Array{Float64,1})
    perfoNB = Float64[]
    for i = 1:1:200
        str = convert(String,"naivebayes")
        push!(perfoNB, EvaluatePerfo(testNews, testUsage, "naivebayes", scores, i))
    end
    perfoRDM = Float64[]
    [ push!(perfoRDM,i/length(testNews.news)) for i in 1:1:200 ]
    perfoNB, perfoRDM

    xarr = [1:1:200]
    plt.xlim([0,210])
    plt.plot(xarr,perfoRDM,"*")
    plt.plot(xarr,perfoNB,"o")
    plt.legend(["random","NaiveBayes on Entities"], "upper left")
    plt.title("Performance Comparison")
    plt.xlabel("Recomm List size")
    plt.ylabel("Precision (tp/tp+fp)")
end

# plot
function plotPrecRandVSNB2(testNews::News,testUsage::DataFrame,scores::Array{Float64,1}) #perfoNB::Array{Float64,1}, perfoRDM::Array{Float64,1})
    perfoNB = Float64[]
    for i = 1:1:200
        str = convert(String,"naivebayes")
        # plot the recall
        push!(perfoNB, EvaluatePerfo2(testNews, testUsage, "naivebayes", scores, i)[2])
    end
    perfoRDM = Float64[]
    [ push!(perfoRDM,i/length(testNews.news)) for i in 1:1:200 ]
    perfoNB, perfoRDM

    xarr = [1:1:200]
    plt.xlim([0,210])
    plt.plot(xarr,perfoRDM,"*")
    plt.plot(xarr,perfoNB,"o")
    plt.legend(["random","NaiveBayes on Entities"], "upper left")
    plt.title("Performance Comparison")
    plt.xlabel("Recomm List size")
    plt.ylabel("Precision (tp/tp+fp)")
end
#===
function plotROCAUC(testNews::News,testUsage::DataFrame,scores::Array{Float64,1})

  rocarr = EvaluateROC(testNews, testUsage, modelname, scores, Nrec)
  include("ROC/roc.jl")
  include("ROC/rocdata.jl")
  include("ROC/rocplot.jl")

  using ROC
  #using Base.Test
  #using DataFrames

  data = readtable("ROCRdata.csv")
  curve = roc(data[:,1],data[:,2],1)
  @test abs( AUC(curve) - 0.834187 ) < 0.000001 # ROCR 0.8341875
  @test abs( AUC(curve, 0.01) - 0.000329615 ) < 0.000000001 # ROCR 0.0003296151
  @test abs( AUC(curve, 0.1) - 0.0278062 ) < 0.0000001 # ROCR 0.02780625

end
===#
