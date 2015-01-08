using Logging

# Tests
#===
function Test(  )
   for userId in testusersIds
        recoList = #recommenderList( __model, __testnewsIds, userId )
                   recommenderList( __model, __testnewsIds, userId, __trainbedata, __testbedata )

        usage = hashtestUsage[userId]

        for i = 1:length(__recommSizes)
            Nrec = __recommSizes[i]
            [ add(__perfs[i], perfoMeasOpt(__testnewsIds,recoList[1:Nrec],use)) for use in usage ]
            __mrr_meas[i] += MRR_Meas(recoList[1:Nrec], usage)
        end
    end
end
===#

# Main test function
function TestPerfos( __model::MODEL,
                     __testusersIds::Array{String,1}, __testnewsIds::Array{String,1},
                     __trainbedata::BEData, __testbedata::BEData,
                     __recommSizes )

    __perfs = [ Perfo(0,0,0,0) for i in __recommSizes ]
    __mrr_meas = [ [0.,0] for i in __recommSizes ]

    #@Logging.configure(level=DEBUG)
    if isa(__model,PredictionIO)

        http = try
            HttpHandler() do req::Request, res::Response

                for userId in __testusersIds
                    # response/query to  predictionIO
                    PIOquery( userId, length(testnews) ) |> JSON.json |> res.Response

                    # handle predictionIO as request
                    reqlist = req.resource |>
                    (_ -> ismatch(r"^/recommendIO/?", _) ? # recommend/dddd/
                              begin
                                  val = try
                                      match(r"^/recommendIO/(\w+)/?$", _) |>
                                      (_ -> Recommendation( recommend(g_Comput, _.captures[1])) )
                                  catch e
                                      #@error("kale_connector.jl::recommendIO $e")
                                      500
                                  end
                                  val
                               end   : 500
                    )

                    recoList = JSON.parse(reqlist)["reclist"]
                    usage = hashtestUsage[userId]

                    for i = 1:length(__recommSizes)
                        Nrec = __recommSizes[i]
                        [ add(__perfs[i], perfoMeasOpt(__testnewsIds,recoList[1:Nrec],use)) for use in usage ]
                        __mrr_meas[i] += MRR_Meas(recoList[1:Nrec], usage)
                    end

                end
            end

        catch e
            pritnln("errrorrr")
            #@error("testHarness.jl::TestPerfos::HttpHandler $e")
        end

    else
        for userId in __testusersIds
            recoList =
                    recommenderList( __model, __testnewsIds, userId, __trainbedata, __testbedata )
            usage = hashtestUsage[userId]

            for i = 1:length(__recommSizes)
                Nrec = __recommSizes[i]
                [ add(__perfs[i], perfoMeasOpt(__testnewsIds,recoList[1:Nrec],use)) for use in usage ]
                __mrr_meas[i] += MRR_Meas(recoList[1:Nrec], usage)
            end
        end
    end

    # Postprocess
    map(_ -> evaluate(_),__perfs)
    __random = map(x -> x/length(__testnewsIds),__recommSizes)

    # Random values for plot
    __N = length(__testusersIds)
    __mrr_meas = map(x -> x[1]/x[2],__mrr_meas)
    __mrr_rand = convert(Array{Float64,1},[ MRR_Meas(__testnewsIds, nb) for nb in __recommSizes ])
    __perfs_rank = PerfoRank( __N,__mrr_meas,__mrr_rand)

    __perfs, __perfs_rank, __random
end

# Main test function
function TestPerfos2( __gmodel::GlobalModel, __recommSizes::Array{Int64,1} ) #Vector{Int64} ) #String,

    __model =__gmodel.model
    __testusersIds = __gmodel.ids.testusersIds
    __testnewsIds = __gmodel.ids.testnewsIds
    __trainbedata = __gmodel.trainbedata
    __testbedata = __gmodel.testbedata
    __hashtestUsage = __gmodel.ids.hashtestUsage
    __perfs = [ Perfo(0,0,0,0) for i in __recommSizes ]
    __mrr_meas = [ [0.,0] for i in __recommSizes ]

    #get("http://localhost:8000/retrain/$__modelName")
    #@Logging.configure(level=DEBUG)
    for userId in __testusersIds
        recoList = recommenderList( __model, __testnewsIds, userId, __trainbedata, __testbedata )
        usage = __hashtestUsage[userId]

            for i = 1:length(__recommSizes)

                Nrec = __recommSizes[i]
                if Nrec <= length(recoList)
                    [ add(__perfs[i], perfoMeasOpt(__testnewsIds,recoList[1:Nrec],use)) for use in usage ]
                    __mrr_meas[i] += MRR_Meas(recoList[1:Nrec], usage)
                else
                    "pass"
                end
            end
    end


    # Postprocess
    map(_ -> evaluate(_),__perfs)
    __random = map(x -> x/length(__testnewsIds),__recommSizes)

    # Random values for plot
    __N = length(__testusersIds)
    __mrr_meas = map(x -> x[1]/x[2],__mrr_meas)
    __mrr_rand = convert(Array{Float64,1},[ MRR_Meas(__testnewsIds, nb) for nb in __recommSizes ])
    __perfs_rank = PerfoRank( __N,__mrr_meas,__mrr_rand)

    return __perfs, __perfs_rank, __random
end
