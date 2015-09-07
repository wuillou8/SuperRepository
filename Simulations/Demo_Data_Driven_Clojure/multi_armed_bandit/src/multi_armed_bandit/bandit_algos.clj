(ns multi-armed-bandit.bandit-algos
  (:require [multi-armed-bandit.mc-methods :refer :all]
            [incanter.core :refer :all]
            [incanter.stats :refer :all]
            [incanter.charts :refer :all]))


; scores functions
(defn score-ucb1 
  ; ucb1 algo, paper 2002 finit-time analysis of mutliarmed bandit
  ; auer/cesa-bianchi/fischer
  [bandit n-overall]
  (let [n (count (:history bandit))
        average (:probability bandit)]
   (if (not= 0 n) 
     ($= average + (sqrt 2 * (log n-overall) / n))
     ($= 1000.))))

(defn score-ucb2 
  ; ucb2 algo, paper 2002 finit-time analysis of mutliarmed bandit
  ; auer/cesa-bianchi/fischer
  [bandit epoque-nb alpha]
  (let [n (count (:history bandit))
        alph ($= 1. + alpha)
        tau ($= pow alph n)
        average (:probability bandit)]
    ($= average + (sqrt ( alph * (log (epoque-nb / n))) / (2 * tau) ))))


; strategies
(defn bandits->random-strategy 
  ; random strategy
  [bandits]
  (let [rand-bandit (rand-nth (keys (:bandits bandits)))]
    rand-bandit))

(defn bandits->ucb1-strategy 
  ; ucb1
  [bandits]
  (let [n (:n bandits)
        key-bandit (key 
            (apply max-key #(score-ucb1 (val %) n) (:bandits bandits)))]
  key-bandit))
