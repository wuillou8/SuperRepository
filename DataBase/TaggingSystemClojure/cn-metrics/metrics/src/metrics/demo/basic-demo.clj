(ns metrics.demo.demo
  (require [metrics.utils :refer :all]
           [metrics.mc-methods :refer :all]
           [metrics.metrics :refer :all]
           [metrics.useritem-behaviour :refer :all]
           [metrics.chat-ganalytics :refer :all]
           ;[metrics.google-analytics :refer :all]
           [incanter.core :refer :all]
           [incanter.stats :refer :all]
           [incanter.charts :refer :all]))




; model glob variables
(def Nusers 100)
(def Nitems 1000)
(def Ntot-features 50)
(def Nuser-features 5)
(def Nitem-features 3)


; generate players
(def users (map #(create-rand-user % Nuser-features Ntot-features) (range Nusers)))
(def items (map #(create-rand-item % Nitem-features Ntot-features) (range Nitems)))



(ns metrics.demo.basic-demo)
