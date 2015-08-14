(ns style-tagger.simulation
  (:require [style-tagger.tables :refer :all]
            [style-tagger.cassandra-db :refer :all]
            [style.productsList :refer :all]
            [simul-tools.mc-methods :refer :all]
            [style-tagger.simulation-utils :refer :all]))

;;;;;;;;;;;;;;;;;;;;;;;;;;
;   simulation           ;
;;;;;;;;;;;;;;;;;;;;;;;;;;

; prepare database
(def cassandra (connect-cassandra ))
(drop-keyspace "analytics0")
(create-keyspace cassandra "analytics0")
(def cassandra-ks (connect-keyspace "analytics0"))

(def my-site 
  {:men (list :dress :shirt :pants)
   :women (list :dress :shirt :pants)
   :bla (list :dress :shirt :pants)
   :bli (list :dress :shirt :pants)
   :blo (list :dress :shirt :pants)})

(defn rand-visit
  [website-tree]
  (let [
        tree-level-1 (nth (keys website-tree) (rand-int (count website-tree)))
        tree-level-2 (nth (tree-level-1 website-tree) (rand-int (count (tree-level-1 website-tree))))
        ]
    (str tree-level-1 tree-level-2)))

(create-table cassandra-ks  
              "analytics0" 
              "conversions0" 
              (assoc product-template 
                     :unixtime :bigint 
                     :action :varchar
                     :eventvalue :varchar 
                     :userid :varchar
                     :location :varchar
                     :pageversion :varchar))

(create-table cassandra-ks
              "analytics0" 
              "events0" 
              event-template) 



(def N-products-insite 100)
(def site-prod-list 
  (products-list N-products-insite))


(for [user-id (range 1000)]
  (let [ 
        userId (poisson-distr->events 10 (str user-id))
        prod (nth site-prod-list (rand-int N-products-insite))
        prod->cassandra (prepare-product prod product-template)
        location (str (rand-visit my-site))
        pageVersion "0"
        unixTime (System/currentTimeMillis)
        event-value (:sku prod) 
        action (if (mc-choice 0.5) 
                 "view"
                 "click&conversion")
        ]
    (cond 
      (= action "view") (try (action-item->cassandra cassandra-ks 
                                                "analytics0"
                                                "events0"
                                                {}
                                                userId action event-value location pageVersion))
      (= action "click&conversion") (try 
                                      (action-item->cassandra cassandra-ks
                                                              "analytics0"
                                                              "events0"
                                                              {}
                                                              userId action event-value location pageVersion) 
                                      (action-item->cassandra cassandra-ks
                                                              "analytics0"
                                                              "conversions0"
                                                              prod->cassandra
                                                              userId action event-value location pageVersion) 
                                    )
      :else "action type not found"))
  )


    


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;);)
      ;(let [
      ;      prod (nth site-prod-list (rand-int N-products-insite))
      ;      prod->cassandra (prepare-product prod product-template)
      ;      ]
      ;(action-item->cassandra "analytics0" 
      ;                        "events0"
      ;                        {}  
      ;                        userId action location pageVersion)
        
      ;(action-item->cassandra "analytics0" 
      ;                        "conversions0"
      ;                        prod->cassandra                   
      ;                        userId action location pageVersion))

;(nth site-prod-list 4)


;(defn action-item->cassandra 
;  ([ks table prepared-product userId action location page-version]
;  (insert-element ks table
;                 (assoc prepared-product 
;                    :unixTime (System/currentTimeMillis) 
;                    :action action
;                    :userId userId
;                    :location location
;                    :pageVersion page-version)))


