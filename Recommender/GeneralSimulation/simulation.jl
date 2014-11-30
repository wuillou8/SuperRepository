#============================================
	SIMULATION       
============================================#


#depart PLW
user(str::ASCIIString) = User(str,PrefdictIntoUser(jair_competP.coords)[1], 1) # str="PLW competition law"
#depart LAWTEL
#usercompetLWTL = User("LWTL competition law",ProfdictIntoUser(profileCompLWTL)[1], 1)

# simulation comparing perfo of different algos within PLW
# the code returns users with their updated history (or consumption)
function SimulationPLW(users::Array{User,1}, RecommMode::ASCIIString = "CollabFilt", ChoiceMode::ASCIIString = "Random")

syst = System(DataFrame(),DataFrame())
initconvert, initgeneral = 0, 0

Ngenerated = 20
Nbflavours = 2
Nrecomm = 10
for time = 2:500 #  150 #100
    store = Store(Ngenerated, Nbflavours) # each day new items
    for user in users  
        @switch RecommMode begin
            "Random" ; recList = Recommender("Random", store, Nrecomm, user, time)
            "LastBased" ; recList = Recommender("LastBased", store, Nrecomm, user, time)
            "CollabFilt" ; recList = Recommender("CollabFilt", store, Nrecomm, user, time)
                "Simulation::RecommMode recognises Random,LastBased,CollabFilt :", exit(1)
        end    

        for i = 1:recList.Nb
            if rand() < recList.viewProba[i]

                if @switch ChoiceMode begin    
                        "Random"; rand_Choice(0.2)
                        "PrefsHard"; prefs_Choice(user, recList.instore[i].kwords) 
                        "LogitU"; logitU_Choice(user, recList.instore[i].kwords)
                            "Simulation::ChoiceMode recognises Random,PrefsHard,LogitU :", exit(1)
                    end
                    for k in recList.instore[i].kwords
			                        append!(user.history, DataFrame(T = time, Items = k))
                    end
                end
            end
        end

    end
end
    
    users
end

function Simulate( str::ASCIIString, Nb::Int64, RecommMode::ASCIIString, ChoiceMode::ASCIIString )
    users = [ user(str) for i in 1:Nb]
    users = SimulationPLW(users, RecommMode, ChoiceMode)
    res = map( x-> size(@where(x.history, :T .> 1))[1] ,users )
    mean(res), std(res)
end
function Simulate( myusers::Array{ProfilePLW,1}, RecommMode::ASCIIString, ChoiceMode::ASCIIString )
    users = restart(myusers)
    users = SimulationPLW(users, RecommMode, ChoiceMode)
    res = map( x-> size(@where(x.history, :T .> 1))[1] ,users )
    mean(res), std(res)
end
function restart(myusers::Array{ProfilePLW,1})
    users = User[]
    n = 1
    for myu in myusersPLW 
        push!(users,User("$n",PrefdictIntoUser(myu.coords)[1], 1 ))
        n += 1
    end
    users
end

function Recommendation(Typ::ASCIIString, store::gStore, Nrec::Int64, user::User = None, time::Int64 = 0, Uprefs::Array{ASCIIString,1} = ASCIIString[])
    @switch Typ begin
        "Random" ; recList = Recommender("Random", store, Nrec, user, time)
        "LastBased" ; recList = Recommender("LastBased", store, Nrec, user, time)
        "CollabFilt" ; recList = Recommender("CollabFilt", store, Nrec, user, time)
        "CollabFiltPerso" ; recList = Recommender("CollabFiltPerso", store, Nrec, user, time, Uprefs )
                "Simulation::RecommMode recognises Random,LastBased,CollabFilt,CollabFiltPerso :", exit(1)
    end    
    recList
end

function Recommendation(Typ::ASCIIString, store::Store, Nrec::Int64, user::User = None, 
                    time::Int64 = 0, Uprefs::Array{ASCIIString,1} = ASCIIString[])
    @switch Typ begin
        "Random" ; recList = Recommender("Random", store, Nrec, user, time)
        "LastBased" ; recList = Recommender("LastBased", store, Nrec, user, time)
        "CollabFilt" ; recList = Recommender("CollabFilt", store, Nrec, user, time)
        "CollabFiltPerso" ; recList = Recommender("CollabFiltPerso", store, Nrec, user, time, Uprefs )
                "Simulation::RecommMode recognises Random,LastBased,CollabFilt,CollabFiltPerso :", exit(1)
    end    
    recList
end

function Recommendation(Typ::ASCIIString, store::StoreLWTL, Nrec::Int64, user::User = None, 
                    time::Int64 = 0, Uprefs::Array{ASCIIString,1} = ASCIIString[])
    @switch Typ begin
        "Random" ; recList = Recommender("Random", store, Nrec, user, time)
        "LastBased" ; recList = Recommender("LastBased", store, Nrec, user, time)
        "CollabFilt" ; recList = Recommender("CollabFilt", store, Nrec, user, time)
        "CollabFiltPerso" ; recList = Recommender("CollabFiltPerso", store, Nrec, user, time, Uprefs )
                "Simulation::RecommMode recognises Random,LastBased,CollabFilt,CollabFiltPerso :", exit(1)
    end    
    recList
end

function InteractWithUser( ChoiceMode::ASCIIString, recList::RecommList, user::User,  time::Int64 = 0 )
#println("DBGinteractenter ")
   for i = 1:recList.Nb
       if rand() < recList.viewProba[i]
           if @switch ChoiceMode begin    
               "Random"; rand_Choice(0.2)
               "PrefsHard"; prefs_Choice(user, recList.instore[i].kwords) 
               "LogitU"; logitU_Choice(user, recList.instore[i].kwords)
                   "Simulation::ChoiceMode recognises Random,PrefsHard,LogitU :", exit(1)
           end
           
               for k in recList.instore[i].kwords
                   append!(user.history, DataFrame(T = time, Items = k))
               end
           end
       end 
    end
end

function InteractWithUser( ChoiceMode::ASCIIString, recList::RecommListPLW, user::User,  time::Int64 = 0 )
   for i = 1:recList.Nb
       if rand() < recList.viewProba[i]
           if @switch ChoiceMode begin    
               "Random"; rand_Choice(0.2)
               "PrefsHard"; prefs_Choice(user, recList.instore[i].kwords) 
               "LogitU"; logitU_Choice(user, recList.instore[i].kwords)
                   "Simulation::ChoiceMode recognises Random,PrefsHard,LogitU :", exit(1)
           end
           
               for k in recList.instore[i].kwords
                   append!(user.history, DataFrame(T = time, Items = k))
               end
           end
       end 
    end
end

function InteractWithUser( ChoiceMode::ASCIIString, recList::RecommListLWTL, user::User,  time::Int64 = 0 )
   for i = 1:recList.Nb
       if rand() < recList.viewProba[i]
           if @switch ChoiceMode begin    
               "Random"; rand_Choice(0.2)
               "PrefsHard"; prefs_Choice(user, recList.instore[i].kwords) 
               "LogitU"; logitU_Choice(user, recList.instore[i].kwords)
                   "Simulation::ChoiceMode recognises Random,PrefsHard,LogitU :", exit(1)
           end
           
               for k in recList.instore[i].kwords
                   append!(user.history, DataFrame(T = time, Items = k))
               end
           end
       end 
    end
end

function ggSimulation(users::Array{User,1}, RecommMode::ASCIIString = "Random", ChoiceMode::ASCIIString = "Random", Uprefs::Array{ASCIIString,1} = ASCIIString[])
    
   syst = System(DataFrame(),DataFrame())
   initconvert, initgeneral = 0, 0

   Ngenerated = 20
   NbflavoursLWTL, NbflavoursPLW = 2, 3
   Nrecomm = 10
   Nsim = 500

   for time = 2:Nsim 

       store = gStore(Ngenerated, NbflavoursPLW, NbflavoursLWTL) # each day new items
    
        for use in users  
   
           recList = Recommendation( RecommMode, store, Nrecomm, use, time, Uprefs )
       
           InteractWithUser( ChoiceMode, recList, use, time )

        end
end

    users
end

function gSimulation2(users::Array{User,1}, RecommMode::ASCIIString = "Random", ChoiceMode::ASCIIString = "Random", 
                                     prefs::Array{ASCIIString,1} = ASCIISTRING[],  Uprefs::Array{ASCIIString,1} = ASCIIString[])
    
syst = System(DataFrame(),DataFrame())
initconvert, initgeneral = 0, 0
usi = User("hack", prefs, 1) 

Ngenerated = 20
NbflavoursLWTL, NbflavoursPLW = 2, 3
Nrecomm = 10
for time = 501:701 #Nsim #150 #100
    store = gStore(Ngenerated, NbflavoursPLW, NbflavoursLWTL) # each day new items
    for use in users  
    
        @switch RecommMode begin
            "Random" ; recList = Recommender("Random", store, Nrecomm, use, time)
            "LastBased" ; recList = Recommender("LastBased", store, Nrecomm, use, time)
            "CollabFilt" ; recList = Recommender("CollabFilt", store, Nrecomm, use, time)
            "CollabFiltPerso" ; recList = Recommender("CollabFiltPerso", store, Nrecomm, use, time, Uprefs )
                "Simulation::RecommMode recognises Random,LastBased,CollabFilt,CollabFiltPerso :", exit(1)
        end    
        for i = 1:recList.Nb
            if rand() < recList.viewProba[i]
                if @switch ChoiceMode begin    
                        "Random"; rand_Choice(0.2)
                        "PrefsHard"; prefs_Choice(usi, recList.instore[i].kwords) 
                        "LogitU"; logitU_Choice(usi, recList.instore[i].kwords)
                            "Simulation::ChoiceMode recognises Random,PrefsHard,LogitU :", exit(1)
                    end
                    for k in recList.instore[i].kwords
                        append!(use.history, DataFrame(T = time, Items = k))
                    end
                end
            end
        end

    end
end

    users 
end


function gSimulation(users::Array{User,1}, RecommMode::ASCIIString = "Random", ChoiceMode::ASCIIString = "Random", 
                                     prefs::Array{ASCIIString,1} = ASCIISTRING[],  Uprefs::Array{ASCIIString,1} = ASCIIString[])
    
syst = System(DataFrame(),DataFrame())
initconvert, initgeneral = 0, 0

usi = User("hack", prefs, 1) 

Ngenerated = 20
NbflavoursLWTL, NbflavoursPLW = 2, 3
Nrecomm = 10
for time = 2:Nsim #150 #100
    store = gStore(Ngenerated, NbflavoursPLW, NbflavoursLWTL) # each day new items
    for use in users  
    
        @switch RecommMode begin
            "Random" ; recList = Recommender("Random", store, Nrecomm, use, time)
            "LastBased" ; recList = Recommender("LastBased", store, Nrecomm, use, time)
            "CollabFilt" ; recList = Recommender("CollabFilt", store, Nrecomm, use, time)
            "CollabFiltPerso" ; recList = Recommender("CollabFiltPerso", store, Nrecomm, use, time, Uprefs )
                "Simulation::RecommMode recognises Random,LastBased,CollabFilt,CollabFiltPerso :", exit(1)
        end    
        for i = 1:recList.Nb
            if rand() < recList.viewProba[i]
                if @switch ChoiceMode begin    
                        "Random"; rand_Choice(0.2)
                        "PrefsHard"; prefs_Choice(usi, recList.instore[i].kwords) 
                        "LogitU"; logitU_Choice(usi, recList.instore[i].kwords)
                            "Simulation::ChoiceMode recognises Random,PrefsHard,LogitU :", exit(1)
                    end
                    for k in recList.instore[i].kwords
                        append!(use.history, DataFrame(T = time, Items = k))
                    end
                end
            end
        end

    end
end

    users 
end

