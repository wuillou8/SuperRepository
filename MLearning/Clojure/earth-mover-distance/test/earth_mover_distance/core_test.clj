(ns earth-mover-distance.core-test
  (:require [clojure.test :refer :all]
            [earth-mover-distance.emd :refer :all]
            [clojure.core.matrix :refer :all]))

; refering to the article:
; E.j. Russel, Extension of Dantzig's Algorithm to finding an initial
; near-optimal basis for the transportation problem , operations research 1969 

(defrecord transportation-pbm [m-costs v-supply v-demand])


;;;;;;;;;;;;;;;;;;;;;;;;;;;
(def houthakker-matrix 
  (array 
    [[73 40 9 79 20]
     [62 93 96 8 13]
     [96 65 80 50 65]
     [57 58 29 12 87]
     [56 23 87 18 12]]))
(def a [8 7 9 3 5])
(def b [6 8 10 4 4]);


(def traspo (->transportation-pbm houthakker-matrix a b))

(deftest test-phantomjs-simulation
 (is (= 1104 (run-russel traspo)))
 )


;(loop [transport-pbm traspo cost 0]
;  (let [m (:m-costs transport-pbm)
;        a (:v-supply transport-pbm)
;        b (:v-demand transport-pbm)] 
;    (if (= 0 (reduce + (concat b a))) 
;      cost
;      (let [t (algo-russel-iteration transport-pbm)]
;        (recur (:transport t) (+ cost (:cost t)))
;    ))))


