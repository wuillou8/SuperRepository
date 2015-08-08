(defproject metrics "0.1.0-SNAPSHOT"
  :description "FIXME: write description"
  :url "http://example.com/FIXME"
  :license {:name "Eclipse Public License"
            :url "http://www.eclipse.org/legal/epl-v10.html"}
  :dependencies [
                 [org.clojure/clojure "1.6.0"]
                 [org.clojure/clojure-contrib "1.2.0"]
                 [org.clojure/data.csv "0.1.2"]
                 [incanter "1.5.6"]
                 [fuzzy-string "0.1.2-SNAPSHOT"]
                 [org.clojure/data.json "0.2.6"]
                 [org.clojure/math.numeric-tower "0.0.4"]
                 [clj-http "1.1.2"]
                 [net.mikera/core.matrix "0.32.1"]
                 
                 ; incompatible somehow with the google methods...
                 ;[clj-webdriver "0.6.0"]
                 ;[org.seleniumhq.selenium/selenium-server "2.43.0"]
                 ;[org.seleniumhq.selenium/selenium-java "2.43.0"]
                 ;[org.seleniumhq.selenium/selenium-remote-driver "2.43.0"]
                 ;[com.github.detro/phantomjsdriver "1.2.0"
                 ; :exclusion [org.seleniumhq.selenium/selenium-java
                 ;             org.seleniumhq.selenium/selenium-server
                 ;             org.seleniumhq.selenium/selenium-remote-driver]]
                 
                 [com.google.api-client/google-api-client "1.17.0-rc"]
                 [com.google.http-client/google-http-client "1.17.0-rc"]
                 [com.google.http-client/google-http-client-jackson2 "1.17.0-rc"]
                 [com.google.apis/google-api-services-analytics "v3-rev64-1.17.0-rc"]
                 [com.google.gdata/gdata-contacts-3.0 "1.41.5"]
                 ]
                 
                 
  :repositories {"mandubian-mvn" "http://mandubian-mvn.googlecode.com/svn/trunk/mandubian-mvn/repository"})
