(ns metrics-ui.handler
  (:require [compojure.core :refer [POST GET defroutes]]
            [compojure.route :refer [not-found resources]]
            [ring.middleware.defaults :refer [site-defaults wrap-defaults]]
            [ring.middleware.cors :refer [wrap-cors]]
            [ring.middleware.json :refer [wrap-json-body]]
            [hiccup.core :refer [html]]
            [hiccup.page :refer [include-js include-css]]
            [prone.middleware :refer [wrap-exceptions]]
            [ring.middleware.reload :refer [wrap-reload]]
            [environ.core :refer [env]]
            [clojurewerkz.cassaforte.client :as cc]
            [clojurewerkz.cassaforte.cql    :as cql]
            [clojurewerkz.cassaforte.query    :refer :all]
            [clojure.pprint :refer [pprint]]))

(def home-page
  (html
   [:html
    [:head
     [:meta {:charset "utf-8"}]
     [:meta {:name "viewport"
             :content "width=device-width, initial-scale=1"}]
     (include-css (if (env :dev) "css/site.css" "css/site.min.css"))]
    [:body
     [:div#app
      [:h3 "ClojureScript has not been compiled!"]
      [:p "please run "
       [:b "lein figwheel"]
       " in order to start the compiler"]]
     (include-js "js/app.js")]]))



(defn event->cassandra-db [ks header event]
  (let [session (cc/connect ["127.0.0.1"] {:keyspace ks})
  ; CREATE TABLE "events" (userid varchar, category varchar, action varchar, location varchar, timestamp bigint, eventid varchar, PRIMARY KEY (timestamp, userid, category, location, action, eventid))
        category  (:category event)
        action    (:action event)
        location  (:referer header)
        event-cassandra {:userid (:id (:userdata event))
                         :category (:category event)
                         :action (:action event)
                         :location location
                         :timestamp (long (:timestamp event))
                         :eventid (:id (:eventdata event))}]
    (cql/insert session "events" event-cassandra)
    ;CREATE TABLE "purchases" (userid varchar, productid varchar, timestamp bigint,
    ;                          location varchar,
    ;                          productname varchar, productcategory varchar, productbrand varchar,
    ;                          productvariant varchar, productprice float, productcosts float,      
    ;                          PRIMARY KEY (timestamp, productid));
    (if (and (= category "transaction") (= action "purchase confirmation"))
      (let [
            userid (:id (:userdata event))
            timestamp (long (:timestamp event))
            
            product (:eventdata event)
            productid (:id product)
            productname (:name product)
            productcategory (:category product)
            productbrand  (:brand product)
            productvariant (:variant product)
            productprice (-> (:price product) read-string float)
            productcosts (-> (:costs product) read-string float)
            product-cassandra {:userid userid, 
                               :productid productid, 
                               :timestamp timestamp, 
                               :productname productname, 
                               :location location,
                               :productcategory productcategory,
                               :productbrand productbrand,
                               :productvariant productvariant,
                               :productprice productprice,
                               :productcosts productcosts}
            ]
      (cql/insert session "purchases" product-cassandra))
    )
  ))

(defn header-parser [header]
  ; list of fields:
  ;origin host user-agent content-type cookie content-length referer connection accept accept-language accept-encoding
  (let [referer (get-in header ["referer"])
        user-agent (get-in header ["user-agent"])]
        {:referer referer :device user-agent}))


(defroutes routes
  (GET "/" [] home-page)
  (POST "/event" req
    (let [event (:body req)
          head-metadata (header-parser (:headers req))] 
      (println "EVENTs:")
      ;(println req)
      (println "1***: " event)
      (println "2***: " (:headers req));head-metadata)
      (event->cassandra-db "analytics0" head-metadata event)
      {:status 200}))
  (resources "/")
  (not-found "Not Found"))

(def app
  (let [handler (wrap-defaults #'routes (dissoc site-defaults :security))
        handler (if (env :dev)
                  (-> handler wrap-exceptions wrap-reload)
                  handler)]
    (-> handler
        (wrap-json-body {:keywords? true})
        (wrap-cors :access-control-allow-origin #".*"
                   :access-control-allow-methods [:post]))))
