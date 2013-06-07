import io
import os
import csv 
import string
import re


###	IO	###
def ImportFile( filename ):
	readinlines = []
	for line in  list( tuple(open(filename, 'r')) ):
		readinlines.append(float(filter(line)))
	return readinlines

def filter ( string ):
	filter = re.sub(r'[\n]+', '', string)
	filter = re.split('   ',filter)
 	filter.remove("")
	return filter #.remove('') 

###	PREPROCESSING	###
#def Normalise( arraylist ):
#	dim = len(arraylist[0])
#	Normalise = 
#	for i in range(0,dim):
		
def normalist( tmplist ):
	normalist = list()
	ave = mean(tmplist)
	sdev = stdDev(tmplist)
	for tmp in tmplist:
		normalist.append( (tmp - ave)/sdev )
	return normalist

def stdDev( tmplist ):
	stdDev = 0.0
	ave = mean( tmplist ) 
	for tmp in tmplist:
		stdDev += (tmp - ave)**2
	return (stdDev**0.5)/len(tmplist)

def mean( tmplist ):
	mean = 0.0 
	for tmp in tmplist:
		mean += tmp
	return mean/len(tmplist)

###	FUNCTIONS	###
#function for calculating h_theta = theta^+ (*) x
def Iteration( alpha, theta, x_vect, y_vect ):
	Iteration = theta
	for i in range(0,len(theta)):
		Iteration[i] = theta[i] - alpha*sum_h_theta(theta, x_vect, y_vect)[i] 
	#Iteration[1] = theta[1] - alpha*sum_h_theta(theta, x_vect, y_vect)[1] 
	#theta[0] = theta[0] - alpha*sum_h_theta(theta, x_vect, y_vect) 
	#theta[1] = theta[1] - alpha*sum_h_theta(theta, x_vect, y_vect) 
	return Iteration

def J_theta ( theta, x_vect, y_vect ):
	J_theta = [0.0]*len(theta)
	one_m = 1.0/(len(x_vect)*2.0)
	for tmp in zip(x_vect, y_vect):
		print "ici", tmp[1]
		j_tmp =  h_theta(theta,tmp[0]) - list(float(tmp[1]))
		print j_tmp, type(j_tmp),  type(h_theta(theta,tmp[0]))
		print  h_theta(theta,tmp[0])**2
		print "jair", list(j_tmp)
		J_theta += one_m*j_tmp*j_tmp
	return J_theta

#sum_i h_theta^i - y^i
def sum_h_theta (theta, x_vect, y_vect): # N-Dim
	sum_h_theta = [0.0]*len(theta)
	one_m = 1.0/len(x_vect)
	for tmp in zip(x_vect, y_vect):
		for i in range(0,len(theta)):
			# h_theta(theta_s, xlist[0])print tmp, tmp[1], type(tmp[1])
			sum_h_theta[i] += one_m*( h_theta(theta,tmp[0]) - float(tmp[1]) )*float(tmp[0][i])
			#print sum_h_theta, one_m, tmp[0], "n",  h_theta(theta,tmp[0]), float(tmp[0][i]), tmp[1]
			#return sum_h_theta
			#sum_h_theta[1] += ( h_theta(theta,tmp[0]) - float(tmp[1]) )*float(tmp[0][1])
		#print sum_h_theta[0] , sum_h_theta[1]
		#print "ici ", h_theta(theta,tmp[0]) , float(tmp[1]) , float(tmp[0][0])
		#sum_h_theta[1] += tmp[0][1] - float(tmp[1]) 
	#sum_h_theta[0] *= 1.0/m
	#sum_h_theta[1] *= 1.0/m
	#print sum_h_theta[0] , sum_h_theta[1]
	return sum_h_theta

#h_theta = theta^+ * x_vect
def h_theta (theta_n, x_vect_i): # N-Dim
	h_theta = 0.0
	for tmp in zip(theta_n,x_vect_i):
		h_theta += tmp[0]*float(tmp[1])
		#theta[0]*tmp[0] + theta[1]*float(tmp[1]) 
		#h_theta.append( l_tmp ) 
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

xlist = ImportFile("DATA/ex3x.dat")
ylist = ImportFile("DATA/ex3y.dat")

#normalise data
ylist = normalist( [float(row[0]) for row in ylist] )
xlist0 = normalist( [float(row[0]) for row in xlist] )
xlist1 = normalist( [float(row[1]) for row in xlist] )
#print mean(xlist0), mean(xlist1)	-->Ok
#print stdDev(xlist0), stdDev(xlist1)	-->Ok

m = len(xlist)
tmp_1 = [1.0]*m
xlist = list(zip(tmp_1,xlist0,xlist1)) # merge data and add intercept term


n = len(xlist[0])
theta_s = [0.0]*n #len(xlist[0])
theta_zero = theta_s
alpha = 0.07

print xlist, n


for i in range(1,10000): #5000):
	theta_zero = theta_s
	theta_s = Iteration(alpha, theta_s, xlist, ylist)	
	print  i, theta_s[0], theta_s[1], theta_s[2] 
	print "Jtheta",  J_theta ( theta_s, xlist, ylist )
	#	dist(theta_s, Iteration(alpha, theta_s, xlist, ylist))

#print "theta final", theta_s

#print h_theta(theta_s, xlist[0]), theta_s, xlist[0]
#print theta_s
#print sum_h_theta(theta_s, xlist, ylist)
