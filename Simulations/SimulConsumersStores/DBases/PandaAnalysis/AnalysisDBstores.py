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

import matplotlib
import pylab as P

matplotlib.rcParams['legend.fancybox'] = True
import matplotlib.pyplot as plt

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
        print "store", self.headers
        MyPandaUtilities.myLazyDispl(self.dframe)
        self.coordsStores = self.GetCoordsStores()
        print self.coordsStores
        self.plotStoresCustos()

    def GetCoordsStores(self):
        ''' Get customers coordinates '''
        tmp = MyPandaUtilities.myfilter( self.dframe,['T',1],[' PosX_stor',' PosY_stor'] )
        MyPandaUtilities.myLazyDispl(tmp)
        GetCoordsStores = []
        [ GetCoordsStores.append( [tmp[' PosX_stor'][idx], tmp[' PosY_stor'][idx]] ) for idx in range(tmp.shape[0]) ]
        del tmp
        return MyPandaUtilities.uniq(GetCoordsStores)
        
        
    def plotStoresCustos(self):
        
        plt.figure()
        plt.title(' Geographical distribution ')
        plt.xlim([0,1000])
        plt.ylim([0,1000])
        plt.xlabel(' X coordinates ')
        plt.ylabel(' Y coordinates ')        
        
        plt.plot( [tmp[0] for tmp in self.coordsStores], [tmp[1] for tmp in self.coordsStores], 'o', color='k')
        plt.draw()
        plt.show()
        return 0