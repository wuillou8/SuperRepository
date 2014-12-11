
# Main test function
function TestPerfos(__model::MODEL,  __testusersIds::Array{String,1}, __recommSizes) 

    __perfs = [ Perfo(0,0,0,0) for i in __recommSizes ]
    __mrr_meas = [ [0.,0] for i in __recommSizes ]

    for userId in testusersIds
        recoList = recommenderList( __model, testnewsIds, userId )
        usage = hashtestUsage[userId]

        for i = 1:length(__recommSizes)
            Nrec = __recommSizes[i]
            [ add(__perfs[i], perfoMeasOpt(testnewsIds,recoList[1:Nrec],use)) for use in usage ]
            __mrr_meas[i] += MRR_Meas(recoList[1:Nrec], usage)
        end
    end

    # Postprocess 
    map(_ -> evaluate(_),__perfs)
    # Random values plot
    __random = map(x -> x/length(testnewsIds),__recommSizes)
    __mrr_meas = map(x -> x[1]/x[2],__mrr_meas)
    __mrr_rand = convert(Array{Float64,1},[ MRR_Meas(testnewsIds, nb) for nb in __recommSizes ])

    __perfs, __mrr_meas, __mrr_rand, __random
end
