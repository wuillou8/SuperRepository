(ns earth-mover-distance.emd
  (:require [clojure.core.matrix :as m]
            [earth-mover-distance.simplex :as simplex]
            [earth-mover-distance.russel :as russel]))

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

(defn- preprocess [sgn1 sgn2 distance-fct]
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


(defn emd-russel [signature-1 signature-2 distance-fct]
  (-> (preprocess signature-1 signature-2 distance-fct)
      russel/run-russel
      :russel-cost))

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

(defn emd [signature-1 signature-2 distance-fct]
  (let [emd-russel (-> (preprocess signature-1 signature-2 distance-fct)
                        russel/run-russel)
       ] 
        ;emd-russel (emd-russel signature-1 signature-2 distance-fct)
       ; emd-russel-table (identity emd-russel)]

    (if (true)
          (:russel-cost emd-russel) ;(:russel-cost emd-russel)
        )
    ))



(defn emd-russel-dbg [signature-1 signature-2 distance-fct]
  (-> (preprocess signature-1 signature-2 distance-fct)
      russel/run-russel
      ))

