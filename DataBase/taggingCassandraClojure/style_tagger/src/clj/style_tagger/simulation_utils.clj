(ns style-tagger.simulation-utils 
  (:require [style-tagger.cassandra-db :refer :all]
            [style.productsList :refer :all]
            [simul-tools.mc-methods :refer :all]))

(defn prepare-event->cassandra 
  [item product-template-el]
  (let [
        key-value (key product-template-el)
        key-type (val product-template-el)
        ]
        (cond 
          (= :varchar key-type) {key-value (key-value item)}
          (= :int key-type) {key-value (-> (key-value item) read-string int)}
          (= :float key-type) {key-value (-> (key-value item) read-string float)}
          (= :bigint key-type) {key-value (-> (key-value item) read-string long)}
          (= :text key-type) {key-value (key-value item)}
          :else "key-type not found")))

(defn prepare-product 
  [product prod-map]
  (let [
        prodmap (dissoc prod-map :primary-key)
        prod (apply merge (map #(prepare-event->cassandra product %) prodmap)) 
        ]
    prod))

(defn action-item->cassandra 
  [conn ks table prepared-product userId action event-value location page-version]
  (insert-element conn ks table
                 (assoc prepared-product 
                    :unixtime (System/currentTimeMillis) 
                    :action action
                    :eventvalue event-value
                    :userid userId
                    :location location
                    :pageversion page-version)))

(defn actions-items->cassandra
  [conn ks table events]
  (for [event events]
    (let[
         action (:action event)
         userId (:userId event)
         location (:location event)
         page-version (:pageVersion event)
         prod   (prepare-product (:prod event) product-template)
         ]
    (action-item->cassandra conn ks table prod userId action location page-version))))


