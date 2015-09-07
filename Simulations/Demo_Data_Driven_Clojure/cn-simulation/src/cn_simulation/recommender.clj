(ns cn-simulation.recommender
  (require [cn-simulation.useritem-behaviour :refer :all] 
           [incanter.core :refer :all]
           [incanter.stats :refer :all]
           [incanter.charts :refer :all]))

(defn rand-recomm [N user hash-items history-db]
  ; produce random recommendations
  (loop [recomm-list []]
    (if (= N (count recomm-list))
      recomm-list
      (recur (distinct 
               (conj recomm-list (rand-nth (vals hash-items))))))))

(defn- item-history->scores [item history hash-items]
  ; produces scores for item-based collaborative filtering
  ; we simply take the mean instead of reweighting for now...
  (mean 
    (map (fn [tmp] 
            (let [converted (map #(get hash-items %) (:converted tmp))
                  recommended (map #(get hash-items %) (:recommended tmp))
                  score (- (sum (map #(item-item->sim item %) converted))
                           (sum (map #(item-item->sim item %) recommended)))]
      score))
    history)))

(defn collab-item-filt [N user hash-items history-db]
  ; item-based collaborative filtering.
  (let [user-id (:id user)
        history (filter #(= user-id (:user-id %)) 
                           history-db)
        scored-list (->> (map (fn [item] 
                          {:item item :score (item-history->scores item history)}) 
                            (vals hash-items))
                      (sort-by :score >) 
                      (map :item))]
    scored-list))
