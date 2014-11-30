#============================================
        SHOPPING
============================================#

shopPLW = convert(Array{ASCIIString,1},[ i[1] for i in dictPLW ])
shopLWTL = convert(Array{ASCIIString,1},[ i[1] for i in dictLWTL ])


abstract Item

type ItemPLW <: Item
    itemid::Int64
    nbkwords::Int64
    kwords::Array{ASCIIString,1}
    # random item creation
    function ItemPLW(id::Int64,nbkwords::Int64)
        kwords = ASCIIString[]
        for i = 1:nbkwords
            push!(kwords,shopPLW[rand(1:SectorPLW.access.count)])
        end
        new(id,nbkwords,kwords)
    end

    function ItemPLW(id::Int64, kwords::Array{ASCIIString,1})
        nbkwords = convert(Int64, sizeof(kwords)/sizeof(ASCIIString))
        new(id, nbkwords, kwords)
    end
 
end

type ItemLWTL <: Item
    itemid::Int64
    nbkwords::Int64
    kwords::Array{ASCIIString,1}
    # random item creation
    function ItemLWTL(id::Int64,nbkwords::Int64)
        kwords = ASCIIString[]
        for i = 1:nbkwords
            push!(kwords,shopLWTL[rand(1:SectorLWTL.access.count)])
        end
        new(id,nbkwords,kwords)
    end

    function ItemLWTL(id::Int64, kwords::Array{ASCIIString,1})
        nbkwords = convert(Int64, sizeof(kwords)/sizeof(ASCIIString))
        new(id, nbkwords, kwords)
    end
    
end

abstract Stor

type gStore <: Stor # store for PLW and LWTL
    Nb::Int64
    flavourPLW::Int64
    flavourLWTL::Int64
    instore::Array{Item,1}
    # random creation of store
    function gStore(Nb::Int64, flavourPLW::Int64, flavourLWTL::Int64)   
        instore = Item[]
        for i = 1:Nb
            nbfPLW=rand(1:flavourPLW)
            nbfLWTL=rand(1:flavourLWTL)
            push!(instore,ItemPLW(i,nbfPLW))
            push!(instore,ItemLWTL(i,nbfLWTL))
            #instore = sample_k!(instore,9)
        end
        new(Nb,flavourPLW,flavourLWTL,instore)
    end
    function gStore(Nb::Int64, flavourPLW::Int64, flavourLWTL::Int64, instore::Array{Item,1})
        #instore = shuffle!(instore,9)
        #println(typeof(instore))
        new(Nb, flavourPLW, flavourLWTL, instore)
    end


end


# store simulates the feeds list proposed each day
type Store <: Stor # specialised on PLW
    Nb::Int64
    flavour::Int64
    instore::Array{ItemPLW,1}
    # random creation of store
    function Store(Nb::Int64,flavour::Int64)   
        instore = ItemPLW[]
        for i = 1:Nb
            nbf=rand(1:flavour)
            push!(instore,ItemPLW(i,nbf)) 
        end
        new(Nb,flavour,instore)
    end

    function Store(Nb::Int64, flavour::Int64, instore::Array{ItemPLW,1})
        new(Nb, flavour, instore)
    end
end

type StoreLWTL <: Stor # specialised on PLW
    Nb::Int64
    flavour::Int64
    instore::Array{ItemLWTL,1}
    # random creation of store
    #function StoreLWTL(Nb::Int64,flavour::Int64)   
    #    instore = ItemLWTL[]
    #    for i = 1:Nb
    #        nbf=rand(1:flavour)
    #        push!(instore,ItemLWTL(i,nbf)) 
    #    end
    #    new(Nb,flavour,instore)
    #end
end

# Decision "Logic"
import Base.rand

logistic(x) = 1 / (1 + exp(-x)) 
alpha = 2.
beta = 1.
gamma = 0.75
#old logitU(user::User, kwrd::String) = logistic( alpha*(sum(@where(user.history, :Items .== kwrd)[:T]) - gamma) + beta*rand_normal(0.,1.))
logitU(x) = logistic( alpha*(x-gamma) + rand_normal(0.,1.) )

#return true if kwrd in user.prefs, false otherwise

function inUserPref(user::User, kwrds::Array{ASCIIString,1})
#println("DBGinUserPrefs ", kwrds)

    for k in kwrds
        # required because PLW names are added with the trunc value
        if k[1:3] == "PLW"
            if ( sum( map( x -> contains( x[max(1,end-length(k[5:end])):end], k[5:end] ), user.prefs ) ) ) > 0
                return true
            end
        elseif k[1:4] == "LWTL"
            if ( sum( map( x -> contains( x[max(1,end-length(k[6:end])):end], k[6:end] ), user.prefs ) ) ) > 0
                return true
            end
        else    
            println("inUserPrefPLW:: data not defined (not in PLW or LWTL)")
        end
    end
    false
end

#=inUserPref(user::User, kwrd::String) = kwrd in user.prefs
function inUserPref(user::User, kwrds::Array{ASCIIString,1})
    for k in kwrds
        if k in user.prefs
            return true
        end
    end
    false
end=#

# random choice
rand_Choice(prob::Float64) = rand() < prob ? true : false   
# simple choice: if one of the items is within the user prefs ones, he picks it.
prefs_Choice(usr::User, kwrds::Array{ASCIIString,1}) = inUserPref(usr, kwrds) #true in map(x->inUserPref(user, x) ,kwrds) 
# choice function based on user's hidden preferences,
# marketing MC simulation taking the logit of the Utility function
# the params alpha,beta,gamma were tuned by hand to get a realistic simulation
logitU_Choice(user::User, kwrds::Array{ASCIIString,1}) = 
                                    rand() < logitU( sum( map(x->inUserPref(user, x) ,kwrds) ) )

