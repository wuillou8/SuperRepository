#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      wuiljai
#
# Created:     18/10/2013
# Copyright:   (c) wuiljai 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import sys
import numpy as np
import pandas as pd
import pylab as P

import matplotlib
matplotlib.rcParams['legend.fancybox'] = True
import matplotlib.pyplot as plt
import math


from matplotlib.backends.backend_pdf import PdfPages

def plotGraph(X,Y):
      fig = plt.figure()
      ### Plotting arrangements ###
      return fig



class DataAnalysis:
#
#   Basic Analysis Class:
#   Reading main parameters.
       def __init__(self,dataFile):
                # read in files and pass it into a numpy vector (first line/column removed)
                self.data = pd.read_csv(dataFile)
                self.DaysList = np.sort(self.data['DayOfWeek'].unique())
                self.LineIdList = np.sort(self.data['Line_id'].unique())
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

def main():
    pass

if __name__ == '__main__':
    main()


myAnalysis = DataAnalysis('q_result2.csv')


#**************************************************

dfff = pd.read_csv('q_result2.csv')
DaysList = np.sort(dfff['DayOfWeek'].unique())

for days in DaysList:
    print dfff[(dfff.Line_id==1) & (dfff.DayOfWeek==days)]

ddf = dfff[(dfff.Line_id==1) & (dfff.DayOfWeek==days)]
print ddf[['Reven','Rev_km']].head()

print "print---------------------------------------------"'Ride_load'

for days in DaysList:
    print dfff[(dfff.Trip_id==1) & (dfff.Line_id==1) & (dfff.DayOfWeek==days)][['Ride_load','Trip_id','Pax','Reven','Line_id','DepartDate','DepartHour','DayOfWeek']] #.head(20) #['Ride_load'].head()

print "***********************************************************"

tmp = list()
for n_days,days in enumerate(DaysList):
    print dfff[(dfff.Trip_id==1) & (dfff.Line_id==1) & (dfff.DayOfWeek==days)]['Ride_load']
    val = dfff[(dfff.Trip_id==1) & (dfff.Line_id==1) & (dfff.DayOfWeek==days)]['Ride_load']
    av = np.average(val)
    var = np.average((val-av)**2)
    tmp.append([n_days+1,av,math.sqrt(var)])

print type(dfff[(dfff.Trip_id==1) & (dfff.Line_id==1) & (dfff.DayOfWeek==1)]['Ride_load'])

Ride_load = np.sort(dfff['Ride_load'])

days = [float(row[0]) for row in tmp]
avs = [float(row[1]) for row in tmp]
vars = [float(row[2]) for row in tmp]


plt.plot(days, avs, linestyle="dashed", marker="o", color="green")
plt.xticks(days)
plt.xlim(0.5,7.5)
plt.errorbar(days, avs, yerr=vars, linestyle="None", marker="None", color="green")


pl1=plt.draw()
P.show(pl1)
v6jycd

