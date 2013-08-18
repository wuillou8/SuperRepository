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
#print sp.info(optimize.fmin) 
#	self.xx_data = loadtxt(testClass) 

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
	#print avg, stdev
	return (vec - avg) / stdev 



def h_theta(theta, vec_2):
	h_theta = dot(theta,vec_2)
	return h_theta
	
def grad_desc(theta,xx,yy,alpha): #gives back the new theta
	grad_desc = 0.0
	m = size(theta)
	grad_desc = (alpha/m)*(h_theta(theta,xx[1])-yy[1])
	# dot((h_theta(theta,xx[1])-yy[1]),)
	print theta, xx[1], yy[1], alpha
	return grad_desc		


class Complex:
	def __init__(self, realpart, imagpart):
		self.r = realpart
		self.i = imagpart


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


	def J_theta(self, theta):
		return  sum((dot(theta,transpose(self.xx_data)) - self.xy_data)**2.0)/(2.0*self.Size)

	def grad_desc(self, alpha, theta): #gives back the new theta
		grad_desc = list()
		for i in range(0,self.Dim):
			grad_desc.append( theta[i] - (alpha/self.Size)*dot( (dot(theta,transpose(self.xx_data))-self.xy_data), transpose(self.xx_data[:,i])))
		return array(grad_desc)

analy = Analysis("ex4y.dat","ex4x.dat")
Analysis.norm_data(analy)

print "Analysis"
theta = array([0, 0, 0]) # Init theta
alpha = 0.001

for i in range(0,100000):
	theta = Analysis.grad_desc(analy, alpha, theta)
	print "iter", i , "theta", theta, "J_theta", Analysis.J_theta(analy, theta)
