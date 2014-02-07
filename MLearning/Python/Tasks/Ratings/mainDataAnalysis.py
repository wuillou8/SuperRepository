# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 12:28:59 2013

@author: jair

"""

import time, setuptools

#-My own Packages -------------------------------------------------------------
import MyPandaUtilities
import MyIO
import AnalysisRankings
import AnalysisGDAXIstaticRankings
import AnalysisFilteringRates
#------------------------------------------------------------------------------

'''
def main():
    pass

if __name__ == '__main__':
    main()
'''

adressRanking = '../Data/rankingsMapegy.dat'   
adressGDAXIstaticRankings = '../Data/yahooGDAXI_static.csv'

start = time.clock()

myRankings = AnalysisRankings.DataStudy( adressRanking )
myRankingsGDAXIstaticRankings = \
            AnalysisGDAXIstaticRankings.DataStudy( adressGDAXIstaticRankings )

myFilter = AnalysisFilteringRates.Filter( \
                            myRankings, myRankingsGDAXIstaticRankings, u'Name' )

print "-----------------------------------------------------------------------"
print ' computation time: %s' % ( time.clock() - start )
print "-----------------------------------------------------------------------"