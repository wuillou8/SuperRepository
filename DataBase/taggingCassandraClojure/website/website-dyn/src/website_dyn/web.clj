(ns website-dyn.web
  (:require [clojure.string :as s]
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


(defn override-userID [page userID]
  (s/replace (slurp (io/resource page)) #"USER_ID" userID))

(defroutes app
 
  (GET "/" []
       (slurp (io/resource "login.html")))

  (POST "/login" [:as request]
      (let [
            userID (-> request :params :userID)
            ]
        ;(println (-> request :params :userID))
        (-> (response  (override-userID "homepage.html" userID)) 
            (content-type "text/html")
            (assoc :session {:userID userID}))))

  (GET "/page/:page" [page :as request]
      ;(println (-> request :params :userID))
      (-> (response (override-userID page (get-in request [:session :userID])))   
          (content-type "text/html")))
  
  (GET "/js/:page" [page :as request]
      ;(println (-> request :params :userID))
      (-> (response (override-userID page (get-in request [:session :userID])))   
          (content-type "text/javascript")))

  ;(ANY "*" []
  ;      (response (route/not-found (slurp (io/resource "404.html"))))))
)

(def middleware-app 
  (-> app 
     (wrap-defaults  (assoc-in site-defaults [:security :anti-forgery] false ))))
