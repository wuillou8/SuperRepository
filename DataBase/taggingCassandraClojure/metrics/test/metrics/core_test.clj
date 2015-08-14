(ns metrics.core-test
  (:require [clojure.test :refer :all]
            [metrics.core :refer :all]
            [metrics.mc-methods :refer :all]
            [incanter.core :refer :all]
            [incanter.stats :refer :all]
            [incanter.charts :refer :all]))

(deftest gaussian-distr
  ; gaussian distr. test 
  (let [
        check-list (take 100000 (repeatedly #(box-mueller 0. 1.)))
        m (mean check-list)
        s (sd check-list)
        ]
  ; check mean and var resp. 0 and 1.
  (and (< (abs m) 0.1) (< (abs (- 1. s)) 0.1) )  ))

(deftest poisson-distr
  ; poisson distr. test
  (let [
        lambda (rand-int 50)
        p-mean (->> (take 100000 (repeatedly #(poisson-law lambda))) (mean))
        p-sd (->> (take 100000 (repeatedly #(poisson-law lambda))) (sd))
        ]
   ; check mean is lambda 
  (< (abs (- lambda p-mean)) 0.03) ))


(deftest a-test
  (testing "FIXME, I fail."
    (is (= 0 1))))
