(ns metrics.utils)

(defn in? 
    "true if seq contains elm"
    [seq elm]  
    (some #(= elm %) seq))

(defn params->query-string [m]
  (clojure.string/join "&" 
    (for [[k v] m] 
      (str (name k) "="  (java.net.URLEncoder/encode v)))))

(defn do-grid []
 (for [i (range 0. 1. 0.01) j (range 0. 1. 0.01)]
  (vector i j)))

(defn do-line [x]
  (for [i (range 0. 1. 0.001)]
      (vector x i)))
