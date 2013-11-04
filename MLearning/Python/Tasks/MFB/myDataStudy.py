#-------------------------------------------------------------------------------
# Name:        PLotforMFB
# Purpose:
#
# Author:      wuillou8
#
# Created:     04/11/2013
# Copyright:   (c) wuiljai 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#-Std Packages------------------------------------------------------------------
import sys
import numpy as np
from pandas import DataFrame
import pandas as pd


import pylab as P
import matplotlib
matplotlib.rcParams['legend.fancybox'] = True
import matplotlib.pyplot as plt
import math

from matplotlib.backends.backend_pdf import PdfPages
#-My own Packages --------------------------------------------------------------
import myPandaUtilities
import myPlotUtilities
import PlotforMFB
#-------------------------------------------------------------------------------


class DataStudy(PlotforMFB.DataAnalysis):
    # plot Attribute against DayOfWeeks
    def __init__( self, dataFile , mode ): #estedAttr,title,titleCompl, compumode ):
        PlotforMFB.DataAnalysis.__init__( self,dataFile )
        self.mode = myPandaUtilities.FilterInput( mode, ['lineRel'] )

        tmp = self.Study()
        myPandaUtilities.myLazyDispl(tmp)

        for i in tmp.iterrows():
            print 'ici', type(i[1]) , type(i) , i[0] , i[1], type(i[1]) #, i[2] #, i.iloc[0,0], i.loc[1]
            print 'la', i


    def Study(self):
        # Filter out data with a sufficiently big statistics
        _count = []
        _line = []
        _trip = []
        for line in [1,2]: #self.LineIdList:
            for trip in self.TripIdList:
                df = myPandaUtilities.myfilter(self.data,['Line_id',line,'Trip_id',trip]) # ,'DayOfWeek',day])
                tmpDF = df.describe()

                if ( tmpDF['Reven']['count'] > 0 ) :
                    _count.append( tmpDF['Reven']['count'] )
                    _line.append( line )
                    _trip.append( trip )
                    print trip, line


        dframe = pd.DataFrame({ 'count' : _count , 'Line_id' : _line, 'Trip_id' : _trip })
        myPandaUtilities.myLazyDispl(dframe)
        del _count, _line, _trip
        dframe=dframe.sort('count',ascending=False)
        dframe = dframe[ dframe['count'] > 100 ]

        return dframe[ ['Line_id','Trip_id'] ]
