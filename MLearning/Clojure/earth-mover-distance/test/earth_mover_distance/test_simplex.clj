(ns earth-mover-distance.test-simplex
  (:require [clojure.test :refer :all]
            [clojure.core.matrix :as m]
            [clojure.math.numeric-tower :as math]
            [earth-mover-distance.emd :as emd]
            [earth-mover-distance.simplex :as simplex]))

; examples from http://college.cengage.com/mathematics/larson/elementary_linear/4e/shared/downloads/c09s3.pdf
(def tableau1  (m/matrix
               [[-1 1 1 0 0 11]
                [1 1 0 1 0 27]
                [2 5 0 0 1 90]
                [-4 -6 0 0 0 0]]))

(def tableau2 (m/matrix 
               [[2 1 0 1 0 0 10]
                [1 2 -2 0 1 0 20]
                [0 1 2 0 0 1 5]
                [-2 1 -2 0 0 0 0]]))

(def tableau3 (m/matrix 
               [[4 1 1 1 0 0 30]
                [2 3 1 0 1 0 60]
                [1 2 3 0 0 1 40]
                [-3 -2 -1 0 0 0 0]]))

(def tableau4 (m/matrix
               [[1 2 1.5 1 0 0 12000]
                [0.666666666666 0.666666666666 1 0 1 0 4600]
                [0.5 0.333333333333 0.5 0 0 1 2400]
                [-11 -16 -15 0 0 0 0]]))

(def tableau4 (m/matrix
               [[1 2 1.5 1 0 0 12000]
                [2/3 2/3 1 0 1 0 4600]
                [1/2 1/3 1/2 0 0 1 2400]
                [-11 -16 -15 0 0 0 0]]))

(def tableau5 (m/matrix
               [[20 6 3 1 0 0 0 182]
                [0 1 0 0 1 0 0 10]
                [-1 -1 1 0 0 1 0 0]
                [-9 1 1 0 0 0 1 0]
                [-100000 -40000 -18000 0 0 0 0 0]]))



(deftest test1-simplex-method
  ; the element on the lower right is the optimised through simplex decomposition 
  (let [optimised-val (m/mget (simplex/simplex-method tableau1) 3 5)]
      (is (> emd/precis (math/abs (- 132. optimised-val))))))


(deftest test2-simplex-method
  ; the element on the lower right is the optimised through simplex decomposition 
  (let [optimised-val (m/mget (simplex/simplex-method tableau2) 3 6)]
      (is (> emd/precis (math/abs (- 15. optimised-val))))))

(deftest test3-simplex-method
  ; the element on the lower right is the optimised through simplex decomposition 
  (let [optimised-val (m/mget (simplex/simplex-method tableau3) 3 6)]
      (is (> emd/precis (math/abs (- 45. optimised-val))))))

(deftest test4-simplex-method
  ; the element on the lower right is the optimised through simplex decomposition 
  (let [optimised-val (m/mget (simplex/simplex-method tableau4) 3 6)]
      (is (> emd/precis (math/abs (- 100200. optimised-val))))))

(deftest test4-simplex-method
  ; the element on the lower right is the optimised through simplex decomposition 
  (let [optimised-val (m/mget (simplex/simplex-method tableau5) 4 7)]
      (is (> emd/precis (math/abs (- 1052000. optimised-val))))))



