import io, os, csv, sys 
import math as ma
import numpy as np
import scipy
from scipy.integrate import simps, trapz


def InFile( filename ): # read tsv file
	InFile = []
	for line in  list( tuple(open(filename, 'r')) ):
		tmp_line = map( float, line.split(' ') ) 
		InFile.append(tmp_line)
	return InFile

class ROC_AUC_1:
	#Implementing the ROC AUC Comput from:
	#Fawcett, 2005, An Introduction to ROC Analysis	
	def __init__(self,fileName):
		self.data = InFile(fileName)
		# first arg: prevision 
		# second arg: 1/0 for (true/false) or a probability
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
				

	def auc(self):
		self.counting
		for tmp in self.data:
			if tmp[0] <> self.fprev:
				self.area += area(self.fp,self.fp_,self.tp,self.tp_)
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

	def counting(self):
		for tmp in self.data:
			if tmp[1] == 1:
				self.P += 1
			else:
				self.N += 1

#########################
#	 main:		#
#########################
# the input file expected has the prediction as first column
# and the testing values (0/1 or real in [0--1]) as second column. 
if len(sys.argv) <> 2:
	sys.stderr.write('Usage: fileName passed as arg #2 ')
	sys.exit(1)

a_roc = ROC_AUC_1(sys.argv[1]) 
a_roc.auc()

for tmp in a_roc.curve:
	print "roc curve", tmp[0], tmp[1]

print "area fawcett", a_roc.area
#print "area trapezoid:", np.trapz([tmp[1] for tmp in a_roc.curve], x=[tmp[0] for tmp in a_roc.curve ])
#print "area Simpson:", scipy.integrate.simps(np.array([tmp[1] for tmp in a_roc.curve]), np.array([tmp[0] for tmp in a_roc.curve]))

