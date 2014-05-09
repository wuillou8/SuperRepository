# -*- coding: utf-8 -*-
"""
Created on Fri May 09 15:30:52 2014

@author: jair
"""
import pandas as pd
import json

import MyIO
import MyPandaUtilities


class MyChaordicAnalysis( MyIO.DataIO ):
    '''
    Analysis in DBcustoms
    '''
    def __init__( self, dataFile ):
        MyIO.DataIO.__init__( self, dataFile )
        MyPandaUtilities.myLazyDispl( self.dframe )
        print self.headers
        print type(self.dframe['userId'])
        
        self.users = self.dframe['userId'].unique()
        print 'lem:', len(self.users)
    
    def Analysis(self):        
        #df = MyPandaUtilities.myfilter(self.dframe,['userId']) #,line,'Trip_id',trip])
        #for i in 