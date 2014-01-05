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
        
        print 'centered data ',0, 100.*self.GetNbCustomsForStore(0,0)/self.N
        print 'centered data ',1, 100.*self.GetNbCustomsForStore(0,1)/self.N
        print 'centered data ',2, 100.*self.GetNbCustomsForStore(0,2)/self.N
        '''        
        for i in range( len(self.coordsStores) ): 
            print i, 100.*self.GetNbCustomsForStore(i)/self.N
        print len( self.coordsCustos )
        '''
        
    def GetCoordsCustomers(self):
        ''' Get customers coordinates '''
        self.dframe['T'] = self.dframe['T'].map(lambda x: x < 3) 
        tmp=self.dframe[[' PosX_cust',' PosY_cust']]
        #tmp = MyPandaUtilities.myfilter( self.dframe,['T',1],[' PosX_cust',' PosY_cust'] )
        GetCoordsCustomers = []
        [ GetCoordsCustomers.append( [tmp[' PosX_cust'][idx], tmp[' PosY_cust'][idx]] ) for idx in range(tmp.shape[0]) ]
        del tmp
        return GetCoordsCustomers
        
    def GetCoordsStores(self):
        ''' Get stores coordinates '''
        tmp = MyPandaUtilities.myfilter( self.dframe,['T',1],[' PosX_stor',' PosY_stor'] )
        GetCoordsStores = []
        [ GetCoordsStores.append( [tmp[' PosX_stor'][idx], tmp[' PosY_stor'][idx]] ) for idx in range(tmp.shape[0]) ]
        del tmp
        return MyPandaUtilities.uniq(GetCoordsStores)
        
        
    def GetNbCustomsForStore(self, storeNb, categ = 0):
        tmp = MyPandaUtilities.myfilter( self.dframe,[' categ',categ,' Nstore',storeNb] )
        return tmp.shape[0]
        
        
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
        #legend.append(' My Store ')

        plt.plot( [tmp[0] for tmp in self.coordsCustos], [tmp[1] for tmp in self.coordsCustos],'*', color='r', markersize=5)
        plt.plot( [tmp[0] for tmp in self.coordsStores], [tmp[1] for tmp in self.coordsStores],'o', color='b', markersize=10)
        #plt.plot( 500, 500,'o', color='r', markersize=10)
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
        