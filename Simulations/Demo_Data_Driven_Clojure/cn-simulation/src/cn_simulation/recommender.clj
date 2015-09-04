(ns cn-simulation.recommender
  (require [incanter.core :refer :all]
           [incanter.stats :refer :all]
           [incanter.charts :refer :all]))


(defn rand-recomm [N items history-db]
  (for [i (range N)] 
    (rand-nth items)))



(defn rand-recomm [N items history-db]
  (loop [recomm-list []]
    (if (= N (count recomm-list))
      recomm-list
      (recur (distinct 
               (conj recomm-list (rand-nth items)))))))


(distinct (conj [1 2 2] 4))

