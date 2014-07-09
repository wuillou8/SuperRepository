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

class Filtering:
    '''
        Filtering two dataframes one against the other.
    '''
    def __init__( self, _dframe_1, __field_1, _dframe_2, __field_2 ):
        
        
        
