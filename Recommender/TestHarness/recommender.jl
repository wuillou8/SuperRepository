

# Create recommendation list
function recommenderList( rec::RandomModel, testnews::Array{String,1}, userId )
    scores = [ rand() for i = 1:length(testnews) ]
    map( x -> testnews[x], findNMax(scores, length(scores)) ) |> 
    ( _ -> convert(Array{String,1},_) )
end


