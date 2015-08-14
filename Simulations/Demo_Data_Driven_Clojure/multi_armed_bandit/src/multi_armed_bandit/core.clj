(ns multi-armed-bandit.core
  (:require [multi-armed-bandit.mc-methods :refer :all]))

(defn strat-1 [] (mc-choice 0.58))
(defn strat-2 [] (mc-choice 0.6))
(defn strat-3 [] (mc-choice 0.55))


(defn mc-choice [x]
  (< (rand) x))

(defn strategy-update [strategy value]
  (if (strategy) (+ value 1.0) value))

;(strat-1)
;(strategy-update  strat-1 0.0)

(defn ucb1-gambling [machines-strategies-vector machines-values-vector]
  (let [index-max  (first (apply min-key second (map-indexed vector machines-values-vector)))
        strategy (nth machines-strategies-vector index-max)
        value (nth machines-values-vector index-max)]
  (strategy-update strategy value)))


(defn foo
  "I don't do a whole lot."
  [x]
  (println x "Hello, World!"))
