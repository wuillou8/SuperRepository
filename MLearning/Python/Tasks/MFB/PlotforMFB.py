#-------------------------------------------------------------------------------
# Name:        PLotforMFB
# Purpose:
#
# Author:      wuillou8
#
# Created:     28/10/2013
# Copyright:   (c) wuillou8 2013
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
#import PlotforMFB
#-------------------------------------------------------------------------------



################################################################################
##               Utilities                                                    ##
################################################################################

class  const:
    # CONSTANT in Python
    DayShift = 5

def mydispl_dfr(dframe):
    print dframe.head(2)
    print "...  ...  ...  ...  ...  ..."
    print dframe.tail(2)

def WhichPower2(number):
    for i in range(0,7):
        if np.power( 2, i ) == number :
            return int(i + 1)
    print "Error: root not found"
    sys.exit(0)

def GetDays(array):
    GetDays = []
    for n_i in array:
        GetDays.append(WhichPower2(n_i))
    return  [ np.mod(tmp+2,const.DayShift)+1 for tmp in GetDays ]

def fctChgDays(x):
    return np.mod(WhichPower2(x)+const.DayShift,7)+1



################################################################################
##            Classes                                                         ##
################################################################################

class DataAnalysis:
    #   Basic Analysis SuperClass:
    #   Reading main parameters.
    def __init__(self,dataFile):
        # read in files and pass it into a numpy vector (first line/column removed)
        self.data = pd.read_csv(dataFile)
        self.DaysList = np.sort(self.data['DayOfWeek'].unique())
        self.LineIdList = np.sort(self.data['Line_id'].unique())
        self.TripIdList = np.sort(self.data['Trip_id'].unique())
        self.DatDescr = self.data.describe()
        print "--------------------------------------------------------"
        print "Reading: ", str(dataFile)
        print "--------------------------------------------------------"
        print self.DatDescr

    #@classmethod
    #def __FilterInput(self, In, Range):
        ## check Input content against array of expected values
        #if (In not in Range):
        #    sys.exit( "Comput Mode must be in " + str(Range))
        #return In

#-------------------------------------------------------------------------------
#
#   class newPlotforMFB
#-------------------------------------------------------------------------------
class newPlotforMFB(DataAnalysis):
    # plot Attribute against DayOfWeek
    def __init__( self,dataFile,TestedAttr,title,titleCompl, compumode ):
            DataAnalysis.__init__( self,dataFile )
            self.testAttr = myPandaUtilities.FilterInput( TestedAttr, ['Pax','Ride_load','Reven','Rev_km'] ) #['Line_id','Trip_id',] )  # Attribute plotted
            self.title = title # plot title
            self.titleCompl = titleCompl # plot title complement

            self.ComputMode = myPandaUtilities.FilterInput( compumode, ['normal','average','runline'] ) # add histogram

            # we loop against the 1: LineId and 2: TripList
            self.AttrList1 = self.TripIdList
            self.AttrList2 = self.LineIdList

            self.runPlotting()
    #---------------------------------------------------------------------------
    def runPlotting(self):
        if self.ComputMode == 'runline':
            #loop over the lines
            for line in self.LineIdList:
                self._line = line
                self.Init_plot(line)
                ifplotted = self.plotLineVSDays()
                if ifplotted == True:
                    self.Finalize_plot(line)
                plt.clf()
                plt.close()
        else:
            self.Init_plot()
            if self.ComputMode == 'normal':
                self.plotAttrVSDays()
            elif self.ComputMode == 'average':
                self.plotHistoVSDays()
            self.Finalize_plot()
    #---------------------------------------------------------------------------
    def Init_plot(self, line = ''):
        plt.figure()
        params = {'legend.fontsize': 6,
        'legend.linewidth': 2}
        plt.rcParams.update(params)

        plt.title( str(self.titleCompl)+str(line)+' '+str(self.testAttr)+' VS DayOfWeek ' )
        plt.xlim([-0.25,7.5])
        plt.xlabel(' DayOfWeek (1=monday, ... , 7=sunday) ')
        plt.ylabel(str(self.testAttr))
    #---------------------------------------------------------------------------
    def Finalize_plot(self, line = ''):
        pp = PdfPages(str(self.title)+str(self.testAttr)+str(self.ComputMode)+str(line)+'.pdf')
        pp.savefig()
        print ' plot printed as: '+str(self.title)+str(self.testAttr)+str(self.ComputMode)+str(line)+'.pdf'
        pp.close()
        #P.show()
    #---------------------------------------------------------------------------
    #Plot the whole, rough data...
    def plotAttrVSDays( self ):
        legend =[]
        for trip in self.AttrList1:
            for line in self.AttrList2:
                legend.append(str(trip)+'_'+str(line))
                dff = []
                for day in self.DaysList:
                    df = myPandaUtilities.myfilter(self.data,['Line_id',line,'Trip_id',trip,'DayOfWeek',day],['DayOfWeek',str(self.testAttr)]) #'Ride_load'])
                    dff.append(df)

                self.plotGeneration(dff, legend)
   #----------------------------------------------------------------------------
   #Plot the whole, rough data as histogram
    def plotHistoVSDays( self ):
        legend = ''
        dff = []
        for day in self.DaysList:
            df = myPandaUtilities.myfilter(self.data,['DayOfWeek',day],['DayOfWeek',str(self.testAttr)])
            dff.append(df)

        self.plotGeneration(dff, legend)
    #---------------------------------------------------------------------------
    def plotLineVSDays( self ):
        legend =[]
        _line = 1
        isplotted = False
        for trip in self.AttrList1:
            legend.append( str(trip) +'_'+str(self._line) )
            dff = []
            for day in self.DaysList:
                df = myPandaUtilities.myfilter(self.data,['Line_id',self._line,'Trip_id',trip,'DayOfWeek',day],['DayOfWeek',str(self.testAttr)])
                dff.append(df)

            if (pd.concat(dff).shape[0] > 5):
                self.plotGeneration(dff,legend)
                isplotted = True

        return isplotted
    #---------------------------------------------------------------------------
    def plotGeneration( self,dframe, legend ):
        dframe = pd.concat(dframe)
        dframe['DayOfWeek'] = dframe['DayOfWeek'].apply( fctChgDays )
        dframe=dframe.sort( 'DayOfWeek' )\
        # plotting only lines with more than 5 days of data
        if ( (dframe.shape[0] != 0 ) & (len(dframe['DayOfWeek'].unique()) > 5) ):
            dfave = dframe.groupby('DayOfWeek').mean() #
            dfvar = dframe.groupby('DayOfWeek').std() #
            dfave.rename(columns={str(self.testAttr): 'mean'}, inplace=True) #
            dfvar.rename(columns={str(self.testAttr): 'std'}, inplace=True) #
            df = dfave.join(dfvar)
            df = df.fillna(0.00000001)
            plt.errorbar( dframe['DayOfWeek'].unique(), df['mean'], df['std'], linestyle="dashed", marker="o", zorder=1 )
            plt.legend( legend, loc='upper left' )
            plt.draw()
#-------------------------------------------------------------------------------
