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

    # Postprocess
    map(_ -> evaluate(_),__perfs)
    __random = map(x -> x/length(__testnewsIds),__recommSizes)

    # Random values for plot
    __N = length(__testusersIds)
    __mrr_meas = map(x -> x[1]/x[2],__mrr_meas)
    __mrr_rand = convert(Array{Float64,1},[ MRR_Meas(__testnewsIds, nb) for nb in __recommSizes ])
    __perfs_rank = PerfoRank( __N,__mrr_meas,__mrr_rand) #,__random )

    __perfs, __perfs_rank, __random
end

#TestPerfos(::SubString{ASCIIString}, ::Array{String,1}, ::Array{String,1}, ::BEData, ::BEData, ::Array{Int64,1})
