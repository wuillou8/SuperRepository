import io
import os
import csv 
import numpy







def InFile( filename ): # read tsv file
	InFile = []
	for line in  list( tuple(open(filename, 'r')) ):
		tmp_line = map( float, line.split('\t') ) 
		InFile.append(tmp_line)
	return InFile

class ROC_AUC_1:

	def __init__(self,dataname):
		self.data = InFile(dataname)
		self.Ndata = len(self.data)
		self.N = 0
		self.P = 0
		self.tp = 0.0
		self.fp = 0.0
		self.fprev = -1000
		self.resu = []

	def auc(self):
		for tmp in self.data:
			if tmp[0] <> self.fprev:
				self.resu.append([self.fp/self.N,self.tp/self.P])
				self.fprev = tmp[0]
			if tmp[1] == 1:
				self.tp += 1
			else:
				self.fp += 1
		self.resu.append([self.fp/self.N,self.tp/self.P])

	def counting(self):
		for tmp in self.data:
			if tmp[1] == 1:
				self.P += 1
			else:
				self.N += 1


a_roc = ROC_AUC_1("test.dat")
a_roc.counting()
a_roc.auc()

print "output: "
for tmp in a_roc.resu:
	print tmp[0], tmp[1]


print a_roc.resu

print a_roc.N, a_roc.P 
myfile = InFile('test.dat')

# Initialisation
l_myfile = len(myfile)


#print type(myfile), l_myfile
# Algorithm 1

tp = 0.0
fp = 0.0
r = []

fprev = - 1000
#N, P
N = 0
P = 0

for tmp in myfile:
	if tmp[1] == 0:
		N += 1
	else: 
		P += 1	
	
print "N and P", N, P

for tmp in myfile:
	if tmp[0] <> fprev:
		r.append([fp/N,tp/P])
		fprev = tmp[0]
	if tmp[1] == 1:
		tp += 1
	else:
		fp += 1
r.append([fp/N,tp/P])

print "r", r	



