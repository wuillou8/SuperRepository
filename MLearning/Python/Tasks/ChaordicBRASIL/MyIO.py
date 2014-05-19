# -*- coding: utf-8 -*-
"""
Created on Fri May 09 15:13:48 2014
@author: jair
"""


import pandas as pd
import json

import MyPandaUtilities

class DataIO:
    '''
        Basic Analysis SuperClass:    
        Read file, stores into into a panda dataframe and print stat. out.
    '''
    def __init__(self,dataFile):
        # read in data and put it into a dframe
        ls = [] 
        with open(dataFile) as f:
            [ ls.append(json.loads(line)) for line in f ]
        self._dframe = pd.DataFrame( ls )
        del ls
        
        # produce dframe summary
        self._DatDescr = self._dframe.describe()
        self._headers = self._DatDescr.columns
        print "---------------------------------------------------------------"
        print "Reading file: ", str(dataFile)
        print "---------------------------------------------------------------"
        print self._DatDescr