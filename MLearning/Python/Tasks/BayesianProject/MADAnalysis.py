import io, os, csv, sys 
import math as ma
import numpy as np

from IOInit import *
from Analysis import *
from Models import BayesNaive #,Learns, BayesTests
from ROC_AUC import *

####################################################################################
#		Runs the Analysis and timing     				   #
####################################################################################

print "--BEGIN-*-*-------"


if len(sys.argv) <> 3:
	sys.stderr.write('Usage: fileName passed as arg #2, TestSample passed as arg #3, features under study as arg #4 ')
	sys.exit(1)


#Read In Learning / Testing Sample
reset = time.time()
learndata = IOInit(sys.argv[1])
IOInit.checkData(learndata) 
IOInit.nbEmptyFields(learndata)

testdata = IOInit(sys.argv[2])
IOInit.checkData(testdata) 
IOInit.nbEmptyFields(testdata)
print "Read In/ Check Data time:", ( time.time()-reset )
reset = time.time()

#Analysis 
featTest = ['site,bannertype','add,account','account,device']
factors = [1.0,0.3,0.1]
cutoffs = [300,200,500]
for nb,SubFeatures in enumerate(featTest):

	featsSub = SubFeatures.split(',')
	print "subfeatures computed: ", featsSub

	if nb == 0:
		# Init
		learnbayesNaive = BayesNaive(learndata,featsSub)
		BayesNaive.BayesLearn(learnbayesNaive,cutoffs[nb])

	else:
		BayesNaive.importTestData(learnbayesNaive,learndata,featsSub)
		BayesNaive.BayesLearn(learnbayesNaive,cutoffs[nb])
		
	BayesNaive.importTestData(learnbayesNaive,testdata,featsSub)
	if factors[nb] == 1.0:
		BayesNaive.BayesTest(learnbayesNaive,testdata)
	else:
		factor = factors[nb]
		BayesNaive.AddBayesTest(learnbayesNaive,testdata,factor)


	roc_analy = ROC_AUC(learnbayesNaive.testList)
	roc_analy.counting()
	roc_analy.get_auc("print")

print "Analysis Time:", ( time.time()-reset )
reset = time.time()

# print out the analysis for the test file
#for tmp in containername:
#	print "output:", tmp[0], tmp[1], tmp[2]


print "--END-*-*-------"


