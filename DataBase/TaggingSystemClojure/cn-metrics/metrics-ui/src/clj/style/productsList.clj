(ns style.productsList
  (:require [clojure.data.json :as json]))

; product-detail extra properties
(def hero-type [
                "style"
                "bookmark"
                nil
                nil
                ])

(def messges-type [
                "Sold out"
                "Low in stock"
                "Runway piece"
                "As seen in Vogue"
                "As seen in GQ"
                nil
                nil
                nil
                  ])
(def brand-type [
                "Sed finibus"
                "Laoreet bibendum"
                "Proin vitae velit"
                "Morbi finibus"
                "Nullam id"
                "Aenean maximus"
                "Nullam"
                "Cras faucibus"
                "Donec fringilla eget"
                "Quisque"
                "Curabitur dictum ipsum"
                ])
(def desc-type [
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit"
                "Etiam erat elit"
                "Id porta elit purus a ligula"
                "Suspendisse ante ante, iaculis vitae"
                "Sagittis ante tempor eu mauris placerat"
                "Tempus ac elit"
                "Velit in mattis luctus, dui"
                "Et aliquam quam finibus"
                "Rhoncus diam tempus"
                "Malesuada vitae, sagittis"
                "Quisque rutrum, libero a vehicula eleifend, lacus nulla"
                "Laoreet bibendum"
                "Morbi vestibulum diam et arcu"
                ])


(defn product-detail
  [ id ]
  {
     :sku (format (str id)), 
     :type "product",
     :href "product-details-fashion.html",
     :image (str "images/placeholders/product-listing/" (+ id 1) ".jpg" ),
     :brand (get brand-type (rand-int (count brand-type))),
     :desc (get desc-type (rand-int (count desc-type))),
     :currency "£",
     :price (format "%.2f" (double (rand-int 1700))),
     :message (get messges-type (rand-int (count messges-type))),
     :hero (get hero-type (rand-int (count hero-type)))
  })

(defn products-list
  [ length ]
  (map product-detail (range length))
)

