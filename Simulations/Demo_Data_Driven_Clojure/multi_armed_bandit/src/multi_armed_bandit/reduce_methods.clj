(ns multi-armed-bandit.reduce-methods
  (:require [incanter.core :refer :all]
            [incanter.stats :refer :all]
            [incanter.charts :refer :all]))


(defn machine->use-stat 
  ; utility function adding the use counts
  [bandit-history-vect]
  (reduce (fn [output element]
            (conj output (assoc element :nuse (count output))))
          []
          bandit-history-vect))


; statistical post-processing 
(defn collect-statistics [dbs-bandits]
  (map (fn [bandit] 
       (let [p (-> bandit :probability)
             nb (-> bandit :history count) 
             variance ($= nb * (p * (1. - p)))
             std (sqrt variance)]
       {:nb nb :p p :std std}))
    dbs-bandits))

(defn do-statistics [statistics-summary strategy-value]
  (let [p-best (apply max (map :p statistics-summary))
        p-mean (mean (map :p statistics-summary) )
        nb-total (reduce + (map :nb statistics-summary))
        gain ($= strategy-value - (p-mean * nb-total))      
        regret ($= strategy-value - (p-best * nb-total))
        error (sqrt (reduce (fn [sum std] (+ sum (pow std 2.))) 0.0 (map :std statistics-summary))) 
      ] 
  {:gain gain :regret regret :sigma error}))

(defn run-statistics [bandit-strategies]
  (let [strategy-conversions (:value bandit-strategies)
        statistics-summary (collect-statistics (vals (:bandits bandit-strategies)))
        statistics-scores (do-statistics statistics-summary strategy-conversions)
        ]
    statistics-scores))









;not in use...
;(defn event->score-update [score-list element]
;  (let[strat-key (:strategy element)
;       n (:n element)
;       score (first score-list)
;       nb (strat-key score)
;       new-score (assoc score strat-key (+ nb 1) :n n)]
 ;   new-score))

;(defn history->machines-scores [f coll]
;  (reduce (fn [output element]
 ;           (cons (f output element) output))
;              scores
;            coll))
;
;(def plot-summary
;  (to-dataset (history->machines-scores event->machine-score coll)))
