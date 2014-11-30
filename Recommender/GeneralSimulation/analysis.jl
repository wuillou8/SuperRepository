getPopatT(df::DataFrame, T::Int64) = size(@where( df , :T .== T))[1]
getPopatT(df::DataFrame, Tmin::Int64, Tmax::Int64) = size(@where( df , Tmax .> :T .> Tmin))[1]
