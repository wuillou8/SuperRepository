import io, os, sys, time

import numpy as np


def InFile( filename ):
	readinlines = []
	for line in  list( tuple(open(filename, 'r')) ):
		tmp_line = line.split('\t')
		readinlines.append(tmp_line)
	return  readinlines

class IOInit: 
	##################################################
	# 	General IO/Init class			 #						
	##################################################
	def __init__ (self,fileName):
		self.data = InFile(fileName)
		self.l_data = len(self.data)
		self.features = ['token', 'site', 'add', 'country', 'rtb', 'account', 'campaign', 'bannertype','spotbuy','app_id','device','token_check','clicks'] 
		self.countEmpty = [0]*len(self.features)

	def SubList (self, feat_list): # extract out particular features
		for tmp in feat_list:
			if tmp not in self.features:
				sys.stderr.write('SubList: feature not recognised')
				sys.exit(1)
		SubList = []
		for tmp in self.data:
			li = []
			for feat in feat_list:
				li.append( tmp[ self.features.index(feat) ])
			li.append( [0,0] )
			SubList.append( li )
		return uniq(SubList)

	def checkData (self):
		for num,tmp in enumerate(self.data):
			if len(tmp) != 14:
				print "irregular length!", tmp
			if( tmp[self.features.index('token')] <> tmp[self.features.index('token_check')] ):
				print 'Warning: pbm token', tmp[0],tmp
			if int(tmp[self.features.index('clicks')]) not in [0,1]:
				print 'Warning: pbm clicks',  tmp[0],tmp
			if tmp[self.features.index('rtb')] not in ['true','false']:
				print 'Warning: pbm rtb', tmp[0],tmp
			if tmp[self.features.index('spotbuy')] not in ['true','false']:
				print 'Warning: pbm spotbuy', tmp[0],tmp
	
	def nbEmptyFields (self):
		nbEmptyFields = [0]*len(self.features)
		for tmp in self.data:
			for n_feat, feat in enumerate(self.features):
				if tmp[n_feat] == '': 
					nbEmptyFields[n_feat] += 1
		self.countEmpty = nbEmptyFields
		for i, feat in enumerate(self.features):
			if nbEmptyFields[i] > 0:
				print "%d empty fields for feature:", feat, nbEmptyFields[i]

