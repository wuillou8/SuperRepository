#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      wuiljai
#
# Created:     02/09/2013
# Copyright:   (c) wuiljai 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import io, os, csv, string, re, sys
from numpy import *

import matplotlib
matplotlib.rcParams['legend.fancybox'] = True
import matplotlib.pyplot as plt
import pylab


class LogisticRegression:
 	#####################################
 	# Class for the logistic regression #
	#####################################

	def __init__(self, InfileX, InfileY):
        	self.xy_data = loadtxt(InfileY)
	        self.xx_data = insert(loadtxt(InfileX), 0, 1, axis=1)
	        self.Size = self.xx_data.shape[0]
        	self.Dim = self.xx_data.shape[1]
		#initial theta set to 0's
		self.theta = zeros(self.Dim)

	def Grad_Desc(self):
		#Newton method
		self.theta = self.theta - squeeze( asarray( dot( self.H_I(), transpose(matrix(self.D_J_theta()))) ))

	def h_theta(self,idx):
        	return 1./(1.+exp( -dot(self.theta,transpose(self.xx_data[idx])) ))

	def D_J_theta(self): # gradient of J_theta
        	D_J_theta = zeros(self.Dim)
		tmp = list()
	        for i in range(0,self.Size):
			tmp.append(self.h_theta(i)-self.xy_data[i])
		return dot( tmp, self.xx_data)/self.Size

	def H_I(self): # Hessian: \frac{1}{m} \sum_i^m \[ h_{\theta}(x^i) (1-h_{\theta}(x^i)) x^i (x^i)^T \]
        	H = matrix(zeros((self.Dim,self.Dim)))
		for i in range(0,self.Size):
			H += (1./self.Size)*self.h_theta(i)*(1.0-self.h_theta(i))\
                	*dot( transpose(matrix(self.xx_data[i])), matrix(self.xx_data[i]))
		return H.I

	def J_theta(self): # Cost Function: \frac{1}{m} \sum_i^m \[ -y^i log(h_{\theta}(x^i) - (1-y^i)log(1-h_{\theta}(x^i)) )
		J_theta = 0.
		for i in range(0,self.Size):
			J_theta += -self.xy_data[i]*log(self.h_theta(i)) - (1.-self.xy_data[i])*log(1.-self.h_theta(i))
		return J_theta/self.Size


	def plot(self):
        	pl1=plt.plot(self.xx_data[self.xy_data[:]==1,1],self.xx_data[self.xy_data[:]==1,2],'ro', label='admitted')
	        pl1=plt.plot(self.xx_data[self.xy_data[:]==0,1],self.xx_data[self.xy_data[:]==0,2],'g^', label='not admitted')
		# plot the line found with the logistic regression:
		# since the separating line is \theta^T \cdot x = 0, one finds y = - theta[1]/theta[2]*x - theta[0]/theta[2]
		x = arange(10, 70, 0.1);
		y = - self.theta[1]/self.theta[2]*x - self.theta[0]/self.theta[2]
		pl1=plt.plot(x,y,'r--',label = 'separation line')
		pl1=plt.title('Student exams scores && logistic regression')
		pl1=plt.xlabel('exam1 scores')
		pl1=plt.ylabel('exam2 scores')
	        pl1=plt.grid(True)
	        pl1=plt.legend(loc=2)
        	pl1=plt.draw()
	        pylab.show(pl1)


#####################################################
#					__MAIN__()						#
#####################################################

# Init the L.Regress./Read in the data
l_Reg = LogisticRegression("ex4x.dat","ex4y.dat")

print l_Reg.xx_data

# Run
for i in range(0,20):
	print( "---*-Ite #%s : Theta = %s , J = %s " % (i, l_Reg.theta, l_Reg.J_theta()))

	theta_in = l_Reg.theta
	l_Reg.Grad_Desc()
	d_theta = theta_in - l_Reg.theta
	if( std(d_theta) <= 1.e-10 ):
		print "---*-Algorithm converged after %s Iteration" % i
		print "---*-theta_conv = %s , J_theta = %s" % (l_Reg.theta , l_Reg.J_theta())
		l_Reg.plot()
		sys.exit()

