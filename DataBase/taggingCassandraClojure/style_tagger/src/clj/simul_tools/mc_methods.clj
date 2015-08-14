(ns simul-tools.mc-methods)

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
    (let [
          ucr (unit-circle-coords) 
          w (first ucr)
          x1 (second ucr)  
          v1 (Math/sqrt (/ (* -2. (Math/log w)) w))
          iid (+ m (* (* x1 v1) s))
          ]
  iid))

(defn noise
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
  (/ 1. (+ 1. (jexp (- (+ x (noise 0. alpha)))) ) ))

(defn poisson-law
  ; Poisson law simulates random events taking place at a known average rate 
  ; reminds for k = 0,1,2,... a discrete time, Prob(Event = k) = \lambda^k e^(-k) / k!
  [lambda]
  (let [
        a  (jexp (- lambda))
        r (atom (rand))
        n (atom 0)
        ]
  (while (> @r a) (do (swap! n inc) (swap! r  #(* % (rand))) ))
  @n))

(defn poisson-distr->events
  ; synchronises poisson distr. events of function fct., lambda is the poisson rate.
  [lambda fct]
  (time (Thread/sleep (poisson-law lambda)))
  fct)

(defn mc-choice [x]
  (< (rand) x))

