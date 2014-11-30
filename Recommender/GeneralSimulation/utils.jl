# helpers
jhead(df) = DataFrames.head(df)
jtail(df) = DataFrames.tail(df)
jp(stuff...) = println(stuff)

#general utils
tsof(x) = jp(typeof(x),sizeof(x))

function nostopwrd(str, list)
    @switch (str in list) begin
        true; return false
        return true
    end
end

## return a random sample from a normal (Gaussian) distribution
function rand_normal(mean, stdev)
    if stdev <= 0.0
        error("standard deviation must be positive")
    end
    u1 = rand()
    u2 = rand()
    r = sqrt( -2.0*log(u1) )
    theta = 2.0*pi*u2
    mean + stdev*r*sin(theta)
end

function findNMax (scor::Array{Float64,1}, N::Int64, arr = Int64[])
    if N < 1 
        return arr
    end

    n = sizeof(scor)/sizeof(Float64)
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

function findNMax (scor::Array{Float64,1}, N::Int64, arr = Int64[])
    if N < 1 
        return arr
    end

    n = sizeof(scor)/sizeof(Float64)
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

# function retrieving the max. If the max is degenerate, i.e., has several multiples
# the function picks up the max randomly
function findOneMax (arr::Array{Float64,1})
    n = findNMax(arr, 1)[1]
    arr = filter( x -> x == arr[n], arr)
    findNMax(arr, 3)[rand(1:length(arr))]
end    

 
