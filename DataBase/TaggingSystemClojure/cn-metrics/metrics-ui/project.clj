(defproject metrics-ui "0.1.0-SNAPSHOT"
  :description "FIXME: write description"
  :url "http://example.com/FIXME"
  :license {:name "Eclipse Public License"
            :url "http://www.eclipse.org/legal/epl-v10.html"}
  :jvm-opts ["-Dphantomjs.binary.path=./phantomjs-1.9.0-macosx/bin/phantomjs"]
  :source-paths ["src/clj" "src/cljs"]

  :dependencies [[org.clojure/clojure "1.7.0"]
                 [incanter "1.5.6"]
                 [ring "1.3.2"]
                 [ring/ring-defaults "0.1.5"]
                 [ring/ring-json "0.4.0"]
                 [ring-server "0.4.0"]
                 [ring-cors "0.1.7"]
                 [prone "0.8.2"]
                 [compojure "1.3.4"]
                 [hiccup "1.0.5"]
                 [environ "1.0.0"]
                 [clojurewerkz/cassaforte "2.0.0"]
  
                 [cljsjs/react "0.13.3-0"]
                 [reagent "0.5.0"]
                 [reagent-forms "0.5.1"]
                 [reagent-utils "0.1.5"]
                 [org.clojure/clojurescript "0.0-3308" :scope "provided"]
                 [secretary "1.2.3"]
                 [cljs-ajax "0.3.11"]
                 
                 [clj-webdriver "0.6.0"]
                 [org.seleniumhq.selenium/selenium-server "2.43.0"]
                 [org.seleniumhq.selenium/selenium-java "2.43.0"]
                 [org.seleniumhq.selenium/selenium-remote-driver "2.43.0"]
                 [com.github.detro/phantomjsdriver "1.2.0"
                  :exclusion [org.seleniumhq.selenium/selenium-java
                              org.seleniumhq.selenium/selenium-server
                              org.seleniumhq.selenium/selenium-remote-driver]]
                 ;[com.github.detro.ghostdriver/phantomjsdriver "1.0.3"]
                 ]

  :plugins [[lein-environ "1.0.0"]
            [lein-asset-minifier "0.2.2"]
            [lein-ring "0.9.6"]]

  :ring {:handler metrics-ui.handler/app
         :uberwar-name "metrics-ui.war"}

  :min-lein-version "2.5.0"

  :uberjar-name "metrics-ui.jar"

  :main metrics-ui.server

  :clean-targets ^{:protect false} [:target-path
                                    [:cljsbuild :builds :app :compiler :output-dir]
                                    [:cljsbuild :builds :app :compiler :output-to]]

  :minify-assets
  {:assets
    {"resources/public/css/site.min.css" "resources/public/css/site.css"}}

  :cljsbuild {:builds {:app {:source-paths ["src/cljs"]
                             :compiler {:output-to     "resources/public/js/app.js"
                                        :output-dir    "resources/public/js/out"
                                        :asset-path   "js/out"
                                        :optimizations :none
                                        :pretty-print  true}}}}

  :profiles {:dev {:repl-options {:init-ns metrics-ui.repl
                                  :nrepl-middleware []}

                   :dependencies [[ring-mock "0.1.5"]
                                  [ring/ring-devel "1.3.2"]
                                  [leiningen-core "2.5.1"]
                                  [lein-figwheel "0.3.5"]
                                  [org.clojure/tools.nrepl "0.2.10"]
                                  [pjstadig/humane-test-output "0.7.0"]]

                   :source-paths ["env/dev/clj"]
                   :plugins [[lein-figwheel "0.3.3"]
                             [lein-cljsbuild "1.0.6"]]

                   :injections [(require 'pjstadig.humane-test-output)
                                (pjstadig.humane-test-output/activate!)]

                   :figwheel {:http-server-root "public"
                              :server-port 3449
                              :nrepl-port 7002
                              :css-dirs ["resources/public/css"]
                              :ring-handler metrics-ui.handler/app}

                   :env {:dev true}

                   :cljsbuild {:builds {:app {:source-paths ["env/dev/cljs"]
                                              :compiler {:main "metrics-ui.dev"
                                                         :source-map true}}
}
}}

             :uberjar {:hooks [leiningen.cljsbuild minify-assets.plugin/hooks]
                       :env {:production true}
                       :aot :all
                       :omit-source true
                       :cljsbuild {:jar true
                                   :builds {:app
                                             {:source-paths ["env/prod/cljs"]
                                              :compiler
                                              {:optimizations :advanced
                                               :pretty-print false}}}}}})
