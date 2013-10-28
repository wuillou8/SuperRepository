#-------------------------------------------------------------------------------
# Name:        MFBAnalysis
# Purpose:
#
# Author:      wuillou8
#
# Created:     18/10/2013
# Copyright:   (c) wuiljai 2013
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
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

start = time.clock()

myAnalysis = PlotforMFB.PlotforMFB('q_result2.csv','Trip_id','totalstuff')

print( "---*-Run took %s seconds " % ( time.clock() - start ) )

