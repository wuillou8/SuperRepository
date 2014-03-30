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

#mini_fct = lambda x: x in

class DataStudy(MyIO.DataAnalysis):
    '''
        Analysis in DBcustoms
    '''
    def __init__( self, dataFile ):
        MyIO.DataAnalysis.__init__( self, dataFile )

        self.coordsCustos = self.GetCoordsCustomers()
        self.coordsStores = self.GetCoordsStores()
        self.plotStoresCustos()
        self.N = len( self.coordsCustos )
        self.Ncategs = len(self.dframe[' categ'].unique())
        
        for categ in range(self.Ncategs):
            print '__centered_data__ ', categ, self.GetNbCustomsForStore( 0, categ )
            #print 'centered data ',1,  self.GetNbCustomsForStore(1,categ)
            #print 'centered data ',2,  self.GetNbCustomsForStore(2,categ)        
        
    def GetCoordsCustomers(self):
        ''' Get customers coordinates '''
        tmp = MyPandaUtilities.myfilter( self.dframe, ['T',1], [' PosX_cust',' PosY_cust'] ) )
        #tmp=self.dframe[[' PosX_cust',' PosY_cust']]
        GetCoordsCustomers = []
        [ GetCoordsCustomers.append( [tmp[' PosX_cust'][idx], tmp[' PosY_cust'][idx]] ) for idx in range(tmp.shape[0]) ]
        del tmp
        return  MyPandaUtilities.uniq( GetCoordsCustomers )
        
    def GetCoordsStores(self):
        ''' Get stores coordinates '''
        tmp = MyPandaUtilities.myfilter( self.dframe, ['T',1], [' PosX_stor',' PosY_stor'] )
        GetCoordsStores = []
        [ GetCoordsStores.append( [tmp[' PosX_stor'][idx], tmp[' PosY_stor'][idx]] ) for idx in range(tmp.shape[0]) ]
        del tmp
        return MyPandaUtilities.uniq( GetCoordsStores )
        
        
    def GetNbCustomsForStore(self, storeNb, categ = 0):
        tmp = MyPandaUtilities.myfilter( self.dframe, [' categ',categ] )
        fact = tmp.shape[0]/self.N
        tmp = MyPandaUtilities.myfilter( self.dframe, [' categ',categ,' Nstore',storeNb] )
        return  100.*tmp.shape[0]/(fact*self.N*1.) #1.* fact * tmp.shape[0]/self.N
        
        
    def plotStoresCustos(self,printname=0):
        
        plt.figure()
        plt.title(' Geographical Distribution ')
        plt.xlim([-10,1010])
        plt.ylim([-10,1010])
        plt.xlabel(' X Coords ')
        plt.ylabel(' Y Coords ')  
        legend = []
        legend.append(' Customers ')
        legend.append(' Stores ')

        plt.plot( [tmp[0] for tmp in self.coordsCustos], [tmp[1] for tmp in self.coordsCustos],'*', color='r', markersize=5)
        plt.plot( [tmp[0] for tmp in self.coordsStores], [tmp[1] for tmp in self.coordsStores],'o', color='b', markersize=10)
        plt.plot( 500, 500,'o', color='r', markersize=15)
        plt.legend( legend, loc='upper right' )
        
        plt.draw()
        #plt.show()
        if printname != 0:
            with PdfPages( 'storesIII.pdf' ) as pdf:
                pdf.savefig()
                pdf.close()
                plt.close()
        #plt.close()
        return 0
        