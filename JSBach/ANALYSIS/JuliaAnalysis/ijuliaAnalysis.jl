
# In[5]:

using DataArrays, DataFrames, RDatasets
using Requests
using PyPlot


# In[48]:

path = "data.csv" #or "btceUSD.csv", "b7USD.csv"

#try
#    arr_ = readcsv( path ) 
#    df = DataFrame( DateUnix = arr_[2:,1], Price = arr_[2:,2], Volume = arr_[2:,3] )
#catch 
#    println "error in data loading"
#end;

arr_ = readcsv( path ) 
df = DataFrame( DateUnix = arr_[2:,1], Price = arr_[2:,2], Volume = arr_[2:,3] );


# In[51]:

function rsiFunc(prices::Array{Float64,1}, n::Int=10)
    up, down = 0., 0.
    for i = 1:(n-1)
        diff = ( prices[i+1]-prices[i] )
        ( diff > 0 ) ? ( up += diff ) : ( down -= diff )
    end
    # check for infty
    down == 0 ? throw("error: down == 0") : pass
    #  construct Index Array
    rsiIdX = Float64[]
    push!(rsiIdX, (100. - 100./(1. + up/down)) )
    for i = n:(length(prices)-1)
        diff = ( prices[i+1]-prices[i] )
        up, down = up*(n-1)/n, down*(n-1)/n
        ( diff > 0 ) ? ( up += diff/n ) : ( down -= diff/n )
        push!(rsiIdX, (100. - 100./(1. + up/down)) )
    end
    return rsiIdX
end

# slightly corrected function
function rsiFunc_Corr(prices::Array{Float64,1}, n::Int=10)    
    up, down = 0., 0.
    for i = 1:(n-1)
        diff = ( prices[i+1]-prices[i] )
        ( diff > 0 ) ? ( up += diff ) : ( down -= diff )
    end
    # check for infty
    down == 0 ? throw("error: down == 0") : pass
    # construct Index Array
    rsiIdX = Float64[]
    push!(rsiIdX, (100. - 100./(1. + up/down)) )
    for i = n:(length(prices)-1)
        # remove the first add the last contribs to rsi IdX
        diff_head = ( prices[i+1]-prices[i] )
        diff_tail = ( prices[(i-n+2)]-prices[(i-n+1)] )
        ( diff_tail > 0 ) ? ( up -= diff_tail ) : ( down += diff_tail )
        ( diff_head > 0 ) ? ( up += diff_head ) : ( down -= diff_head )
        push!(rsiIdX, (100. - 100./(1. + up/down)) )
    end
    return rsiIdX
end

function rsiFunc_Corr2(prices::DataArray{Float64,1}, n::Int=10)    
    up, down = 0., 0.
    for i = 1:(n-1)
        diff = ( prices[i+1]-prices[i] )
        ( diff > 0 ) ? ( up += diff ) : ( down -= diff )
    end
    # check for infty
    down == 0 ? throw("error: down == 0") : pass
    #  construct Index Array
    rsiIdX = Float64[]
    push!(rsiIdX, (100. - 100./(1. + up/down)) )
    for i = n:(length(prices)-1)
        #remove the first add the last contribs to rsi IdX
        diff_head = ( prices[i+1]-prices[i] )
        diff_tail = ( prices[(i-n+2)]-prices[(i-n+1)] )
        ( diff_tail > 0 ) ? ( up -= diff_tail ) : ( down += diff_tail )
        ( diff_head > 0 ) ? ( up += diff_head ) : ( down -= diff_head )
        push!(rsiIdX, (100. - 100./(1. + up/down)) )
    end
    return rsiIdX
end;


# In[12]:

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


# Out[12]:

#     rand_normal (generic function with 1 method)

# In[28]:

print( typeof(df) )
print( "indices: ", df.colindex )


# Out[28]:

#     DataFrameindices: Index(["DateUnix"=>1,"Price"=>2,"Volume"=>3],["DateUnix","Price","Volume"])

# In[76]:

x = df[:DateUnix]
y = df[:Price]
yy = DataFrames.vector(y)
y_rsi = rsiFunc_Corr( yy, 50 )
#y_rsi = rsiFunc( yy, 50 )
PyPlot.figure(facecolor="#07000d")
PyPlot.subplot2grid((6,4), (2,0), rowspan = 4, colspan = 4, axisbg="#07000d")
plot(x, y, color="red", linewidth=2.0, linestyle="--")
xlabel("UnixTime")
ylabel("Prices")

PyPlot.subplot2grid((6,4), (0,0), rowspan = 2, colspan = 4, axisbg="#07000d")
plot(x[50:], y_rsi, color="blue", linewidth=2.0, linestyle="--")
ylabel("RSI Index")
axhline(y=75, linewidth=1)
axhline(y=25, linewidth=1)
title("Prices & RSI Index VS Unix time");


# Out[76]:

# image file:
