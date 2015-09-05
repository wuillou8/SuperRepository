(ns cn-simulation.new-simulation
 (require  [cn-simulation.mc-methods :refer :all]
           [cn-simulation.metrics :refer :all]
           [cn-simulation.useritem-behaviour :refer :all]
           [cn-simulation.recommender :refer [rand-recomm]]
           [incanter.core :refer :all]
           [incanter.stats :refer :all]
           [incanter.charts :refer :all]
           [incanter.pdf :refer :all]))




(defrecord simulation [users items model n-recommlist t-init t-end history-db])

(defn init-history-db []
  []) 

; model glob variables
(def Nusers 5)
(def Nitems 1000)

(def Ntot-features 50)
(def Nuser-features 5)
(def Nitem-features 3)
(def t-init 0)
(def t-end 100)
(def n-iterations 100)
(def history-db (init-history-db))
(def n-recommlist 10)

; generate players
(def users (map #(create-rand-user % Nuser-features Ntot-features) (range Nusers)))
(def items (map #(create-rand-item % Nitem-features Ntot-features) (range Nitems)))
(def table-items (zipmap (map :id items) items))

; Params
(def my-simulation (->simulation users items rand-recomm n-recommlist  t-init t-end history-db))

(defn rand-choice [N items]
  (loop [choice-list []]
    (if (= N (count choice-list))
      choice-list
      (recur (distinct 
               (conj choice-list (rand-nth items)))))))

(defn sweep-simulation [simulation t]
  (let [users (:users simulation)
        items (:items simulation)
        model (:model simulation)
        n-recommlist (:n-recommlist simulation)
        history-db (:history-db simulation)]
   (into []
    (for [user users]
      (let [recommended (model n-recommlist items history-db)
            converted (rand-choice 2 recommended)
            user-id (:id user)]
        {:t t :user-id user-id :recommended (map :id recommended) :converted (map :id converted)}))
      )))

(defn run-simulation [simulation]
  (let [t-init (:t-init simulation)
        t-end (:t-end simulation)]
    (loop [t t-init simul simulation]
      (if (= t t-end)
        simul
        (recur (inc t)
               (assoc simul :history-db
                  (concat (sweep-simulation simul t) (:history-db simul))))
        ))))

      
(def simul (run-simulation my-simulation))

  (:history-db simul)




