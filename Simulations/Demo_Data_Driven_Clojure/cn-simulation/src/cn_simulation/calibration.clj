(ns cn-simulation.calibration
  (require [cn-simulation.utils :refer :all]
           [cn-simulation.mc-methods :refer :all]
           [cn-simulation.metrics :refer :all]
           [cn-simulation.useritem-behaviour :refer :all]
           ;[metrics.chat-ganalytics :refer :all]
           ;[metrics.google-analytics :refer :all]
           [incanter.core :refer :all]
           [incanter.stats :refer :all]
           [incanter.charts :refer :all]))


(defn buy-boundary0
  [x threshold]
  ; criterion for buying/ not buying, linear function:
  ; f(x, thres) = thres + (1-thres) * x
  ($= threshold + (1. - threshold) * x ))  
  ;(1. - threshold) * (1 - jexp(- x)) + threshold))

(defn buy-boundary1
  [x threshold]
  ; criterion for buying/ not buying:
  ; f(x, thres) = thres + (1-thres) * (1 - exp(-x))
  ($= (1. - threshold) * (1 - jexp(- x)) + threshold))

(defn buy-boundary2
  [x threshold]
  ; criterion for buying/ not buying:
  ; just imagine it would be a sinus function
  ($= ( 1. +  (sin (* 10 x)) ) / 2.  )) 

(defn user-model->proba [y f_val alpha sigma]
  ; p_choice (x, y, fct, \sigma) = logit ( alpha (y  - fct) + \sigma \epsilon )
  ; alpha is deformation parameter while sigma is the white noise sigma
  ; with \epsilon white noise
  (let [
        epsilon (noise 0.  sigma) 
        expo ($= alpha * (y - f_val) + epsilon) 
        ]
  (logit expo)))

(defn- buy-not-buy? 
  ; alpha: extension param (for logit)
  ; epsilon: white noise distributed N(0,sigma)
  ; threshold: fit at price = 0.0 
  [vall boundary_fct alpha sigma threshold]
  (let [
        x (first vall)
        y (second vall)
        boundary (boundary_fct x threshold) ; fit function
        p-choice (user-model->proba y boundary alpha sigma) ;#(buy-boundary % 0.4))
        tag-buy (mc-choice p-choice) ;(> 0.5 p-choice) ;(mc-choice p-choice)
        ] 
    {:x x, :y y, :p-choice p-choice, :tag-buy tag-buy}))

; calibration 1: distance to utility boundary
(def test-lines (concat (do-line 0.0) (do-line 0.5) (do-line 1.0)) )

(def test-data-lines (to-dataset (map #(buy-not-buy? % buy-boundary0 10. 1. 0.4) test-lines)))
(def test-data-lines (to-dataset (map #(buy-not-buy? % buy-boundary1 10. 1. 0.4) test-lines)))
(def test-data-grid (to-dataset (map #(buy-not-buy? % buy-boundary2 10. 1. 0.4) test-lines)))

(doto (scatter-plot :y :p-choice
                    :title "Calibration: P_buy VS Util(abstract)"
                    :x-label "Util(abstract)"
                    :y-label "P_buy"
                    :group-by :x
                    :data test-data-lines)
  view)

; calibration 2: 2-D view bought not bought.
(def test-grid (do-grid))
(def test-data-grid (to-dataset (map #(buy-not-buy? % buy-boundary0 10. 2. 0.5) test-grid)))
(def test-data-grid (to-dataset (map #(buy-not-buy? % buy-boundary1 10. 1. 0.4) test-grid)))
(def test-data-grid (to-dataset (map #(buy-not-buy? % buy-boundary2 10. 5. 2.) test-grid)))

; view grid
(doto 
  (scatter-plot :x :y
                    :title "Calibration: Util(abstract) VS Price"
                    :x-label "Price"
                    :y-label "Util(abstract)"
                    :group-by :tag-buy 
                    :data test-data-grid)
  (add-function #(buy-boundary0 % 0.4) 0. 1.)
  (add-function #(buy-boundary1 % 0.4) 0. 1.)
  (add-function #(buy-boundary2 % 0.4) 0. 1.)
  view)

;;;;;;;;;;;;
; logit calibration

(doto (function-plot #(logit-noisy % 0) -5 5)
    (add-function #(logit-noisy % 1)  -5 5)
    (add-function #(logit-noisy % 3)  -5 5)
    view)

