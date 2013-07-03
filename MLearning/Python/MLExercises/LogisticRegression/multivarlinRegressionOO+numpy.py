import io
import os
import csv 
import string
import re

from numpy import *
#import scipy as sp
#import matplotlib as mpl
#import matplotlib.pyplot as plt
#from scipy import linalg, optimize

#class Computation:
def get_avg(vec):
	get_avg = 0.0
	for tmp in vec:
		get_avg += tmp
	get_avg = get_avg / size(vec)
	return get_avg

def get_stdev(vec, avg):
	get_stdev = 0.0
	for tmp in vec:
		get_stdev += (tmp-avg)**2
	get_stdev = get_stdev  / size(vec)
	return (get_stdev)**0.5

def get_normalise(vec):
	avg = get_avg(vec)
	stdev = get_stdev(vec, avg)
	return (vec - avg) / stdev 

def g_theta(theta, vec):
	g_theta = 1.0/(1.0+exp(h_theta(theta,vec)))
	return g_theta

class Analysis:
	# Testing sample
	def __init__(self, testValname, testClass):
		self.xy_data = loadtxt(testValname) 
		self.xx_data = insert(loadtxt(testClass), 0, 1, axis=1) 
		self.Size = self.xx_data.shape[0]
		self.Dim = self.xx_data.shape[1]
	
	def norm_data(self): #self):
		for i in range(1,self.Dim):
			self.xx_data[:,i] = get_normalise(self.xx_data[:,i])

	def g_theta(self,theta):
		return 1.0/(1.0+exp( dot(theta,transpose(self.xx_data)) ))

	def J_theta(self, theta):
		J_theta = -dot( self.xy_data,transpose( log(self.g_theta(theta)) ) ) - dot( 1.0-self.xy_data,transpose( 1.0-log(self.g_theta(theta))) )
		return  J_theta/(2.0*self.Dim)

	def D_J_theta(self, theta):
		D_J_theta = list()
		for i in range(0,self.Dim):
			D_J_theta.append( dot( self.g_theta(theta)-self.xy_data , transpose(analy.xx_data[:,i]) ) )
		return  array(D_J_theta)/(self.Dim)
		
	def H(self,theta):
		H = self.g_theta(theta)*(1.0-self.g_theta(theta)) 
		return H		
		



analy = Analysis("ex4y.dat","ex4x.dat")
Analysis.norm_data(analy)

print "Analysis"
theta = array([1, 1, 1]) # Init theta
alpha = 0.001


print "xx_data",  analy.xx_data #, exp(h_theta(theta,vec))

print "xy_data",  analy.xy_data 

print "test9", Analysis.J_theta(analy, theta)

print "test13",  Analysis.D_J_theta(analy, theta)

print "test10",  analy.g_theta(theta)-analy.xy_data , transpose(analy.xx_data)  
print "test11",  dot( analy.g_theta(theta)-analy.xy_data , transpose(analy.xx_data[:,1]) )  

print "test12",  analy.g_theta(theta), (1.0-analy.g_theta(theta))

jair = dot( transpose(analy.xx_data), analy.xx_data )

print "test14", jair, shape(jair)

print "test15", analy.xx_data, transpose(analy.xx_data)


print "test15", analy.xx_data[1], transpose(analy.xx_data[1]), dot(analy.xx_data[1], transpose(analy.xx_data[1]))



#for i in range(0,100000):
#	theta = Analysis.grad_desc(analy, alpha, theta)
#	print "iter", i , "theta", theta, "J_theta", Analysis.J_theta(analy, theta)
