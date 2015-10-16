(ns crawlers.core
  (:require [net.cgrand.enlive-html :as html]
            [clojure.data.json :as json]
            [clojure.java.io :as io]
            [clojure.core.async :as async])
  (:gen-class))

(defn fetch-product-page
  [pid]
  (html/html-resource
    (java.net.URL. (str "http://www.yoox.com/uk/38475607IB/item#dept=men&sts=ip_baynote&bnwidget=PDSameDesigner&bnslot=3&bnpid=38475607&cod10=38475607IB&sizeId="))))

                     ;                     "http://www.yoox.com/uk/44846529ED/item#dept=men&sts=ip_baynote&bnwidget=PDSameDesigner&bnslot=4&bnpid=44846529&cod10=44846529ED&sizeId="))))
                     ;"http://www.yoox.com/uk/44846523UN/item#dept=shoesmen&sts=sr_shoesmen80&cod10=44846523UN&sizeId="))))
                     ;"http://www.yoox.com/uk/44810269JC/item#dept=women&sts=sr_women80&cod10=44810269JC&sizeId=")
                   ;"http://www.yoox.com/uk/42407818NJ/item#dept=denimwomen&sts=sr_denimwomen80&cod10=42407818NJ&sizeId=")))) 
                     ;"http://www.yoox.com/uk/42407818NJ/item#dept=denimwomen&sts=sr_denimwomen80&cod10=42407818NJ&sizeId="))))

(defn- flatten-tags
  [tag-seq]
  (apply str (map #(if-let [c (and (map? %) (:content %))] (first c) %) tag-seq)))

;;$('#itemTitle').find('h2').find('a').find('span').html()


(defn get-product-info
  [pid]
  (let [
        page (fetch-product-page pid)
        brand (first (html/select page [:div#itemTitle :h2 :a :span]))
        ;price (html/select page [:div#itemPrice :span#infoPrice :span]) ; :div#oldprice])
        ]
    (println "3 "  brand)
    {:category "data-category"
     :brand (first (:content brand))
     :price "data-price"
     :currency "data-currency"
     :name "product-name"; (first (:content product-name))
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
