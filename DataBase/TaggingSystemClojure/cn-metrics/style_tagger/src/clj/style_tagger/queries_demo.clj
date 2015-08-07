(ns style-tagger.queries
  (:require [style-tagger.cassandra-db :refer :all]
            [clojurewerkz.cassaforte.client :as cc]
            [clojurewerkz.cassaforte.cql :as cql]
            [clojurewerkz.cassaforte.query :as q]
            [incanter.core :refer :all]
            [incanter.stats :refer :all]
            [incanter.charts :refer :all]))



(defn get-userid<->data
  ([conn-ks table userid time-init time-end]
    (cql/select conn-ks table
        (q/where [[> (q/token :timestamp) (q/token time-init)]
                  [< (q/token :timestamp) (q/token time-end)]
                  [= :userid userid]])
        (q/allow-filtering)))
  ([conn-ks table userid time-init time-end category]
    (cql/select conn-ks table
        (q/where [[> (q/token :timestamp) (q/token time-init)]
                  [< (q/token :timestamp) (q/token time-end)]
                  [= :userid userid]
                  [= :category category]])
        (q/allow-filtering))))
  
(defn get-timestamp<->productid []
  (cql/select cassandra-ks :purchases 
            (q/where [[> (q/token :timestamp) (q/token time-init)]
                      [< (q/token :timestamp) (q/token time-end)]])))



;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; DB Reduce
(def time-init 0)
(def time-end 1000000000000)
(def cassandra-ks (connect-keyspace "analytics0"))


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; goal 1: 
;   I want to see a list of all users 
(def user-ids 
  (-> (get-column-elements cassandra-ks :events :userid)
      :userid
      distinct))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; goal 2:
;  retrieve userId <-> itemId

; browsing activity
(def userid<->itemid-browse    
  (for [user-id user-ids]
    (let [
          category "browse"
          q (get-userid<->data cassandra-ks :events user-id time-init time-end category)
          ]
    (to-dataset q))))

(def userid<->itemid-transaction    
  (for [user-id user-ids]
    (let [
          category "transaction"
          q (get-userid<->data cassandra-ks :events user-id time-init time-end category)
          ]
    (to-dataset q))))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; goal 3:
;   select $ <-> unixtime

(def timestamp<->productid
  (to-dataset 
    (sort-by :timestamp 
      (get-timestamp<->productid))))

(head timestamp<->productid)


(def site-turnover (atom 0.0))
(def timestamp<->turnover 
  (to-dataset
    (for [row (:rows timestamp<->productid)]
      (let [
        turnover  (swap! site-turnover (fn[r] 
                                         (let [price (:productprice row)
                                               cost (:productcosts row)
                                               revenue ($= price - cost)]
                                          ($= r + revenue))))
        timestamp  (:timestamp row)
        ]
      {:timestamp timestamp :turnover turnover}))
  ))

(doto
      (scatter-plot :timestamp :turnover
                    :data timestamp<->turnover
                    :title "Turnover (time)")
      (view)
    )



