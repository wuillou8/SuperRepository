
# coding: utf-8

# In[5]:

read = readcsv("DATA/test_minidress.csv");


# In[6]:

abstract Attribute

function dist(path1::Vector{UTF8String},path2::Vector{UTF8String})
    n = 0
    for i = 1:length(path1) 
        if !(path1[i] == path2[i])
            n += 1
        end
    end
    n
end

#####################
# Taxo gender       #
#####################
immutable Gender <: Attribute
    path::UTF8String
end

type taxoGenders
    coords::Vector{Gender}
    __dict::Dict{Any,Any}
end

sim(t1::Gender,t2::Gender) = t1.path == t2.path ? __p_gender^0 : __p_gender^1
    
#####################
# Taxo brand        #
#####################

# basical taxo cell
immutable Brand <: Attribute
    path::Vector{UTF8String}
end

type taxoBrands
    coords::Vector{Brand}
    __dict::Dict{Any,Any}
end

sim(t1::Brand,t2::Brand) = t1.path == t2.path ? __p_brand^0 : __p_brand^1
    
    
#####################
# Taxo Type         #
#####################

# basis cell
immutable Type <: Attribute
    path::Vector{UTF8String}
end

type taxoTypes
    coords::Vector{Type}
    __dict::Dict{Any,Any}
end

sim(t1::Type,t2::Type) = (__p_type)^(dist(t1.path,t2.path))

#####################
# Taxo Colours      #
#####################

# basis cell
immutable Colour <: Attribute
    path::Vector{UTF8String}
end

type taxoColours
    coords::Vector{Colour}
    __dict::Dict{Any,Any}
end

sim(t1::Colour,t2::Colour) = (__p_colour)^(dist(t1.path,t2.path))

######################
# Taxo Fabric        #
######################

# basis cell
immutable Fabric <: Attribute
    path::Vector{UTF8String}
end

type taxoFabrics
    coords::Vector{Fabric}
    __dict::Dict{Any,Any}
end

sim(t1::Fabric,t2::Fabric) = (__p_fabric)^(dist(t1.path,t2.path))

######################
# Taxo SleeveType    #
######################

# basis cell
immutable SleeveT <: Attribute
    path::Vector{UTF8String}
end

type taxoSleeveT
    coords::Vector{SleeveT}
    __dict::Dict{Any,Any}
end

sim(t1::SleeveT,t2::SleeveT) = (__p_sleeveT)^(dist(t1.path,t2.path))

######################
# Taxo SleeveLength  #
######################

# basis cell
immutable SleeveL <: Attribute
    path::Vector{UTF8String}
end

type taxoSleeveL
    coords::Vector{SleeveL}
    __dict::Dict{Any,Any}
end

sim(t1::SleeveL,t2::SleeveL) = (__p_sleeveL)^(dist(t1.path,t2.path))

##################
# Price          #
##################

sim(t1::Float64,t2::Float64) = exp(-abs(log(t1) - log(t2)))


# In[7]:

type Item
    label::String
            
    brand::Brand            # "Marni"           
    gender::Gender          # "female"          
    thetype::Type           # "top"             
    colour::Colour          # "navy "
    colour2::Colour
    fabric::Fabric
    #sleeveT::SleeveT
    sleeveL::SleeveL
    price::Float64          # 630.0                

    function Item(label::String,__dict::Dict{Any,Any})
        brand = Brand(t_brands.__dict[__dict["brand"]])
        gender = Gender(t_gender.__dict[__dict["gender "]])
        thetype = Type(t_types.__dict[__dict["Type"]])
        colour = Colour(t_colours.__dict[__dict["colour"]])
        colour2 = Colour(t_colours.__dict[__dict["colour2"]])
        fabric = Fabric(t_fabrics.__dict[__dict["fabric"]])
        #sleeveT = SleeveT(t_sleeveTs.__dict[__dict["sleeve type"]])
        sleeveL = SleeveL(t_sleeveLs.__dict[__dict["sleeve length"]])
        price = __dict["price"]
        
        new(label,brand,gender,thetype,colour,colour2,fabric,sleeveL,price)
    end
end

__parGender = 1.
__parBrand = 1.
__parType = 1.
__parColour = 1.
__parColour2 = 1.
__parFabric = 1.
__parfabric = 1.
__parSleeveT = 1.
__parSleeveL = 1.
__parPrice = 0.

################################
# Similarity functions         #
################################
#==  Similarity function are compositions of the similarities
    within the different taxonomy dimensions              ==#

# additive similarity
sim_add(itm1::Item,itm2::Item) = 
    ( 
      __parGender*sim(itm1.gender,itm2.gender)
    + __parBrand*sim(itm1.brand,itm2.brand)
    + __parType*sim(itm1.thetype,itm2.thetype)
    + __parColour*sim(itm1.colour,itm2.colour)
    + __parColour2*sim(itm1.colour2,itm2.colour2)
    + __parFabric*sim(itm1.fabric,itm2.fabric)
    #+ __parSleeveT*sim(itm1.sleeveT,itm2.sleeveT)
    + __parSleeveL*sim(itm1.sleeveL,itm2.sleeveL)   
    + __parPrice*sim(itm1.price,itm2.price)
    ) / 
    ( __parGender + __parBrand + __parType + __parColour + __parColour2 + __parFabric + __parSleeveL #+ __parSleeveT
     + __parPrice ) # normalising

    # tweaked version
sim_add(itm1::Item,itm2::Item) = 
    ( 
      __parGender*sim(itm1.gender,itm2.gender)
    + __parBrand*sim(itm1.brand,itm2.brand)
    + __parType*sim(itm1.thetype,itm2.thetype)
    + __parColour*sim(itm1.colour,itm2.colour)
    + __parColour2*maximum([sim(itm1.colour2,itm2.colour2),sim(itm1.colour2,itm2.colour),sim(itm1.colour,itm2.colour2)])
    + __parFabric*sim(itm1.fabric,itm2.fabric)
    #+ __parSleeveT*sim(itm1.sleeveT,itm2.sleeveT)
    + __parSleeveL*sim(itm1.sleeveL,itm2.sleeveL)   
    + __parPrice*sim(itm1.price,itm2.price)
    ) / 
    ( __parGender + __parBrand + __parType + __parColour + __parColour2 + __parFabric + __parSleeveL #+ __parSleeveT
     + __parPrice ) # normalising
    
mapcontent_string(item::Item) =
    item |> (_ -> #_.thetype.path[end]*"_"*
             _.colour.path[end]*"_"*
             _.colour2.path[end]*"_"*
             _.brand.path[1]*"_"*
             _.fabric.path[end]*"_"*
             _.sleeveL.path[end]
             )

function NmostSim(itemlist::Vector{Item},item::Item,Nsim::Int64, f_sim::Function = sim_add)
    sims = Float64[]
    for __it in itemlist 
        push!(sims, f_sim(item,__it)) 
    end
    
    __N = Int64[]
    for i = 1:Nsim
        _n=findmax(sims)
        sims[_n[2]] = sims[_n[2]] - _n[1]
        push!(__N,_n[2])
    end
    __N
end
    


# In[8]:




# In[9]:




# In[10]:

##################
# gender         #
##################
vect = [Gender("male"),Gender("female")]
__dict = { t.path => t.path  for t in vect }

t_gender = taxoGenders(vect,__dict)

##################
# brands         #
##################
read = readcsv("DATA/taxobrands.csv")[1:end,1];

vect = Brand[]
for rea in read
    colpath = UTF8String[]
    push!(colpath,rea)
    push!(vect,Brand(colpath))
end
__dict = { t.path[end] => t.path  for t in vect }

t_brands = taxoBrands(vect,__dict)

#################
# types         #
#################
read = readcsv("DATA/taxotype.txt");
path1 = read[1,1]
path2 = read[1,2]

vect = Type[] 

for i = 1:size(read)[1]
    
    if !(read[i,1] in ["\t",""])
        path1 = [read[i,1]]
    end
    if !(read[i,2] in ["\t",""])
        path2 = read[i,2]
    end
    
    path = [path1, path2, read[i,3]]
    push!(vect,Type(path))
end
__dict = { t.path[end] => t.path  for t in vect }

t_types = taxoTypes(vect,__dict)

#################
# colours       #
#################
read = readcsv("DATA/colourjair.csv")[2:end,1:end]
path1 = read[1,1]
path2 = read[1,2]

vect = Colour[] 

for i = 1:size(read)[1]
    
    if !(read[i,1] in ["\t",""])
        path1 = [read[i,1]]
    end
    if !(read[i,2] in ["\t",""])
        path2 = read[i,2]
    end
    
    if read[i,3] != ""
        path = [path1, path2, read[i,3]]
        push!(vect,Colour(path))
    end
end
__dict = { t.path[end] => t.path  for t in vect }

t_colours = taxoColours(vect,__dict);

#################
# Fabrics       #
#################
read = readcsv("DATA/Fabric.csv")[2:end,1:end]
path1 = read[1,1]
path2 = read[1,2]

vect = Fabric[] 

for i = 1:size(read)[1]
    
    if !(read[i,1] in ["\t",""])
        path1 = [read[i,1]]
    end
    if !(read[i,2] in ["\t",""])
        path2 = read[i,2]
    end
    
    if read[i,3] != ""
        path = [path1, path2, read[i,3]]
        push!(vect,Fabric(path))
    end
end
__dict = { t.path[end] => t.path  for t in vect }

t_fabrics = taxoFabrics(vect,__dict)

#################
# Sleeve Length #
#################
read = readcsv("DATA/Sleeve\ length.csv") #[2:end,1:end]
path1 = read[1,1]
path2 = read[1,2]

vect = SleeveL[] 

for i = 1:size(read)[1]
    
    if !(read[i,1] in ["\t",""])
        path1 = [read[i,1]]
    end
    if !(read[i,2] in ["\t",""])
        path2 = read[i,2]
    end
    
    if read[i,3] != ""
        path = [path1, path2, read[i,3]]
        push!(vect,SleeveL(path))
    end
end
__dict = { t.path[end] => t.path  for t in vect }

t_sleeveLs = taxoSleeveL(vect,__dict)

#################
# Sleeves Types #
#################
read = readcsv("DATA/Sleeve\ type.csv") #[2:end,1:end]
path1 = read[1,1]
path2 = read[1,2]

vect = SleeveT[] 

for i = 1:size(read)[1]
    
    if !(read[i,1] in ["\t",""])
        path1 = [read[i,1]]
    end
    if !(read[i,2] in ["\t",""])
        path2 = read[i,2]
    end
    
    if read[i,3] != ""
        path = [path1, path2, read[i,3]]
        push!(vect,SleeveT(path))
    end
end
__dict = { t.path[end] => t.path  for t in vect }

t_sleeveTs = taxoSleeveT(vect,__dict);



# In[11]:

#=================
 Read items   
=================#

#itemNames = 
#    ["navyTop","beigeKnitwear","blueknitwear","blueknitwear","blackPants","navyPants","redBag","paleredBag","creamSkirt","creamDress"]

read = readcsv("DATA/test_minidress.csv")
    
types = 
    ["brand","gender ","Type","colour","colour2","price","Sub type","fabric","sleeve type","sleeve length"] #,"Shape","Silk","Style","Pattern Type","Fastening"]
dict_types = 
    { types[i] => "" for i = 1:length(types)}    

tmp = String[]
for i = 1:length(types)
    push!(tmp,"")
end
    
shoppinglistreal = Item[]
label = read[1,1]
__dict = dict_types


for i = 0:12
    for j = 1:11
        _iloc = i*11+j
        read[_iloc,1:end] |> ( _ -> 
                            !(_[1] in ["\t",""]) ? label = _[1] :  
                                                __dict[_[2]] = _[3] 
                        )
    end

    push!(shoppinglistreal,Item(label,__dict))
end;


# In[12]:

__dict


# In[13]:

using MultivariateStats
using PyPlot

function makePlot(labels::String)
         
    itemNames = 
            labels == "std" ?
                ["A","B","C","D","E","F","G","H","I","J","K","L","M"] :
                map(x->mapcontent_string(x),shoppinglistreal)            
            
    # similarity matrix
    N = length(shoppinglistreal)
    mat = zeros(N,N)
    for i = 1:N 
        for j = 1:i 
            mat[i,j] = sim_add(shoppinglistreal[i],shoppinglistreal[j])
            mat[j,i] = mat[i,j]
        end
    end

    # apply classical multidimensional scaling: 
    # http://multivariatestatsjl.readthedocs.org/en/latest/cmds.html
    # http://en.wikipedia.org/wiki/Multidimensional_scaling
    D = gram2dmat(mat)
    mds = classical_mds(D, 2)

    # plotting with PyPLot
    plt.title("Items similarities // 2-Dimensional visualisation")

    for i = 1:N
        plt.scatter(mds[1:end,i][1], mds[1:end,i][2], alpha = 0.9)
    end

    for i = 1:N
        annotate(itemNames[i],xy=[mds[1:end,i][1], mds[1:end,i][2]])
    end

    itemNames |> println
end


# In[14]:

# weights
#===
__parGender = 1.
__parBrand = 2.
__parType = 1.
__parColour = 1.5
__parColour2 = 1.
__parFabric = 1.
__parSleeveL = 1.
#__parSleeveT = 0.
__parPrice = 0.
===#

__parGender = 1.
__parBrand = 20.
__parType = 1.
__parColour = 2.
__parColour2 = .5
__parFabric = 1.
__parSleeveL = 1.
#__parSleeveT = 0.
__parPrice = 0.

# split params for a basic tree model
__p_gender = 0.
__p_brand = .5
__p_type = .5
__p_colour = .5
__p_fabric = .5
__p_sleeveL = .5
__p_sleeveT = .5

makePlot("stdd")


# In[15]:




# In[16]:

# any itmem in my collection
itm = shoppinglistreal[1]
# closest items
[ shoppinglistreal[n] for n in NmostSim(shoppinglistreal,itm,3) ] |> 
        (_ ->  map(x->mapcontent_string(x), _))  


# In[3]:


type MainParams
    __parGender::Float64 # 1.
    __parBrand::Float64 # 20.
    __parType::Float64 # 1.
    __parColour::Float64  # 2.
    __parColour2::Float64 # .5
    __parFabric::Float64 # 1.
    __parSleeveL::Float64 # 1.
    #__parSleeveT = 0.
    __parPrice::Float64 # 0.
end

type SpecParams
    __p_gender::Float64 # 0.
    __p_brand::Float64 # .5
    __p_type::Float64 # .5
    __p_colour::Float64 # .5
    __p_fabric::Float64 # .5
    __p_sleeveL::Float64 # .5
    __p_sleeveT::Float64 # .5
end

type MyParams
    myMain::MainParams
    specParams::SpecParams
end

myParams = MyParams( MainParams(1., 20., 1., 2., .5, 1., 1., 0.), 
                       SpecParams(0.,.5, .5, .5, .5, .5, .5))


# In[4]:

MainParams(1., 20., 1., 2., .5, 1., 1., 0.)


# In[2]:

dict_json |> (_ -> _["myMain"]) |> ( _ -> 
_["__parGender"] = 0.

# split params for a basic tree model
    __p_gender = 0.
    __p_brand = .5
    __p_type = .5
    __p_colour = .5
    __p_fabric = .5
    __p_sleeveL = .5
    __p_sleeveT = .5


# In[6]:

using JSON

json_obj = myParams |> JSON.json
dict_json = json_obj |> JSON.parse


# In[28]:

(__parGender,
__parBrand,
__parType,
__parColour,
__parColour2,
__parFabric,
__parSleeveL,
#__parSleeveT = 0.
__parPrice) = dict_json |> (_ -> _["myMain"]) |> ( _ -> 
                (_["__parGender"],
                _["__parBrand"],
                _["__parType"],
                _["__parColour"],
                _["__parColour2"],
                _["__parFabric"],
                _["__parSleeveL"],
                #_["__parSleeveT"],
                _["__parPrice"])
                )

(__p_gender,
__p_brand,
__p_type,
__p_colour,
__p_fabric,
__p_sleeveL,
__p_sleeveT) = dict_json |> (_ -> _["specParams"]) |> ( _ -> 
                (_["__p_gender"],
                _["__p_brand"],
                _["__p_type"],
                _["__p_colour"],
                _["__p_fabric"],
                _["__p_sleeveL"],
                _["__p_sleeveT"])
                )


# In[27]:




# In[10]:

dict_json |> (_ -> _["myMain"]) |> ( _ -> 
_["__parGender"] )


# In[23]:

dict_json |> (_ -> _["specParams"]) |> ( _ -> 
                (_["__p_sleeveL"],_["__parGender"]))


# In[24]:

dict_json


# In[8]:

dict_json |> (_ -> _["myMain"])


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:

__parGender, __parBrand, __parType, __parColour, __parColour2, __parFabric, __parSleeveL, __parPrice

type SpecParams
    __p_gender::Float64 # 0.
    __p_brand::Float64 # .5
    __p_type::Float64 # .5
    __p_colour::Float64 # .5
    __p_fabric::Float64 # .5
    __p_sleeveL::Float64 # .5
    __p_sleeveT::Float64 # .5


# In[ ]:




# In[ ]:




# In[31]:

keys(dict_json)


# In[ ]:




# In[ ]:




# In[ ]:




# In[9]:

# similarity matrix
    N = length(shoppinglistreal)
    mat = zeros(N,N)
    for i = 1:N 
        for j = 1:i 
            mat[i,j] = sim_add(shoppinglistreal[i],shoppinglistreal[j])
            mat[j,i] = mat[i,j]
        end
    end

    # apply classical multidimensional scaling: 
    # http://multivariatestatsjl.readthedocs.org/en/latest/cmds.html
    # http://en.wikipedia.org/wiki/Multidimensional_scaling
    D = gram2dmat(mat)
    mds = classical_mds(D, 2)


# In[51]:

D


# In[49]:

g = dmat2gram(D)


# In[45]:

N = size(mds)[2]
mat = zeros(N,N)
for i = 1:N #size(mds)[2]
    for j = 1:N
        mat[i,j] = mds[1:end,i] - mds[1:end,j] |> (_ -> map(x -> x^2,_)) |> sum |> sqrt
        mat[j,i] = mat[i,j]
    end
end


# In[ ]:




# In[ ]:

N = size(mds)[2]
distmat = zeros(N,N)
for i = 1:N #size(mds)[2]
    for j = 1:N
        distmat[i,j] = mds[1:end,i] - mds[1:end,j] |> (_ -> map(x -> x^2,_)) |> sum |> sqrt
        distmat[j,i] = distmat[i,j]
    end
end

dist_max = max(distmat)


# In[ ]:




# In[ ]:




# In[46]:

mat


# In[42]:




# In[37]:


# similarity matrix
    N = length(shoppinglistreal)
    mat = zeros(N,N)
    for i = 1:N 
        for j = 1:i 
            mat[i,j] = sim_add(shoppinglistreal[i],shoppinglistreal[j])
            mat[j,i] = mat[i,j]
        end
    end

writecsv("mat.csv", mat)


# In[42]:

run(`python run_multidimscaling.py`)
mds = readcsv("mdsout.csv");



# In[41]:

# plotting with PyPLot
    plt.title("Items similarities // 2-Dimensional visualisation")
    
    for i = 1:N
        plt.scatter(mds[i,1:end][1], mds[i,1:end][2], alpha = 0.9)
    end
itemNames = ["A","B","C","D","E","F","G","H","I","J","K","L","M"]
    for i = 1:N
        annotate(itemNames[i],xy=[mds[i,1:end][1], mds[i,1:end][2]])
    end


# In[29]:

N


# In[32]:

mds[1,1:end]


# In[23]:

shoppinglistreal


# In[27]:

#itemNames = 
#            labels == "std" ?
#                ["A","B","C","D","E","F","G","H","I","J","K","L","M"] :
#                map(x->mapcontent_string(x),shoppinglistreal)            
            

    # similarity matrix
    N = length(shoppinglistreal)
    mat = zeros(N,N)
    for i = 1:N 
        for j = 1:i 
            mat[i,j] = sim_add(shoppinglistreal[i],shoppinglistreal[j])
            mat[j,i] = mat[i,j]
        end
    end

    # apply classical multidimensional scaling: 
    # http://multivariatestatsjl.readthedocs.org/en/latest/cmds.html
    # http://en.wikipedia.org/wiki/Multidimensional_scaling
    D = gram2dmat(mat)
    mds = classical_mds(D, 2)

    # plotting with PyPLot
    plt.title("Items similarities // 2-Dimensional visualisation")

    for i = 1:N
        plt.scatter(mds[1:end,i][1], mds[1:end,i][2], alpha = 0.9)
    end

    for i = 1:N
        annotate(itemNames[i],xy=[mds[1:end,i][1], mds[1:end,i][2]])
    end

    itemNames |> println


# In[11]:

using PyPlot


# In[12]:

jx = [1.,.2,.2,.3,4.,5.]
jy = [.3,4.,.4,5.,6.,7.]


# In[13]:

PyPlot.plot(jx,jy)


# In[14]:

Pkg.test("PyPlot")


# In[15]:

Pkg.checkout("PyCall")


# In[41]:

using PyCall
@pyimport("matplotlib.pyplot")


# In[21]:

using PyCall
matplotlib = pyimport("matplotlib")
#matplotlib[:use]("tkagg")
#pltm = pyimport("matplotlib.pyplot")


# In[20]:


x = -2pi:0.1:2pi;
plot(x, sin(x.^2)./x);


# In[18]:

using PyCall
pygui(:tk)
using PyPlot


# In[ ]:



