# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 16:41:12 2013

@author: jair
"""

#-Std Packages-----------------------------------------------------------------
import sys, time, math
import numpy as np
from pandas import DataFrame
import pandas as pd

#import pylab as P
#import matplotlib
#matplotlib.rcParams['legend.fancybox'] = True
#import matplotlib.pyplot as plt

#from matplotlib.backends.backend_pdf import PdfPages
#-My own Packages -------------------------------------------------------------
import MyPandaUtilities
import MyIO
#------------------------------------------------------------------------------

class DataStudy(MyIO.DataAnalysis):
    '''
        Analysis in stores
    '''
    def __init__( self, dataFile ):
        MyIO.DataAnalysis.__init__( self, dataFile )

        #You can get the values as a list by doing:
        #list(my_dataframe.columns.values)
