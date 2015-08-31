(ns multi-armed-bandit.bandits
  (:require [incanter.core :refer :all]
            [incanter.stats :refer :all]
            [incanter.charts :refer :all]))



; bandits definitions
(defrecord bandit 
  ; n time for bandits (exteral time)
  ; strategy return function (item/user later)
  ; value is the conversions or income for particular good
  ; history is the data stored into database
  [n strategy probability value history])

(defrecord bandits 
  ; portfolio general performance
  ; n iterations of bandit
  ; strategy return function (item/user later)
  ; value is the conversions or income for particular good
  ; history is the data stored into database
  [n bandits probability value history])

; basic function
(defn get-bandit-value [bandit]
  (let [n (:n bandit)
        strategy (str (:strategy bandit))
        average (:probability bandit)
        value (:value bandit)]
  {:n n :strategy strategy :probability average :value value}))

; simulation functions
(defn sweep-bandit 
  ([bandit n]  
    (let[strategy (:strategy bandit)
         value (:value bandit)
         ;n (:n bandit)
         history (:history bandit)
       
         value-update (if (strategy) (+ value 1.) value)
         n-average (count history)
         average-update  (if (not= 0 n-average)
                          (float (/ value-update n-average))
                          value-update)
        
        bandit-update (->bandit n strategy average-update value-update history) 
        history-update (conj history (get-bandit-value bandit-update))]
      (assoc bandit-update :history history-update))))

(defn sweep-bandits [bandits strategy-bandits->key n]
    (let[value (:value bandits)
         history (:history bandits)

         bandit-key (strategy-bandits->key bandits)
         bandit (bandit-key (:bandits bandits))
         
         value-bandit (:value bandit) 
         bandit-update (sweep-bandit bandit n)

         value-update (+ value (- (:value bandit-update) value-bandit))  
         n-average (count history)
         average-update (if (not= 0 n-average)
                          (float (/ value-update (count history)))
                          value-update)
         bandits-update (assoc (:bandits bandits) bandit-key bandit-update)
         history-update (conj history (assoc {:n n :value value-update :probability average-update} :strategy bandit-key))
         bandits (->bandits n bandits-update average-update value-update history-update)
         ]
      bandits))


(defn simulation-run [my-bandits strategy-fct iterations-nb] 
  (loop [bandits my-bandits cnt 0]  
    (if (= cnt iterations-nb)
      bandits 
      (recur (sweep-bandits bandits strategy-fct cnt) (inc cnt))))) 



