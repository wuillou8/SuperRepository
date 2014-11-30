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

############################
#   Get Date Time          #
############################

function getMonth(str)
    months = ["January","February","March","April","May","June","July","August","September","October","November","December"]
    for n = 1:length(months)
        m = months[n]
        idx = search(str,m)
        if length(str[idx]) > 0
            return n
        end
    end
end

function getDateTime(str)
    year = str[end-12:end-8]
    date = str[end-16:end-15]
    month = getMonth(str)
    time = str[end-7:end]
    #println(DateTime(int(year),int(month),int(date),int(time[1:2]),int(time[4:5]),int(time[7:8])))
    DateTime(int(year),int(month),int(date),int(time[1:2]),int(time[4:5]),int(time[7:8]))
end

# Evaluate diversity
function diversityMeas(df::DataFrame)
    # ±measure diversity
    idsNews = String[]
    for i in df[:Custom1]
        if length(i) > 12
            push!(idsNews,i)
        end
    end
    idsNews = countmap(idsNews)
    arr = Int64[]
    [ push!(arr,n) for n in values(idsNews) ]

    stps = 2
    bins = [1:stps:2000]
    cntarr = zeros(length(bins))
    for ar in arr
        n = 1
        while ar >= bins[n+1]
            n += 1
        end
        cntarr[n] += 1
    end

    summ, N = 0., Base.sum(arr)
    for nb in cntarr[1:5]
        summ += (nb/N)*(nb/N)
    end
    summ
end
