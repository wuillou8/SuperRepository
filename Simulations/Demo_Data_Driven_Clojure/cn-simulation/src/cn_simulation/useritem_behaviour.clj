(ns cn-simulation.useritem-behaviour
  (:require [cn-simulation.utils :refer :all]
            [cn-simulation.mc-methods :refer :all]
            [incanter.core :refer :all]))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;             User Item & Interaction                           ;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;synthetic data
; items
(defrecord item [id features price])
; users
(defrecord user [id tastes budget])

; utilities
(defn create-rand-item
  [id Nitem-features Ntot-features]
  (let [
        features (for [idx (range Nitem-features)] 
        (rand-int Ntot-features)) ; uniform tastes
        price (rand)
        ]
   (->item id features price)))

(defn create-rand-user
  [id Nuser-features Ntot-features]
  (let [ 
        tastes (for [idx (range Nuser-features)] (rand-int Ntot-features)) ; uniform tastes
        budget (rand) ; uniform money
        ]
  (->user id tastes budget)))

(defn user-item->sim
  ; cosine similarity:
  ; sim(\vec x, \vec y) = ( \vec x \cdot \vec y )/ ( \norm(x) \times \norm(y) )
  [user item]
  ( let[
        user-tastes (:tastes user)
        item-feats  (:features item)
        matches (count (filter #(in? item-feats %) user-tastes))
        score (/ matches (Math/sqrt (* (count user-tastes) (count item-feats))))
        ]  
  score))

(defn item-item->sim
  ; cosine   ; sim(\vec x, \vec y) = ( \vec x \cdot \vec y )/ ( \norm(x) \times \norm(y) )
  [item1 item2]
  ( let[
        item-feats1  (:features item1)
        item-feats2  (:features item2)
        matches (count (filter #(in? item-feats1 %) item-feats2))
        score (/ matches (Math/sqrt (* (count item-feats1) (count item-feats2))))
        ]  
  score))

(defn user-item->utility 
  ; utility function v0:
  ; U(user,item,alpha,beta,epsilon) = 
  ;     -\alpha Price + \beta sim_{cos}(user, item) + \epsilon e, 
  ;     with e in N(0,1). 
  [user item alpha beta epsilon]
  (+ (- (* alpha  (:price item)) ) 
     (* beta (user-item->sim user item))
     (* epsilon (white-noise 0. 1.))) 
  )

; conversion logic
;(defn user-choice->conversion [user items choice]
;  (mapcat #(choice user %) items))

(defn user-choice->conversion [user items choice]
  (mapcat (fn [item] (cond 
                        (choice user item) [(:id item)]
                        :else [])) 
          items))

(defn random-choice [user item]
  (mc-choice 0.05)) 

(defn preference-choice [user item]
  (<= 0.5 (user-item->sim user item)))

; (defn logit-choice [user item]
;  ; logit function calibrated in order to reach approx 5% of conversions
(defn logo-choice-score [user item]
  ; logit function calibrated in order to reach approx 5% of conversions
  (-> ($=  ( 5 * (user-item->sim user item) - (exp (:price item) - (:budget user)) - 1.5))
      (logit-noisy 3.  0.2)))

(defn logit-choice [user item]
;  ; logit function calibrated in order to reach approx 5% of conversions
;  (println user item (user-item->sim user item))
;  (let [value ($= ( 5.0 * (user-item->sim user item) - ( (:price item)) - 1.5))]
    ;(println  user item (user-item->sim user item) (item-item->sim item item))
    (mc-choice (logo-choice-score user item)))





