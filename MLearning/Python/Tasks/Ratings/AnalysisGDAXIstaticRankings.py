# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 16:40:19 2013

@author: jair
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


class DataStudy( MyIO.DataAnalysis ):
    '''
        Analysis in DBcustoms
    '''
    def __init__( self, dataFile):
        self.headers = ['Symbol',\
                        'Name',\
                        'Last Trade',\
                        'Change',\
                        'Volume']   
        #MyIO.DataAnalysis.__init__( self, dataFile, self.headers )
        MyIO.DataAnalysis.__init__( self, dataFile, self.headers )
        MyPandaUtilities.myLazyDispl( self.dframe )