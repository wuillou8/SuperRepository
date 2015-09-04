(ns cn-simulation.mc-methods
  (require [incanter.core :refer :all]
           [incanter.stats :refer :all]
           [incanter.charts :refer :all]))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;             MC Tools module                                   ;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(defn unit-circle-coords
 ; generate coordinates within the unit circle 
  []
  (let [
        x1 (- (* 2.0 (rand 1.)) 1.)
        x2 (- (* 2.0 (rand 1.)) 1.)
        w  (+ (* x1  x1) (* x2  x2))
        ]
    (if (or (>= w 1.) (= w 0.))
      (recur)
      [w x1])
  ))

(defn box-mueller
  ; boxmueller rand gaussian generator
  ; m s for mu and sigma, distribution is N(mu, sigma). 
  [m s]
  (let [ucr (unit-circle-coords) 
        w (first ucr)
        x1 (second ucr)  
        v1 (Math/sqrt (/ (* -2. (Math/log w)) w))
        iid (+ m (* (* x1 v1) s))]
  iid))

(defn white-noise
  ; white Gaussian noise wrapper
  ; mu, sigma -> \epsilon \in N(0, sigma)
  [mu sigma]
  ; current generator model is box-mueller
  (box-mueller mu sigma)) 

(defn jexp [x] 
  ; wrapper for jexpn function.
  (Math/exp x))

(defn logit [x] 
  ; standard logit function.
  (/ 1. (+ 1. (jexp (- x)) ) ))

(defn logit-noisy [x alpha]
  ; white gaussian noise on the top of the logit function:
  ; x -> x + \epsilon, \epsilon \in N(0., \alpha)
  (/ 1. (+ 1. (jexp (- (+ x (white-noise 0. alpha)))) ) ))

(defn poisson-law
  ; Poisson law simulates random events taking place at a known average rate 
  ; reminds for k = 0,1,2,... a discrete time, Prob(Event = k) = \lambda^k e^(-lambda ) / k!
  [lambda]
  (let [
        a  (jexp (- lambda))
        r (atom (rand))
        n (atom 0)
        ]
  (while (> @r a) (do (swap! n inc) (swap! r  #(* % (rand)))) )
  @n))

(defn poisson-distr->events
  ; synchronises poisson distr. events of function fct., lambda is the poisson rate.
  [lambda fct]
  (time (Thread/sleep (poisson-law lambda)))
  fct)

(defn mc-choice [x]
  (< (rand) x))

(defn poisson-law [average]
  ; recall that for a Poisson process, 
  ; cdf is F(x) = 1. - \e^{-\lambda x}
  ; So the y axis of the cdf is between 0. and 1.
  ; A standard technique to generate random sampling is to draw random 
  ; events on the y axis and infer the positions on the x axix.
  ; this way, x = - \frac{\ln (1 - rand)}{lambda} 
  (let [r (rand)
        arg ($= 1. - r)
        ; recall lambda =  1 / average
        lambda ($= 1. / average)] 
    ($= -1. / lambda * (log arg))))


