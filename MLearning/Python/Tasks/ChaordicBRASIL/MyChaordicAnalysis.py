# -*- coding: utf-8 -*-
"""
Created on Fri May 09 15:30:52 2014

@author: jair
"""
import sys, json 
import numpy as np
import pandas as pd

import MyIO
import MyPandaUtilities
from scipy import stats

###############################################################################
import pylab as P
import matplotlib
matplotlib.rcParams['legend.fancybox'] = True
import matplotlib.pyplot as plt
import math
###############################################################################
def func(x, a, c, d):
    return a*np.exp(-c*x)+d    

class MyChaordicAnalysis( MyIO.DataIO ):
    '''
    Analysis of customers
    '''
    def __init__( self, dataFile ):
        MyIO.DataIO.__init__( self, dataFile )
        self._dframe = self._dframe.sort(['userId'])
        self._dframe = self._dframe.reset_index(drop=True) 
        MyPandaUtilities.myLazyDispl( self._dframe )
        self._users = self._dframe['userId'].unique()
        self._users = np.sort(self._users)
        self._productId = self._dframe['productId'].unique()      
    
    def Analysis( self ):    
        dframeheaders = [ 'userId', 'NbEntries', 'NbMulticlicks', 'Buy?' ] 
        mydf = MyPandaUtilities.myDframe( dframeheaders )
        numMarker = 0
        for n,idx in enumerate( self._users ):
            # speeding up the analysis with a cutoff of 500 and removal of self.dframe els.
            if( self._dframe['userId'].ix[numMarker:numMarker+100].tail(1) != idx ):
                df = MyPandaUtilities.myfilter( self._dframe.ix[numMarker:(numMarker+101)], [ 'userId',idx ], ['buyer', 'productId'] )
            else:
                print 'exceptlong', idx
                df = MyPandaUtilities.myfilter( self._dframe.ix[numMarker:(numMarker+5000)], [ 'userId',idx ], ['buyer', 'productId'] )
            #sys.exit(0)     
            
            numMarker += len(df)
            mydf.Append( [ idx, len(df), \
                             ( len(df) - len( MyPandaUtilities.uniq( df['productId'] ) ) ), \
                                 df.applymap(int)['buyer'].mean() ] )
                        
            #print idx, len(df)
            if( len(df) == 0 ) :
                print idx, df
                print ' ***** ERROR in the Analysis ***** '
                sys.exit(0)

        mydf.DoFrame()
        self._AnalysisDframe = mydf.PDFrame
        del mydf.PDFrame   
        self._AnalysisDframe.to_csv('analysis.dat')


    def Train(self):
        self._AnalysisDframe = pd.DataFrame.from_csv('analysis.dat')
        
        print '---training model1---------------'
        self._train1 = MyPandaUtilities.myDframe( [ 'NbEntries', 'P_Buy', 'P_err', 'stat' ] )
        self._NbEntries = np.sort( self._AnalysisDframe['NbEntries'].unique() )
        for i in self._NbEntries:
            tmp = MyPandaUtilities.myfilter( self._AnalysisDframe , [ 'NbEntries', i ] ,  ['Buy?'] )
            m = tmp['Buy?'].mean()
            sigma = (tmp['Buy?'].var()/len(tmp))**0.5
            if ( len(tmp) == 1 ):
                sigma = 1      
            self._train1.Append( [ i, m, sigma, tmp.shape[0] ] )
        self._train1.DoFrame()
        self._train1 = self._train1.PDFrame
        MyPandaUtilities.myLazyDispl(self._train1)
        print '---training model2---------------'
        self._train2 = MyPandaUtilities.myDframe( ['NbMulticlicks', 'P_Buy', 'P_err', 'stat'] )
        self._NbMultiClicks = np.sort( self._AnalysisDframe['NbMulticlicks'].unique() )
        for i in self._NbMultiClicks:
            tmp = MyPandaUtilities.myfilter( self._AnalysisDframe, [ 'NbMulticlicks', i ],  ['Buy?'] )
            m = tmp['Buy?'].mean()
            sigma = (tmp['Buy?'].var()/len(tmp))**0.5
            if ( len(tmp) == 1 ):
                m= 0.5
                sigma = 1
            self._train2.Append( [ i, m, sigma, tmp.shape[0] ] )
        self._train2.DoFrame()
        self._train2 = self._train2.PDFrame
        MyPandaUtilities.myLazyDispl(self._train2)
        self._train1.to_csv('train1.dat')        
        self._train2.to_csv('train2.dat')
        
        '''
        plt.figure()
        self.plot()
        plt.draw()
        plt.show()
        '''
        #sys.exit(0)        
        
        
    def plot(self):
        '''
        plt.errorbar(x=self._train1['NbEntries'], y=self._train1['P_Buy'], yerr=self._train1['P_err'], fmt='rx') #, xlim=[0,20])
        plt.errorbar(x=self._train2['NbMulticlicks'], y=self._train2['P_Buy'], yerr=self._train2['P_err'], fmt='bx',xuplims = [0,20]) #, xlim=[0,20])
        plt.errorbar()
        
        x=agged[k].index,
        y=agged[k]['CPS_norm_mean'],
        yerr=agged[k]['CPS_norm_std'])
        '''
        self._train1.plot(x='NbEntries', y='P_Buy', style='rx', xlim=[0,50])
        self._train2.plot(x='NbMulticlicks', y='P_Buy', style='bo', xlim=[0,50])
        


    def bla(self):
        from scipy.optimize import curve_fit
        from matplotlib.backends.backend_pdf import PdfPages
        
        CUTOFF1, CUTOFF2 = 40, 30
        #CUTOFF2 = 30
        legend = ['model1 pts', 'model1 fit', 'model2 pts', 'model2 fit']
        #Model 1, fit & plot
        tmp1 = pd.DataFrame.from_csv('train1.dat')
        tmp1 = tmp1[['NbEntries','P_Buy','P_err','stat']]
        tmp1 = tmp1[tmp1['NbEntries'] < CUTOFF1+1]
        x, y = np.array( [ i for i in tmp1['NbEntries'] ] ), 1-np.array( [ i for i in tmp1['P_Buy'] ] )
        err = np.array( [ i for i in tmp1['P_err'] ] )
        self._popt1, pcov1 = curve_fit(func, x, y, p0=(0.9, 0.25, 0.2), sigma = err)
        xx = np.linspace(0, max(CUTOFF1+1, CUTOFF2+1), 100)
        yy = func(xx, *self._popt1)
    
        P.plot(x, 1-y, 'ro')
        P.errorbar(x,1-y,yerr=err)
        P.plot(xx, 1-yy)
        
        #Model 2, fit & plot
        tmp2 = pd.DataFrame.from_csv('train2.dat')
        tmp2 = tmp2[['NbMulticlicks','P_Buy','P_err','stat']]
        tmp2 = tmp2[tmp2['NbMulticlicks'] < CUTOFF2+1]      
        x, y = np.array( [ i for i in tmp2['NbMulticlicks'] ] ), 1-np.array( [ i for i in tmp2['P_Buy'] ] )
        err = np.array( [ i for i in tmp2['P_err'] ] )
        self._popt2, pcov2 = curve_fit(func, x, y, p0=(0.9, 0.25, 0.2), sigma = err)
        xx = np.linspace(0, max(CUTOFF1+1, CUTOFF2+1), 100)
        yy = func(xx, *self._popt2)
    
        P.plot(x, 1-y, 'bo')
        P.errorbar(x,1-y,yerr=err)
        P.plot(xx, 1-yy)
        P.legend(legend, loc='lower right')
        #p=PdfPages('file.pdf')
        #p.savefig()
        #p.close()
        print '1', self._popt1
        print '2', self._popt2
        
    def ModelConstr(self):
        self._popt1 = [ 0.81228557,  0.26642522,  0.22705101]
        self._popt2 = [ 0.55058917,  0.47290533,  0.24460433]
        
        self._AnalysisDframe = pd.DataFrame.from_csv('analysis.dat')
        self._users = self._AnalysisDframe['userId'].unique()
        for idx in self._users:
            #tmp = self._AnalysisDframe[self._AnalysisDframe['userId'] == idx]
            nNentries = np.array( MyPandaUtilities.myfilter(self._AnalysisDframe, ['userId', idx], ['NbEntries'] ))[0][0]
            nMulticlicks = np.array( MyPandaUtilities.myfilter(self._AnalysisDframe, ['userId', idx], ['NbMulticlicks'] ))[0][0]

            print idx, func(nNentries, *self._popt1)
            print idx, func(nMulticlicks, *self._popt2)

    def fit(self):
        from scipy.optimize import curve_fit
        #from P import *
        self._AnalysisDframe = pd.DataFrame.from_csv('analysis.dat')
        tmp = self._AnalysisDframe[['NbEntries','Buy?']]
        MyPandaUtilities.myLazyDispl(tmp)
        
        
        print type(tmp['NbEntries'])
        
        #for i in tmp['NbEntries']:
        #    print i
            
        x = np.array( [ i for i in tmp['NbEntries'] ] )
        y = np.array( [ i for i in tmp['Buy?'] ] )
        y = 1-y
        
        popt, pcov = curve_fit(func, x, y, p0=(1, 1e-6, 0.1))
        print popt
        print pcov
        
        xx = np.linspace(0, 5000, 10)
        yy = func(xx, *popt)

        P.plot(x, 1-y, 'ko') #, xlim=[0,50])
        P.plot(xx, 1-yy) #, xlim=[0,50])   
        
        self._train1.plot(x='NbEntries', y='P_Buy', style='rx', xlim=[0,50])
        '''
        from scipy.optimize import curve_fit        
        x = np.array([399.75, 989.25, 1578.75, 2168.25, 2757.75, 3347.25, 3936.75, 4526.25, 5115.75, 5705.25])
        y = np.array([109,62,39,13,10,4,2,0,1,2])  
        popt, pcov = curve_fit(func, x, y)
        '''      
        
    def fit2(self):
        from scipy.optimize import curve_fit
        #from P import *
        tmp1 = pd.DataFrame.from_csv('train1.dat')
        tmp1 = tmp1[['NbEntries','P_Buy','P_err','stat']]
        tmp1 = tmp1[tmp1['NbEntries'] < 51]
        
        tmp2 = pd.DataFrame.from_csv('train2.dat')
        tmp2 = tmp2[['NbMulticlicks','P_Buy','P_err','stat']]
        tmp2 = tmp2[tmp2['NbMulticlicks'] < 41]       
        
        MyPandaUtilities.myLazyDispl(tmp1)
        MyPandaUtilities.myLazyDispl(tmp2)
        '''
        x = np.array( [ i for i in tmp1['NbEntries'] ] )
        print x
        y = np.array( [ i for i in tmp1['P_Buy'] ] )
        y = 1-y
        '''
        x = np.array( range(50) )
        y = np.array( range(50) )
        print y          
        err = np.array( [ i for i in tmp1['P_err'] ] )
        print err
        print len(x), len(y)
        P.plot(x, y, 'ko')
        #P.plot(x, y, 'ko')
        #P.show()
        print 'fin'
        #sys.exit()
        #popt, pcov = curve_fit(func, x, y, p0=(1, 1e-6, 0.1), sigma = err)
        #print popt
        sys.exit()
    def AnalysisOutput(self):
        for i in self._AnalysisDframe:
            print i
        dataFile = 'outputtest.json'
        ls = []
  
        for i in self._AnalysisDframe:
            print i
            ls.append( {'4': 5, '6': 7} )
            
        f = open( dataFile, 'w' )
        j = json.dumps( ls )
        print >> f, j
        
        for i in xrange(10):
            print >> f, json.dumps( {'4': 5, '6': 7} )   
        f.close()        