#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      wuillou8
#
# Created:     18/10/2013
# Copyright:   (c) wuillou8 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#-Std Packages------------------------------------------------------------------

import sys, time

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
import myDataStudy
#-------------------------------------------------------------------------------



def main():
    pass

if __name__ == '__main__':
    main()

start = time.clock()

for run in ['Pax','Ride_load','Reven','Rev_km']:
    #myPlot = PlotforMFB.newPlotforMFB('q_result2.csv',run,'totRideLoadVSDayOfWeek','All Data: ','normal')
    #myPLot = PlotforMFB.newPlotforMFB('q_result2.csv',run,'totRideLoadVSDayOfWeek','Averaged Data: ','average')
    #myPLot = PlotforMFB.newPlotforMFB('q_result2.csv',run,'totRideLoadVSDayOfWeek','line: ','runline')
    print 'Run %s over' % run

myStudy = myDataStudy.DataStudy('q_result2.csv','lineRel')

#print PlotforMFB.fctChgDays(1)
print( "---*-Run took %s seconds " % ( time.clock() - start ) )
#P.show()
sys.exit(0)
