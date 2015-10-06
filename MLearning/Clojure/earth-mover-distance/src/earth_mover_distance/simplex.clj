(ns earth-mover-distance.simplex
  (:require [clojure.core.matrix :as m]
            [clojure.math.numeric-tower :as math]))


(defn check-optimality [s-tableau]
  (if (< 0 (count (filter #(< % 0) (last s-tableau))))
    false true))

(defn find-min-abs-key 
  ([array]
    ; for now...
    (first (apply min-key second (map-indexed vector (m/to-double-array array)))))
  ([array fn] 
    (first (apply min-key second (map-indexed vector (map #(fn %) (m/to-double-array array)))))))

(defn find-pivot [table]
  (let [enter-idx (find-min-abs-key (last table))
        x (butlast (m/slice table 1 enter-idx))
        y (butlast (last (m/columns table)))
        depart-idx (find-min-abs-key (m/div y x) 
                                     (fn [tmp] (if (< tmp 0) Double/MAX_VALUE tmp))) ]
    [depart-idx enter-idx]))

(defn jordan-gauss-decompose-step [table pivot-i pivot-j]
    (let [nb-lines (first (m/shape table))
        pivot (float (m/mget table pivot-i pivot-j))
        pivot-row (m/slice table 0 pivot-i)]
        (loop [i 0 table table]
            (if (< i nb-lines)
              (let [t (if (not= i pivot-i)
                (let [row (m/get-row table i)
                      fact (float (/ (m/mget row pivot-j) pivot))
                      row (m/sub row (m/mul pivot-row  fact))]
                  (m/set-row table i row))
                  ; else pivot row
                  (m/multiply-row table i (/ 1. pivot)))]
          (recur (inc i) t))
      table))))

(defn simplex-method [table]
    (loop [t table] 
        (if (check-optimality t)
            t
            (recur (apply jordan-gauss-decompose-step t (find-pivot t))))))



