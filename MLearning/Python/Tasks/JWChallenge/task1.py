import sys
from numpy import *


class ProbCalculator:

	def __init__(self,coefFile,dataFile):
		# read in files and pass it into a numpy vector (first line/column removed)
		self.v_coef = loadtxt(coefFile,'string',delimiter=',')[1:, 1:].astype(float)
		self.v_data = loadtxt(dataFile,'string',delimiter=',')[1:, 1:].astype(float)
		self.N_custs = int(self.v_data[(self.v_data.shape[0]-1)][0])
		self.Size_file = self.v_data.shape[0]-1

	def P_n_t_j(self,n_start,n_end): # index n redundant (data structure)
		P_n_t_j = []
		# select out data necessary for the comput
		v_data = self.v_data[n_start:n_end]
		#print v_data
		for n_,tmp in enumerate(v_data):
			n = tmp[0] # customer index
			P_n_t_j.append(exp(dot(v_data[n_][3:], transpose(self.v_coef[n-1][1:]))))
		# Normalisation
		P_n_t_j = P_n_t_j/sum(P_n_t_j)
		# Output
		for n_,tmp in enumerate(v_data):
			print int(tmp[0]),',',int(tmp[1]),',',int(tmp[2]),',',P_n_t_j[n_]
			
####################
#	Main	   #
####################

# Initialisation
comput = ProbCalculator("Coef.csv","Data.csv")	
print '"n"','"t"','"j"','"P_njt"'

# Computation
i_t = 0
n = 1
t = 1
for n_tmp,tmp in enumerate(comput.v_data):
	if tmp[0] == float(n):
		if tmp[1] == float(t):
			i_t += 1
		else: 
			ProbCalculator.P_n_t_j(comput,n_tmp-i_t,n_tmp)
			i_t = 1
			t += 1
	else:	
		ProbCalculator.P_n_t_j(comput,n_tmp-i_t,n_tmp)
		t = 1
		n += 1
		i_t = 1

ProbCalculator.P_n_t_j(comput,n_tmp-i_t+1,n_tmp+1)
