# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 12:28:59 2013

@author: jair
"""

import time

#-My own Packages -------------------------------------------------------------
import MyPandaUtilities
import MyIO
import AnalysisDBcustoms
import AnalysisDBstores
#------------------------------------------------------------------------------

'''
def main():
    pass

if __name__ == '__main__':
    main()
'''    

adressDBcustoms = '../Data/DBcustoms.txt'    
adressDBstore = '../Data/DBstore.txt' 

start = time.clock()

#bla = MyIO.DataAnalysis( '../../Debug/test.data' ) 

#myDBcustoms = MyIO.DataAnalysis( adressDBcustoms )
#myDBstores = MyIO.DataAnalysis( adressDBstore )

#myDBstores = AnalysisDBstores.DataStudy( adressDBstore ) 
myDBcustoms = AnalysisDBcustoms.DataStudy( adressDBcustoms )

print "-----------------------------------------------------------------------"
print ' computation time: %s' % ( time.clock() - start )
print "-----------------------------------------------------------------------"