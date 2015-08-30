(ns multi-armed-bandit.run
  (:require [multi-armed-bandit.mc-methods :refer :all]
            [multi-armed-bandit.bandit-algos :refer :all]
            [multi-armed-bandit.bandits :refer :all]
            [incanter.core :refer :all]
            [incanter.stats :refer :all]
            [incanter.charts :refer :all]
            [incanter.pdf :refer [save-pdf]]))



; generate 3 different machines, with different performance rates
(defn strat-1 [] (mc-choice 0.05))
(defn strat-2 [] (mc-choice 0.065))
(defn strat-3 [] (mc-choice 0.055))

(def bandit-1 (->bandit 0 strat-1 0.0 0.0 [])) 
(def bandit-2 (->bandit 0 strat-2 0.0 0.0 [])) 
(def bandit-3 (->bandit 0 strat-3 0.0 0.0 [])) 

(def bandits-init (->bandits 0
                      {:m1 bandit-1 :m2 bandit-2 :m3 bandit-3}
                        0.0 0.0 []))


; simulation
(def n-simul 10000)

; random run
(def bandits-db-rand (simulation-run bandits-init bandits->random-strategy n-simul))
; ucb1 run
(def bandits-db (simulation-run bandits-init bandits->ucb1-strategy n-simul))

; harvest the histories (vector format)
; multi-armed strategy
(def db-bandits (-> bandits-db :history))
(def dbs-bandits (let [bandit-keys (-> bandits-db :bandits keys)
                       dbs (zipmap bandit-keys (map #(-> bandits-db :bandits % :history) bandit-keys))]
                   dbs))
; random strategy
(def db-bandits-rand (-> bandits-db-rand :history))
(def dbs-bandits-rand (let [bandit-keys (-> bandits-db-rand :bandits keys)
                       dbs (zipmap bandit-keys (map #(-> bandits-db-rand :bandits % :history) bandit-keys))]
                   dbs))

; plot
;(save-pdf 
(doto
  (xy-plot :n :value
    :title "Multiarmed bandits"
    :y-label "conversions"
    :x-label "iterations"
    :data (to-dataset db-bandits)
    :series-label  "bandits portfolio"
    :legend true)
  (add-lines :n :value :data (to-dataset (:m1 dbs-bandits)) :series-label "5% convs")
  (add-lines :n :value :data (to-dataset (:m2 dbs-bandits)) :series-label "6.5% convs")
  (add-lines :n :value :data (to-dataset (:m3 dbs-bandits)) :series-label "5.5% convs")
  
  (set-stroke-color java.awt.Color/black :series 0)
  (set-stroke-color java.awt.Color/red :series 1)
  (set-stroke-color java.awt.Color/blue :series 2)
  (set-stroke-color java.awt.Color/green :series 3)
  
  clear-background
  view
  )
;"./resources/multiarmed_bandit.pdf")


(save-pdf 
(doto
  (xy-plot :n :average
    :title "Multiarmed bandits"
    :y-label "conversion averages"
    :x-label "iterations"
    :data (to-dataset db-bandits)
    :series-label  "bandits portfolio"
    :legend true)
  (add-lines :n :average :data (to-dataset (:m1 dbs-bandits)) :series-label "5% convs")
  (add-lines :n :average :data (to-dataset (:m2 dbs-bandits)) :series-label "6.5% convs")
  (add-lines :n :average :data (to-dataset (:m3 dbs-bandits)) :series-label "5.5% convs")
  
  (set-stroke-color java.awt.Color/black :series 0)
  (set-stroke-color java.awt.Color/red :series 1)
  (set-stroke-color java.awt.Color/blue :series 2)
  (set-stroke-color java.awt.Color/green :series 3)
  
  clear-background
;view
  )
"./resources/multiarmed_bandit_avrg.pdf")


(save-pdf 
(doto
  (xy-plot :n :nuse
    :title "Multiarmed bandits"
    :y-label "Activation Frequency"
    :x-label "iterations"
    :data (to-dataset (machine->use-stat db-bandits))
    :series-label  "bandits portfolio"
    :legend true)
  (add-lines :n :nuse :data (to-dataset (machine->use-stat (:m1 dbs-bandits))) :series-label "5% convs")
  (add-lines :n :nuse :data (to-dataset (machine->use-stat (:m2 dbs-bandits))) :series-label "6.5% convs")
  (add-lines :n :nuse :data (to-dataset (machine->use-stat (:m3 dbs-bandits))) :series-label "5.5% convs")
  
  (set-stroke-color java.awt.Color/black :series 0)
  (set-stroke-color java.awt.Color/red :series 1)
  (set-stroke-color java.awt.Color/blue :series 2)
  (set-stroke-color java.awt.Color/green :series 3)
  
  clear-background
;view
  )
"./resources/multiarmed_bandit_activity.pdf")


; plot comparison random vs multiarmed ucb1
;(save-pdf 
(doto
  (xy-plot :n :value
    :title "Multiarmed bandits vs Random"
    :y-label "conversions"
    :x-label "iterations"
    :data (to-dataset db-bandits)
    :series-label  "ucb1 strategy"
    :legend true)
  (add-lines :n :value :data (to-dataset db-bandits-rand) :series-label "random choice")
  
  (set-stroke-color java.awt.Color/blue :series 0)
  (set-stroke-color java.awt.Color/red :series 1)
 ; (set-stroke-color java.awt.Color/blue :series 2)
 ; (set-stroke-color java.awt.Color/green :series 3)
  
  clear-background
  view
  )
;"./resources/multiarmed_vs_random.pdf")




(last (:m1 dbs-bandits))
{:n 9970, :strategy "multi_armed_bandit.run$strat_1@c1f1229", :average 0.047008548, :value 33.0}
(count (:m1 dbs-bandits))
703
(last (:m2 dbs-bandits))
{:n 9999, :strategy "multi_armed_bandit.run$strat_2@454b27c2", :average 0.064076506, :value 536.0}
(count (:m2 dbs-bandits))
8366
(last (:m3 dbs-bandits))
{:n 9964, :strategy "multi_armed_bandit.run$strat_3@1f113659", :average 0.051612902, :value 48.0}
(count (:m3 dbs-bandits))
931

(defn run-statistics [bandits]
  (let [bandits-keys (keys bandits)

        ])  
  )

(last (val (first dbs-bandits)))
(last (val (:average db-bandits)))
;(:value bandits-db)

(def strat-value (:value bandits-db))
(second (:bandits bandits-db))

(def stat-summary
  (map (fn [bandit] 
       (let [p (-> bandit val last :average)
             nb (-> bandit val count) 
             variance ($= nb * (p * (1. - p)))
             std (sqrt variance)]
       {:nb nb :p p :std std}))
    dbs-bandits))

(let [p-best (apply max (map :p stat-summary))
      p-mean (mean (map :p stat-summary) )
      nb-total (reduce + (map :nb stat-summary))

      gain ($= strat-value - (p-mean * nb-total))      
      regret ($= strat-value - (p-best * nb-total))
      ] 
  {:gain gain :regret regret})

(apply max (list 2 3 4))



(mean [1 2 3 3])
