# x, y vector integration using trapezoid for the ROC AUC
function trapz{T<:Real}(x::Vector{T}, y::Vector{T})
    local len = length(y)
    if (len != length(x))
        error("Vectors must be of same length")
    end
    r = 0.0
    for i in 2:len
        r += (x[i] - x[i-1]) * (y[i] + y[i-1])
    end
    r/2.0
end

# find N first elements: [int_1, int_2, ..., int_N]
function findNMax (scor::Array{Float64,1}, N::Int64, arr = Int64[])
    if N < 1
        return arr
    end
    n = length(scor)
    tmp, tmpkw = 0., 0
    for i = 1:n
        if !(i in arr)
            if tmp < scor[i]
                tmp, tmpkw = scor[i], i
            end
        end
    end
   if tmp != 0
        push!(arr,tmpkw)
        findNMax(scor,N-1,arr)
    else
        return arr
    end
end


