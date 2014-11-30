#============================================
        RECOMMENDER
============================================#
# CONTROLLERS for recommenders

# function checking wether the recommendation are well balanced across the sources
function checkBalance(reco::RecommList, threshold::Int64)
    nLWTL, nPLW = 0, 0
    for i in reco.instore
        preKW = i.kwords[1][1:3]
        @switch preKW begin
            "LWT"; nLWTL += 1
            "PLW"; nPLW += 1
                "pickOneSim::No max recognised"
        end
    end
    return abs(nLWTL - nPLW) > threshold
end

# function picking the most similar element from the other taxonomy (or news space)
# it requires that mat_tfidf_LWTL_PLW and SectorPLW and SectrLWTL precomputations.
function pickOneSim(kwrd::ASCIIString)
    a = kwrd[1:3]
    @switch a begin
        "LWT"; SectorPLW.cells[findOneMax(mat_tfidf_LWTL_PLW[SectorLWTL.access[kwrd],1:end][1:end])].key
        "PLW"; SectorLWTL.cells[findOneMax(mat_tfidf_LWTL_PLW[1:end,SectorPLW.access[kwrd]][1:end])].key
            "pickOneSim::No max regcognised"
    end 

end

# HELPERS for Recommenders 

function kwrdsinLastItem(user::User,item::Item,tpast::Int64)
    lastT = user.history[:T][min(1,end-tpast):end]
    for kwrd in item.kwords
        for strgs in @where(user.history, :T .== lastT)[:Items]  # for t in lastT ]
            if kwrd == strgs
                return true
            end
        end
    end
    false
end    

# time decay function
funct(t::Array{Int64,1}) = 1
fexp(t::Int64, alpha::Float64) = exp(-alpha*t)

# collabfilt
function collabfiltScores(store::gStore, user::User, Time::Int64)
    scores = zeros(store.Nb)
    for i = 1:store.Nb
        for kwrd in store.instore[i].kwords
            tmp = @where(user.history, :Items .== kwrd)[:T]
            tmp != [] ? scores[i] += sum( map(x->fexp(x,0.01) , 
                        @where(user.history, :Items .== kwrd)[:T]) ) : "pass"
        end
    end
    scores
end



function collabfiltScores(store::Store, user::User, Time::Int64)
    scores = zeros(store.Nb)
    for i = 1:store.Nb
        for kwrd in store.instore[i].kwords
            tmp = @where(user.history, :Items .== kwrd)[:T]
            tmp != [] ? scores[i] += sum( map(x->fexp(x,0.01) , 
						@where(user.history, :Items .== kwrd)[:T]) ) : "pass"
        end
    end
    scores
end

function collabfiltScores(store::StoreLWTL, user::User, Time::Int64)
    scores = zeros(store.Nb)
    for i = 1:store.Nb
        for kwrd in store.instore[i].kwords
            tmp = @where(user.history, :Items .== kwrd)[:T]
            tmp != [] ? scores[i] += sum( map(x->fexp(x,0.01) , 
						@where(user.history, :Items .== kwrd)[:T]) ) : "pass"
        end
    end
    scores
end

# RECOMMENDERS

# random... just pass the store list first elements unchanged
randomReco(store::Store, Nrec::Int64) = store.instore[1:min(Nrec,end)]
randomReco(store::gStore, Nrec::Int64) = store.instore[1:min(Nrec,end)]
randomReco(store::StoreLWTL, Nrec::Int64) = store.instore[1:min(Nrec,end)]

# based on the appearance of item in the tpast latest "picks" of the items. 
function lastpurchReco(store::gStore, user::User, Nrec::Int64, tpast::Int64 = 5)
    head, tail, n = Item[], Item[], 0
    for i = 1:store.Nb
        if kwrdsinLastItem(user, store.instore[i], tpast)
            push!(head, store.instore[i])
        n += 1
        else
            push!(tail, store.instore[i])
        end
    end
    print("head_last", n) 
    [head,tail][1:Nrec]
end

function lastpurchReco(store::Store, user::User, Nrec::Int64, tpast::Int64 = 5)
    head, tail, n = ItemPLW[], ItemPLW[], 0
    for i = 1:store.Nb
        if kwrdsinLastItem(user, store.instore[i], tpast)
            push!(head, store.instore[i])
	    n += 1
        else
            push!(tail, store.instore[i])
        end
    end
    print("head_last", n) 
    [head,tail][1:Nrec]
end

function lastpurchReco(store::StoreLWTL, user::User, Nrec::Int64, tpast::Int64 = 5)
    head, tail, n = ItemLWTL[], ItemLWTL[], 0
    for i = 1:store.Nb
        if kwrdsinLastItem(user, store.instore[i], tpast)
            push!(head, store.instore[i])
	    n += 1
        else
            push!(tail, store.instore[i])
        end
    end
    print("head_last", n) 
    [head,tail][1:Nrec]
end

# collaborative filtering in a context where the user have an history stored in a dataframe
# the time dependency can be tweeked in function collabfiltScores

#=
function collabReco333(store::gStore, user::User, Nrec::Int64, Time::Int64) 
    instore::Array{Item,1}
    
end =#

function collabReco(store::gStore, user::User, Nrec::Int64, Time::Int64) 
    head_scor, head_itm, n = Float64[], Item[], 0
    scores = collabfiltScores(store, user, Time)
    maxsIdx = findNMax(scores,10)
    
    for i in maxsIdx
        push!(head_scor, scores[i]), push!(head_itm, store.instore[i])
        n += 1
    end
    print("head_collabfilt", n)
     
    for i in 1:max(1,(Nrec-n))
        dumm = rand(1:store.Nb)
        while( dumm in maxsIdx )
        dumm = rand(1:store.Nb)
    end
    push!(maxsIdx, dumm)
        push!(head_scor, scores[dumm]), push!(head_itm, store.instore[dumm])
    end  
    head_itm #, head_scor 
end

function collabReco(store::Store, user::User, Nrec::Int64, Time::Int64) 
    head_scor, head_itm, n = Float64[], ItemPLW[], 0
    scores = collabfiltScores(store, user, Time)
    maxsIdx = findNMax(scores,10)
    
    for i in maxsIdx
        push!(head_scor, scores[i]), push!(head_itm, store.instore[i])
        n += 1
    end
    print("head_collabfilt", n)
   
    for i in 1:max(1,(Nrec-n))
        dumm = rand(1:store.Nb)
        while( dumm in maxsIdx )
	    dumm = rand(1:store.Nb)
	end
	push!(maxsIdx, dumm)
        push!(head_scor, scores[dumm]), push!(head_itm, store.instore[dumm])
    end  
    head_itm #, head_scor 
end

function collabReco(store::StoreLWTL, user::User, Nrec::Int64, Time::Int64) 
    head_scor, head_itm, n = Float64[], ItemLWTL[], 0
    scores = collabfiltScores(store, user, Time)
    maxsIdx = findNMax(scores,10)
    
    for i in maxsIdx
        push!(head_scor, scores[i]), push!(head_itm, store.instore[i])
        n += 1
    end
    print("head_collabfilt", n)
   
    for i in 1:max(1,(Nrec-n))
        dumm = rand(1:store.Nb)
        while( dumm in maxsIdx )
	    dumm = rand(1:store.Nb)
	end
	push!(maxsIdx, dumm)
        push!(head_scor, scores[dumm]), push!(head_itm, store.instore[dumm])
    end  
    head_itm #, head_scor 
end

# Toward personalised recommendation across News domains
function scoreUprefs(Uprfs::Array{ASCIIString,1} , kw::Array{ASCIIString,1})
    nb = 0
    for k in kw
        if (k in Uprfs)
            nb+=1 
        end
    end
    nb
end

function getPersomatchers(Uprfs,items::Array{Item,1})
    scores = map(x->scoreUprefs(Uprefs,x.kwords),items)
    maxsIdx = findNMax(scores,10)
end

function collabRecoPerso(store::gStore, user::User, Nrec::Int64, Time::Int64, Uprefs::Array{ASCIIString,1}) 
    head_scor, head_itm, n = Float64[], Item[], 0
    scores = collabfiltScores(store, user, Time)
     
    maxs = getPersomatchers(Uprefs, store.instore)
    maxsIdx = findNMax(scores,Nrec + convert(Int64,sizeof(maxs)/sizeof(Int64)))

    
    for i in unique([maxs,maxsIdx])[1:min(end,Nrec)]
        push!(head_itm, store.instore[i])
        n += 1
    end
     
    for i in 1:max(1,(Nrec-n))
        dumm = rand(1:store.Nb)
        while( dumm in maxsIdx )
        dumm = rand(1:store.Nb)
    end
    push!(maxsIdx, dumm)
        push!(head_itm, store.instore[dumm])
    end  
    head_itm #, head_scor 
end


# type Store simulates the feeds list proposed each day
# and the recomm. list is the filtrated, reordered recomm. list
type RecommList
    Nb::Int64
    instore::Array{Item,1}
    viewProba::Array{Float64,1}
    
    function RecommList(Nb::Int64, instore::Array{Item,1})   
        viewProba = zeros(Nb)
        for i = 1:Nb
            viewProba[i] = 1.*fexp(i-1,0.25)
        end
        new(Nb, instore, viewProba)
    end
end

type RecommListPLW
    Nb::Int64
    instore::Array{ItemPLW,1}
    viewProba::Array{Float64,1}
    
    function RecommListPLW(Nb::Int64, instore::Array{ItemPLW,1})   
        viewProba = zeros(Nb)
        for i = 1:Nb
            viewProba[i] = 1.*fexp(i-1,0.25)
        end
        new(Nb, instore, viewProba)
    end
end

type RecommListLWTL
    Nb::Int64
    instore::Array{ItemLWTL,1}
    viewProba::Array{Float64,1}
    
    function RecommListLWTL(Nb::Int64, instore::Array{ItemLWTL,1})   
        viewProba = zeros(Nb)
        for i = 1:Nb
            viewProba[i] = 1.*fexp(i-1,0.25)
        end
        new(Nb, instore, viewProba)
    end
end

# Recommender function calls the recommendation routines and produce 
# a recommendation list (type RecommList).
function Recommender(Typ::ASCIIString, store::gStore, Nrec::Int64, user::User = None, Time::Int64 = 0, Uprefs::Array{ASCIIString,1} = ASCIIString[] )
    
    recomm = @switch Typ begin
        "Random"; randomReco(store, Nrec)
        "LastBased"; lastpurchReco(store, user, Nrec, 1)
        "CollabFilt"; collabReco(store, user, Nrec, Time)
        "CollabFiltPerso"; collabRecoPerso(store, user, Nrec, Time, Uprefs)
        println("Recommender:: Type must be in Random,LastBased,CollabFilt :"), exit(1)
    end
println("ici")
    RecommList(Nrec, recomm)
end

function Recommender(Typ::ASCIIString, store::Store, Nrec::Int64, user::User = None, Time::Int64 = 0)
    t = Typ
    recomm = @switch t begin
        "Random"; randomReco(store, Nrec)
        "LastBased"; lastpurchReco(store, user, Nrec, 1)
        "CollabFilt"; collabReco(store, user, Nrec, Time) #[1]
        println("Recommender:: Type must be in Random,LastBased,CollabFilt :"), exit(1)
    end
    RecommListPLW(Nrec, recomm)
end

function Recommender(Typ::ASCIIString, store::StoreLWTL, Nrec::Int64, user::User = None, Time::Int64 = 0)
    t = Typ
    recomm = @switch t begin
        "Random"; randomReco(store, Nrec)
        "LastBased"; lastpurchReco(store, user, Nrec, 1)
        "CollabFilt"; collabReco(store, user, Nrec, Time) #[1]
        println("Recommender:: Type must be in Random,LastBased,CollabFilt :"), exit(1)
    end
    RecommListLWTL(Nrec, recomm)
end
