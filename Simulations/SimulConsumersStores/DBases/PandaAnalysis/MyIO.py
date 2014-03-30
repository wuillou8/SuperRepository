# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 12:44:38 2013

@author: jair
"""
#-Packages --------------------------------------------------------------------
import numpy as np
from pandas import DataFrame
import pandas as pd
#-My own Packages -------------------------------------------------------------
import MyPandaUtilities
#------------------------------------------------------------------------------


class DataAnalysis:
    '''
        Basic Analysis SuperClass:    Reading main parameters.
    '''
    def __init__(self,dataFile):
        # read in files and pass it into a numpy vector (first line/column removed)
        self.dframe = pd.read_csv(dataFile)
        #pd.DataFrame.from_csv(dataFile)
        #headers = ['GoodsNb','price','CustoNb','PosX_cust','PosY_cust','PosX_stor','PosY_stor','Dist']
        self.DatDescr = self.dframe.describe()
        self.headers = self.DatDescr.columns
        print "---------------------------------------------------------------"
        print "Reading: ", str(dataFile)
        print "---------------------------------------------------------------"
        print self.DatDescr