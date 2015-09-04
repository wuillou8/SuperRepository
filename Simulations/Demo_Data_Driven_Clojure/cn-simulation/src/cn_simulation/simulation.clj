(ns metrics.simulation
  (require [metrics.utils :refer :all]
           [metrics.mc-methods :refer :all]
           [metrics.metrics :refer :all]
           [metrics.useritem-behaviour :refer :all]
           [metrics.recommender :refer :all]
           [metrics.calibration :refer :all]
           [incanter.core :refer :all]
           [incanter.stats :refer :all]
           [incanter.charts :refer :all]
           [incanter.pdf :refer :all]))



; model glob variables
(def Nusers 1)
(def Nitems 1000)
(def Ntot-features 50)
(def Nuser-features 5)
(def Nitem-features 3)

; generate players
(def users (map #(create-rand-user % Nuser-features Ntot-features) (range Nusers)))
(def items (map #(create-rand-item % Nitem-features Ntot-features) (range Nitems)))
(def table-items (zipmap (map :id items) items))

; functions
(def usage-history0 (to-dataset 
  {:t-time (), :usr-id (), :item-id (), :util (), 
   :price (), :tag-buy (), :p-choice ()}))

(defn filter-dataset
  ; function taking an event list and preprocessing it into a summary 
  [dataset]
  (for [t (distinct ($ :t-time dataset))]
    (let [
          t-dataset ($where {:t-time t} dataset)
          views  (into () ($ :item-id t-dataset))
          convs  (flatten (conj nil ($ :item-id  ($where {:tag-buy true} t-dataset))))
          ]
      {:t t, :convs convs, :views views})))
      
(defn user-item->usage 
  [ t-time user item b-fct alpha sigma threshold]
  (let [
        usr-id  (:id user)
        item-id (:id item)
        
        util    (user-item->sim user item)
        p       (:price item)

        boundary (apply b-fct (list p threshold))
        p-choice (user-model->proba util boundary alpha sigma)        
        tag-buy (mc-choice p-choice)
        ]
  ;(println (mc-choice p-choice))
  {:t-time t-time, :usr-id usr-id, :item-id item-id, :util util, :price p, :tag-buy tag-buy, :p-choice p-choice}))

(defn simulation-model1
  [users items nb-events size-recolist recommender usage-history]
  (loop [usage-history usage-history0 t 0]
   (if (<= nb-events t)
     usage-history
     (let [
           user (first users)
           usage ($where {:usr-id (:id user)} usage-history)
           recomm-list (if (= usage-history usage-history0)
                         (apply rand-recomm (list size-recolist items))
                         (apply rand-recomm (list size-recolist items)))
           latest-usage (to-dataset (map #(user-item->usage t user % buy-boundary1 10. 1. 0.4) recomm-list))
           ]
       (recur (conj-rows usage-history latest-usage) (inc t)))
     )))

(defn simulation-model2
  [users items nb-events size-recolist recommender usage-history]
  (loop [usage-history usage-history0 t 0]
   (if (<= nb-events t)
     usage-history
     (let [
           user (first users)
           usage ($where {:usr-id (:id user)} usage-history)
           recomm-list (if (= usage-history usage-history0)
                         (apply rand-recomm (list size-recolist items))
                         ;(apply rand-recomm (list size-recolist items)))
                         (apply recommender (list (:id user) size-recolist usage)))
           latest-usage (to-dataset (map #(user-item->usage t user % buy-boundary1 10. 1. 0.4) recomm-list))
           ]
       (recur (conj-rows usage-history latest-usage) (inc t)))
     )))


; Run Params           ;
(def N-iterations 100)
(def N-recommlist 50)

; Run random algos     ;
(def historical-usage
  (simulation-model1 users items N-iterations N-recommlist collab-filtering0 usage-history0))
(def filtered-historical-usage 
    (filter-dataset (to-dataset (rest (:rows historical-usage)))))
(def toplot-dataset 
                  (to-dataset (map (fn [events] 
                    (assoc (event->perfo events perfo-ctr) :t (:t events) :type-recomm "random"))
                      filtered-historical-usage)))

; Run collabfilt algos ;
(def historical-usage
  (simulation-model2 users items N-iterations N-recommlist collab-filtering0 usage-history0))
(def filtered-historical-usage 
    (filter-dataset (to-dataset (rest (:rows historical-usage)))))
(def toplot-dataset-collfilt 
                  (to-dataset (map (fn [events] 
                    (assoc (event->perfo events perfo-ctr) :t (:t events) :type-recomm "collabfilt"))
                      filtered-historical-usage)))

(def toplot-total (conj-rows toplot-dataset toplot-dataset-collfilt))

(save-pdf
  (doto 
    (scatter-plot :t :convs
                :title "Performance: random vs coll. filtering"
                :y-label "CTR"
                :x-label "time"
                :group-by :type-recomm
                :data toplot-total
                )
  clear-background
  view)
 "./resources/perfo_recommenders.pdf")

