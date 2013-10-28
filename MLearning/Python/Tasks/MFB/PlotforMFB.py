#-------------------------------------------------------------------------------
# Name:        PLotforMFB
# Purpose:
#
# Author:      wuillou8
#
# Created:     28/10/2013
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
#import PlotforMFB
#-------------------------------------------------------------------------------



################################################################################
##               Utilities                                                    ##
################################################################################

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

class  const:
    DayShift = 5

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
#
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
                print "Reading in: ", str(dataFile)
                print "--------------------------------------------------------"
                print self.DatDescr


#########################################################################

class PlotforMFB(DataAnalysis):
    # plot Attribute against DayOfWeek
    def __init__(self,dataFile,list1, title):
            DataAnalysis.__init__(self,dataFile)
            self.title = title
            self.AttrList1 = np.sort(self.data[list1].unique())
            self.AttrList2 = np.sort(self.data['Line_id'].unique())

            self.Init_plot()
            
	    self.ComputMode = 0 # 0 or 1 or 2
            if self.ComputMode == 0:
                self.plotAttrVSDays()
            elif self.ComputMode == 1:
                self.plot2AttrVSDays() #AttrList)
            elif self.ComputMode == 2:
                self.plot2AttrVSDaysHisto()

            self.Finalize_plot()

    #---------------------------------------------------------------------------
    def Init_plot(self):
        plt.figure()
        params = {'legend.fontsize': 6,
        'legend.linewidth': 2}
        plt.rcParams.update(params)

        plt.title(' Ride_load vs DayOfWeek ' )
        plt.xlim([-0.25,7.5])
        plt.xlabel(' DayOfWeek (1=monday, ... , 7=sunday) ')
        plt.ylabel(' Ride_load ')

    #---------------------------------------------------------------------------
    def plotAttrVSDays( self ):
        tmp0 =[]
        for tmp in self.AttrList1:
            tmp0.append(str(tmp)+'_'+str(self._line))
            dff = []
            for tmp1 in self.DaysList:
                df = myPandaUtilities.myfilter(self.data,['Line_id',self._line,'Trip_id',tmp,'DayOfWeek',tmp1],['DayOfWeek','Ride_load'])
                dff.append(df)

            dff = pd.concat(dff)
            dff['DayOfWeek'] = dff['DayOfWeek'].apply( fctChgDays )
            dff=dff.sort('DayOfWeek')
            if (dff.shape[0] != 0) & (len(dff['DayOfWeek'].unique()) > 5):
                dfave = dff.groupby('DayOfWeek').mean() #
                dfvar = dff.groupby('DayOfWeek').std() #
                dfave.rename(columns={'Ride_load': 'mean'}, inplace=True) #
                dfvar.rename(columns={'Ride_load': 'std'}, inplace=True) #
                df = dfave.join(dfvar)
                df = df.fillna(0.00000001)
                print ' ---df--- ', df, dff['DayOfWeek'].unique()
                print "tmp0=============", tmp0
                plt.errorbar( dff['DayOfWeek'].unique(), df['mean'], df['std'], linestyle="dashed", marker="o",zorder=1)
                plt.legend(tmp0, loc='upper left') #'lower left'
                plt.draw()

    #---------------------------------------------------------------------------
    def plot2AttrVSDays( self ):
        tmp0 =[]
        for tmp in self.AttrList1:
            for line in self.AttrList2:
                tmp0.append(str(tmp)+'_'+str(line))
                dff = []
                for tmp1 in self.DaysList:
                    df = myPandaUtilities.myfilter(self.data,['Line_id',line,'Trip_id',tmp,'DayOfWeek',tmp1],['DayOfWeek','Ride_load'])
                    dff.append(df)

                dff = pd.concat(dff)
                dff['DayOfWeek'] = dff['DayOfWeek'].apply( fctChgDays )
                dff=dff.sort('DayOfWeek')
                if (dff.shape[0] != 0) & (len(dff['DayOfWeek'].unique()) > 5):
                    dfave = dff.groupby('DayOfWeek').mean() #
                    dfvar = dff.groupby('DayOfWeek').std() #
                    dfave.rename(columns={'Ride_load': 'mean'}, inplace=True) #
                    dfvar.rename(columns={'Ride_load': 'std'}, inplace=True) #
                    df = dfave.join(dfvar)
                    df = df.fillna(0.00000001)
                    plt.errorbar( dff['DayOfWeek'].unique(), df['mean'], df['std'], linestyle="dashed", marker="o",zorder=1)
                    plt.legend(tmp0, loc='upper left') #'lower left'
                    plt.draw()

                    #print tmp, line

    #---------------------------------------------------------------------------
    #def analysisData( self ):
    def plot2AttrVSDaysHisto( self ):
        dff = []
        for tmp1 in self.DaysList:
            df = myPandaUtilities.myfilter(self.data,['DayOfWeek',tmp1],['DayOfWeek','Ride_load'])
            dff.append(df)

        dff = pd.concat(dff)
        dff['DayOfWeek'] = dff['DayOfWeek'].apply( fctChgDays )
        dff=dff.sort('DayOfWeek')
        myPandaUtilities.myLazyDispl(dff)
        dfave = dff.groupby('DayOfWeek').mean() #
        dfvar = dff.groupby('DayOfWeek').std() #
        dfave.rename(columns={'Ride_load': 'mean'}, inplace=True) #
        dfvar.rename(columns={'Ride_load': 'std'}, inplace=True) #
        df = dfave.join(dfvar)
        df = df.fillna(0.00000001)
        myPandaUtilities.myLazyDispl(df) #Dframe)
        print df.head(10)
        plt.errorbar( dff['DayOfWeek'].unique(), df['mean'], df['std'], linestyle="dashed", marker="o",zorder=1)
        plt.legend(loc='upper left') #'lower left'
        plt.draw()

    #---------------------------------------------------------------------------
    def Finalize_plot(self):
        pp = PdfPages(str(self.title)+str(self._line)+'.pdf') #'multipage.pdf')
        pp.savefig()
        pp.close()
        P.show()


################################################################################
#	OLD Classes
################################################################################



class LoadQuestionAnalysis(DataAnalysis):

        def __init__(self,dataFile):
                #super(BayesSimple,self).__init__(testsample,featsSub)
                DataAnalysis.__init__(self,dataFile)
                self.rideLoad = np.sort(self.data['Ride_load'])
                x = self.rideLoad
                n, bins, patches = P.hist(x, 50, normed=1, histtype='stepfilled')
                #fig = P.setp(patches, 'facecolor', 'grey', 'alpha', 0.75)
                fig = P.setp(patches)
                P.title('ride_load Distribution')
                P.xlabel('ride_load')
                P.ylabel('% distribution')
                fig = P.draw() #figure()
                pp = PdfPages('foo.pdf')
                pp.savefig(fig)
                P.show()


def update_line(hl, new_data):
    hl.set_xdata(numpy.append(hl.get_xdata(), new_data))
    hl.set_ydata(numpy.append(hl.get_ydata(), new_data))
    plt.draw()


class PaxLAnalysisine(DataAnalysis):

    def __init__(self,dataFile):
            DataAnalysis.__init__(self,dataFile)

            tmp=self.filter(1)

            days = [float(row[0]) for row in tmp]
            avs = [float(row[1]) for row in tmp]
            vars = [float(row[2]) for row in tmp]

            plt.plot(days, avs, linestyle="dashed")#, marker="o") #, color="green")
            plt.plot(days, avs, linestyle="dashed")#, marker="o") #, color="green")

            plt.xticks(days)
            plt.xlim(0.5,7.5)
            plt.errorbar(days, avs, yerr=vars, linestyle="None", marker="None") #, color="green")
            pl1=plt.draw()
            P.show(pl1)
            pl1 = self.run()
            P.show(pl1)

    def filter(self, lineId):
        tmp = list()
        for n_days,days in enumerate(self.DaysList):
            val = self.data[(self.data.Trip_id==1) & (self.data.Line_id==lineId) & (self.data.DayOfWeek==days)]['Ride_load']
            print "val.L", val
            av = np.average(val)
            var = np.average((val-av)**2)
            tmp.append([n_days+1,av,math.sqrt(var)])
        return tmp

    def run(self):
        t_mp = list()
        days = list()
        avs = list()

        hl, = plt.plot([], [])
        for Num, line in enumerate([1,2]):
            print Num, line
            P.figure(Num)
            P.title('ride_load Distribution'+str(Num+1))
            P.xlabel('ride_load')
            P.ylabel('% distribution')
            tmp = self.filter(line)
            days.append([float(row[0]) for row in tmp])
            avs.append([float(row[1]) for row in tmp])
            vars = [float(row[2]) for row in tmp]

            plt.plot(days, avs, linestyle="dashed", marker="o", color="green")
            #plt.xticks(days)
            #plt.xlim(0.5,7.5)
            #plt.errorbar(days, avs, yerr=vars, linestyle="None", marker="None", color="green")
        return plt.draw()
