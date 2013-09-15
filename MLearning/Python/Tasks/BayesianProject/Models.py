import io, os, csv, sys 
import math as ma
import numpy as np

from IOInit import *
from Analysis import *
##############################################################


def getEls_(data,indexList):
	getEls = []
	for i in indexList:
		getEls.append(data[i])
	return getEls

def getFeats_(data,featsList,featsSub):
	#token and clicks fields  also selected
	indx = [featsList.index('token'),featsList.index('clicks')]
	for tmp in featsSub:
		indx.append(featsList.index(tmp))
		getFeats = [getEls(row,indx) for row in data]
	return getFeats

def get_StatCorr(cutoff,listing,listcount,nb_confs,nb_clicks,nb_file):
	solve_stat = []
	solve_conf = []
	cut_count = 0
	cut_click = 0

	for n_tmp,tmp in enumerate(listcount): # use alpha function
		if int(tmp[1]) > cutoff:
			cut_click += tmp[0]
			cut_count += tmp[1]

	p_click1 = float(cut_click)/float(cut_count) 
	p_click2 = float(nb_clicks - cut_click)/float(nb_file - cut_count)  
	for n_tmp,tmp in enumerate(listcount):
		if int(tmp[1]) > cutoff:
			solve_stat.append((float(tmp[0])/float(cut_click),float(tmp[1])/(cut_count)))
			solve_conf.append(listing[n_tmp])

	#print "SUMMARY Corr:", len(listing), cut_count
	#print "--- 2 ---in/ out", p_click1, p_click2
	return solve_stat,solve_conf,p_click2,p_click1


class BayesNaive(Analysis):
		
	def __init__(self,testsample,featsSub):
		#super(BayesSimple,self).__init__(testsample,featsSub)
		Analysis.__init__(self,testsample,featsSub)
		self.cutoff = 300 # starting cutoff
		self.testList = []
		self.SubSetP_clicks = 0
		self.SetP_clicks = 0


	def BayesLearn(self,cutoff=300):
		# Implements Bayes for a conf of features elements: [feat1,feat2,feat3]
		# A cut-off can be given, such that only confs over a certain number of elements
		# get their probability computed.

		self.analyStat = []
		self.analyConf = []

		listing = []
		listcnt = []
		countempty = [0]*2
		for tmp in self.data:
			config = []

			for n_feat,feat in enumerate(self.featsSub):
				if tmp[2+n_feat] == '':
					countempty[0] += int(tmp[1])	# click
					countempty[1] += 1		# occurence
					break
				else:
					config.append(tmp[2+n_feat])
				
			if config not in listing:
				listing.append(config)
				listcnt.append([int(tmp[1]),1]) 
			else:
				listcnt[listing.index(config)][0] += int(tmp[1])	# add clicks
				listcnt[listing.index(config)][1] += 1			# add occurence
	
		# readjust statistics
		self.Clicks -= countempty[0] 
		self.l_data -= countempty[1]
		#print "data loss nb:", countempty[1],countempty[0]

		# solve stat:
		self.cutoff = cutoff
		stat = get_StatCorr(self.cutoff,listing,listcnt,self.l_data,self.Clicks,self.l_data)
		self.analyStat.append(stat[0])
		self.analyConf.append(stat[1])
		self.SubSetP_clicks = stat[2]
		self.SetP_clicks = stat[3]

		#print "SubSetP_clicks", stat[2],stat[3]
	
	def BayesTest(self, data): # initial test
		val = 0
		for tmp in self.data:
			config = []

			for n_feat,feat in enumerate(self.featsSub):
				config.append(tmp[2+n_feat])
			
			if config in self.analyConf[0]:
				n_b = self.analyConf[0].index(config)
				p =  self.SetP_clicks*self.analyStat[0][n_b][0]/self.analyStat[0][n_b][1]
				val += p
			else: 	
				p = self.SubSetP_clicks
				val += p
					
			self.testList.append(list((tmp[0],p,int(tmp[1]))))
		#print "probaTOT ",val/len(data.data), self.P_Clicks	
		
	
	def MultBayesTest(self,data):
		# function p (A,B)= pA * pB assuming independance
		val = 0
		lisstat = [row[1] for row in self.testList]
		self.testList = []
		for n_tmp,tmp in enumerate(self.data):
			config = []
			p = lisstat[n_tmp]
			for n_feat,feat in enumerate(self.featsSub):
				config.append(tmp[2+n_feat])
			
			if config in self.analyConf[0]:
				n_b = self.analyConf[0].index(config)
				if p == 0:
					p =  0.5*self.P_Clicks*self.analyStat[0][n_b][0]/self.analyStat[0][n_b][1]
				else:
					p *= self.analyStat[0][n_b][0]/self.analyStat[0][n_b][1]
				p *= self.SetP_clicks/self.P_Clicks	
				val += p
			else:
				p *= self.SubSetP_clicks/self.P_Clicks	
				val +=p

		
			self.testList.append(list((tmp[0],p,int(tmp[1]))))
		#print "probaTOT ",val/len(data.data), self.P_Clicks	

	def AddBayesTest(self,testdata,factor):
		# function summing up the model probas
		lisstat = [row[1] for row in self.testList]
		self.testList = []
		val = 0.0
		for n_tmp,tmp in enumerate(self.data):
			config = []
			p = lisstat[n_tmp] 
	
			for n_feat,feat in enumerate(self.featsSub):
				config.append(tmp[2+n_feat])

			if config in self.analyConf[0]:
				n_b = self.analyConf[0].index(config)
				p = (1.0-factor)*p + factor*self.SetP_clicks*self.analyStat[0][n_b][0]/self.analyStat[0][n_b][1]
			# Here we take only the contributions of the better sampled configs.
			# else:
			#	p = (1.0-factor)*p + factor*self.SubSetP_clicks

			self.testList.append(list((tmp[0],p,int(tmp[1]))))

