(ns earth-mover-distance.basic-test
  (:require [clojure.test :refer :all]
            [clojure.math.numeric-tower :as math]
            [clojure.core.matrix :as m]
            [earth-mover-distance.emd :as emd]
            [earth-mover-distance.simplex :as simplex]))

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


(emd/emd-russel signature1 signature2 distance-fct)
(emd/emd-russel signature2 signature1 distance-fct)
(emd/emd-simplex-dbg signature1 signature2 distance-fct)

;[[109.92724866929036 97.28309205612247 352.90083592986855] 
; [211.95518394226644 195.97193676646665 348.09481466979656] 
; [244.18026128252055 115.4296322440646 254.9097879642914] 
; [141.43549766589715 52.0 334.75214711783406]]

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
;4  from  1  to:  4
;3  from  1  to:  3
;8  from  0  to:  2
;5  from  4  to:  1
;2  from  3  to:  2
;1  from  3  to:  3
;3  from  2  to:  1
;6  from  2  to:  0


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; examples 3X3 EMD signatures,                     ;
; Russel & Simplex compared with c code;           ;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(defrecord feature [x y z])

; distance or cost function
(defn distance-fct [f1 f2]
  (Math/sqrt
    (+ (Math/pow (- (:x f1) (:x f2)) 2)
       (Math/pow (- (:y f1) (:y f2)) 2)
       (Math/pow (- (:z f1) (:z f2)) 2))))

; features
(def f1 [(->feature 211 20 2) (->feature 32 190 150) (->feature 2 100 100)])
(def f2 [(->feature 0 0 0) (->feature 50 100 80)  (->feature 255 255 255)])
; weights vector
(def w1  [0.4 0.3 0.3])
(def w2  [0.5 0.3 0.2])
; signatures
(def sgna1 {:features f-1  :weights w-1})
(def sgna2 {:features f-2  :weights w-2})

(deftest test-russel-simplex-C
 (let [russel (emd/emd-russel signature1 signature2 distance-fct)
       simplex (emd/emd-simplex sgna1 sgna2 distance-fct)] 
  (is (> emd/precis (math/abs (- 175.782059 russel)))) 
  (is (> emd/precis (math/abs (- 171.850555 (:minimum simplex)))))))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; examples  from the c code and its python wrapper ;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
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


(emd/emd-russel signature1 signature2 distance-fct)
(emd/emd-russel signature2 signature1 distance-fct)
(emd/emd-simplex-dbg signature1 signature2 distance-fct)





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
 (is (> emd/precis (- 2.2 (emd/emd-russel sign-1 sign-2 distance-example
