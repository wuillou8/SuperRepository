(ns run-website.phantom-site)

;;;;http://blog.zolotko.me/2012/12/clojure-selenium-webdriver-and-phantomjs.html

;(require [clj-webdriver.driver :only [init-driver]]))

(use '[clj-webdriver.driver :only [init-driver]])

(use 'clj-webdriver.taxi) 
(import 'org.openqa.selenium.phantomjs.PhantomJSDriver
                'org.openqa.selenium.remote.DesiredCapabilities)
(use '[clj-webdriver.driver :only [init-driver]])
 



(set-driver! (init-driver {:webdriver (PhantomJSDriver. (DesiredCapabilities. ))}))
 
(html "body")

(to  "morning-beach-6895.herokuapp.com")

(take-screenshot :file "phantom.png")

(close)


