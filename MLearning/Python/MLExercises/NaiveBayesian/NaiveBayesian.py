#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      wuiljai
#
# Created:     09/09/2013
# Copyright:   (c) wuiljai 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import io, os, collections, csv, string, re, sys
from numpy import *

import matplotlib
matplotlib.rcParams['legend.fancybox'] = True
import matplotlib.pyplot as plt
import pylab

class NaiveBayesian:
    ############################################################################
    #       Class: Naive Bayesian Analysis                                     #
    ############################################################################
    def __init__(self, dirLearn):
        self.dirLearn = os.getcwd()+"\\"+dirLearn
        self.dirFiles = [f for f in os.listdir(self.dirLearn)]
        self.Dict = self.MakeDict()
        self.Train = self.GenerTriplet()
        for i in [1,2,3]:
            print self.Train[i]

    def MakeDict(self):
        MakeDict = {}
        for tfile in self.dirFiles:
            filename= self.dirLearn+"\\"+tfile
            for word in sorted( filter( lambda x: len(x) > 2, [tfile for tfile in loadtxt(filename,dtype='str') ] ) ):
                MakeDict[word] = MakeDict.get(word, 0) + 1
        # Sorted in the alphab. order
        return MakeDict

    def GenerTriplet(self):
        # (docID, wordID, count)
        GenerTriplet = {}
        for n_file, tfile in enumerate(self.dirFiles):
            filename= self.dirLearn+"\\"+tfile
            for word in sorted( filter( lambda x: len(x) > 2, [tfile for tfile in loadtxt(filename,dtype='str') ] ) ):
                GenerTriplet[word] = [ GenerTriplet.get(word, 0) , 1 ]
        return GenerTriplet


def main():
    pass

if __name__ == '__main__':
    main()

l_naiveB = NaiveBayesian("spam-train") # 5 for the poly_order
