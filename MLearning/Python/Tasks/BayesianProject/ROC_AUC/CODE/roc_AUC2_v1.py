import io
import os
import csv 
import math as ma
import numpy


def InFile( filename ): # read tsv file
	InFile = []
	for line in  list( tuple(open(filename, 'r')) ):
		tmp_line = map( float, line.split('\t') ) 
		InFile.append(tmp_line)
	return InFile

def area(x1,x2,y1,y2): # trapezoid area
	b = ma.fabs(x1-x2) 
	h = (y1+y2) 
	return  b*h/2.0 


class ROC_AUC_1:
	#Implementing the ROC AUC Comput from:
	#Fawcett, 2005, An Introduction to ROC Analysis	
	def __init__(self,fileName):
		self.data = InFile(fileName)
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

	def auc(self):
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
		self.area += area(self.N,self.fp_,self.N,self.tp_)
		self.area = self.area/(self.P*self.N)
		self.curve.append([self.fp/self.N,self.tp/self.P])

	def counting(self):
		for tmp in self.data:
			if tmp[1] == 1:
				self.P += 1
			else:
				self.N += 1
				

#def main():
a_roc = ROC_AUC_1("test2.dat")
a_roc.counting()
a_roc.auc()

print "output: "
for tmp in a_roc.curve:
	print "roc curve", tmp[0], tmp[1]

print "area", a_roc.area	
