# -*- coding: utf-8 -*-
"""
Created on Fri May 09 12:28:38 2014
@author: jair
"""

#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import time
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import MyChaordicAnalysis
import MyModels
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

infile = 'input-challenge.json'
outfile = 'testout.json'

analysis = MyChaordicAnalysis.MyChaordicAnalysis( infile )
reset = time.time()
analysis.Analysis()
print "Analysis Time:", ( time.time() - reset )

analytime = ( time.time() - reset )
analysis.Train()
analysis.fit2()
analysis.fitting()
analysis.RunROCAUConModel('OUT')

