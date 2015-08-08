(ns metrics.recommender
  (require [incanter.core :refer :all]
           [incanter.stats :refer :all]
           [incanter.charts :refer :all]))


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; collaborative filtering
(defn rand-recomm [N items]
  (for [i (range N)] 
    (rand-nth items)))


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; collaborative filtering
(defn collab-score0 
  ;usage dataset with user usage, item-id is number
  ;table items is the items table.
  [id-item usage]
  (let [ 
        item-scored (get table-items id-item)
        scores (map 
                 (fn [line]
                    (let [
                          t (:t-time line)
                          id (:item-id line)
                          item-line (get table-items id)
                          buy? (if (:tag-buy line) 1 0)
                          sim (item-item->sim item-scored item-line)
                          score ($= sim * buy?)
                          ]
                  {:score score :sim sim}))
                 (:rows usage))
        collab-score ($= (sum (map :score scores)) / ( 1 + (count scores) )) 
       ]
   {:id-item id-item :collab-score collab-score})) 

(defn collab-filtering0 
  [user-id recomm-length full-usage-history]
  (let [
        user-history ($where {:usr-id user-id} full-usage-history)
        scores (map #(collab-score0 % user-history) (keys table-items))
        rankings (sort-by :collab-score > scores)         
        recomm-list (take recomm-length rankings)
        
        recomm-items (map #(get table-items (:id-item %)) recomm-list)
        ]
     recomm-items))


