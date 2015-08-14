(defproject website-dyn "0.1.0-SNAPSHOT"
    :description "Demo Clojure web app"
    :url "http://website-dyn.herokuapp.com"
    :license {:name "Eclipse Public License v1.0"
              :url "http://www.eclipse.org/legal/epl-v10.html"}
    :dependencies [[org.clojure/clojure "1.6.0"]
                   [compojure "1.1.8"]
                   [ring "1.4.0"]
                   [environ "0.5.0"]
                   [ring/ring-defaults "0.1.5"]
                   [hiccup "1.0.5"]
                    ]
    :min-lein-version "2.0.0"
    :plugins [[environ/environ.lein "0.2.1"]
              [lein-ring "0.9.6"]]
    :ring {:handler website-dyn.web/middleware-app}
    :hooks [environ.leiningen.hooks]
    :uberjar-name "website-dyn-standalone.jar"
    :profiles {:production {:env {:production true}}})
