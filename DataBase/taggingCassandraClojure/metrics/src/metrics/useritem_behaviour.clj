(ns metrics.useritem-behaviour
  (:require [metrics.utils :refer :all]
            [metrics.mc-methods :refer :all]
            [incanter.core :refer :all]))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;             User Item Behaviour                               ;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

; synthetic data
(defrecord item0 [id features price])
;users
(defrecord user0 [id  tastes budget])

; utilities
(defn create-rand-item
  [id Nitem-features Ntot-features]
  (let [
        features (for [idx (range Nitem-features)] (rand-int Ntot-features)) ; uniform tastes
        price (rand)
        ]
   (->item0 id features price)))

(defn create-rand-user
  [id Nuser-features Ntot-features]
  (let [ 
        tastes (for [idx (range Nuser-features)] (rand-int Ntot-features)) ; uniform tastes
        budget (rand) ; uniform money
        ]
  (->user0 id tastes budget)))

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

(defn user-item->utility 
  ; utility function v0:
  ; U(user,item,alpha,beta,epsilon) = 
  ;     -\alpha Price + \beta sim_{cos}(user, item) + \epsilon e, 
  ;     with e in N(0,1). 
  [user item alpha beta epsilon]
  (+ (- (* alpha  (:price item)) ) 
     (* beta (user-item->sim user item))
     (* epsilon (noise 0. 1.))) 
  )

(defn item-item->sim
  ; cosine similarity:
  ; sim(\vec x, \vec y) = ( \vec x \cdot \vec y )/ ( \norm(x) \times \norm(y) )
  [item1 item2]
  ( let[
        item-feats1  (:features item1)
        item-feats2  (:features item2)
        matches (count (filter #(in? item-feats1 %) item-feats2))
        score (/ matches (Math/sqrt (* (count item-feats1) (count item-feats2))))
        ]  
  score))

