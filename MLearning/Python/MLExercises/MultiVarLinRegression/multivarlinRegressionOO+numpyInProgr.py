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


def get_normalise(vec):
	return (vec - average(vec)) / std(vec) 


class Analysis:
	# Testing sample
	def __init__(self, testValname, testClass):
		self.xy_data = loadtxt(testValname) 
		self.xx_data = insert(loadtxt(testClass), 0, 1, axis=1) 
		self.Size = self.xx_data.shape[0]
		self.Dim = self.xx_data.shape[1]
	
	def norm_data(self): 
		self.xx_data[:,1:] = get_normalise(self.xx_data[:,1:])

	def h_theta(self,theta):
		return 1.0/(1.0+exp( dot(theta,transpose(self.xx_data)) ))

	def D_J_theta(self, theta):
		D_J_theta = list()
		for i in range(0,self.Dim):
			D_J_theta.append( dot( self.h_theta(theta)-self.xy_data , transpose(self.xx_data[:,i]) ) )
		return  array(D_J_theta)/self.Dim
		
	def H(self,theta):
		for i in range(0,self.Dim):
			H = self.h_theta(theta)*(1.0-self.h_theta(theta)) #dot( self.xx_data,  transpose(self.xx_data) )
			print "Check1 ", i, shape(H)
			print "Check2 ", i, shape(self.xx_data)
			print "Check3 ", i, shape(dot( self.xx_data,  transpose(self.xx_data) ) ) 
			print "CheckH", H
			print "CheckH1", shape(dot(dot( self.xx_data,  transpose(self.xx_data) ), H))
			print  self.Dim
			#print "Check4 ", i, dot( transpose(H), shape(dot( self.xx_data, transpose(self.xx_data) ) ) )
		return H/self.Dim		
		



analy = Analysis("ex4y.dat","ex4x.dat")
Analysis.norm_data(analy)

print "Analysis"
theta = array([1, 1, 1]) # Init theta
alpha = 0.001


print "test14", Analysis.H(analy, theta)

print "test13", shape( Analysis.D_J_theta(analy, theta) )



