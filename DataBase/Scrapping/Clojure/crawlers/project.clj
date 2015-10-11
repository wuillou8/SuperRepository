(defproject crawlers "0.1.0-SNAPSHOT"
  :description "FIXME: write description"
  :url "http://example.com/FIXME"
  :license {:name "Eclipse Public License"
            :url "http://www.eclipse.org/legal/epl-v10.html"}
  :dependencies [[org.clojure/clojure "1.7.0"]
                 [enlive "1.1.5"]
                 [clj-http "2.0.0"]
                 [http-kit "2.1.19"]
                 [wharf "0.2.0-SNAPSHOT"]
                 [org.jsoup/jsoup "1.8.3"]
                 [org.clojure/data.json "0.2.5"]
                 [org.clojure/core.async "0.1.346.0-17112a-alpha"]]
  :main ^:skip-aot crawlers.core
  :target-path "target/%s"
  :profiles {:uberjar {:aot :all}})
