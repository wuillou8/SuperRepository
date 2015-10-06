(ns earth-mover-distance.test-simplex
  (:require [clojure.test :refer :all]
            [clojure.core.matrix :as m]
            [clojure.math.numeric-tower :as math]
            [earth-mover-distance.emd :as emd]
            [earth-mover-distance.simplex :as simplex]))

(def tableau1  (m/matrix
               [[-1 1 1 0 0 11]
               [1 1 0 1 0 27]
               [2 5 0 0 1 90]
               [-4 -6 0 0 0 0]]))

(deftest test-simplex-method-for-emd
  ; the element on the lower right is the optimised through simplex decomposition 
  (let [optimised-val (m/mget (simplex/simplex-method tableau1) 3 5)]
      (is (> emd/precis (Math/abs (- 132. optimised-val))))))


