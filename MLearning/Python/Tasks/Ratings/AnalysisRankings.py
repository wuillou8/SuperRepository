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
    def __init__( self, dataFile ):
        self.headers = ['area_id','field_id','sub_field_id','oem_type',\
                        'rank',\
                        'Name',\
                        'FAI',\
                        'MC',\
                        'TR',\
                        'PS',\
                        'FC',\
                        'PC',\
                        'is_berlin']
                        
        MyIO.DataAnalysis.__init__( self, dataFile, self.headers )
        
        print 'area_id', self.dframe[u'area_id']
        print 'field_id', self.dframe[u'field_id']
        print 'sub_field_id', self.dframe[u'sub_field_id']
        print 'oem_type', self.dframe[u'oem_type']
        print 'rank', self.dframe[u'rank']
        print 'OEM', self.dframe[u'Name'] #[u'OEM']
        '''
        print 'FAI', self.dframe[u'FAI']
        print 'MC', self.dframe[u'MC']
        print 'TR', self.dframe[u'TR']
        print 'PS', self.dframe[u'PS']
        print 'FC', self.dframe[u'FC']
        print 'PC', self.dframe[u'PC']
        print 'is_berlin', self.dframe[u'is_berlin']
        '''
        
        MyPandaUtilities.myLazyDispl( self.dframe )
  
