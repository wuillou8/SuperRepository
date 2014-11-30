PATH = "/Users/jair/Desktop/PROJECTS/KALE/KaleAUTO/USERAnalysis/"

using DataFrames
using Lazy
using Dates
include("DataFramesMeta.jl")
using DataFramesMeta;

include("utilitiesjuno.jl")
include("classesjuno.jl")
include("testingjuno.jl")

#===     IO parameters     ===#
__newspath = PATH*"NEWS/news0601_1118filter.json"
#__usagepath = ###
__usageClusterparams = ["France", "Germany", "Switzerland", "Japan", "Hong Kong", "China", "Turkey", "Nigeria"]
__newsClusterparams = ["everything"]
__T1 = DateTime(2014,6,1)
__T2 = DateTime(2014,10,20)
__T3 = DateTime(2014,10,22)


# load news
t1 = time()
mynews = News(JSON.parsefile(__newspath)["news"])
# load usage
myusage = DataFrame() # = readtable(__usagepath)
t2 = time()
println("Load News: ", t2 - t1)

# Load cluster: as first the cluster are approx the countries.
# there will be a mapping userId -> Cluster(s), which is built overnight.
# load cluster parameters, they are trained elsewhere:
t1 = time()
cntrsClust = Countries(__usageClusterparams)
chanlClust = Channels(__newsClusterparams)
# Prepare Usage and News data and decompose into clusters
Prepare4Test(myusage, cntrsClust, __T1, __T2, __T3)
Prepare4Test(mynews, chanlClust, __T1, __T2, __T3)
t2 = time()
println("Cluster News/Usage: ", t2 - t1)
