(defproject run-website "0.1.0-SNAPSHOT"
  :description "FIXME: write description"
  :url "http://example.com/FIXME"
  :license {:name "Eclipse Public License"
            :url "http://www.eclipse.org/legal/epl-v10.html"}
  :jvm-opts ["-Dphantomjs.binary.path=./phantomjs-1.9.0-macosx/bin/phantomjs"]
  :dependencies [
                 [org.clojure/clojure "1.6.0"]
                 [incanter "1.5.6"]
                 [clj-webdriver "0.6.0"]

                 [org.seleniumhq.selenium/selenium-server "2.43.0"]
                 [org.seleniumhq.selenium/selenium-java "2.43.0"]
                 [org.seleniumhq.selenium/selenium-remote-driver "2.43.0"]
                 [com.github.detro/phantomjsdriver "1.2.0"
                  :exclusion [org.seleniumhq.selenium/selenium-java
                              org.seleniumhq.selenium/selenium-server
                              org.seleniumhq.selenium/selenium-remote-driver]]
                 [com.github.detro.ghostdriver/phantomjsdriver "1.0.3"]
                 ]
  ;:main ^:skip-aot run-website.core
  :target-path "target/%s"
  :profiles {:uberjar {:aot :all}})
