(ns earth-mover-distance.core-test
  (:require [clojure.test :refer :all]
            [earth-mover-distance.emd :as emd]
            [clojure.core.matrix :as m]))

(defrecord emd-pbm [m-costs v-supply v-demand])

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

(def transp-houtakker (->emd-pbm houthakker-matrix a b))

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
  (is (> emd/precis (Math/abs (- 0.0 (emd/emd-russel signature1 signature1 distance-fct)))))
  (is (> emd/precis (Math/abs (- 163.0713 (emd/emd-russel signature1 signature2 distance-fct)))))
  (is (> emd/precis (Math/abs (- 125.32115 (emd/emd-russel signature1> signature2 distance-fct)))))
  (is (> emd/precis (Math/abs (- 159.13945 (emd/emd-russel signature1 signature2> distance-fct)))))
  (is (> emd/precis (Math/abs (- 167.80612 (emd/emd-russel signature1> signature2> distance-fct))))))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; comparison against c code                      ;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(def c-example2
  ; cost matrix from example2
  (m/matrix 
    [[3 5 2]
     [0 2 5]
     [1 1 3]
     [8 4 3]
     [7 6 5]]))

(defn distance-example2 [sgn1 sgn2]
  (m/mget c-example2 sgn1 sgn2))

(def sign-1 {:weights [0.4 0.2 0.2 0.1 0.1] :features [0 1 2 3 4]})
(def sign-2 {:weights [0.6 0.2 0.1] :features [0 1 2]})

(deftest tests-emd-vs-C
  ; testing against the c code
  (is (> emd/precis (Math/abs (- 1.890 (emd/emd-russel sign-1 sign-2 distance-example2))))))


(defn test-within-precision [value expression]
  (> emd/precis (value expression)))


