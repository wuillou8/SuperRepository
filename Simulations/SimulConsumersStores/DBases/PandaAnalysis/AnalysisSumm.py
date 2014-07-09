# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 12:28:59 2013

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
import AnalysisDBcustoms
import AnalysisDBstores
#------------------------------------------------------------------------------


def plotStoresCustos(analy, printname=''):    
    plt.figure()
    plt.title(' Customers VS Price: '+printname)
    plt.xlim([-0.05,3.05])
    plt.ylim([-1,101])
    plt.xlabel(' Price (store in the center) ')
    plt.ylabel(' Customers Percent ')  
    legend = []
    legend.append('cheap good')
    legend.append('normal good')
    legend.append('expensive good')
    
    store=[]
    store.append( MyPandaUtilities.myfilter( analy, ['store',0], ['price','percent'] ) )
    store.append( MyPandaUtilities.myfilter( analy, ['store',1], ['price','percent'] ) )
    store.append( MyPandaUtilities.myfilter( analy, ['store',2], ['price','percent'] ) )

    plt.vlines(1.,-1,101,color='lightgreen')
    plt.plot( store[0]['price'], store[0]['percent'], 'o', color='b' )
    plt.plot( store[1]['price'], store[1]['percent'], '^', color='c' )
    plt.plot( store[2]['price'], store[2]['percent'], '*', color='r' )
    plt.legend( legend, loc='upper right' )
    
    plt.draw()
    #plt.show()
    '''
    if printname != '':
        with PdfPages( printname ) as pdf:
             pdf.savefig()
             pdf.close()
             plt.close()
        #plt.close()
    return 0
    '''


start = time.clock()

#headers: [u'price', u'store', u'percent']
sum0 = MyIO.DataAnalysis( '../Analysis/summaryDiag.txt' )
sum1 = MyIO.DataAnalysis( '../Analysis/summaryRect.txt' )
sum2 = MyIO.DataAnalysis( '../Analysis/summaryRect.txt' )


plotStoresCustos(sum0.dframe,"Diagonal Config.")
plotStoresCustos(sum1.dframe,"Rectangle Config.")
plotStoresCustos(sum2.dframe,"Random/ordered Config.")