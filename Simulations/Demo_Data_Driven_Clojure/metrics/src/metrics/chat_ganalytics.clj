(ns metrics.chat-ganalytics
  (:require [metrics.mc-methods :refer :all]
            [metrics.utils :refer :all]
            ;[metrics.core :refer :all]
            [clj-http.client :as client]
            [incanter.core :refer :all]
            [incanter.stats :refer :all]
            [incanter.charts :refer :all]
            [clojure.data.json :as json]))


;;;;;;;;;;;;;;;;;;;
; TESTS
; get general url, with all fields
; https://developers.google.com/analytics/resources/concepts/gaConceptsTrackingOverview
(def json-filename "resources/ga_url_object.json")
(def urljsonobj (json/read-str (slurp json-filename) :key-fn keyword))
(def map-tobe-url (zipmap (map #(symbol (:variable %)) urljsonobj) (map :examplevalue urljsonobj)) )
(def url2 (params->query-string map-tobe-url))
; ...
;

; basical url for pushing signals
(def ga-query { :utmwv "5.6.4",
                :utms "39",
                :utmn "1750312921",
                :utmhn "salty-retreat-4888.herokuapp.com",
                :utmt "event",
                :utme "5(link*view*test)" ;"5(link*click*test)",
                :utmcs "UTF-8",
                :utmsr "1440x900",
                :utmvp "1318x689",
                :utmsc "24-bit",
                :utmul "en-us",
                :utmje "1",
                :utmfl "17.0 r0",
                :utmdt "Hello World",
                :utmhid "2108250189",
                :utmr "-",
                :utmp "/",
                :utmht "1434124059402",
                :utmac "UA-63941181-1",
                :utmcc "__utma=116456068.340550294.1433934831.1433935132.1434008713.3;+__utmz=116456068.1433934831.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none);",
                :utmjid "",
                :utmu "6AAAAAAAAAAAAAAAAAAAAAAE~" })

(def url2 (params->query-string ga-query))
(def url (str "https://ssl.google-analytics.com/__utm.gif?" url2))
; push signal
(client/get url)

;(defn poisson-distr->events
;  ;runs poisson distr. events of function fct., lambda is the poisson rate.
;  [lambda fct]
;  (time (Thread/sleep (poisson-law lambda)))
;  (apply fct))

(defn realistic-events->GAnal
  ; generate N times random, Poisson-law distributed events,
  ; events are specified through fct
  [N lambda fct]
  (take N (repeatedly #(poisson-distr->events lambda fct))))
          
;!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
; run Poisson distr unique click event against GAnalytics !         
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;(take 1000 (repeatedly #(poisson-distr->events 10 (client/get url))))

;49677
;(take 1000 (repeatedly #(poisson-distr->events 10 (interaction-modelv0 1 10 select-print))))
;(interaction-modelv0 100 10 select-print)

;(defn hallo-GAnal [] (client/get url))
;(realistic-events->GAnal 1000 10 (hallo-GAnal)) ;(client/get url))

;(client/get "https://ssl.google-analytics.com/__utm.gif?utmwv=5.6.4&utms=31&utmn=498674438&utmhn=salty-retreat-4888.herokuapp.com&utmt=event&utme=5(link*click*test)&utmcs=UTF-8&utmsr=1440x900&utmvp=1318x689&utmsc=24-bit&utmul=en-us&utmje=1&utmfl=17.0%20r0&utmdt=Hello%20World&utmhid=2108250189&utmr=-&utmp=%2F&utmht=1434122410029&utmac=UA-63941181-1&utmcc=__utma%3D116456068.340550294.1433934831.1433935132.1434008713.3%3B%2B__utmz%3D116456068.1433934831.1.1.utmcsr%3D(direct)%7Cutmccn%3D(direct)%7Cutmcmd%3D(none)%3B&utmjid=&utmu=6AAAAAAAAAAAAAAAAAAAAAAE~")

; purchase
;(client/get "https://ssl.google-analytics.com/__utm.gif?utmwv=5.6.4&utms=29&utmn=1129119803&utmhn=salty-retreat-4888.herokuapp.com&utmt=event&utme=5(link*purchase*test)&utmcs=UTF-8&utmsr=1440x900&utmvp=1318x689&utmsc=24-bit&utmul=en-us&utmje=1&utmfl=17.0%20r0&utmdt=Hello%20World&utmhid=2108250189&utmr=-&utmp=%2F&utmht=1434008835154&utmac=UA-63941181-1&utmcc=__utma%3D116456068.340550294.1433934831.1433934831.1433935132.2%3B%2B__utmz%3D116456068.1433934831.1.1.utmcsr%3D(direct)%7Cutmccn%3D(direct)%7Cutmcmd%3D(none)%3B&utmjid=&utmu=6AAAAAAAAAAAAAAAAAAAAAAE~")
