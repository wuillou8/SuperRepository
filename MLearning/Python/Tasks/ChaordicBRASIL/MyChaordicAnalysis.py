# -*- coding: utf-8 -*-
"""
Created on Fri May 09 15:30:52 2014

@author: jair
"""

import MyIO
import MyPandaUtilities


class MyChaordicAnalysis( MyIO.DataIO ):
    '''
    Analysis of customers
    '''
    def __init__( self, dataFile ):
        MyIO.DataIO.__init__( self, dataFile )
        MyPandaUtilities.myLazyDispl( self.dframe )
        self.users = self.dframe['userId'].unique()

    
    def Analysis(self):    
        dframeheaders = [ 'userId','NbEntries','PercentBuy' ] 
        mydf = MyPandaUtilities.myDframe( dframeheaders )
        for n,idx in enumerate(self.users):
            df = MyPandaUtilities.myfilter(self.dframe,['userId',idx],['buyer'])   
            mydf.Append( [ idx, len(df), df.applymap(int)['buyer'].mean() ] )
        mydf.DoFrame()
        
	print '-----Quick Summary------'
        print mydf.PDFrame.head()
        print mydf.PDFrame.tail()
        print '------------------------'
        self.AnalysisDframe = mydf.PDFrame
        del mydf.PDFrame
        return 1
    
    
    def AnalysisOutput(self):
        #for i in self.users:
        for i in self.AnalysisDframe:
            print i
        #print json.dumps({'4': 5, '6': 7})
        
        
