

# Create recommendation list
function recommenderList( rec::RandomModel, testnews::Array{String,1}, userId::ASCIIString, traindata::BEData, testdata::BEData )
    scores = [ rand() for i = 1:length(testnews) ]
    map( x -> testnews[x], findNMax(scores, length(scores)) ) |> 
    ( _ -> convert(Array{String,1},_) )
end

# bug two els lost along the way... findNmax probably
function recommenderList( rec::PersoModel, testnews::Array{String,1}, userId::ASCIIString, traindata::BEData, testdata::BEData )
    #if userId in rec.persoIds
    usrPrf = getEntssourceMap(traindata, userId) |> 
                                            EntityFan
    scores = map( x -> scoreNew(usrPrf, testdata, x)[1], testnews)
    map( x -> testnews[x], findNMax(scores+100, length(scores)) ) |> 
                                    ( _ -> convert(Array{String,1},_) )    
end

# recommenderList(::PersoModel, ::Array{String,1}, ::ASCIIString, ::BEData, ::BEData)
