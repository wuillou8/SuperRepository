  CREATE TABLE "events" (userid varchar, category varchar, action varchar, location varchar, timestamp bigint, eventid varchar, PRIMARY KEY (timestamp, userid, category, location, action, eventid))
  

CREATE TABLE "purchases" (userid varchar, productid varchar, timestamp bigint,
                          location varchar,
                          prodhead-metadatauctname varchar, productcategory varchar, productbrand varchar,
                          productvariant varchar, productprice float, productcosts float,      
                          PRIMARY KEY (timestamp, productid));

