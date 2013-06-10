import io
import os
import csv 
import string
import re


###	IO	###
def ImportFile( filename ):
	readinlines = []
	for line in  list( tuple(open(filename, 'r')) ):
		readinlines.append(filter(line))
	return readinlines

def filter ( string ):
	filter = re.sub(r'[ \n]+', '', string)
	return filter 

###	FUNCTIONS	###

#function for calculating h_theta = theta^+ (*) x
def Iteration( alpha, theta, x_vect, y_vect ):
	Iteration = theta
	Iteration[0] = theta[0] - alpha*sum_h_theta(theta, x_vect, y_vect)[0] 
	Iteration[1] = theta[1] - alpha*sum_h_theta(theta, x_vect, y_vect)[1] 
	return Iteration

#sum_i h_theta^i - y^i
def sum_h_theta (theta, x_vect, y_vect):
	sum_h_theta = [0.0, 0.0]
	m = len(x_vect)
	for tmp in zip(x_vect, y_vect):
		sum_h_theta[0] += ( h_theta(theta,tmp[0]) - float(tmp[1]) )*float(tmp[0][0])
		sum_h_theta[1] += ( h_theta(theta,tmp[0]) - float(tmp[1]) )*float(tmp[0][1])
	sum_h_theta[0] *= 1.0/m
	sum_h_theta[1] *= 1.0/m
	return sum_h_theta

#h_theta = theta^+ * x_vect
def h_theta (theta_n, x_vect_i):
	h_theta = 0.0
	for tmp in zip(theta_n,x_vect_i):
		h_theta += tmp[0]*float(tmp[1])
	return h_theta

def dist(vec1,vec2):
	dist = 0.0
	for tmp in zip(vec1,vec2):
		dist += (tmp[0]-tmp[1])**2
		print tmp[0], tmp[1]
	return dist

#####################################################################
############			Main			#############
#####################################################################

xlist = ImportFile("DATA/ex2x.dat")
ylist = ImportFile("DATA/ex2y.dat")

m = len(xlist)
tmp_1 = [1.0]*m
xlist = zip(tmp_1,xlist) #add intercept term

theta_s = [0.0]*2
theta_zero = theta_s
alpha = 0.07

#f = open("LinearRegression.txt","w")

#Iterations/Analysis
for i in range(0,5000):
	theta_zero = theta_s
	theta_s = Iteration(alpha, theta_s, xlist, ylist)	
	print  i, theta_s[0], theta_s[1] 
	#	dist(theta_s, Iteration(alpha, theta_s, xlist, ylist))
	#	print "theta final", theta_s
