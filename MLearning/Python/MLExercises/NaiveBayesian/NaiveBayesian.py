#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      wuillou8
#
# Created:     09/09/2013
# Copyright:   (c) wuiljai 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import io, os, collections, csv, string, re, sys
from numpy import *
import panda as pd
import matplotlib
matplotlib.rcParams['legend.fancybox'] = True
import matplotlib.pyplot as plt
import pylab


class NaiveBayesian:
    ############################################################################
    #       Class: Naive Bayesian Analysis                                     #
    ############################################################################
    def __init__(self, dirLearnspam, dirLearnnospam):
        self.dirLearnspam = os.getcwd()+"//DATA//ex6DataEmails//"+dirLearnspam
	self.dirLearnnospam = os.getcwd()+"//DATA//ex6DataEmails//"+dirLearnnospam
        self.dirFilesspam = [f for f in os.listdir(self.dirLearnspam)]
	self.dirFilesnospam = [f for f in os.listdir(self.dirLearnnospam)]
        self.DictSpam = self.MakeDict("spam")
	self.DictnoSpam = self.MakeDict("non-spam")

    def MakeDict(self,spamornot):
        MakeDict = {}
	
	if (spamornot == "spam"):
		files = self.dirFilesspam
		dirLearn = self.dirLearnspam
	elif (spamornot == "non-spam"):
		files = self.dirFilesnospam
		dirLearn = self.dirLearnnospam
	
	for tfile in files:
        	filename= dirLearn+"//"+tfile
            	for word in sorted( filter( lambda x: len(x) > 2, [tfile for tfile in loadtxt(filename,dtype='str') ] ) ):
                	MakeDict[word] = MakeDict.get(word, 0) + 1
        # Sorted in the alphab. order
        return MakeDict

    def buildProb(self, testDir):
	# fction analysing the probas spam/non-spam 
	# based on the Dictionaries computed above
	buildProb = []
	dirTested = os.getcwd()+"//DATA//ex6DataEmails//"+testDir

	fff = open(testDir+".txt", 'w')
	for tfile in [f for f in os.listdir(dirTested)]:
            	fileName= dirTested+"//"+tfile
		PSpam = 0. 
		PnoSpam = 0.
		for word in sorted( filter( lambda x: len(x) > 0, loadtxt(fileName,dtype='str') ) ):
			PSpam += self.DictSpam.get(word, 0) + 1
    			PnoSpam += self.DictnoSpam.get(word, 0) + 1

		if( log(PSpam) >= log(PnoSpam) ):
			fff.write( tfile+" spam\n" )
		else:
			fff.write( tfile+" non-spam\n" )
	pass

#####################################################################
def main():
    pass

if __name__ == '__main__':
    main()
#####################################################################

# Init over nonspam/spam dirs in DATA/ex6DataEmails/
l_naiveB = NaiveBayesian("spam-train","nonspam-train") 
# Analysis run over the nonspam/spam dirs in DATA/ex6DataEmails/
l_naiveB.buildProb("nonspam-test")
l_naiveB.buildProb("spam-test")
