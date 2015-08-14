(ns metrics.core
  (require [metrics.utils :refer :all]
           [metrics.mc-methods :refer :all]
           [metrics.metrics :refer :all]
           [metrics.useritem-behaviour :refer :all]
           [metrics.chat-ganalytics :refer :all]
           ;[metrics.google-analytics :refer :all]
           [incanter.core :refer :all]
           [incanter.stats :refer :all]
           [incanter.charts :refer :all]
           [clojure.core.matrix :as mat] 
           [clojure.data.json :as json]
           [clj-http.client :as client]))


; model glob variables
(def Nusers 100)
(def Nitems 1000)
(def Ntot-features 50)
(def Nuser-features 5)
(def Nitem-features 3)

; generate players
(def users (map #(create-rand-user % Nuser-features Ntot-features) (range Nusers)))
(def items (map #(create-rand-item % Nitem-features Ntot-features) (range Nitems)))
;(println (first users))
;(println (first items))

(defn buy-boundary
  [x threshold]
  ; criterion for buying/ not buying:
  ; f(x, thres) = thres + (1-thres) * (1 - exp(-x))
  ($= (1. - threshold) * (1 - jexp(- x)) + threshold))

(defn make-tagged-data
  [users items]
  (to-dataset 
    (apply concat 
      (for [user  users]
        (map (fn [item] 
          (let [
                item-id (:id item)
                usr-id  (:id user) 
                p       (:price item)
                util    (user-item->sim user item)
                tag-buy (>= util 0.5) ;(buy-boundary p 0.5)) ;threshold))    
                ]
          {:usr-id usr-id, :item-id item-id, :price p, :util util, :tag-buy tag-buy} )) 
        items)) 
  )))

(def tag-dataset (make-tagged-data users items))
(def buy-stat (float (/ (nrow ($where {:tag-buy true} tag-dataset)) (nrow tag-dataset))))


(doto (scatter-plot :price :util 
                    :group-by :tag-buy 
                    :data tag-dataset )
  (add-function #(buy-boundary % 0.4) 0. 1.)
  view)

(view tag-dataset)

;;;;;;;;;;;;;;;;;
;; toy model

(defn rand-itemlist [N items]
  (for [i (range N)] 
    (rand-nth items)))

(defn interaction-modelv01
  [nb-events size-recolist _fct]
  (for [n (range nb-events)] 
    (let [
          user (rand-nth users)
          show-list (rand-itemlist size-recolist items)
          conv-list ($where {:tag-buy true} (make-tagged-data (list user) show-list))
          event { :usr-id (:id user), :conv (->> ($ :item-id conv-list)(conj []) flatten), :views (map #(:id %) show-list) } 
          event-json (json/write-str event) 
          ]
    (_fct event-json))))

(defn send-to-ga
  ; update standard url - prepare url - send ganal
  [query-map json-str]
  (let [
        lambda 10
        str-to-ga (str "5(link*" json-str "*test)" ) ;5(link*")
        query (assoc query-map :utme str-to-ga)
        url (str "https://ssl.google-analytics.com/__utm.gif?" (params->query-string query))
        ]
    (println json-str)  
    (time (Thread/sleep (poisson-law lambda)))
  (client/get url)))

; push interaction into google analytics
(interaction-modelv01 1000 10 #(send-to-ga ga-query %))

; pull all info from google analytics
(type (q)) ;(type))


; run metrics
(def usage (interaction-modelv01 100 10 identity)) 
(-> (map #(json/read-str % :key-fn keyword) usage) to-dataset)
(type usage)


(defn run-model [nb-users size-list model-label]
  (let [
        usage (interaction-modelv01 nb-users size-list identity)  
        usage-dataset (:rows (to-dataset (map #(json/read-str % :key-fn keyword) usage)))
        precision (events->precision-perfo usage-dataset)
        mrr (events->mrr-perfo usage-dataset)     
        ]
  {:model-label model-label, :nb-users nb-users, :size-list size-list, 
   :precis (:precis precision), :recall (:recall precision), :specif (:specif precision), :f1 (:f1 precision)  
   :mrr (:mrr mrr)}))


(def runs-dataset  
  (apply conj-rows (for [n [10 30 50 70 90 100]]
      (-> (map #(run-model n % "random recommendation") (range 10 100 10)) (to-dataset)))
  ))

(doto 
  (scatter-plot :size-list :recall
                :title "Performance for Random Recomm."
                :y-label "Recall"
                :x-label "Recomm. list size"
                :data runs-dataset
                :group-by :nb-users
                ) ;:legend true :nb-users "")
  clear-background
  ;#(save-pdf % "./pdf-chart.pdf")
  view)

(use '(incanter core charts pdf))
(save-pdf 
  (doto
    (scatter-plot :size-list :recall
                :title "Performance for Random Recomm."
                :y-label "Recall"
                :x-label "Recomm. list size"
                :data runs-dataset
                :group-by :nb-users
                )
  clear-background)
 "./resources/perfo_rand_recall.pdf")

(save-pdf 
  (doto
    (scatter-plot :size-list :precis
                :title "Performance for Random Recomm."
                :y-label "Precision"
                :x-label "Recomm. list size"
                :data runs-dataset
                :group-by :nb-users
                )
  clear-background)
 "./resources/perfo_rand_precis.pdf")

(save-pdf 
  (doto
    (scatter-plot :size-list :f1
                :title "Performance for Random Recomm."
                :y-label "F1"
                :x-label "Recomm. list size"
                :data runs-dataset
                :group-by :nb-users
                )
  clear-background)
 "./resources/perfo_rand_F1.pdf")


(save-pdf 
  (doto
    (scatter-plot :size-list :mrr
                :title "Performance for Random Recomm."
                :y-label "Mean Recip. Rank"
                :x-label "Recomm. list size"
                :data runs-dataset
                :group-by :nb-users
                )
  clear-background)
 "./resources/perfo_rand_mrr.pdf")


(view (scatter-plot (get-dataset :iris) :bins 20 :group-by :Species :legend true))


(view (scatter-plot  (view (scatter-plot) -10 10)


