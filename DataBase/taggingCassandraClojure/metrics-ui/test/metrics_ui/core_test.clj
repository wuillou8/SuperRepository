(ns metrics-ui.core-test
      (:require [clojure.test :refer :all]
                [metrics-ui.cassandra-db :refer :all]
                [metrics-ui.tables :refer :all]
                [clj-webdriver.taxi :as t]
                ))


;init
(def session (connect-cassandra))
(drop-keyspace "test")
(create-keyspace session "test")
(def cassandra-ks (connect-keyspace "test"))
(create-table cassandra-ks "events" events-template)
(create-table cassandra-ks "purchases" purchases-template)

;;;;;

(use 'clj-webdriver.taxi)
(System/setProperty "webdriver.chrome.driver" "/Users/jairwuiloud/Downloads/chromedriver")


(set-driver! {:browser :chrome} "http://localhost:3000/refer.html")
(click "#Gototestpage")

(def click-list (list "#viewEvent" "#clickEvent" "#menuNavigation" "#addtobasket" "#purchase" "#paymentConfirmation"))

(for [cl click-list]
  ;(println cl)
  (t/click cl))





;;;;;

(click "#viewEvent")
(click "#clickEvent")
(click "#menuNavigation")
(click "#addtobasket")
(click "#purchase")
(click "#paymentConfirmation")



