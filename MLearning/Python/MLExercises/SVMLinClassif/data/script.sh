# prepa data
sed 's/:/ /g' twofeature.txt | awk '{print $1,$3,$5}' > twofeature_prepa.txt
