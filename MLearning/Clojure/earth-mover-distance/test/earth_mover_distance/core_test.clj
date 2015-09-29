(ns earth-mover-distance.core-test
  (:require [clojure.test :refer :all]
            [earth-mover-distance.emd :as emd]
            [clojure.core.matrix :as m]))





; refering to the article:
; E.j. Russel, Extension of Dantzig's Algorithm to finding an initial
; near-optimal basis for the transportation problem , operations research 1969 

(defrecord transportation-pbm [m-costs v-supply v-demand])

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; example from Russel paper, Houthaker matrix ;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
(def houthakker-matrix 
  (m/array 
    [[73 40 9 79 20]
     [62 93 96 8 13]
     [96 65 80 50 65]
     [57 58 29 12 87]
     [56 23 87 18 12]]))
(def a [8 7 9 3 5])
(def b [6 8 10 4 4])

(def transp-houtakker (->transportation-pbm houthakker-matrix a b))

(deftest test-houthakker-matrix 
 (is (= 34.5 (emd/run-russel transp-houtakker))))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; examples  from the c code and its python wrapper ;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
(defrecord feature [x y z])

; distance or cost function
(defn distance-fct [f1 f2]
  (Math/sqrt
    (+ (Math/pow (- (:x f1) (:x f2)) 2)
       (Math/pow (- (:y f1) (:y f2)) 2)
       (Math/pow (- (:z f1) (:z f2)) 2))))

; features
(def f-1 [(->feature 100 40 22) (->feature 211 20 2) (->feature 32 190 150) (->feature 2 100 100)])
(def f-2 [(->feature 0 0 0) (->feature 50 100 80)  (->feature 255 255 255)])

; weights vector
(def w-1  [0.4 0.3 0.2 0.1])
(def w-1>  [0.4 0.3 0.2 0.3])
(def w-2  [0.5 0.3 0.2])
(def w-2>  [0.5 0.3 0.4])

; signatures
(def signature1 {:features f-1  :weights w-1})
(def signature1> {:features f-1  :weights w-1>})
(def signature2 {:features f-2  :weights w-2})
(def signature2> {:features f-2  :weights w-2>})


(deftest tests-emd-russel
  (is (> emd/precis (- 163.0713 (emd/emd-russel signature1 signature2 distance-fct))))
  (is (> emd/precis (- 125.32115 (emd/emd-russel signature1> signature2 distance-fct))))
  (is (> emd/precis (- 159.13945 (emd/emd-russel signature1 signature2> distance-fct))))
  (is (> emd/precis (- 167.80612 (emd/emd-russel signature1> signature2> distance-fct)))))





