(ns multi-armed-bandit.bandit-algos
  (:require [multi-armed-bandit.mc-methods :refer :all]
            [incanter.core :refer :all]
            [incanter.stats :refer :all]
            [incanter.charts :refer :all]))


; ucb alrorithms
(defn score-ucb1 [machine n-overall]
  (let [n (:n machine)
        average (:average machine)]
    ($= average + (sqrt 2 * (log n-overall) / n))))

(defn score-ucb2 [machine epoque-nb alpha]
  (let [n (:n machine)
        alph ($= 1. + alpha)
        tau ($= pow alph n)
        average (:average machine)]
    ($= average + (sqrt ( alph * (log (epoque-nb / n))) / (2 * tau) ))))



;random strategy
(defn random-machine-key [machines]
  (let [rand-key (rand-nth (keys (:machines machines)))]
    rand-key))
