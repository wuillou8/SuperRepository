#=========================================================
        Global Model for:
                          Recommendation
                          TestHarness
=========================================================#

type PerfoMeasure
    perfs::Vector{Vector{Perfo}}
    perfs_ranks::Vector{PerfoRank}
    randoms::Vector{Vector{Float64}}
    modelNames::Vector{String}
    #outresults = Vector{OUTPUTRES}
    PerfoMeasure() = new(Vector{Perfo}[], PerfoRank[], Vector{Float64}[], String[])
end

type GlobalModel
    model::MODEL
    trainbedata::BEData
    testbedata::BEData
    ids::Ids
    perfo::PerfoMeasure

    # void initialiser
    GlobalModel() = new()
end

# model type
getmodelType(gm::GlobalModel) = typeof(gm.model) |>
                                       (_ -> _ == RandomModel ? "Random" :
                                             _ == PersoModel ? "PersoSimple" :
                                             _ == PersoBernoulliNB ? "PersoNaiveBayes" :
                                             _ == PredictionIO ? "PredictionIO" :
                                                 "Model not recognised" )

#update(gm::GlobalModel,model::MODEL)  = gm.model = model
update(gm::GlobalModel,model::RandomModel) = gm.model = model
update(gm::GlobalModel,tupl::(RandomModel,Ids)) = begin
                                                      gm.model = tupl[1]
                                                      gm.ids = tupl[2]
                                                  end

update(gm::GlobalModel,__tupl::(BEData,BEData,Ids)) = begin
                                                      gm.trainbedata = __tupl[1]
                                                      gm.testbedata = __tupl[2]
                                                      gm.ids = __tupl[3]
                                                  end

update(gm::GlobalModel,__tupl::(RandomModel,BEData,BEData,Ids)) = begin
                                                      gm.model = __tupl[1]
                                                      gm.trainbedata = __tupl[2]
                                                      gm.testbedata = __tupl[3]
                                                      gm.ids = __tupl[4]
                                                  end


update(gm::GlobalModel,__tupl::(PersoModel,BEData,BEData,Ids)) = begin
                                                      gm.model = __tupl[1]
                                                      gm.trainbedata = __tupl[2]
                                                      gm.testbedata = __tupl[3]
                                                      gm.ids = __tupl[4]
                                                  end

update(gm::GlobalModel, __tupl::(Array{Perfo,1},PerfoRank,Array{Float64,1})) = begin
                                                      gm.perfo.perfs = push!(gm.perfo.perfs,__tupl[1])
                                                      gm.perfo.perfs_ranks = push!(gm.perfo.perfs_ranks,__tupl[2])
                                                      gm.perfo.randoms = push!(gm.perfo.randoms,__tupl[3])
                                                      #gm.perfo.outresults =
                                                    println(gm.perfo)
                                                  end

update{T<:MODEL}(gm::GlobalModel,__tupl::(T,BEData,BEData,Ids)) = begin
                                                      gm.model = __tupl[1]
                                                      gm.trainbedata = __tupl[2]
                                                      gm.testbedata = __tupl[3]
                                                      gm.ids = __tupl[4]
                                                  end


