#!/bin/bash

# features['token', 'site', 'add', 'country', 'rtb', 'account', 'campaign', 'bannertype','spotbuy','app_id','device','to  ken_check','clicks']i

for i  in `cat list` 
do 
echo $i
#time python FeaturesAnalysis.py sample10000.tsv ${i} > RESU/resu10000${i}  # test
time python FeaturesAnalysis.py sample100000.tsv ${i} > RESU/resu100000${i} 
time python FeaturesAnalysis.py sample500000.tsv ${i} > RESU/resu500000${i}
time python FeaturesAnalysis.py samplehead.tsv ${i} > RESU/resu1000000${i}
done
