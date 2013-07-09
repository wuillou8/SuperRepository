import io
import os
import csv
import string
import re
import sys

from numpy import *


def ImportFile( filename ):
	readinlines = []
	for line in  list( tuple(open(filename, 'r')) ):
 		tmp_line = CorrLine( line.split('\t') ) # file correct: fields 4 and 7 are not regular and are corrected!
		if(len(tmp_line)) == 13:
			readinlines.append(tmp_line)
		else:
			print "error",tmp_line #sys.exit("error, not enough elements!")
	return readinlines


def CorrLine( linename ):
	if len(linename) != 13:
		if linename[4] not in ['false', 'true']:
			linename.insert(3,"None")										
		if linename[8] not in ['false', 'true']:
			linename.insert(6,"None")										
	return	linename


testValname = "tmp"
#jair = genfromtxt(StringIO(testValname),delimiter=1)
#jair = loadtxt(dtype='float', delimiter=",")
#mylist = ImportFile("tmp")
#print mylist


#for tmp in mylist:
#	print len(tmp)
reader = csv.reader(open("sample.tsv", "rb"), 
		                    delimiter='\t', quoting=csv.QUOTE_NONE)
print reader

header = []
records = []
fields = 14

#if thereIsAHeader: header = reader.next()

for row, record in enumerate(reader):
	if len(record) != fields:
		print "Skipping malformed record", record, row, array(record), len(record)
		#%i, contains %i fields (%i expected)" %(record, len(record), fields)
	else:
		records.append(record)



