(ns run_website.demo
  (require ;[metrics.utils :refer :all]
           ;[metrics.mc-methods :refer :all]
           ;[metrics.metrics :refer :all]
           ;[metrics.useritem-behaviour :refer :all]
           ;[metrics.chat-ganalytics :refer :all]
           ;[metrics.google-analytics :refer :all]
           [incanter.core :refer :all]
           [incanter.stats :refer :all]
           [incanter.charts :refer :all]
           [clj-webdriver.taxi :as t]))


; model glob variables
(def Nusers 100)
(def Nitems 1000)
(def Ntot-features 50)
(def Nuser-features 5)
(def Nitem-features 3)

; generate players
(def users (map #(create-rand-user % Nuser-features Ntot-features) (range Nusers)))
(def items (map #(create-rand-item % Nitem-features Ntot-features) (range Nitems)))
;(ns metrics.demo.basic-demo)





;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;     RUN                                            ;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(use 'clj-webdriver.taxi)


(def sitemap {:trunc ['menswear' 'womenswear'] :first ['top' 'dress' 'shirt' 'trouser']})

(def size-trunc (count (:trunc sitemap)))
(def size-first (count (:first sitemap)))


(defn run-site-standard 
  [userId]

  (set-driver! {:browser :firefox} "https://morning-beach-6895.herokuapp.com");(str "https://morning-beach-6895.herokuapp.com/" userId))

  (let [my-count1 (rand-int size-trunc)]
    (case my-count1
      0 (click "#menswear")
      1 (click "#womenswear")))

  (let [my-count2 (rand-int size-first)]
    (case my-count2
      0 (click "#top")
      1 (click "#dress")
      2 (click "#shirt")
      3 (click "#trouser")
    ))

  (close)
)


(defn path-funnel [link-click]
  (if (exists? link-click)
    (if (= 1 (rand-int 2))
      (click link-click) ;"#funnelPlaceIntoCart")
      (click "#STOP") 
  )))

(defn run-site-funnel
  [userId]

  (set-driver! {:browser :firefox} "https://morning-beach-6895.herokuapp.com")
  
  (click "#funnel")
  
  (path-funnel "#funnelPlaceIntoCart")
   
  (path-funnel "#funnelEnterPayment")
  
  (path-funnel "#funnelPaymentSuccess")
  
  (path-funnel "#funnelPayedSuccess")
  
  (close)
)

(set-driver! {:browser :firefox} "https://morning-beach-6895.herokuapp.com")
(click "#funne")
(click "#ff")
(click  "#funnelPlaceIntoCart")

(for [i (range 100)]
  (run-site-standard (str "user"  (rand-int 1000))
))


(for [i (range 20)]
  (run-site-funnel (str "user"  (rand-int 1000))
))


(exists? "#menswear")

(str "dd" 2)


(run-site-funnel "5678")
(run-site-funnel "5678")
(run-site-funnel "5678")
(run-site-funnel "5678")
(run-site-funnel "5678")
(run-site-funnel "5678")
(run-site-funnel "5678")
(run-site-funnel "5678")
(run-site-funnel "5678")
(run-site-funnel "5678")



(if (= 1 (rand-int size-trunc))
  (click "a[href*='menswear']")
  (click "a[href*='womenswear']")
  )


(set-driver! {:browser :firefox} "https://morning-beach-6895.herokuapp.com")
