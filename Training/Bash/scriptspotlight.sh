#!/bin/bash
#DATEFROM="2014-11-01T00:00:00-0000"
#DATETO="2014-11-11T00:00:00-0000"

if [ "$1" = "" -o "$2" = "" ] 
then 
        echo "args in terminal: #1 Datefrom #2 Dateto"
	echo "e.g. ./scriptspotligth.sh   2014-11-01T00:00:00-0000 2014-11-11T00:00:00-0000"
	exit
 
elif [ "$2" = "rerun" ]
then
	str1=`grep \"published\"\: 1.json | tail -1 | awk '{print $2}' | sed 's|\,||g' | sed 's|Z||' | sed 's|"||g'`
	str2="-0000"
        DATEFROM=$1
	DATETO=$str1$str2
	#echo ---*-*Datetime: $DATETO

else
	rm data.json
	DATEFROM=$1
	DATETO=$2
	echo > tmptrack
	echo > data.json 

fi

echo -------- Datefrom $DATEFROM Dateto $DATETO -------

BASE_URL="http://apiservice.reuters.com/api/feed/channelarticles?channel=everything&count=100&edition=US&format=json&apikey=72461C50B1CEAD3135BA6BDA53B203D3&deviceid=E7CDD293-9C3A-5AB9-9181-58E1B572DD44&datefrom=$DATEFROM&dateto=$DATETO"

echo Fetching $BASE_URL 

wget $BASE_URL -O 1.json

# if the code get twice the same data it stops. 
# Either there is a prbm or it is done.
if [ `diff 1.json tmptrack | wc | awk '{print $1}'` = 0 ]
then  
	rm -rf tmptrack
	echo ] >> data.json
	echo } >> data.json
	exit
else 
	cat 1.json > tmptrack
	if [ `wc data.json | awk '{print $1}'` = 1 ]
	then 
		l=`wc 1.json | awk '{printf $1}'`
		v=1
 		LL=$(($l-$v)) 
		head -$LL 1.json >> data.json
	else
		echo , >> data.json
		l=`wc 1.json | awk '{printf $1}'`
		min=16
		L=$(($l - $min))
		v=2
		LL=$(($L-$v)) 
		tail -$L 1.json | head -$LL >> data.json
	fi
	./scriptspotlight.sh $1 "rerun"
fi
