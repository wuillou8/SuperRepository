(ns cn-simulation.new-simulation
 (require [cn-simulation.mc-methods :refer :all]
          [cn-simulation.metrics :refer :all]
          [cn-simulation.useritem-behaviour :refer :all]
          [cn-simulation.recommender :refer :all]
          [incanter.core :refer :all]
          [incanter.stats :refer :all]
          [incanter.charts :refer :all]
          [incanter.pdf :refer :all]))


(defrecord simulation [users items recommender choice n-recommlist t-init t-end history-db])

(defn init-history-db []
  []) 

; model glob variables
(def Nusers 5)
(def Nitems 1000)
(def Ntot-features 50)
(def Nuser-features 5)
(def Nitem-features 3)

(def t-init 0)
(def t-end 100)
(def history-db (init-history-db))
(def n-recommlist 10)

; generate players
(def users (map #(create-rand-user % Nuser-features Ntot-features) (range Nusers)))
(def items (map #(create-rand-item % Nitem-features Ntot-features) (range Nitems)))
(def hash-items (zipmap (map :id items) items))
(def hash-users (zipmap (map :id users) users))

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
  (assoc my-simulation2 :choice random-choice))


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
(events-filter simul1 {} 0 101)

; kpi
; 1)
(defn reduce-conversions [data]
  (reduce  
    (fn [output element]
      (let [nb (count (:converted element))
            n (:cumul-convers (last output))
            nnb (count (:recommended element))
            nn (:cumul-recomms (last output))]
        (conj output (assoc element :cumul-convers (+ n nb) :cumul-recomms (+ nn nnb)))))
    [(merge (first data) (let [dat (first data)
                               cumul-convers (-> data first :converted count)
                               cumul-recomms (-> data first :recommended count)]
                              {:cumul-convers cumul-convers :cumul-recomms cumul-recomms}))]
    (rest data)))


(defn summary-vs-time [simulation query-map t-init t-end]
  (-> (events-filter simulation query-map t-init t-end) 
      reverse
      reduce-conversions))

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
  (run-simulation my-simulation2))

(def sum1 (summary-vs-time simul1 {} 0 101))
(def sum11 (summary-final sum1)) ;simul1 {} 0 101))
(def sum2 (summary-vs-time simul2 {} 0 101))
(def sum22 (summary-final sum2)) ; {} 0 101))
(def sum3 (summary-vs-time simul3 {} 0 101))
(def sum33 (summary-final sum3)) ; {} 0 101))

(println (:convs-per-recomm sum11))
(println (:convs-per-recomm sum22))
(println (:convs-per-recomm sum33))

(println sum1)

