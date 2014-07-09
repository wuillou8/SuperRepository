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
    def __init__( self, dataFile, mode, CutOff ):
        PlotforMFB.DataAnalysis.__init__( self,dataFile )
        self.CutOff = CutOff
        self.mode = myPandaUtilities.FilterInput( mode, ['lineRel'] )
        self.FilteredList = self.Study()
        myPandaUtilities.myLazyDispl(self.FilteredList)
        
    def Study(self):
        # Filter out data with a sufficiently big statistics
        _count = []
        _line = []
        _trip = []
        for line in [1,2]: #self.LineIdList:
            for trip in self.TripIdList:
                df = myPandaUtilities.myfilter(self.data,['Line_id',line,'Trip_id',trip])
                tmpDF = df.describe()

                if ( tmpDF['Reven']['count'] > 0 ) :
                    _count.append( tmpDF['Reven']['count'] )
                    _line.append( line )
                    _trip.append( trip )

        dframe = pd.DataFrame({ 'count' : _count , 'Line_id' : _line, 'Trip_id' : _trip })
        myPandaUtilities.myLazyDispl(dframe)
        del _count, _line, _trip
        dframe=dframe.sort('count',ascending=False)
        dframe = dframe[ dframe['count'] > self.CutOff ]

        return dframe[ ['Line_id','Trip_id' ] ] 
