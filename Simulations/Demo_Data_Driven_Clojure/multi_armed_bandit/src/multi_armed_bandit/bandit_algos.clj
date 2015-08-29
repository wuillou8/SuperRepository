(ns multi-armed-bandit.bandit-algos
  (:require [multi-armed-bandit.mc-methods :refer :all]
            [incanter.core :refer :all]
            [incanter.stats :refer :all]
            [incanter.charts :refer :all]))

; ucb alrorithms
(defn score-ucb1 [bandit n-overall]
  (let [n (:n bandit)
        average (:average bandit)]
    ($= average + (sqrt 2 * (log n-overall) / n))))

(defn score-ucb2 [bandit epoque-nb alpha]
  (let [n (:n bandit)
        alph ($= 1. + alpha)
        tau ($= pow alph n)
        average (:average bandit)]
    ($= average + (sqrt ( alph * (log (epoque-nb / n))) / (2 * tau) ))))



;random strategy
(defn random-bandit-key [bandits]
  (let [rand-key (rand-nth (keys (:bandits bandits)))]
    rand-key))
