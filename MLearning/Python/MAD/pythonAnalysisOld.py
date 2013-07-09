import io
import os
import csv 


def uniq(input):
  output = []
  for x in input:
    if x not in output:
      output.append(x)
  return output


def ImportFile( filename ):
	readinlines = []
	for line in  list( tuple(open(filename, 'r')) ):
		tmp_line = line.split('\t') #CorrLine(line.split('\t')) # file correct: fields 4 and 7 are not regular and are corrected!
		readinlines.append(tmp_line)
	return readinlines


def CorrLine( linename ):
	if len(linename) != 13:
		if linename[4] not in ['false', 'true']:
			linename.insert(3,"None")
		if linename[8] not in ['false', 'true']:
			linename.insert(6,"None")
	return	linename


def GetList( mylist, num ):
	GetList = uniq([row[num] for row in megaList])
	return GetList


def SubList ( listing ): # extract parameters considered relevant
	SubList = []
	for param in ['ad','country','bannertype']:
		SubList.append( listing[ fields.index(param) ])
	return SubList


def ClickedCoords( elems ): # stores clicked configs
	ClickedCoords = [[]]
	for elem in elems:
		ClickedCoords.append(SubList(elem))
	return uniq(ClickedCoords) 


def checkData(data, num):
	if( data[fields.index('token')] <> data[fields.index('token_check')] ):
		print 'Warning: line %d  is irregular, pbm token' % num, data, data[fields.index('token')], data[fields.index('token_check')]
	if data[fields.index('clicks')] not in ['0','1']:
		print 'Warning: line %d is irregular, pbm clicks' % num, data[fields.index('clicks')]
	if data[fields.index('convers')] not in ['0\n','1\n']:
                print 'Warning: line %d is irregular, pbm conversions' % num, data[fields.index('convers')]
	if data[fields.index('rtb')] not in ['true','false']:
		print 'Warning: line %s is irregular, pbm rtb' % num, data[fields.index('rtb')]
	if data[fields.index('spotbuy')] not in ['true','false']:
		print 'Warning: line %s is irregular, pbm spotbuy' % num,data[fields.index('spotbuy')]


#########################################
#		_main_()		#
#########################################


### IO and preparation ###
fields = ['token', 'site', 'ad', 'country', 'rtb', 'account', 'campaign', 'bannertype','spotbuy','app_id','device','token_check','clicks','convers']


megaList = ImportFile("sampletest.tsv")
lmegaList = len(megaList)
print "file length",  lmegaList 

for row, record in enumerate(megaList):
	#print record,record[fields.index('clicks')],record[fields.index('clicks')]
	checkData(record, row)


print "Params Analysis:"
for fi in ['site', 'ad', 'country', 'rtb', 'account', 'campaign', 'bannertype','spotbuy','app_id','device','clicks']:
	print fi, len( uniq([ tmp[fields.index(fi)] for tmp in megaList ]) )
	print uniq([ tmp[fields.index(fi)] for tmp in megaList ])


#print uniq([ tmp[fields.index('bannertype')] for tmp in megaList ])
### ANALYSIS ###
### analysis ###
