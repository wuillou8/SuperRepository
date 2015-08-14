(ns metrics.demo.demo
  (require [metrics.utils :refer :all]
           [metrics.mc-methods :refer :all]
           [metrics.metrics :refer :all]
           [metrics.useritem-behaviour :refer :all]
           [metrics.chat-ganalytics :refer :all]
           ;[metrics.google-analytics :refer :all]
           [incanter.core :refer :all]
           [incanter.stats :refer :all]
           [incanter.charts :refer :all]
           [clj-webdriver.taxi :as t]))


; model glob variables
(def Nusers 100)
(def Nitems 1000)
(def Ntot-features 50)
(def Nuser-features 5)
(def Nitem-features 3)

; generate players
(def users (map #(create-rand-user % Nuser-features Ntot-features) (range Nusers)))
(def items (map #(create-rand-item % Nitem-features Ntot-features) (range Nitems)))
;(ns metrics.demo.basic-demo)


(require 'clj-webdriver.taxi)

(set-driver! {:browser :firefox} "https://morning-beach-6895.herokuapp.com")

(click "a[href*='menswear']")

(close)




(str "a[href*=" bla "]")

(def sitemap {:trunc ['menswear' 'womenswear'] :first ['top' 'dress' 'shirt' 'trouser']})

(def size-trunc (count (:trunc sitemap)))
(def size-first (count (:first sitemap)))


(set-driver! {:browser :firefox} "https://morning-beach-6895.herokuapp.com")

(let [my-count1 (rand-int size-trunc)]
  (case my-count1
    0 (click "a[href*='menswear']")
    1 (click "a[href*='womenswear']")))

(let [my-count2 (rand-int size-first)]
  (case my-count2
    0 (click "a[href*='top']")
    1 (click "a[href*='dress']")
    2 (click "a[href*='shirt']")
    3 (click "a[href*='trouser']")
  ))

(close)





(if (= 1 (rand-int size-trunc))
  (click "a[href*='menswear']")
  (click "a[href*='womenswear']")
  )

