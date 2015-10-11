(ns crawlers.core
  (:require [net.cgrand.enlive-html :as html]
            [clojure.data.json :as json]
            [clojure.java.io :as io]
            [clojure.core.async :as async])
  (:gen-class))

(defn fetch-product-page
  [pid]
  (html/html-resource
    (java.net.URL. (str "http://www.yoox.com/uk/42407818NJ/item#dept=denimwomen&sts=sr_denimwomen80&cod10=42407818NJ&sizeId="))))

(defn- flatten-tags
  [tag-seq]
  (apply str (map #(if-let [c (and (map? %) (:content %))] (first c) %) tag-seq)))

;;$('#itemTitle').find('h2').find('a').find('span').html()


(defn get-product-info
  [pid]
  (let [page (fetch-product-page pid)
        product-name (first (html/select page [:div#itemTitle :h2 :a :span]))]
    (println (first (:content product-name)))
    {:category "data-category"
     :brand "data-brand"
     :price "data-price"
     :currency "data-currency"
     :name (first (:content product-name))
     :description "desc"
     :details "details"
     ;:raw-product-info (html/select page [:div#product-info])
     ;:raw-product-details (html/select page [:div#product-details-container :ul])
     }))

(defn -main
  "I don't do a whole lot ... yet."
  [& args]
  (println "Hello, World!")
  (println (get-product-info 590986)))
