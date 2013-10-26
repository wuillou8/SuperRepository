#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      wuillou8
#
# Created:     18/10/2013
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

#-------------------------------------------------------------------------------

def mydispl_dfr(dframe):
    print dframe.head(2)
    print "...  ...  ...  ...  ...  ..."
    print dframe.tail(2)


class DataAnalysis:
#
#   Basic Analysis Class:
#   Reading main parameters.
       def __init__(self,dataFile):
                # read in files and pass it into a numpy vector (first line/column removed)
                self.data = pd.read_csv(dataFile)
                self.DaysList = np.sort(self.data['DayOfWeek'].unique())
                self.LineIdList = np.sort(self.data['Line_id'].unique())
                self.TripIdList = np.sort(self.data['Trip_id'].unique())
                self.DatDescr = self.data.describe()
                ##self.Ride_load = np.sort(self.data['Ride_load'].unique())

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

            print "self.LineIdList ", self.LineIdList
            print "self.TripIdList ", self.TripIdList

            tmp=self.filter(1)

            days = [float(row[0]) for row in tmp]
            avs = [float(row[1]) for row in tmp]
            vars = [float(row[2]) for row in tmp]

            plt.plot(days, avs, linestyle="dashed", marker="o", color="green")
            plt.plot(days, avs, linestyle="dashed", marker="o", color="green")
            plt.xticks(days)
            plt.xlim(0.5,7.5)
            plt.errorbar(days, avs, yerr=vars, linestyle="None", marker="None", color="green")
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

def main():
    pass

if __name__ == '__main__':
    main()


#myAnalysis = DataAnalysis('q_result2.csv')

dfff = pd.read_csv('q_result2.csv')
DaysList = np.sort(dfff['DayOfWeek'].unique())

df = myPandaUtilities.myfilter( dfff, ["Line_id",1,"Trip_id",1], ['Pax'])
mydispl_dfr(df)


# figure
df = df.cumsum()
df.plot()
plt.legend(loc = 'best')
plt.show()
