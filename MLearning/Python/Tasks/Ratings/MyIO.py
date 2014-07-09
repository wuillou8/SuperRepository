# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 12:44:38 2013

@author: jair
"""
#-Packages --------------------------------------------------------------------
import sys
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
    def __init__( self, dataFile, headers ):
        # read in files and pass it into a numpy vector (first line/column removed)
        # hack because the headers are inconsistent
        self.dframe = pd.read_csv( dataFile, names = headers ) # skiprows=1,

        self.DatDescr = self.dframe.describe()
        self.headers = self.DatDescr.columns
        print "panda version : ",pd.version
        print "---------------------------------------------------------------"
        print "Reading: ", str(dataFile)
        print "---------------------------------------------------------------"
        print self.DatDescr
        print self.headers
