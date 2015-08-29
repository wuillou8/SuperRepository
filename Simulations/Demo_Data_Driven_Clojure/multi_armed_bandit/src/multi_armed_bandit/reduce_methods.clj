(ns multi-armed-bandit.reduce-methods
  (:require [incanter.core :refer :all]
            [incanter.stats :refer :all]
            [incanter.charts :refer :all]))



(defn event->score-update [score-list element]
  (let[strat-key (:strategy element)
       n (:n element)
       score (first score-list)
       nb (strat-key score)
       new-score (assoc score strat-key (+ nb 1) :n n)]
    new-score))

(defn history->machines-scores [f coll]
  (reduce (fn [output element]
            (cons (f output element) output))
              scores
            coll))

(def plot-summary
  (to-dataset (history->machines-scores event->machine-score coll)))
