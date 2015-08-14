(ns metrics-ui.queries
  (:require [metrics-ui.cassandra-db :refer :all]
            [clojurewerkz.cassaforte.client :as cc]
            [clojurewerkz.cassaforte.cql :as cql]
            [clojurewerkz.cassaforte.query :as q]
            [incanter.core :refer :all]
            [incanter.stats :refer :all]
            [incanter.charts :refer :all]))


(defn get-column-elements
  ; get elements within a column, 
  ; lowercase symbol is expected as the column name,e.g. :userid
  [conn-ks table column-symbol]
  (let [ 
        elems  (cql/select conn-ks table (q/columns column-symbol))
        elements (map column-symbol elems)
        ]
    {column-symbol elements}))


(def time-init 0)
(def time-end 1000000000000)


(defn find-userid<->data
  [conn-ks table userid time-init time-end actions] ;column-symbol]
  (cql/select conn-ks table
            (q/where [[> (q/token :unixtime) (q/token time-init)]
                      [< (q/token :unixtime) (q/token time-end)]
                      [:in :action actions];["view" "click&conversion"]]
                      [= :userid userid]])
            (q/allow-filtering)))
            ;(apply q/columns (concat (list :unixtime :userid) column-symbol))))

; DB Reduce
(def cassandra-ks (connect-keyspace "analytics0"))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; goal 1: 
;   I want to see a list of all users 
(def userids 
  (get-column-elements cassandra-ks :events0 :userid))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; goal 2:
;  retrieve userId <-> itemId
(def userid<->itemid
  (let [
        q-db (for [ids (:userid userids)]
              (let [
                    q (first (find-userid<->data cassandra-ks :events0 ids time-init time-end ["click&conversion"]))
                    unixtime (:unixtime q)
                    userid (:userid q)
                    action (:action q)
                    eventvalue (:eventvalue q)
                    ]
                {:unixtime unixtime :userid userid :action action :item-id eventvalue}))
       ]
  (to-dataset (filter #(not= nil (:userid %)) q-db))))

(head userid<->itemid)

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; goal 3:
;   select $ <-> unixtime
(def unixtime-price (to-dataset
      (sort-by :unixtime
        (cql/select cassandra-ks "conversions0"
          (q/where [[> (q/token :unixtime) (q/token time-init)]
                    [< (q/token :unixtime) (q/token time-end)]
                    [= :action "click&conversion"]])
          ;(q/order-by [:unixtime :desc])    
          (q/allow-filtering true)
          (q/columns :unixtime :price)
      )))) 

(head unixtime-price)

(doto
      (scatter-plot :unixtime :price
                    :data unixtime-price
                    :title "Perfo (time)")
      (view)
    )

(def site-turnover (atom 0.0))
(def unixtime-turnover 
  (to-dataset
    (for [i (:rows unixtime-price)]
      (let [
        turnover  (swap! site-turnover (fn[$] (+ $ (:price i))))
        unixtime  (:unixtime i)
        ]
      {:unixtime unixtime :turnover turnover}))
  ))

(doto
      (scatter-plot :unixtime :turnover
                    :data unixtime-turnover
                    :title "Turnover (time)")
      (view)
    )


