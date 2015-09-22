(ns metrics.calibration
  (require [metrics.utils :refer :all]
           [metrics.mc-methods :refer :all]
           [metrics.metrics :refer :all]
           [metrics.useritem-behaviour :refer :all]
           [metrics.chat-ganalytics :refer :all]
           ;[metrics.google-analytics :refer :all]
           [incanter.core :refer :all]
           [incanter.stats :refer :all]
           [incanter.charts :refer :all]
           [incanter.pdf :refer :all])
  )


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

(defn- buy-not-buy?-predic 
  ; alpha: extension param (for logit)
  ; epsilon: white noise distributed N(0,sigma)
  ; threshold: fit at price = 0.0 
  [vall boundary_fct alpha sigma threshold]
  (let [
        x (first vall)
        y (second vall)
        boundary (boundary_fct x threshold) ; fit function
        p-choice (user-model->proba y boundary alpha sigma) ;#(buy-boundary % 0.4))
        tag-buy  p-choice ;(>= p-choice 0.5) 
        ;(mc-choice p-choice) ;(> 0.5 p-choice) ;(mc-choice p-choice)
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
(doto (scatter-plot :y :p-choice
                    :title "Calibration: P_buy VS Util(abstract)"
                    :x-label "Util(abstract)"
                    :y-label "P_buy"
                    :group-by :x
                    :data (to-dataset (map #(buy-not-buy? % buy-boundary2 10. 1. 0.4) test-lines))
                    )
  view)

; calibration 2: 2-D view bought not bought.
(def test-grid (do-grid))
(def test-data-grid (to-dataset (map #(buy-not-buy? % buy-boundary0 10. 2. 0.5) test-grid)))
(def test-data-grid (to-dataset (map #(buy-not-buy? % buy-boundary1 10. 1. 0.4) test-grid)))
(def test-data-grid (to-dataset (map #(buy-not-buy? % buy-boundary2 10. 5. 2.) test-grid)))

; view grid
(save-pdf
(doto 
  (scatter-plot :x :y
                    :title "logit distribution1: Util vs Price"
                    :x-label "Price"
                    :y-label "Utility"
                    :group-by :tag-buy 
                    :data (to-dataset (map #(buy-not-buy? % buy-boundary1 10. 1. 0.4) test-grid)))
  ;(add-function #(buy-boundary0 % 0.4) 0. 1.)
  (add-function #(buy-boundary1 % 0.4) 0. 1. )
  ;(add-function #(buy-boundary2 % 0.4) 0. 1.)
  clear-background
  )
"./resources/utilvsprice_1.pdf")

(save-pdf
(doto 
  (scatter-plot :x :y
                    :title "logit distribution2: Util vs Price"
                    :x-label "Price"
                    :y-label "Utility"
                    :group-by :tag-buy 
                    :data (to-dataset (map #(buy-not-buy? % buy-boundary1 5. 2. 0.8) test-grid)))
  ;(add-function #(buy-boundary0 % 0.4) 0. 1.)
  (add-function #(buy-boundary1 % 0.4) 0. 1.)
  ;(add-function #(buy-boundary2 % 0.4) 0. 1.)
  clear-background
  view)
"./resources/utilvsprice_2.pdf")

(save-pdf
(doto 
  (scatter-plot :x :y
                    :title "logit distribution3: dimN vs dim1"
                    :x-label "dim1"
                    :y-label "dimN"
                    :group-by :tag-buy 
                    :data (to-dataset (map #(buy-not-buy? % buy-boundary2 10. 1. 0.4) test-grid)))
  ;(add-function #(buy-boundary0 % 0.4) 0. 1.)
  (add-function #(buy-boundary2 % 0.4) 0. 1. )
  ;(add-function #(buy-boundary2 % 0.4) 0. 1.)
  clear-background
  view)
"./resources/utilvspricesin_1.pdf")

(save-pdf
(doto 
  (scatter-plot :x :y
                    :title "logit distribution4: dimN vs dim1"
                    :x-label "dim1"
                    :y-label "dimN"
                    :group-by :tag-buy 
                    :data (to-dataset (map #(buy-not-buy? % buy-boundary2 5. 2. 0.8) test-grid)))
  ;(add-function #(buy-boundary0 % 0.4) 0. 1.)
  (add-function #(buy-boundary2 % 0.4) 0. 1.)
  ;(add-function #(buy-boundary2 % 0.4) 0. 1.)
  clear-background
  view)
"./resources/utilvspricesin_2.pdf")
;;;;;;;;;;;;
; logit calibration

(doto (function-plot #(logit-noisy % 0) -5 5)
    (add-function #(logit-noisy % 1)  -5 5)
    (add-function #(logit-noisy % 3)  -5 5)
    view)


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
(defn do-grid2 [incr]
 (for [i (range 0. 1. incr) j (range 0. 1. incr)]
  (vector i j)))


(def synth-grid
  (map :coord  
    (filter #(:choice %) 
      (map (fn [tmp] {:choice (mc-choice 0.001) :coord tmp}) (do-grid2 0.001)))))

(def synth-data (map #(buy-not-buy? % buy-boundary2 5. 2. 0.8) synth-grid))

;{:x 0.0, :y 0.1220000000000001, :p-choice 0.029373299647095088, :tag-buy false}
;(first synth-data)

(defn cost-fn [score data]
  (let [tag-buy (if (:tag-buy data) 0.75 0.25)
        tmp (- tag-buy (:p-choice data))
        score-tag (pow tmp 2.0)];(if (> tmp 0) 
                  ;  tmp
                  ;  (* -1. tmp))]
    (+ score score-tag)))

(defn cost-fn [score data]
  (let [tag-buy (:tag-buy synth-data)
        tmp (mc-choice (:p-choice data))
        score-tag (if (= tag-buy tmp) 1 0)]
    (+ score score-tag)))

(defn fit-cost-fn [data] 
  (reduce cost-fn
  0
  data))


(defn cost-fn [score data synth-data]
  (let [tag-buy (:tag-buy synth-data)
        tmp (mc-choice (:p-choice data))
        score-tag (if (= tag-buy tmp) 1 0)]
    (+ score score-tag)))

(defn fit-cost-fn [data] 
  (reduce cost-fn
  0
  data 
  synth-data))


(first
 (mapcat #( {:1 %1} ) synth-data synth-data)
)

(def my-score
  (for [i (range 2. 10. 0.25) j (range 0. 4. 0.2)]
    ;(println i j)
    (let [data (map #(buy-not-buy? % buy-boundary2 i j 0.8) synth-grid)
        score (fit-cost-fn data)]  
        {:i i :j j :score score})))

(take 5 (sort-by :score < my-score))

(int (Math/ceil (/ 3 2)))
(int (Math/floor (/ 3 2)))
(int 1.6)
(fit-score-fn synth-data)

(def bla
(doto 
  (scatter-plot :x :y
                    :title "logit distribution4: dimN vs dim1"
                    :x-label "dim1"
                    :y-label "dimN"
                    :group-by :tag-buy 
                    :data (to-dataset (map #(buy-not-buy? % buy-boundary2 5. 2. 0.8) synth-grid)))
  ;(add-function #(buy-boundary0 % 0.4) 0. 1.)
  ;(add-function #(buy-boundary2 % 0.4) 0. 1.)
  ;(add-function #(buy-boundary2 % 0.4) 0. 1.)
  clear-background
  ))

(def plot (.getPlot bla))
(.setAxisLineVisible (.getDomainAxis plot) true)
(.setAxisLineVisible (.getRangeAxis plot) true)
(save-pdf bla "./resources/bla.pdf")




;(fit-cost-fn
;  (map #(buy-not-buy? % buy-boundary2 5. 2. 0.8) synth-grid)
;)
;7752


