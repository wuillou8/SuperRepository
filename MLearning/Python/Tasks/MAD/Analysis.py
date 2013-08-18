import io, os, csv, sys 
import math as ma
import numpy as np

from IOInit import *

def getEls(data,indexList):
	getEls = []
	for i in indexList:
		getEls.append(data[i])
	return getEls

def checkFeats(featsList,featsSub):
	for tmp in featsSub:
		if tmp not in featsList:
			print "Model:checkFeats: feature selected not in features list", tmp
			sys.exit(1)
	return featsSub

def getFeats(data,featsList,featsSub):
	indx = [featsList.index('token'),featsList.index('clicks')] #token and clicks fields selected
	for tmp in featsSub:
		indx.append(featsList.index(tmp))
	getFeats = [getEls(row,indx) for row in data]
	return getFeats

def getClicks(data,featsList): # use lambda fction instead
	getClicks = 0
	ind = featsList.index('clicks')
	for tmp in data:
		if int(tmp[ind]) == 1:
			getClicks += 1
	return getClicks 		



class Analysis: 

	def __init__(self,testsample,featsSub):
		self.data = testsample.data
		self.l_data = testsample.l_data
		self.features = testsample.features
		self.Clicks =  getClicks(self.data,self.features)
		self.P_Clicks = float(self.Clicks)/float(self.l_data) 
		# filtrate only the sub features only
		self.featsSub = checkFeats(self.features,featsSub)
		self.data = getFeats(self.data,self.features,self.featsSub)
		self.countEmpty = testsample.countEmpty 
		#Containers for Analysis Ouptput: [feat1(resu), feat2(resu), ...]
		self.analyConf = []  
		self.analyStat = []
		self.clicksPercs = []

	def importTestData(self, testdata, featsSub):
		self.featsSub = checkFeats(self.features,featsSub)
		self.data = getFeats(testdata.data,self.features,featsSub)

