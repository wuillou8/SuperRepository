#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      wuiljai
#
# Created:     04/09/2013
# Copyright:   (c) wuiljai 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import io, os, csv, string, re, sys
from numpy import *

import matplotlib
matplotlib.rcParams['legend.fancybox'] = True
import matplotlib.pyplot as plt
import pylab


class SVM:
    ############################################################################
    #       			Class: SVM Lin. Classif.                       #
    ############################################################################
    def __init__(self, InfileX):
        self.row_dat = loadtxt(InfileX) 
	self.dat1 = self.row_dat[self.row_dat[:][0] == 1. ]
	self.dat2 =  [ tmp of  self.row_dat[self.row_dat[:][0] == -1. ]
	#self.y_dat = loadtxt(InfileY)

################################################################################
def main():
    pass

if __name__ == '__main__':
    main()
################################################################################

l_reg = SVM("data/twofeature_prepa.txt")
print l_reg.row_dat
print l_reg.dat1

