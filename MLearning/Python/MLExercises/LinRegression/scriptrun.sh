#!/bin/bash          
        
python CODE/linearRegression.py > linRegression.resu
tail -1 linRegression.resu > linRegressionConv.resu
mv *.resu RESU/.
