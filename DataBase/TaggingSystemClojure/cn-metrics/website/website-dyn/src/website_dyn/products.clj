(ns website-dyn.products)

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; create products
(defn set-action-purchase 
  [action id affiliation revenue tax shipping coupon]
  {:ec-action "ec:setAction",
   :action "purchase",
   :id id,
   :affiliation affiliation,
   :revenue revenue,
   :tax tax,
   :shipping shipping,
   :coupon coupon})

(defn add-prod
  [id name category brand variant price quantity] 
  {:ec-action "ec:addProduct",
   :id id,
   :name name,
   :category category,
   :brand brand,
   :variant variant, 
   :price price,
   :quantity quantity}) 

(defn checkout-step
  [step option] 
  {:ec-action "ec:setAction",
   :action "checkout",
   :step step,
   :option option})


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; products
(def checkout 
  {:ec-action "ec:setAction",
   :action "checkout",
   :step "1",
   :option "Visa"})

(def prod-tshirt
  {:ec-action "ec:addProduct",
   :id "P12345",
   :name "Android Warhol T-Shirt",
   :category "Apparel",
   :brand "Google",
   :variant "black", 
   :price "29.20",
   :quantity 1}) 

(def example-purchase 
  {:ec-action "ec:setAction",
   :action "purchase",
   :id "T12345",
   :affiliation "Google Store - Online",
   :revenue "37.39",
   :tax "2.85",
   :shipping "5.34",
   :coupon "SUMMER2013"})
