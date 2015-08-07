(ns website-dyn.html-generator
  (:require 
            [website-dyn.products :refer :all]
            [clojure.string :as s]
            [compojure.core :refer [defroutes GET PUT POST DELETE ANY]]
            [compojure.handler :refer [site]]
            [compojure.route :as route]
            [clojure.java.io :as io]
            [ring.adapter.jetty :as jetty]
            [environ.core :refer [env]]
            [ring.middleware.session :refer [wrap-session]]
            [ring.middleware.defaults :refer :all]
            [ring.util.response :refer [response content-type]]
            [hiccup.core :refer :all])
  (:gen-class))

; utilities
(defn g [& args] 
  (apply str (map #(str "'" % "',") args)))

; Google Analytics
(defn ga-single-event 
  ([arg & args]
    (str "ga(" (apply g (concat (list arg) args)) "1);"))
  ([args]
    (str "ga(" (apply g args) "1);"))
  )

(ga-single-event (vals example-purchase))
;(ga-single-event "send" "event" "link" "click" "top")
;(ga-single-event (list "send" "event" "link" "click" "top"))

(def contents 
  (list 
    (link-click "menswear" "menswear.html"  
      (ga-single-event (g "send" "event" "link" "click" "menswear"))) 
    (link-click "womenswear" "womenswear.html"
      (ga-single-event (g "send" "event" "link" "click" "womenswear"))) 
    (link-click "funnelEntry" "funnelEntry.html"
      (ga-single-event (g "send" "event" "link" "click" "funnelEntry")))
  ))

(defn web-page-head 
  [button-name to-page ga-events]
    [:a { :id button-name :href (str "#" to-page) :onClick ga-events } (str "/--" button-name "--/") ])

(defn site-squeleton [head txt-title txt-comment contents]
  (html [:html {:lang "en"} [:head head] [:body [:h1 txt-title] [:p txt-comment] contents]]))

(def my-site
  (site-squeleton "myhead" "my-title" "!!!Not for fashion victims!!!" contents))

(spit "ressources/my-site.html" my-site)


