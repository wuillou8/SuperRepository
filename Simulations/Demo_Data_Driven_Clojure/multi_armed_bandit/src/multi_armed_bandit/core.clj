(ns multi-armed-bandit.core
  (:require [multi-armed-bandit.mc-methods :refer :all]
            [incanter.core :refer :all]
            [incanter.stats :refer :all]
            [incanter.charts :refer :all]))

(defn strat-1 [] (mc-choice 0.58))
(defn strat-2 [] (mc-choice 0.6))
(defn strat-3 [] (mc-choice 0.55))


;(defn mc-choice [x]
;  (< (rand) x))
(defrecord machine [n strategy average value])

(def machine-1 (->machine 0 strat-1 0.0 0.0)) 
(def machine-2 (->machine 0 strat-2 0.0 0.0)) 
(def machine-3 (->machine 0 strat-3 0.0 0.0)) 

((:strategy machine-1))

(defn strategy-update [strategy value]
  (if (strategy) (+ value 1.0) value))

(defn strategy-update [my-machine]  
  (let[strategy (:strategy my-machine)
       value (:value my-machine)
       n (:n my-machine)
       value-update (if (strategy) (+ value 1.) (value))
       n-update (+ n 1)
       average-update (float (/ value-update n-update))]
  (->machine n-update strategy average-update value-update)))


(defn recur-machine-run [my-machine] 
  (loop [mach my-machine cnt 10]
   (if (= cnt 0)
     machine
    (recur (strategy-update mach) (dec cnt)))))

(def mach1 (->> (strategy-update machine-1) (fn [m] (->machine  (:n m) (:strategy m) (:average m) (:value m)))))
(println (:n mach1))

(recur-machine-run machine-1)

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
