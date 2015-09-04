(ns cn-simulation.new-simulation
 (require  [cn-simulation.mc-methods :refer :all]
           [cn-simulation.metrics :refer :all]
           [cn-simulation.useritem-behaviour :refer :all]
           [cn-simulation.recommender :refer [rand-recomm]]
           [incanter.core :refer :all]
           [incanter.stats :refer :all]
           [incanter.charts :refer :all]
           [incanter.pdf :refer :all]))




(defrecord simulation [users items model n-iterations n-recommlist t-init t-end history-db])
(defn init-history-db []
  []) 

; model glob variables
(def Nusers 1)
(def Nitems 1000)
(def Ntot-features 50)
(def Nuser-features 5)
(def Nitem-features 3)
(def t-init 0)
(def t-end 10000)
(def n-iterations 100)
(def history-db (init-history-db))

; generate players
(def users (map #(create-rand-user % Nuser-features Ntot-features) (range Nusers)))
(def items (map #(create-rand-item % Nitem-features Ntot-features) (range Nitems)))
(def table-items (zipmap (map :id items) items))

; Params
;(def n-recommlist 50)

(def my-simulation (->simulation users items rand-recomm n-recommlist  t-init t-end history-db))

(defn sweep-simulation [simulation t]
  (let [users (:users simulation)
        items (:items simulation)
        model (:model simulation)
        n-recommlist (:n-recommlist simulation)
        history-db (:history-db simulation)
        ]
    (model n-recommlist items history-db)))

(defn run-simulation [simulation]
  (let [t-init (:t-init simulation)
        t-end (:t-end simulation)
        history-db (:history-db simulation)]
    (for [t (range t-init t-end)]
      (println t)
      (let[recommended (sweep-simulation simulation t)
           converted (rand-nth recommended)]
        (cons {:t t :recommended recommended :converted converted} bhistory-db)))))

(run-simulation my-simulation)





