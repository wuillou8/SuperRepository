(ns earth-mover-distance.core-test
  (:require [clojure.test :refer :all]
            [earth-mover-distance.emd :refer :all]
            [clojure.core.matrix :refer :all]))

; refering to the article:
; E.j. Russel, Extension of Dantzig's Algorithm to finding an initial
; near-optimal basis for the transportation problem , operations research 1969 



; example from Russel paper, Houthaker matrix

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

; example 1

(defrecord feature [x y z])
(def f-1 [(->feature 100 40 22) (->feature 211 20 2) (->feature 32 190 150) (->feature 2 100 100)])
(def f-2 [(->feature 0 0 0) (->feature 50 100 80)  (->feature 255 255 255)])

;weights

(def w-1  [0.4 0.3 0.2 0.1]) ; supply
(def w-2  [0.5 0.3 0.2]) ; demand

(defn distance-fct [f1, f2]
  (sqrt
    (+ (pow (- (:x f1) (:x f2)) 2)
       (pow (- (:y f1) (:y f2)) 2)
       (pow (- (:z f1) (:z f2)) 2))))
       
(def c (array
  (for [el f-1] 
    (mapv #(distance-fct el %)  f-2)))) ;)  

(def transpo1 (->transportation-pbm c w-1 w-2))
;(println "cost: " (run-russel transpo1))



(deftest test-russel-article 
 (is (= 1104 (run-russel traspo))))

(deftest test-example1
  (is (= 163.07130724471503 (run-russel transpo1))))












;(loop [transport-pbm traspo cost 0]
;  (let [m (:m-costs transport-pbm)
;        a (:v-supply transport-pbm)
;        b (:v-demand transport-pbm)] 
;    (if (= 0 (reduce + (concat b a))) 
;      cost
;      (let [t (algo-russel-iteration transport-pbm)]
;        (recur (:transport t) (+ cost (:cost t)))
;    ))))


