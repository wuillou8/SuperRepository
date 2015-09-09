(ns cn-simulation.new-simulation
 (require [cn-simulation.mc-methods :refer :all]
          [cn-simulation.metrics :refer :all]
          [cn-simulation.useritem-behaviour :refer :all]
          [cn-simulation.recommender :refer [rand-recomm collab-filtering-item collab-filtering-item-p]]
          [incanter.core :refer :all]
          [incanter.stats :refer :all]
          [incanter.charts :refer :all]
          [incanter.pdf :refer :all]))

(defrecord simulation [users items recommender choice n-recommlist t-init t-end history-db])

(defn init-history-db []
  []) 

; model glob variables
;(def Nusers 1)
;(def Nitems 1000)
;(def Ntot-features 50)
;(def Nuser-features 5)
;(def Nitem-features 3)

; model glob variables
(def Nusers 20)
(def Nitems 100)
(def Ntot-features 10)
(def Nuser-features 4)
(def Nitem-features 4)


(def users (map #(create-rand-user % Nuser-features Ntot-features) (range Nusers)))
(def items (map #(create-rand-item % Nitem-features Ntot-features) (range Nitems)))

;(first users)

;(defn price-function [user item]
;  (exp (- (:budget user) (:price item))))
;
;(price-function (first users) (first items))

(defn logit-choice-score [user item]
  ; logit function calibrated in order to reach approx 5% of conversions
  (-> ($= 2 * ((user-item->sim user item) - (0.2 * (:price item)) - 0.7))
      (logit-noisy 2.  0.2)))


(-> 
  (map #(logit-choice-score (first users) %) items)
  (histogram :nbins 30) 
  view
  )

(->
  (map #(logit-choice-score (first users) %) (vals (update-hash-items hash-items 1.2)))
  (histogram :nbins 30) 
  view
  )

(def t-init 0)
(def t-end 50)
(def history-db (init-history-db))
(def n-recommlist 5)

; generate players
(def users (map #(create-rand-user % Nuser-features Ntot-features) (range Nusers)))
(def items (map #(create-rand-item % Nitem-features Ntot-features) (range Nitems)))

(def hash-items (zipmap (map :id items) items))
(def hash-users (zipmap (map :id users) users))


(defn update-hash-items [hash-items price-delta]
  (let[items (map (fn [item] 
                        (assoc item :price (* price-delta (:price item)))) (vals hash-items))
       ]
    (zipmap (map :id items) items)))



; Params
(def my-simul
  {:users hash-users
   :items hash-items
   :recommender rand-recomm
   :choice logit-choice
   :n-recommlist n-recommlist
   :t-init t-init
   :t-end t-end
   :history-db history-db})

(def my-simulation1
  (apply ->simulation (vals my-simul)))

(def my-simulation2
  (assoc my-simulation1 :recommender collab-filtering-item))

(def my-simulation3 
  (assoc my-simulation1 :recommender collab-filtering-item-p))


;  (apply ->simulation (vals my-simul)));my-simulation1)
;  (assoc my-simulation2 :choice random-choice))


;(count items)


;(user-choice->conversion (first users) items random-choice)
; (user-choice->conversion (first users) items preference-choice)
;(user-choice->conversion (first users) items logit-choice)

(defn sweep-simulation [simulation t]
  (let [users (:users simulation)
        items (:items simulation) 
        recommender (:recommender simulation)
        choice (:choice simulation)
        n-recommlist (:n-recommlist simulation)
        history-db (:history-db simulation)]
    (map
      (fn [user]
        (let [recommended (recommender n-recommlist user items history-db)
              converted (user-choice->conversion user recommended choice)
              user-id (:id user)]
;(println (count recommended))
          {:timestamp t :user-id user-id :recommended (map :id recommended) :converted  converted}))
        (vals users))))

(defn run-simulation [simulation]
  (let [t-init (:t-init simulation)
        t-end (:t-end simulation)]
    (loop [t t-init simul simulation]
      (if (= t t-end)
        simul
        (recur (inc t)
               (assoc simul :history-db
                  (concat (sweep-simulation simul t) (:history-db simul))))))))




(def nnil? (complement nil?))

(defn key-filter [my-key-symbol query-map events]
    ; this is a function filtering keys dimension that have a non-nil value.
    (let [my-key-val (my-key-symbol query-map)]
      (if (nnil? my-key-val) 
        (filter #(= my-key-val (my-key-symbol %)) events) 
        events)))

(defn events-filter [simulation query-map t-init t-end]
  (->> (:history-db simulation)
       (filter (fn [qm] (and (< t-init (:timestamp qm)) (> t-end (:timestamp qm)))))
       (key-filter :user-id query-map)
       (key-filter :recommended query-map)
       (key-filter :converted query-map)))

;(reduce-functions simul1 {:user-id 1} 0 101)
;(events-filter simul1 {} 0 101)

; kpi
; 1)
(defn reduce-conversions [data hash-items]
  (reduce  
    (fn [output element]
      (let [nb (count (:converted element))
            n (:cumul-convers (last output))
            nnb (count (:recommended element))
            nn (:cumul-recomms (last output))
            benef (:cumul-benefit (last output))
            nbenef (->> element :converted (map #(:price (get hash-items %))) sum)
            ]
        (conj output 
          (assoc element :cumul-convers (+ n nb) :cumul-recomms (+ nn nnb) :cumul-benefit (+ benef nbenef)))))
    [(merge (first data) (let [dat (first data)
                               cumul-convers (-> data first :converted count)
                               cumul-recomms (-> data first :recommended count)
                               cumul-benefit (->> data first :converted (map #(:price (get hash-items %))) sum)]
                           {:cumul-convers cumul-convers :cumul-recomms cumul-recomms :cumul-benefit cumul-benefit}))]
    (rest data)))




(defn summary-vs-time [simulation query-map t-init t-end]
  (-> (events-filter simulation query-map t-init t-end) 
      reverse
      (reduce-conversions (:items simulation))))

(defn summary-final 
  ([simulation query-map t-init t-end]
    (let [data (last (summary-vs-time simulation query-map t-init t-end))
          convs-per-recomm (float (/ (:cumul-convers data) (:cumul-recomms data)))]
      (assoc data :convs-per-recomm convs-per-recomm)))
  ([summary-vs-time]
   (let [data (last summary-vs-time)
         convs-per-recomm (float (/ (:cumul-convers data) (:cumul-recomms data)))]
      (assoc data :convs-per-recomm convs-per-recomm))))

(def simul1 
  (run-simulation my-simulation1))
(def simul2 
  (run-simulation my-simulation2))
(def simul3 
  (run-simulation my-simulation3))

(def sum1 (summary-vs-time simul1 {} 0 101))
(def sum11 (summary-final sum1)) ;simul1 {} 0 101))
(def sum2 (summary-vs-time simul2 {} 0 101))
(def sum22 (summary-final sum2)) ; {} 0 101))
(def sum3 (summary-vs-time simul3 {} 0 101))
(def sum33 (summary-final sum3)) ; {} 0 101))

(println (:convs-per-recomm sum11))
(println (:convs-per-recomm sum22))
(println (:convs-per-recomm sum33))

(keys (first sum1))
(mean 
(map #(count (:converted %)) sum1))
(mean
(map #(count (:converted %)) sum2))
(mean
(map #(count (:converted %)) sum3))

(doto 
  (xy-plot :timestamp :cumul-convers
          ;     :title "Multiarmed bandits vs Random"
          ;         :y-label "conversions"
          ;             :x-label "iterations"
          :data (to-dataset sum1)
          :series-label  "random strategy"
          :legend true)
  (add-lines :timestamp :cumul-convers :data (to-dataset sum2) :series-label  "anti-collab. filtering")
  (add-lines :timestamp :cumul-convers :data (to-dataset sum3) :series-label  "collab. filtering")

;  (set-stroke-color java.awt.Color/blue :series 0)
;  (set-stroke-color java.awt.Color/red :series 1)
;  (set-stroke-color java.awt.Color/green :series 2)
  clear-background
  view)

(doto 
  (xy-plot :timestamp :cumul-benefit ;convers
          ;     :title "Multiarmed bandits vs Random"
          ;         :y-label "conversions"
          ;             :x-label "iterations"
          :data (to-dataset sum1)
          :series-label  "random strategy"
          :legend true)
  (add-lines :timestamp :cumul-benefit :data (to-dataset sum2) :series-label  "anti-collab. filtering")
  (add-lines :timestamp :cumul-benefit :data (to-dataset sum3) :series-label  "collab. filtering")

;  (set-stroke-color java.awt.Color/blue :series 0)
;  (set-stroke-color java.awt.Color/red :series 1)
;  (set-stroke-color java.awt.Color/green :series 2)
  clear-background
  view)

;(mean (map :price (vals (:items (assoc my-simulation3 :items (update-hash-items (:items my-simulation3) 0.4))))))

;(mean (map :price (vals (:items (assoc my-simulation3 :items (update-hash-items (:items my-simulation3) 1.2))))))

(def run-1 (-> (run-simulation 
                  (assoc my-simulation3 :items (update-hash-items (:items my-simulation3) 0.4)))
                (summary-vs-time {} 0 101)))

(def run0 (-> (run-simulation 
                  (assoc my-simulation3 :items (update-hash-items (:items my-simulation3) 0.6)))
                (summary-vs-time {} 0 101)))

(def run1 (-> (run-simulation 
                  (assoc my-simulation3 :items (update-hash-items (:items my-simulation3) 0.8)))
                (summary-vs-time {} 0 101)))

(def run2 (-> (run-simulation 
                  (assoc my-simulation3 :items (update-hash-items (:items my-simulation3) 0.9)))
                (summary-vs-time {} 0 101)))

(def run3 (-> (run-simulation (assoc my-simulation3 :items (update-hash-items (:items my-simulation3) 1.0)))
                (summary-vs-time {} 0 101)))

(def run4 (-> (run-simulation (assoc my-simulation3 :items (update-hash-items (:items my-simulation3) 1.1)))
                (summary-vs-time {} 0 101)))

(def run5 (-> (run-simulation (assoc my-simulation3 :items (update-hash-items (:items my-simulation3) 1.2)))
                (summary-vs-time {} 0 101)))


(save-pdf 
(doto 
  (xy-plot :timestamp :cumul-benefit ;convers
           :title "Revenue optimisation through behavioural simulation"
           :y-label "site revenue"
           :x-label "timestamp"
          :data (to-dataset run-1)
          :series-label  "0.4 price"
          :legend true)
  (add-lines :timestamp :cumul-benefit :data (to-dataset run0) :series-label  "0.6 price")
  (add-lines :timestamp :cumul-benefit :data (to-dataset run1) :series-label  "0.8 price")
  (add-lines :timestamp :cumul-benefit :data (to-dataset run2) :series-label  "0.9 price")
  (add-lines :timestamp :cumul-benefit :data (to-dataset run3) :series-label  "1.0 price")
  (add-lines :timestamp :cumul-benefit :data (to-dataset run4) :series-label  "1.1 price")
  (add-lines :timestamp :cumul-benefit :data (to-dataset run5) :series-label  "1.2 price")


;  (set-stroke-color java.awt.Color/blue :series 0)
;  (set-stroke-color java.awt.Color/red :series 1)
;  (set-stroke-color java.awt.Color/green :series 2)
  clear-background
  view)
"./resources/price_optimisation_by_simulation0.pdf")

(for [ i (list run-1 run0 run1 run2 run3 run4 run5) ]
  (println (last i)))

