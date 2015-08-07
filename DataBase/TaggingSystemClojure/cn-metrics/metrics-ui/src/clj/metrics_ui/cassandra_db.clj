(ns metrics-ui.cassandra-db
  (:require [clojurewerkz.cassaforte.client :as cc]
            [clojurewerkz.cassaforte.cql :as cql]
            [clojurewerkz.cassaforte.query :refer :all]))

; cassaforte is a clojure wrapper for cassandra
; documentation under:
; http://clojurecassandra.info/articles/getting_started.html
; http://reference.clojurecassandra.info/clojurewerkz.cassaforte.cql.html

;;;;;;;;;;;;;;;;;;;;;;;;;;;
; basic functionalities

(defn connect-cassandra []
  (cc/connect ["127.0.0.1"]))

(defn connect-keyspace [ks]
  (cc/connect ["127.0.0.1"] {:keyspace ks}))

(defn create-keyspace [conn ks]
  ; simple keyspace creation, params not suitable for prod...
  (let [conn (cc/connect ["127.0.0.1"])]
    (cql/create-keyspace conn ks
      (if-not-exists)      
      (with {:replication
              {:class "SimpleStrategy"
               :replication_factor 1}}))))

(defn drop-keyspace [ks]
  ; delete keyspace
  (let [conn (cc/connect ["127.0.0.1"])]
  (cql/drop-keyspace conn ks)
  (if-exists))) 

(defn create-table [conn table c-defs]
  ; t is table name, c-defs is a map with the table keys, e.g
  ; c-defs = {:name :varchar
  ;           :age  :int                                                               
  ;           :primary-key [:name]}))))
  (cql/create-table conn table
      (if-not-exists)
      (column-definitions c-defs)))       

(defn drop-table [ks table-name]
  ; delete table in keyspace
  (let [conn (cc/connect ["127.0.0.1"] {:keyspace ks})]
   (cql/drop-table conn table-name)
   (if-exists)))

;(def cassandra-ks (connect-keyspace "analytics0"))
;(drop-table "analytics0" "events")

(defn insert-element [conn ks table obj-map]
  ; ks is keyspace, table is table name, obj-map is the map to be push into cassandra, e.g. {:userid (int 4554) :fname "bbb"  :lname "ccc"}
  (cql/insert conn table obj-map))

;;;;;;;;;;;;;;;;;;;;;;;;;;;
; product functionalities

(defn map-event->cassandra [item product-template-el]
  (let [key-value (key product-template-el)
        key-type (val product-template-el)]
      (if-not-exists)  (cond 
          (= :varchar key-type) {key-value (key-value item)}
          (= :int key-type) {key-value (-> (key-value item) read-string int)}
          (= :float key-type) {key-value (-> (key-value item) read-string float)}
          (= :bigint key-type) {key-value (-> (key-value item) read-string long)}
          (= :text key-type) {key-value (key-value item)}
          :else "key-type not found")))

(defn event->cassandra  [product prod-map]
  (let [prodmap (dissoc prod-map :primary-key)]
    (apply merge (map #(map-event->cassandra product %) prodmap))))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;



;[conn ks table obj-map]

;(def session (connect-cassandra))

;(cql/create-keyspace session "main"
;    (if-not-exists)
;        (with {:replication {:class "SimpleStrategy"
;                              :replication_factor 1}}
;        )
;)

;(drop-keyspace "main")


;(defn action-item->cassandra 
;  [conn ks table prepared-product userId action event-value location page-version]
;  (insert-element conn ks table
;                 (assoc prepared-product 
;                    :unixtime (System/currentTimeMillis) 
;                    :action action
;                    :eventvalue event-value
;                    :userid userId
;                    :location location
;                    :pageversion page-version)))

;(defn actions-items->cassandra
;  [conn ks table events]
;  (for [event events]
;    (let[
;         action (:action event)
;         userId (:userId event)
;         location (:location event)
;         page-version (:pageVersion event)
;         prod   (prepare-product (:prod event) product-template)
;         ]
;    (action-item->cassandra conn ks table prod userId action location page-version))))


