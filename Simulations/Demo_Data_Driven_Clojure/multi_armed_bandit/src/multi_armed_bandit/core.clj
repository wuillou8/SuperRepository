(ns multi-armed-bandit.core
  (:require [multi-armed-bandit.mc-methods :refer :all]
            [incanter.core :refer :all]
            [incanter.stats :refer :all]
            [incanter.charts :refer :all]))


(defrecord machine [n strategy average value history])
(defrecord machines [n machines average value history])

(defn get-machine-value [machine]
  (let [n (:n machine)
        strategy (str (:strategy machine))
        average (:average machine)
        value (:value machine)]
  {:n n :strategy strategy :average average :value value}))

(defn random-machine-key [machines]
  (let [rand-key (rand-nth (keys (:machines machines)))]
    rand-key))

(defn strat-1 [] (mc-choice 0.5))
(defn strat-2 [] (mc-choice 0.65))
(defn strat-3 [] (mc-choice 0.55))

(def machine-1 (->machine 0 strat-1 0.0 0.0 [])) 
(def machine-2 (->machine 0 strat-2 0.0 0.0 [])) 
(def machine-3 (->machine 0 strat-3 0.0 0.0 [])) 

(def machines-pfolio (->machines 0
                        {:m1 machine-1 :m2 machine-2 :m3 machine-3}
                                 0.0 0.0 []))

(defn strategy-update [strategy value]
  (if (strategy) (+ value 1.0) value))

(defn sweep-iteration 
  ([machine]  
    (let[strategy (:strategy machine)
         value (:value machine)
         n (:n machine)
         history (:history machine)
       
         n-update (+ n 1)
         value-update (if (strategy) (+ value 1.) value)
         average-update (float (/ value-update n-update))
         history-update (conj history (get-machine-value machine))]
      (->machine n-update strategy average-update value-update history-update)))

  ([machines strategy-choice-fct]
    (let[n (:n machines)
         value (:value machines)
         history (:history machines)

         machine-key (strategy-choice-fct machines)
         value-machine (-> machines :machines machine-key :value) 
         machine-update (sweep-iteration (-> machines :machines machine-key))
         
         n-update (+ n 1)
         value-update (+ value (- (:value machine-update) value-machine))  
         average-update (float (/ value-update n-update))
         machines-update (assoc (:machines machines) machine-key machine-update)
         history-update (conj history (assoc (get-machine-value machine-update) :strategy (str machine-key)))]
      (->machines n-update machines-update average-update value-update history-update))))
;(println machine-key ;n value history machine-key value-machine
       ;value-update
       ;average-update
 ;      machines-update
 ;      " -------- "
 ;      history-update
 ;      ))))

(sweep-iteration machine-1)
(sweep-iteration machines-pfolio random-machine-key)
;(keys (:machines machines-pfolio))

;(random-machine-key machines-pfolio)
;(sweep-iteration machines-pfolio)
;
;
;
(defn recur-machine-run [my-machines strategy-choice iterations-nb] 
  (loop [machines my-machines cnt iterations-nb result []]  
    (if (= cnt 0)
       result
      (recur (sweep-iteration machines strategy-choice) (dec cnt) (conj result (get-machine-value machine)))))) 

(defn recur-machine-run [my-machine iterations-nb] 
  (loop [machine my-machine cnt iterations-nb result []]  
    (if (= cnt 0)
       result
      (recur (:machine (sweep-iteration machine)) (dec cnt) (conj result (get-machine-value machine)))))) 


(defn run-simulation [n-simulation]
  (let [m-1 (recur-machine-run machine-1 n-simulation)
        m-2 (recur-machine-run machine-2 n-simulation)
        m-3 (recur-machine-run machine-3 n-simulation)]
  (concat m-1 m-2 m-3)))


;(recur-machine-run machine-1 4)
(def n 50000)
(def my-data (-> (run-simulation n) to-dataset) );1000000)

(doto
  (scatter-plot :n :value
    :title "Comparison machines"
    :y-label "value"
    :x-label "n"
    :data my-data
    :group-by :strategy)
  clear-background
  view)



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

;(defn score-epsilon-greedy [] 
;  )

(defn random-strategy [strategy-list]
  )

(def machine-1 (->machine 1 strat-1 0.0 0.0))
(score-ucb1 machine-1 1)




(defn foo
  "I don't do a whole lot."
  [x]
  (println x "Hello, World!"))
