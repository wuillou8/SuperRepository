(ns earth-mover-distance.emd
  (:require [clojure.core.matrix :refer :all]))


(defn find-dantzig-max [m w y i_idx j_idx]
 ; find the best variable x_{ij}^* = max_{ij} [w_i + y_i -c_{ij} > 0]
 ; which is equivalent to finding min_{ij} [ c_{ij} - w_i - y_i < 0]
 (reduce 
   (fn [min-val el]
    (if (< (:dantzig el) (:dantzig min-val))
      el
      min-val))
    {:dantzig 0 :i -1 :j -1}
    (for [i i_idx j j_idx]
     {:dantzig (- (mget m i j) (mget w i) (mget y j)) :i i :j j})))


(defn algo-russel-iteration [transport]  
  (let [m (:m-costs transport) ;houthakker-matrix
        a (:v-supply transport) ; i insdex  
        b (:v-demand transport) ; j index
        ; authorised indices : only non-zero weights enter the computation 
        i_idx (filter #(not= 0 (nth a %)) (range (ecount a)))
        j_idx (filter #(not= 0 (nth b %)) (range (ecount b)))
        ; step 1 : build w and y 
        w (mapv #(apply max %) (rows m))
        y (mapv #(apply max %) (columns m))
        ; step 2 : find best combinaison ij for transport
        pos (select-keys (find-dantzig-max m w y i_idx j_idx) [:i :j])
        ; step 4 : activity level
        nb-ship (min (mget a (:i pos)) (mget b (:j pos))) 
        ; step 3 : remove activity level to the supply/deamdn level
        a (assoc a (:i pos) (- (nth a (:i pos)) nb-ship)) 
        b (assoc b (:j pos) (- (nth b (:j pos)) nb-ship))
        ; compute transaction costs: nb-ship*c_ij 
        cost (* nb-ship (mget m (:i pos) (:j pos)))]
  ;(println (:i pos) " : " (:j pos) " " nb-ship)
 {:transport (assoc transport :v-supply a :v-demand b) :cost cost}))

(defn run-russel [transport]
  (loop [trans transport cost 0]
    (let [a (:v-supply trans)
          b (:v-demand trans)] 
      (if (= 0 (reduce + (concat b a))) 
        cost
        (let [t (algo-russel-iteration trans)]
          (recur (:transport t) (+ cost (:cost t))))))))




;;;;;;;;;;;;;;;;;;
; play
;;;;;;;;;;;;;;;;;;

(def histo-1 [0 1])
(def histo-2 [5 3])

; warm-up
(defn vec-prod [histo-1 histo-2]
  (reduce +
    (map #(* %1 %2) histo-1 histo-2)))

(defn scal-prod [histo-1 histo-2]
  (/ (vec-prod histo-1 histo-2) (Math/sqrt (* (vec-prod histo-1 histo-1) (vec-prod histo-2 histo-2)))))

(vec-prod  histo-1 histo-2)
(scal-prod  histo-1 histo-2)



; emd for histograms
(defn emd-simple [histo-1 histo-2]
  (assert (= (count histo-1) (count histo-2)))
     
  )

(emd-simple histo-1 histo-2)


(def histo-1 [9 0 1])
(def histo-2 [1 5 3])

;(map #(- %1 %2) histo-1 histo-2)






