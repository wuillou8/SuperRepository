# Create Recommendation list from generalMOdel Object
function recommenderList(__gm::GlobalModel, __userId::String)

    recommenderList( __gm.model, __gm.ids.testnewsIds, __userId, __gm.trainbedata, __gm.testbedata )
end

# Recomendation from predictionIO:
# http://docs.prediction.io/recommendation/quickstart/
function recommenderList( model::PredictionIO, testnews::Array{String,1}, userId::ASCIIString, traindata::BEData, testdata::BEData )
    #=== protocol:
    import predictionio
    engine_client = predictionio.EngineClient(url="http://localhost:8000")
    print engine_client.send_query({"user": "1", "num": 4}) ===#
    #in Julia : get("http://httpbin.org/get"; query = {"title" => "page1"})
    #PIOquery( userId, length(testnews) )
    # call Random instead or PIO for now...
    scores = [ rand() for i = 1:length(testnews) ]
    map( x -> testnews[x], findNMax(scores, length(scores)) ) |>
    ( _ -> convert(Array{String,1},_) )
    #rmodel = RandomModel()
    #recommenderList(rmodel, testnews, userId, traindata, testdata)
end

# Create recommendation list
function recommenderList( rec::RandomModel, testnews::Array{String,1}, userId::String, traindata::BEData, testdata::BEData )
    scores = [ rand() for i = 1:length(testnews) ]
    map( x -> testnews[x], findNMax(scores, length(scores)) ) |>
    ( _ -> convert(Array{String,1},_) )
end

# bug two els lost along the way... findNmax probably
function recommenderList( recmodel::PersoModel, testnews::Array{String,1}, userId::ASCIIString, traindata::BEData, testdata::BEData )

    # if userId in globalIds
    if userId in recmodel.context.globalIds
        recommenderList( recmodel.globModel, testnews, userId, traindata, testdata )

    #if userId in persoIds
    else
        # create profile
        usrPrf = getEntssourceMap(traindata, userId) |>
                                                   EntityFan

        map( x -> scoreNew(usrPrf, testdata, x)[1], testnews ) |>
                     ( _ -> map( x -> testnews[x], findNMax(_+100, length(_)) ) ) |>
                     ( _ -> convert(Array{String,1},_) )
    end
end

# bug two els lost along the way... findNmax probably
function recommenderList( recmodel::PersoBernoulliNB, testnews::Array{String,1}, userId::ASCIIString, traindata::BEData, testdata::BEData )

    # if userId in globalIds
    if userId in recmodel.context.globalIds #persoIds
        recommenderList( recmodel.globModel, testnews, userId, traindata, testdata )

    else

        usrPrf = getEntssourceMap( traindata, userId ) |> EntityFan
        # in this model, NB has to be trained "live"
        prior, probvec, prior_, probvec_ = TrainBernoulliNB( recmodel, usrPrf )

        testnews |>
        (_ -> map( x -> applyBernoulliNB( recmodel, userId, prior, probvec ), _)) |>
                     ( _ -> map( x -> testnews[x], findNMax(convert(Vector{Float64}, _)+1000_000_000_000., length(_)) ) ) |>
                     ( _ -> convert(Array{String,1},_) ) #|> println

    end
end
