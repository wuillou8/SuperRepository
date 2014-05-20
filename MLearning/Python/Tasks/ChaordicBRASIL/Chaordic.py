# -*- coding: utf-8 -*-
"""
Created on Fri May 09 12:28:38 2014
@author: jair
"""

#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import time
#import pandas as pd
#import json
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import MyChaordicAnalysis
import MyModels
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

infile = 'input-challenge.json' #'jair.json'
outfile = 'testout.json'

analysis = MyChaordicAnalysis.MyChaordicAnalysis( infile )
reset = time.time()
#
#analysis.Analysis()
print "Analysis Time:", ( time.time() - reset )
analytime = ( time.time() - reset )

#analysis.Train()
#analysis.fit()
#analysis.fit2()
analysis.fitting()


#analysis.ModelConstr2() #ModelConstr2(self)

#sys.exit()
#analysis.RunROCAUConModel('OUT')

#for j in np.arange(0,1.1,0.2):
#    for i in np.arange(0,1.1,0.2):
#        analysis.ModelConstr(i,j)


traintime = time.time() - analytime

print 'Analysis Time:', analytime
print 'Train Time:', traintime

#jair = MyModels.MyModel1(ananas)
#analysis.AnalysisOutput()