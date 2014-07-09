"""
@author: jair
"""
import pandas as pd
import json
#-------------------------
import MyPandaUtilities

class DataIO:
    '''
        Basic Analysis SuperClass:    
        Read file, stores into into a panda dataframe and print stat. out.
    '''
    def __init__(self, dataFile, fileOut):
        # read in data and put it into a dframe
        ls = [] 
        try:
            with open(dataFile) as f:
                [ ls.append(json.loads(line)) for line in f ]
                self._dframe = pd.DataFrame( ls )
        except Exception:
            print 'Pbm with IO'
        self._dataOut = fileOut
        del ls
        
        # produce dframe summary
        self._DatDescr = self._dframe.describe()
        self._headers = self._DatDescr.columns
        print "---------------------------------------------------------------"
        print "Input file: ", str(dataFile)
        print "Output file: ", self._dataOut
        print "---------------------------------------------------------------"
        print self._DatDescr
        
    def printout(self, mylist):
        f = open( self._dataOut, 'w' )
        for tmp in mylist:
            print >> f, json.dumps( {"Buyer": tmp[0], "user": tmp[1]} )