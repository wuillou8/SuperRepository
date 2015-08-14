(ns style.productDetails
  (:require [clojure.data.json :as json]))


(def product-details
  {
    :currency "£"
    :titles {
      :brand "Alexander McQueen"
      :brandLink "product-listing.html"
      :name "Caroline asymmetric printed silk and crepe dress" }
    :prices {
      :current "2,895.00"
      :old "3,350.00"
      :saving "70"
      :sold_out false }
    :colours [{
        :label "Black"
        :rgb "#000000"
        :stock "available"
        :selected true }
      {
        :label "Navy Blue"
        :rgb "#0B2E59"
        :stock "available"}
      {
        :label "Blood Red"
        :rgb "#8A0707"
        :stock "available"}
      {
        :label "Dark Blue"
        :rgb "#20293F"
        :stock "unavailable"}
      {
        :label "Peace Green"
        :rgb "#79BD9A"
        :stock "unavailable"}]
    :sizes [{
        :label "6"
        :stock "unavailable"}
      {
        :label "8"
        :stock "unavailable"}
      {
        :label "10"
        :stock "low"}
      {
        :label "12"
        :stock "in stock"}
      {
        :label "14"
        :stock "in stock"}]
    :details [{
        :title "Models Measurements"
        :text "<ul><li>Height: 1.77</li><li>Bust/Chest (cm): 83</li><li>Waist (cm): 60</li><li>Hips (cm): 90</li><li>Model is wearing size: S</li></ul>"}
      {
        :title "Composition & care"
        :text "<ul><li>Outer Composition Polyester 20%</li><li>Lining Composition Cotton 50%</li><li>Lining Composition Acetate 50%</li><li>Outer Composition Virgin Wool 80%</li></ul>"}
      {
        :text "<p>Washing Instructions: Dry Clean Only</p>"}]
    :description "<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc ut sapien urna. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Vivamus maximus condimentum arcu, quis porta nulla porttitor eu. Etiam eu facilisis dui. Nunc interdum erat sem, a lacinia eros tincidunt non. Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p><p>Sed tincidunt, metus ac hendrerit egestas, tortor felis aliquet diam, sit amet elementum nisl nulla at augue.</p>"
    :SKU "915045935"
    :hero {
      :src "/images/placeholders/product-details/hero.jpg"
      :alt  "Lorem ipsum dolor"
    }
    :gallery [{
        :type "single"
        :src "/images/placeholders/product-details/dress.jpg"
        :alt "Lorem ipsum dolor"}
      {
        :type "single"
        :src "/images/placeholders/product-details/fabric.jpg"
        :alt "Lorem ipsum dolor"}
      {
        :type "pair"
        :src1 "/images/placeholders/product-details/front-side.jpg"
        :alt1 "Lorem ipsum dolor"
        :src2 "/images/placeholders/product-details/rear-side.jpg"
        :alt2 "Lorem ipsum dolor"}]
    :shipping_returns []
    :more_grid []
    :similar_grid []
  })

; (defn product-details
;   [ ]
;   {

;   })
