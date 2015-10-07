(ns earth-mover-distance.real-signs-tests
  (:require [clojure.test :refer :all]
            [clojure.data.json :as json]            
            [clojure.core.matrix :as m]
            [clojure.math.numeric-tower :as math]
            [earth-mover-distance.emd :as emd]
            [earth-mover-distance.simplex :as simplex]
            [earth-mover-distance.utilities :as utils]))



(def items-list ["Asymmetric_cotton_camisole",
            	 "Asymmetric_striped_cotton_T-shirt",
            	 "Boxy_organic_cotton_tank",
            	 "Cotton-terry_sweater",
            	 "Cotton_top"])

; generate distance small emd dist matrix 
(def item-sgns (map #(utils/get-signature "resources/" %) items-list))

(def dist-matrix 
        (for [el item-sgns]
          (mapv #(emd/emd-russel el % emd/distance-L2) item-sgns)))


; compare distance matrix agains c code: Russel algo.
(deftest test-dist-matrix-vs-C-code-1
  (is (= dist-matrix 
        (m/matrix 
         [[ 0.000000 39.675880 39.282978 84.164192 391.517548 ]
         [ 39.675880 0.000000 7.740604 87.643730 415.876648 ]
         [ 39.282978 7.740602 0.000000 83.595070 410.016418 ]
         [ 84.164192 87.643730 83.595070 0.000000 338.979553 ]
         [ 383.448853 415.297729 409.151520 338.981232 0.000000 ]]
         ))))

; compare distance matrix agains c code: Russel + simplex algos.
(deftest test-dist-matrix-vs-C-code-2
  (is (= dist-matrix 
        (m/matrix
          [[ 0.000000 39.361423 39.282978 83.868637 380.422821 ]
          [ 39.361427 0.000000 7.740602 87.633888 399.629364 ]
          [ 39.282978 7.740600 0.000000 83.593231 400.031403 ]
          [ 83.868637 87.633888 83.593231 0.000000 312.880951 ]
          [ 380.418243 399.548187 400.077026 312.883331 0.000000 ]]))))


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;   tests with simplex method   ;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;



;(def s_a
;  (utils/get-signature "resources/" "Asymmetric_cotton_camisole"))
;(def s_b
;  (utils/get-signature "resources/"  "Asymmetric_striped_cotton_T-shirt"))
;(def emd-pbm
;  (emd/preprocess s_a s_b emd/distance-L2))


;(create-table (:m-costs emd-pbm) (:v-supply emd-pbm) (:v-demand emd-pbm))

;(->
;(simplex/create-table (:m-costs emd-pbm) (:v-supply emd-pbm) (:v-demand emd-pbm))
;
;simplex/simplex-method
;)




