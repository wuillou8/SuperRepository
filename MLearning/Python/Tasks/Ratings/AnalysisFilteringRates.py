# -*- coding: utf-8 -*-
"""
Created on Wed Feb 05 14:50:58 2014

@author: wuiljai
"""

#-Std Packages-----------------------------------------------------------------
import sys, time, math
import numpy as np
from pandas import DataFrame
import pandas as pd

import matplotlib
import pylab as P

#import matplotlib
matplotlib.rcParams['legend.fancybox'] = True
import matplotlib.pyplot as plt

from matplotlib.backends.backend_pdf import PdfPages
#-My own Packages -------------------------------------------------------------
import MyPandaUtilities
import MyIO
#------------------------------------------------------------------------------

class Filter:
    '''
        Filtering two dataframes one against the other.
    '''
    def __init__( self, _dframe_1, _dframe_2, __field_ ):
        self.dframe1 = _dframe_1.dframe
        self.dframe2 = _dframe_2.dframe
        
        df1 = pd.Series( map( lambda x : x.upper(), self.dframe1['Name'] ) )
        df2 = pd.Series( map( lambda x : x.upper(), self.dframe2['Name'] ) )

        _matches = df1.isin(df2)
        
        l_Name = []
        for n, i in enumerate(_matches):
            if i:
                print n, i
                l_Name.append( df1[n] )
 
        print 'rates present in both Yahoo and techno ratings : ',l_Name
