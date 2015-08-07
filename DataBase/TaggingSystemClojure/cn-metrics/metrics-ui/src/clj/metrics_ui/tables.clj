(ns metrics-ui.tables)


; CREATE TABLE "events" (userid varchar, category varchar, action varchar, location varchar, timestamp bigint, eventid varchar, PRIMARY KEY (timestamp, userid, category, location, action, eventid))

(def events-template { 
                :timestamp :bigint
                :userid :varchar
                :category :varchar 
                :action :varchar 
                
                :location :varchar
                :eventid :varchar
                :primary-key  [:timestamp :userid :category :location :action :eventid]
                })

(def purchases-template { 
                :timestamp :bigint
                :userid :varchar
                :productid :varchar
                
                :location :varchar
                :productname :varchar
                :productcategory :varchar
                :productbrand :varchar
                :productvariant :varchar 
                :productprice :float 
                :productcosts :float
                :primary-key [:timestamp :productid]
                })

(def event-template {
                :unixtime :bigint 
                :action :varchar
                :eventvalue :varchar 
                :userId :varchar
                :location :varchar
                :pageversion :varchar
                :primary-key [:unixtime :action :userid]})

(def product-template {
      :hero :varchar
      :sku :int
      :type :varchar
      :href :varchar
      :image :varchar
      :brand :varchar
      :descr :text
      :currency :varchar
      :price :float
      :message :text
      :primary-key [:unixtime :action :userid]})



