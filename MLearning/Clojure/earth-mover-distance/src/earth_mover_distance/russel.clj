(ns earth-mover-distance.russel
  (:require [clojure.core.matrix :as m]))




(defn- find-dantzig-max [m w y i_idx j_idx]
 ; find the best variable x_{ij}^* = max_{ij} [w_i + y_i -c_{ij} > 0]
 ; which is equivalent to finding min_{ij} [ c_{ij} - w_i - y_i < 0]
 (reduce 
   (fn [min-val el]
    (if (< (:dantzig el) (:dantzig min-val))
      el
      min-val))
    {:dantzig 0 :i -1 :j -1}
    (for [i i_idx j j_idx]
     {:dantzig (- (m/mget m i j) (m/mget w i) (m/mget y j)) :i i :j j})))

(defn- algo-russel-iteration [transport]  
  (let [m (:m-costs transport) ;houthakker-matrix
        a (:v-supply transport) ; i insdex  
        b (:v-demand transport) ; j index
        ; authorised indices : only non-zero weights enter the computation 
        i_idx (filter #(< 0.00001 (nth a %)) (range (m/ecount a)))
        j_idx (filter #(< 0.00001 (nth b %)) (range (m/ecount b)))
        ; step 1 : build w and y 
        w (mapv #(apply max %) (m/rows m))
        y (mapv #(apply max %) (m/columns m))
        ; step 2 : find best combinaison ij for transport
        pos (find-dantzig-max m w y i_idx j_idx)
        ; step 4 : activity level
        ships (min (m/mget a (:i pos)) (m/mget b (:j pos))) 
        ; step 3 : remove activity level to the supply/deamdn level
        a (assoc a (:i pos) (- (nth a (:i pos)) ships)) 
        b (assoc b (:j pos) (- (nth b (:j pos)) ships))
        ; compute transaction costs: nb-ship*c_ij 
        cost (* ships (m/mget m (:i pos) (:j pos)))]
 (println ships " from " (:i pos) " to: " (:j pos))
 {:transport (assoc transport :v-supply a :v-demand b) :cost cost :ships ships :from-to-v {:i (:i pos) :j (:j pos) :ships ships}}))

(defn run-russel [transport]
  (println ">>run *russ*el algorit*hm: ")
  ; run the algo and returns
  (loop [trans transport cost 0 ships 0 from-to-v []]

     ; the algorithm terminates when the supply has been attributed to the demand.
      (if (> 0.00001 (reduce + (:v-supply trans)))
        {:russel-cost (float (/ cost ships)) :from-to-v from-to-v :trans-debug trans}
        (let [t (algo-russel-iteration trans)]
          (recur (:transport t) (+ cost (:cost t)) (+ ships (:ships t)) (conj from-to-v (:from-to-v t)))))))






