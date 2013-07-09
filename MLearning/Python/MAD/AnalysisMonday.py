import io
import os
import csv
import string
import re
import sys

import numpy as np
#from numpy import *


def f(x): return x % 2 != 0 and x % 3 != 0
# 3 <--> 4  6 <--> 8 
# token == cusip --> filter

def InFile( filename ):
	readinlines = []
	for line in  list( tuple(open(filename, 'r')) ):
 		tmp_line = FilterData( line.split('\t') ) # file correct: fields 4 and 7 are not regular and are corrected!
		print len(tmp_line)
		if( len(tmp_line) == 14 ):
			readinlines.append(tmp_line)	
		else:
			sys.exit("pbm line")
	return readinlines

def InFile2( filename ):
	readinlines = []
	for line in  list( tuple(open(filename, 'r')) ):
		tmp_line = line.split('\t')
		readinlines.append(tmp_line)
	return  readinlines #np.array(readinlines)



def FilterData( linename ):
	if len(linename) != 13:
		if linename[4] not in ['false', 'true']:
			linename.insert(3,"None")										
		if linename[8] not in ['false', 'true']:
			linename.insert(6,"None")										
	return	linename


class MADAnalysis:

	def __init__(self,infile):
		self.dt = np.dtype([('token',np.str_,32),('site',np.str_,32),('add',np.str_,32),('country',np.int64),('rtb',np.bool),('account',np.int64),('campaign',np.int64),('spotbuy',np.int64),('app_id',np.int64),('device',np.str_,32),('token_check',np.str_,32),('clicks',np.bool),('conversions',np.int64)]) #, (2,))])
		#np.dtype([('token',str_),('site',str_),('add',str_),('country',int64),('rtb',bool),('account',int64),('campaign',int64),('spotbuy',int64),('app_id',int64),('device',str_),('token_check',str_),('clicks',bool),('conversions',int64)]) #, (2,))])
		self.data = InFile(infile)
		



testValname = "tmp"
#jair = genfromtxt(StringIO(testValna'1szge' '32785' '21761' '219' 'false' '3675' '' '1' 'false' '' '4501'me),delimiter=1)
#jair = loadtxt(dtype='float', delimiter=",")

dt = np.dtype([('name', np.str_, 16), ('grades', np.float64, (2,))])
x = np.array([('Sarah', (8.0, 7.0)), ('John', (6.0, 7.0))], dtype=dt)
print x

dt = np.dtype([("name", np.str_, 64), ("grades", np.float64)])
xy = np.array([('Sarah', 8.0), ('John', 7.0)], dtype=dt)
print xy, xy['name']
#mylist = ImportFile("sampletest.tsv")

#def ff(x): return x % 2 != 0 and x % 3 != 0
def ff(x): return (abs(x['grades']) == 1.0) # or ['name'] == -1.0)


jair = np.array([('Sarah', -1.0)], dtype=dt)
test = ff(jair)
print test, jair
def gg(x): return ( x['truefalse'] == 'true' or  x['truefalse'] == 'false')
dtest = np.dtype([('token',np.str_,32),('site',np.str_,32),('add',np.str_,32),('country',np.int64),('rtb',np.bool),('account',np.int64),('campaign',np.int64),('spotbuy',np.int64),('tmp',np.str_),('app_id',np.int64),('device',np.str_,32),('token_check',np.str_,32),('clicks',np.bool),('conversions',np.int64)]) 
#mylist = ImportFile("sampletest.tsv")


dte = np.dtype([("name",np.str_,64),("grades",np.float64),("truefalse",np.str_,64)])
#def gg(x): return ( x['truefalse'] == 'true' or  x['truefalse'] == 'false')
jair = np.array([('Sarah',-1.0,'false'),('Sarah1',-1.01,'false1')],dtype=dte)
#test = gg(jair)
#print test, jair

def checkData(data, num):
	if( data['token'] <> data['token_check'] ):
		print 'Warning: line %d is irregular, pbm token' % num
	if data['clicks'] not in [0,1]:
		print 'Warning: line %d is irregular, pbm clicks' % num
	if data['conversions'] not in [0,1]:
		print 'Warning: line %d is irregular, pbm conversions' % num
	if data['rtb'] not in ['true','false']:
		print 'Warning: line %s is irregular, pbm rtb' % num
	if data['spotbuy'] not in ['true','false']:
		print 'Warning: line %s is irregular, pbm spotbuy' % num
	return data	
	#return ( x['truefalse'] == 'true' or  x['truefalse'] == 'false')


mylist = InFile2("test.tsv")
for tmpi in mylist:
	print tmpi, len(tmpi)

'', '3998', '11oqxw', '0', '0\n'
#'false', '3038', '2075', '1', 'false'

dtested = np.dtype([('token',np.str_,32),('site',np.str_,32),('add',np.str_,32),('country',np.int64),('rtb',np.bool),('account',np.int64),('campaign',np.str_,32),('banner',np.int64),('spotbuy',np.bool),('app_id',np.int64),('device',np.str_,32),('token_check',np.str_,32),('clicks',np.int64),('conv',np.int64)])

dtested1 = np.dtype([('token',np.str_,32),('site',np.str_,32),('add',np.str_,32),('country',np.str_,32),('rtb',np.str_,32),('account',np.str_,32),('campaign',np.str_,32),('banner',np.str_,32),('spotbuy',np.str_,32),('app_id',np.str_,32),('device',np.str_,32),('token_check',np.str_,32),('clicks',np.str_,32),('conv',np.str_,32)])
#jair = np.array(['1sze','32785', '21761','219',True,'3675', '', '1','false', '', '4501', '1szge', 1, 1],dtype=dtested)

jair = np.array(('11oqxw', '18996', '22044', '82', 'false', '3038', '2075', '1', 'false', '', '4501', '1szge', '1', '1'),dtype=dtested1)
print np.append( jair, np.array(('11oqxw', '18996', '22044', '82', 'false', '3038', '2075', '1', 'false', '', '4501', '1szge', '1', '1'),dtype=dtested1)) 

jair = np.append( jair, np.array(('11oqxw', '18996', '22044', '82', 'false', '3038', '2075', '1', 'false', '', '4501', '1szge', '1', '1'),dtype=dtested1 ))
#jair = np.append( jair, np.array(['11oqxw', '18996', '22044', '82', 'false', '3038', '2075', '1', 'false', '', '3998', '11oqxw', '0', '0\n'], dtype=dtested1))


print "jair",jair
tmp = InFile2("test.tsv")
for tmpi in mylist:
	print tuple(tmpi), len(tmpi)
	jair = np.append( jair, np.array(tuple(tmpi),dtype=dtested1) )

print "finaal", jair
#print "finaaaal", np.array(jair)


def InFile3( filename ):
	readinlines = ()
	for line in   tuple(open(filename, 'r')):
		print line
		i
		tmp_line = line.split('\t')
		readinlines.append(tmp_line)
	return  readinlines #np.array(readinlines)

tmp= InFile3("test.tsv")


