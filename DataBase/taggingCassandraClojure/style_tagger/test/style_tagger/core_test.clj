(ns style-tagger.core-test
  (:require [clojure.test :refer :all]
            [style-tagger.tables :refer :all]
            [style-tagger.cassandra-db :refer :all]
            [clj-webdriver.taxi :as t]))



(defn test-tagging [f]
  (let [session (connect-cassandra)
        dummy (create-keyspace session "test")
        cassandra-ks (connect-keyspace "test")]
    (create-table cassandra-ks "events" events-template)
    (create-table cassandra-ks "purchases" purchases-template))
  (f "fiyif")
  (drop-keyspace "test"))

(test-tagging println)




(defn test-sequence []
  (System/setProperty "webdriver.chrome.driver" "/Users/jairwuiloud/Downloads/chromedriver")
  (t/set-driver! {:browser :chrome} "http://localhost:3000/refer.html")
  (t/click "#Gototestpage"))


(defn test-sequence-phantomjs []
  (System/setProperty "webdriver.chrome.driver" "/Users/jairwuiloud/Downloads/chromedriver")
  
  ;(t/set-driver! {:browser :chrome} "http://localhost:3000/refer.html")
  ;(t/click "#Gototestpage"))


(test-sequence)





;init
(def session (connect-cassandra))
(try (drop-keyspace "test"))
(create-keyspace session "test")
(def cassandra-ks (connect-keyspace "test"))
(create-table cassandra-ks "events" events-template)
(create-table cassandra-ks "purchases" purchases-template)


(def session (connect-cassandra)) 
(create-keyspace session "test")
(connect-keyspace "test")
(create-table session "events" events-template)


;;;;;

(use 'clj-webdriver.taxi)
(System/setProperty "webdriver.chrome.driver" "/Users/jairwuiloud/Downloads/chromedriver")


(set-driver! {:browser :chrome} "http://localhost:3000/refer.html")
(click "#Gototestpage")

(def click-list (list "#viewEvent" "#clickEvent" "#menuNavigation" "#addtobasket" "#purchase" "#paymentConfirmation"))

(for [cl click-list]
  (t/click cl))

(close)


;;;;;
(click "#viewEvent")
(click "#clickEvent")
(click "#menuNavigation")
(click "#addtobasket")
(click "#purchase")
(click "#paymentConfirmation")
;;;;


; query

(get-column-elements cassandra-ks "purchases" "referer")
;conn-ks table column-symbol)

(get-column-elements cassandra-ks :purchases :referer)

(println cassandra-ks)


; phantomjs
; http://blog.zolotko.me/2012/12/clojure-selenium-webdriver-and-phantomjs.html
(use 'clj-webdriver.taxi)
(import 'org.openqa.selenium.phantomjs.PhantomJSDriver
                'org.openqa.selenium.remote.DesiredCapabilities)
(use '[clj-webdriver.driver :only [init-driver]])

(set-driver! (init-driver {:webdriver (PhantomJSDriver. (DesiredCapabilities. ))}))
(to "http://google.com")
(html "body")


; Now let's take a screenshot
(take-screenshot :file "phantom.png")





(def cassandra-ks (connect-keyspace "test"))
(get-column-elements cassandra-ks :purchases :referer) 














(deftest a-test
    (testing "FIXME, I fail."
          (is (= 0 1))))









