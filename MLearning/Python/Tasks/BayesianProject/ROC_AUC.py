import io, os, csv, sys 
import math as ma
import numpy as np
import scipy
from scipy.integrate import simps, trapz


def InFileROC( filename ): # read tsv file
	InFileROC = []
	for line in  list( tuple(open(filename, 'r')) ):
		tmp_line = map( float, line.split(' ') ) 
		InFile.append(tmp_line)
	return InFileROC

def InTestROC( containername ):
	InTestROC = []
	for tmp in containername:
		InTestROC.append(list( tmp[1:] ))
	return InTestROC

def area(x1,x2,y1,y2): # trapezoid area
	b = ma.fabs(x1-x2) 
	h = (y1+y2) 
	return  b*h/2.0

class ROC_AUC:
	###########################################################
	#	Implementation the ROC AUC Comput from:		  #	
	#	Fawcett, 2005, An Introduction to ROC Analysis	  #
	###########################################################
	def __init__(self,containername): #fileName):
		self.data = InTestROC(containername)
		self.data.sort( key=lambda tup: tup[0], reverse=True)
		self.Ndata = len(self.data)
		self.N = 0
		self.P = 0
		self.tp = 0.0
		self.fp = 0.0
		self.tp_ = 0.0
		self.fp_ = 0.0
		self.fprev = -1000
		self.area = 0.0
		self.curve = []

	def trapz_area(self):
		return np.trapz([tmp[1] for tmp in self.curve], x=[tmp[0] for tmp in self.curve])
	

	#should be @classmethod
	def get_auc(self,printflag):
		self.counting
		print self.P
		for tmp in self.data:
			if tmp[0] <> self.fprev:
				self.curve.append([self.fp/self.N,self.tp/self.P])
				self.fprev = tmp[0]
				self.tp_ = self.tp 
				self.fp_ = self.fp
			if tmp[1] == 1:
				self.tp += 1
			else:
				self.fp += 1
		# Finalising
		self.curve.append([self.fp/self.N,self.tp/self.P])
		self.area = self.trapz_area()
		if printflag == "print":
			#for i,tmp in enumerate(self.curve):
			#	print i, tmp
			print "ROC_AUC value: ", self.area


	def counting(self):
		for tmp in self.data:
			if tmp[1] == 1:
				self.P += 1
			else:
				self.N += 1
