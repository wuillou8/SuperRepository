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
  [n strategy average value history])

(defrecord bandits 
  ; portfolio general performance
  ; n iterations of bandit
  ; strategy return function (item/user later)
  ; value is the conversions or income for particular good
  ; history is the data stored into database
  [n bandits average value history])

; basic function
(defn get-bandit-value [bandit]
  (let [n (:n bandit)
        strategy (str (:strategy bandit))
        average (:average bandit)
        value (:value bandit)]
  {:n n :strategy strategy :average average :value value}))

; simulation functions

(defn sweep-bandit 
  ([bandit n]  
    (let[strategy (:strategy bandit)
         value (:value bandit)
         ;n (:n bandit)
         history (:history bandit)
       
         n-update (+ n 1)
         value-update (if (strategy) (+ value 1.) value)
         n-average (count history)
         average-update  (if (not= 0 n-average)
                          (float (/ value-update (count history)))
                          value-update)
         
         history-update (conj history (get-bandit-value bandit))]
      (->bandit n-update strategy average-update value-update history-update))))

(defn sweep-bandits [bandits strategy-choice-fct]
    (let[n (:n bandits)
         value (:value bandits)
         history (:history bandits)

         bandit-key (strategy-choice-fct bandits)
         value-bandit (-> bandits :bandits bandit-key :value) 
         bandit-update (sweep-bandit (-> bandits :bandits bandit-key) n)

         n-update (+ n 1)
         value-update (+ value (- (:value bandit-update) value-bandit))  
         average-update (float (/ value-update n-update))
         bandits-update (assoc (:bandits bandits) bandit-key bandit-update)
         history-update (conj history (assoc {:n n-update :value value-update :average average-update} :strategy bandit-key) 
                        )
         bandits (->bandits n-update bandits-update average-update value-update history-update)
         ]
      bandits))


(defn simulation-run [my-bandits strategy-fct iterations-nb] 
  (loop [bandits my-bandits cnt iterations-nb]  
    (if (= cnt 0)
      bandits 
      (recur (sweep-bandits bandits strategy-fct) (dec cnt))))) 



