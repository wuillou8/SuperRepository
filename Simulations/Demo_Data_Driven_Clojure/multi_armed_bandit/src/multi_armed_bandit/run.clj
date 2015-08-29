(ns multi-armed-bandit.core
  (:require [multi-armed-bandit.mc-methods :refer :all]
            [multi-armed-bandit.bandit-algos :refer :all]
            [multi-armed-bandit.bandits :refer :all]
            [incanter.core :refer :all]
            [incanter.stats :refer :all]
            [incanter.charts :refer :all]))



; generate 3 different machines, with different performance rates
(defn strat-1 [] (mc-choice 0.5))
(defn strat-2 [] (mc-choice 0.65))
(defn strat-3 [] (mc-choice 0.55))

(def bandit-1 (->bandit 0 strat-1 0.0 0.0 [])) 
(def bandit-2 (->bandit 0 strat-2 0.0 0.0 [])) 
(def bandit-3 (->bandit 0 strat-3 0.0 0.0 [])) 

(def bandits-pfolio (->bandits 0
                      {:m1 bandit-1 :m2 bandit-2 :m3 bandit-3}
                        0.0 0.0 []))


; simulation
(def n-simul 100000)
(def bandits-db (simulation-run bandits-pfolio random-bandit-key n-simul))
; harvest the histories (vector format)
(def db-bandits (-> bandits-db :history))
(def dbs-bandits (let [bandit-keys (-> bandits-db :bandits keys)
                       dbs (zipmap bandit-keys (map #(-> bandits-db :bandits % :history) bandit-keys))]
                   dbs))
; plotting
(doto
  (xy-plot :n :value
    :title "Comparison bandits"
    :y-label "value"
    :x-label "n"
    :data (to-dataset db-bandits))
  
  (add-lines :n :value :data (to-dataset (:m1 dbs-bandits)))
  (add-lines :n :value :data (to-dataset (:m2 dbs-bandits)))
  (add-lines :n :value :data (to-dataset (:m3 dbs-bandits)))

  clear-background
  view)

