(ns metrics.google-analytics
    (:import
         (com.google.api.client.googleapis.auth.oauth2 GoogleCredential$Builder)
         (com.google.api.client.googleapis.javanet GoogleNetHttpTransport)
         (com.google.api.client.json.jackson2 JacksonFactory)
         (com.google.api.services.analytics Analytics$Builder AnalyticsScopes)))


;https://gist.github.com/terjesb/6783675
;http://nakkaya.com/2010/03/02/analytics-with-incanter/ 


(def HTTP_TRANSPORT (GoogleNetHttpTransport/newTrustedTransport))
(def JSON_FACTORY (JacksonFactory.))
 
(defn credential []
    (let [credential
                  (doto (GoogleCredential$Builder.)
                              (.setTransport HTTP_TRANSPORT)
                              (.setJsonFactory JSON_FACTORY)
                              (.setServiceAccountId "408190945737-jf3cbq866lb61ol6orc61eq5f6q2anrg@developer.gserviceaccount.com")
                              (.setServiceAccountScopes (seq [AnalyticsScopes/ANALYTICS_READONLY]))
                              (.setServiceAccountPrivateKeyFromP12File (java.io.File. "/Users/jairwuiloud/Desktop/WORK/GITAccounts/ThinkTopic/cn-metrics/website/client_secrets.p12")))]
          (.build credential)))

(defn service []
      (let [creds (credential)
                      analytics
                      (doto (Analytics$Builder. HTTP_TRANSPORT JSON_FACTORY creds)
                                    (.setApplicationName "cn-metrics")
                                    (.setHttpRequestInitializer creds))]
              (.build analytics)))
 
(defn q 
    ([]
    (let [analytics (service)
                  data (.data analytics)
                  ga (.ga data)
                  ; view id harcoded below
                  ;table (.get ga "ga:EXAMPLE" "2013-10-01" "2013-10-01" "ga:totalValue")
                  table (.get ga "ga:103643533" "2015-06-25" "2015-06-26" "ga:sessions,ga:pageviews")
            query (.. table
                                  (setDimensions "ga:eventAction")
                                  ;(setStartIndex (int 10001))
                                  (setMaxResults (int 10000)))]
          (.execute query)))
    ([date-start date-end metrics dimensions]
    (let [analytics (service)
                  data (.data analytics)
                  ga (.ga data)
                  ; view id harcoded below
                  ;table (.get ga "ga:EXAMPLE" "2013-10-01" "2013-10-01" "ga:totalValue")
                  table (.get ga "ga:103643533" date-start date-end metrics) ;"ga:sessions,ga:pageviews")
              query (.. table
                                  (setDimensions dimensions) ;"ga:eventAction")
                                  ;(setStartIndex (int 10001))
                                  (setMaxResults (int 10000)))]
      ; (.execute query) returns an object of type 
      ; com.google.api.services.analytics.model.GaData
      ; which headers are:
      ;[{"columnType" "DIMENSION", "dataType" "STRING", "name" "ga:eventAction"} {"columnType" "METRIC", "dataType" "INTEGER", "name" "ga:sessions"} {"columnType" "METRIC", "dataType" "INTEGER", "name" "ga:pageviews"}
      ; here I return the rows as lazyseq.
      (lazy-seq (.getRows (.execute query)))))
  )
  

; run
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
(def date-start "2015-06-25")
(def date-end "2015-06-26")
(def testj
  (q date-start date-end "ga:sessions,ga:pageviews" "ga:eventAction"))

; example for ecommerce
;(def query-ecommerce
;  (q date-start date-end "ga:transactions" "ga:transactionId") )




