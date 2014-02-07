# -*- coding: utf-8 -*-
#
import pandas.io.data as web

import datetime

import re, io, os, csv, string
import MyPandaUtilities


### old IO ###
def ImportFile( filename ):
    readinlines = []
    for line in list( tuple(open(filename, 'r')) ):
        readinlines.append(filter(line))
    return readinlines

def filter ( string ):
    filter = re.sub(r'[ \n]+', '', string)
    return filter 
##############


start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2014, 2, 6)


DAXFile = "..//DAXData//DAXIndicesList.dat"
with open(DAXFile, 'r') as f:
    read_Symbols = f.read()
f.closed 

xlist = ImportFile(DAXFile)

'''
Importing rates time-series
'''
for i in xlist:
    print i, type(i)
    f=web.DataReader( i, 'yahoo', start, end)
    print 'rate : ', i
    MyPandaUtilities.myLazyDispl(f)
