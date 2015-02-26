"""
	Python script writing excel files into csv
	usage: 
		python excelintocsv.py myexcelsheet.xlsm --> myexcelsheet.csv 
"""

import os, sys
import pandas as pd

def correct_unicode(x):
    """ correcting 'ascii' codec can't encode character u'\xbe'
    """
    if type(x) == unicode:
        return x.encode('utf')
    return x

if len(sys.argv) != 2:
	print "one file name expected"

print sys.argv[1]

filename = "GUCCI Test products V3.xlsm"
try:
	xl = pd.ExcelFile(filename)

except:
	print "file could not be read"

try:
	names = xl.sheet_names
	df = xl.parse(names[0])
except: 
	print "error in parting the first sheet: ", names[0]
	sys.exit(1)

try:
	df = df.applymap(lambda x: correct_unicode(x))
	df.to_csv(filename[0:-4]+'csv')
except:
	print "error outputting/intocsvying"
	sys.exit(1)

print filename[0:-4]+'csv'," was successfully created"

