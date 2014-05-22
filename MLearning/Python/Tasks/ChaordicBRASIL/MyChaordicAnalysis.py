"""
@author: jair
"""
import sys, os
import numpy as np
import pandas as pd
import pylab as P
import matplotlib
matplotlib.rcParams['legend.fancybox'] = True
from matplotlib.backends.backend_pdf import PdfPages
from scipy.optimize import curve_fit
#------------------------------------------------------------------------------
import MyIO
import MyPandaUtilities
import ROC_AUC
#------------------------------------------------------------------------------

def func(x, a, b, c):
    '''
    fit function for models 1 & 2
    1 - exponential decay
    '''
    return 1. - a*np.exp(-b*x) + c

def funConst(x, a): #, b):    
    '''
    fitted const function for model 3
    '''
    ls = []
    for i in x:
        ls.append(a)
    return np.array( ls )
    
def funStep(x, threshold, a, b):
    '''
    fitted step funct for model 3
    '''
    if (x <= threshold):
        return a
    else:
        return b
#------------------------------------------------------------------------------
    
    
class MyChaordicAnalysis( MyIO.DataIO ):
    '''
    Analysis of customers
    '''
    def __init__( self, dataFile, outfile ):
        MyIO.DataIO.__init__( self, dataFile, outfile )
        self._dframe = self._dframe.sort(['userId'])
        self._dframe = self._dframe.reset_index(drop=True) 
        self._users = self._dframe['userId'].unique()
        self._users = np.sort(self._users) 
        #MyPandaUtilities.myLazyDispl( self._dframe )
    
    def Analysis( self, path_analysis ): 
        if os.path.isfile(path_analysis):
            try:
                print 'read file: ', path_analysis
                self._AnalysisDframe = pd.DataFrame.from_csv(path_analysis)
            except OSError:
                print 'reading pbm: ', path_analysis      
        else:
            print 'run the analysis and write it in: ', path_analysis
            dframeheaders = [ 'userId', 'NbEntries', 'NbMulticlicks', 'Buy?' ] 
            mydf = MyPandaUtilities.myDframe( dframeheaders )
            numMarker = 0
            for n,idx in enumerate( self._users ):
            # speeding up the analysis with a cutoff of 500 and removal of self.dframe els.
                if( self._dframe['userId'].ix[numMarker:numMarker+100].tail(1) != idx ):
                    df = MyPandaUtilities.myfilter( self._dframe.ix[numMarker:(numMarker+101)], \
                                    [ 'userId',idx ], ['buyer', 'productId'] )
                else:
                    #print 'exceptlong', idx
                    df = MyPandaUtilities.myfilter( self._dframe.ix[numMarker:(numMarker+5000)], \
                                    [ 'userId',idx ], ['buyer', 'productId'] )  
            
                numMarker += len(df)
                mydf.Append( [ idx, len(df), \
                                 ( len(df) - len( MyPandaUtilities.uniq( df['productId'] ) ) ), \
                                     df.applymap(int)['buyer'].mean() ] )
                        
                if( len(df) == 0 ) :
                    print idx, df
                    print ' ***** ERROR in the Analysis ***** '
                    sys.exit(0)

            mydf.DoFrame()
            self._AnalysisDframe = mydf.PDFrame
            del mydf.PDFrame   
            #store analysis            
            try:
                self._AnalysisDframe.to_csv(path_analysis)
            except OSError:
                print 'printing pbm: ', path_analysis

    def Preprocessing(self, pathmodel1, pathmodel2, pathmodel3):
        #if analysis already done, read files
        if ( os.path.isfile(pathmodel1) and os.path.isfile(pathmodel2) and os.path.isfile(pathmodel3) ):
            try:
                self._train1 = pd.DataFrame.from_csv(pathmodel1)        
                self._train2 = pd.DataFrame.from_csv(pathmodel2)
                self._train3 = pd.DataFrame.from_csv(pathmodel3)
            except OSError:
                print 'reading pbm: ', pathmodel1, pathmodel2, pathmodel3
        else:
            #do analysis
            print '---train model1---------------'
            self._train1 = MyPandaUtilities.myDframe( [ 'NbEntries', 'P_Buy', 'P_err', 'stat' ] )
            self._NbEntries = np.sort( self._AnalysisDframe['NbEntries'].unique() )
            for i in self._NbEntries:
                tmp = MyPandaUtilities.myfilter( self._AnalysisDframe , \
                                                [ 'NbEntries', i ] ,  ['Buy?'] )
                m = tmp['Buy?'].mean()
                sigma = (tmp['Buy?'].var()/len(tmp))**0.5
                if ( len(tmp) == 1 ):
                    m, sigma = 0.5, 1 #data with unique el...
                self._train1.Append( [ i, m, sigma, tmp.shape[0] ] )
            self._train1.DoFrame()
            self._train1 = self._train1.PDFrame
            #MyPandaUtilities.myLazyDispl(self._train1)
        
            print '---train model2---------------------------------------------'
            self._train2 = MyPandaUtilities.myDframe( ['NbMulticlicks', 'P_Buy', 'P_err', 'stat'] )
            self._NbMultiClicks = np.sort( self._AnalysisDframe['NbMulticlicks'].unique() )
            for i in self._NbMultiClicks:
                tmp = MyPandaUtilities.myfilter( self._AnalysisDframe, [ 'NbMulticlicks', i ],  ['Buy?'] )
                m = tmp['Buy?'].mean()
                sigma = (tmp['Buy?'].var()/len(tmp))**0.5
                if ( len(tmp) == 1 ):
                    m, sigma = 0.5, 1 #data  with unique el...
                self._train2.Append( [ i, m, sigma, tmp.shape[0] ] )
            self._train2.DoFrame()
            self._train2 = self._train2.PDFrame
            #MyPandaUtilities.myLazyDispl(self._train2)
        
            print '---train model3------------------------------------------------'
            self._train3 = MyPandaUtilities.myDframe( ['NbMulticlicks/NbEntries', 'P_Buy', 'P_err', 'stat'] )
            self._users = self._AnalysisDframe['userId']
            Nstat, ls, res = 1000, [], []
            for n,idx in enumerate(xrange(len(self._users))):
                tmp = self._AnalysisDframe.ix[n]
                ls.append( [ 1.*tmp['NbMulticlicks']/tmp['NbEntries'], tmp['Buy?']] )
                ls.sort( key=lambda x: x[0] )
        
            for i in range(len(self._users)/Nstat):
                tmp = ls[(i*Nstat):(i*Nstat+Nstat)]
                tmp1 , tmp2 =  [ i[0] for i in tmp ], [ i[1] for i in tmp ]
                self._train3.Append( [ np.average(tmp1), np.average(tmp2) , np.std(tmp2), len(tmp) ] )
            self._train3.DoFrame()
            self._train3 = self._train3.PDFrame
            #MyPandaUtilities.myLazyDispl(self._train3)
        
            try:
                self._train1.to_csv(pathmodel1)        
                self._train2.to_csv(pathmodel2)
                self._train3.to_csv(pathmodel3)
            except OSError:
                print 'printing pbm: ', pathmodel1, pathmodel2, pathmodel3
                
    def fitting(self, printing):
        '''
        function fitting 3 models, as I kept it general
        the models listed can be printed:
            i.e. 'Model3' or ['Model1','Model2'] prints resp. Model3 or Model1 & Model2
        '''
        #cutoff for curve_fit convergence
        CUTOFF1, CUTOFF2 = 40, 30
        tmp1, tmp2, tmp3 = self._train1, self._train2, self._train3
        
        #Model 1, fit & plot---------------------------------------------------            
        tmp1 = tmp1[['NbEntries','P_Buy','P_err','stat']]
        tmp1 = tmp1[tmp1['NbEntries'] < CUTOFF1+1]
        x, y, err = np.array( [ i for i in tmp1['NbEntries'] ] ), \
                    np.array( [ i for i in tmp1['P_Buy'] ] ), \
                        np.array( [ i for i in tmp1['P_err'] ] )
        self._popt1, pcov1 = curve_fit(func, x, y, p0=(0.9, 0.25, 0.2), sigma = err)

        if ( 'Model1' in printing ):
            xx = np.linspace(0, CUTOFF1+1, 100)
            yy = func(xx, *self._popt1)
            legend = ['Model & Error', 'exponential fit']
            P.title('Fit Model 1: Nb total Clicks')
            P.xlabel('Nb total Clicks')
            P.ylabel('Buy Probability')
            P.errorbar(x,y,yerr=err)
            P.plot(xx, yy)
            self.plotprint(legend, '../FIG/model1.pdf')

        #Model 2, fit & plot---------------------------------------------------
        tmp2 = tmp2[['NbMulticlicks','P_Buy','P_err','stat']]
        tmp2 = tmp2[tmp2['NbMulticlicks'] < CUTOFF2+1]      
        x, y, err = np.array( [ i for i in tmp2['NbMulticlicks'] ] ), \
                        np.array( [ i for i in tmp2['P_Buy'] ] ), \
                            np.array( [ i for i in tmp2['P_err'] ] )
        self._popt2, pcov2 = curve_fit(func, x, y, p0=(0.9, 0.25, 0.2), sigma = err)
  
        if ( 'Model2' in printing ):
            xx = np.linspace(0, CUTOFF2+1, 100)
            yy = func(xx, *self._popt2)
            
            legend = ['Model & Error', 'exponential fit']
            P.title('Fit Model 2: Nb identical Clicks')
            P.xlabel('Nb identical Clicks')
            P.ylabel('Buy Probability')
            P.errorbar(x,y,yerr=err)
            P.plot(xx, yy)
            self.plotprint(legend, '../FIG/model2.pdf')
        
        #Model 3, fit & plot---------------------------------------------------
        tmp3 = tmp3[['NbMulticlicks/NbEntries','P_Buy','P_err','stat']]
        #extracting two distinct behaviours identified
        tmp3m = tmp3[ tmp3['NbMulticlicks/NbEntries'] < 0.002 ] 
        tmp3p = tmp3[ tmp3['NbMulticlicks/NbEntries'] > 0.002 ]
        x, y, err = np.array( [ i for i in tmp3['NbMulticlicks/NbEntries'] ] ), \
                        np.array( [ i for i in tmp3['P_Buy'] ] ), \
                            np.array( [ i for i in tmp3['P_err'] ] )
        tm, tp = np.array( tmp3m['P_Buy'] ), np.array( tmp3p['P_Buy'] )
        self._popt3 = [tm.mean(), tp.mean()]
        
        if ( 'Model3' in printing ):
            xx = np.linspace(0., 1., 1000)
            yy1, yy2 = funConst(xx, tm.mean()), funConst(xx, tp.mean())
            legend = ['Model & Error', 'const fit 1', 'const fit 2']
            P.title('Fit Model 3: Nb identical Clicks/Nb total Clicks')
            P.xlabel('Nb identical Clicks/Nb total Clicks')
            P.ylabel('Buy Probability')
            P.errorbar(x,y,yerr=err)
            P.plot(xx, yy1)
            P.plot(xx, yy2)
            self.plotprint(legend, '../FIG/model3.pdf')

        #print 'fitted model 1', self._popt1
        #print 'fitted model 2', self._popt2
        #print 'fitted model 3', self._popt3
        '''        
        values I found:
            self._popt1 = [ 0.81228557,  0.26642522,  0.22705101]
            self._popt2 = [ 0.55058917,  0.47290533,  0.24460433]
            self._popt3, threshold = [0.20450724637681153, 0.51254838709677408], 0.002
        '''     
        
    def ModelConstr(self, alpha1, alpha2):
        p, q = alpha1, 1. - alpha2
        a1, a2, a3 = q*p, q*(1-p), 1. - q

        self._users = self._AnalysisDframe['userId']
        self._Pmean = self._AnalysisDframe['Buy?'].mean()
        ls, LL = [], len(self._users)
       
        for n,idx in enumerate(xrange(LL)):
            tmp = self._AnalysisDframe.ix[n]
            #models 1 & 2 & 3
            tm1 = func(tmp['NbEntries'], *self._popt1)
            tm2 = func(tmp['NbMulticlicks'], *self._popt2)
            tm3 = funStep( 1.*tmp['NbMulticlicks']/tmp['NbEntries'], 0.002, *self._popt3) 
            ls.append( [ tm1 ,tm2, tm3, tmp['Buy?'] ] )
        
        #Renormalisation step (corr for model deviations)
        c_f1 = self._Pmean/np.mean( [i[0] for i in ls ] )
        c_f2 = self._Pmean/np.mean( [i[1] for i in ls ] )
        c_f3 = self._Pmean/np.mean( [i[2] for i in ls ] )
        #Linear combs. performed the best as well as 100% model 1
        return [ [ (a1*i[0]*c_f1 + a2*i[1]*c_f2 + a3*i[2]*c_f3), i[3] ] for i in ls ]

    def RunROCAUConModel(self, printing = 'NO'):
        '''
        pass no arguments or one or two, for instance ['YES','OUT']
        '''
        if (not printing in ['NO','YES','OUT']):
            print 'wrong key word passed in RunROCAUConModel::printing'
            sys.exit(0)
                
        alpha1, alpha2 = 1., 0.
        ls = self.ModelConstr(alpha1, alpha2)
        
        if ( 'OUT' in printing ): 
            #correction for enforcing 30% of bought items, 
            #but it should be the same in term of matching percentage.
            corr = 0 #self._Pmean - np.mean( [int(round(i[0])) for i in ls ] )
            tmp = []
            for n, idx in enumerate(self._users):
                tmp.append( [ str(int(round(ls[n][0]+corr))), idx ] )
            self.printout(tmp)
                
        a_roc = ROC_AUC.ROC_AUC_1(ls)
        a_roc.counting()
        a_roc.auc()
        print 'roc AUC area (trapezoid integration)', \
                np.trapz([tm[1] for tm in a_roc.curve], x=[tm[0] for tm in a_roc.curve]) 
        
        if ( 'YES' in printing ):
            xx = np.linspace(0, 1, 10000)
            legend = ['My Model 1', 'Random Model']
            P.title('ROC AUC curve: Surface 0.74')
            P.xlabel('True Pos rate')
            P.ylabel('False Pos rate')
            P.plot([tm[0] for tm in a_roc.curve],[tm[1] for tm in a_roc.curve ])
            P.plot(xx,xx)
            self.plotprint(legend, '../FIG/rocAUC.pdf')        
        
    def plotprint(self, legend, path):
            try:            
                P.legend(legend, loc='lower right')
                p=PdfPages(path)
                p.savefig()
                p.close()
            except Exception:
                print 'plotting pbm'
