(ns earth-mover-distance.emd
  (:require [clojure.core.matrix :as m]
            [earth-mover-distance.simplex :as simplex]))

; refering to the article:
; E.j. Russel, Extension of Dantzig's Algorithm to finding an initial
; near-optimal basis for the transportation problem , operations research 1969 

(def precis 0.00001)

(defrecord emd-pbm [m-costs v-supply v-demand])

; L2 for vectors
(defn distance-L2 [rgb1 rgb2]
  (Math/sqrt
    (reduce + 
      (map #(Math/pow (- %1 %2) 2) rgb1 rgb2))))

(defn preprocess [sgn1 sgn2 distance-fct]
  ; by convention and analogy to the transportation problem, supply/demand are first/second var. 
  (let [a (:weights sgn1)
        b (:weights sgn2)
        
        ; the supply has to be smaller than the demand
        ; this is a generic feature that is not useful for normalised weights (sum => 1)
        [a b sgn1 sgn2] (if (< (reduce + a) (reduce + b))
                            [a b sgn1 sgn2]
                            [b a sgn2 sgn1])
        
        supply (reduce + a) 
        demand (reduce + b)

        n-a (count a)
        n-b (count b)
        ; generate cost matrix
        c (m/array 
            (for [el (:features sgn1)]
              (mapv #(distance-fct el %) (:features sgn2))))]
    ; if supply \neq demand, create a compensating weight and enter
    ; zero cost entries in the matrix
    (cond
      (> precis (Math/abs (- supply demand))) (->emd-pbm c a b)
      
      (> supply demand) (->emd-pbm (m/set-column c n-b (m/new-vector n-a))
                              a (conj b (- supply demand)))   
      (< supply demand) (->emd-pbm  (m/set-row c n-a (m/new-vector n-b))
                              (conj a (- demand supply)) b))))

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
     {:dantzig (- (m/mget m i j) (m/mget w i) (m/mget y j)) :i i :j j})))

(defn algo-russel-iteration [transport]  
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
 {:transport (assoc transport :v-supply a :v-demand b) :cost cost :ships ships}))

(defn run-russel [transport]
  (println ">>run *russ*el algorit*hm: ")
  (loop [trans transport cost 0 ships 0]
    (let [a (:v-supply trans)
          b (:v-demand trans)]
     ;(println "   weights: " a b) 
      (if (> 0.00001 (reduce + (concat b a)))
        (float (/ cost ships))
        (let [t (algo-russel-iteration trans)]
          (recur (:transport t) (+ cost (:cost t)) (+ ships (:ships t))))))))

(defn emd-russel [signature-1 signature-2 distance-fct]
  (-> (preprocess signature-1 signature-2 distance-fct)
      run-russel))

(defn emd-simplex [signature-1 signature-2 distance-fct]
  (-> (preprocess signature-1 signature-2 distance-fct) 
       simplex/create-table
       simplex/table->dual
       simplex/simplex-method
       simplex/get-result-simplex
       ))
  
(defn emd-simplex-dbg [signature-1 signature-2 distance-fct]
  (-> (preprocess signature-1 signature-2 distance-fct) 
       simplex/create-table
       ;simplex/table->dual
       ;simplex/simplex-method
       ;simplex/get-result-simplex
       ))



