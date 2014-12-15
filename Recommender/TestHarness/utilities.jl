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

#===== MODEL ===========================================#

# select users for the local model:
# if they read more than Cutoff articles in the training period
function Users4LocalModel(train_bedata::BEData, test_bedata::BEData, __cutoff::Int64)
    __selectedIds, __unselectedIds = String[], String[]

    # select users in train/test sets
    testfullusersids = getAllarticleIds(test_bedata)
    trainfullusersids = getAllarticleIds(train_bedata)
    arry = Any[]
    for user in unique(testfullusersids)
        cnt1, cnt2  = 0, 0
        for use in trainfullusersids
            if use == user
                cnt1 += 1
            end
        end
        for use in testfullusersids
            if use == user
                cnt2 += 1
            end
        end
        push!(arry,[user,cnt1,cnt2]);
    end

    # selection users for Perso
    for _arr in arry
        if _arr[2] > __cutoff
            push!(__selectedIds,_arr[1])
        else
            push!(__unselectedIds,_arr[1])
        end
    end

    __selectedIds, __unselectedIds
end
