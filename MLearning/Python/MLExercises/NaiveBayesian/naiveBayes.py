import io
import os
import csv 
import string
import re
import math


###	IO	###
def ImportFile( filename ):
	readinlines = []
	for line in  list( tuple(open(filename, 'r')) ):
		readinlines.append(filter(line))
	return readinlines

def filter ( string ):
	#print "ici", string
	filter = re.sub(r'[\t\n]+', '', string)
	filter = re.split(' ', filter)
	#print "ici" , filter
	filter = map(int, filter)
	return filter 

def uniq (input ):
  output = []
  for x in input:
    if x not in output:
      output.append(x)
  return output

def enum( mylist ): # N-Dim
	enum = list()
	num=1
	for tmp in range(0,len(mylist)):
		enum.append(num)
		num += 1
	enum = zip(enum, mylist)
	return [ list(row) for row in enum ]	

def getNbSpams( dico, featlist, lablist ):
	# dico: Nbword NbSpams nbSpams
	# featlist: Nbmail Nbword NbIt
	# lablist: Spam?
	getNbSpams = list()
	for tmp in dico:
		#print "dico", tmp
		stat = [ tmp[0], 0.0, 0.0 ] # phi_y=1, phi_y=0
		tm = [ i for i in featlist if i[1] == tmp[0] ] 
		#print "tm",  tm
		for t in tm:
			#print "step:", t, lablist[t[0]-1], lablist[t[0]-1][1], len(t)
			if lablist[t[0]-1][1] == 1:
				stat[1] += t[2]
			elif lablist[t[0]-1][1] == 0:	
				stat[2] += t[2]
			else:
				print "pbm in tablist alloc", t, lablist[t[0]-1]
				return
		getNbSpams.append(stat)
	return getNbSpams

def normProbs( mylist, dico ): # normalise probs as in 
	#http://openclassroom.stanford.edu/MainFolder/DocumentPage.php?course=MachineLearning&doc=exercises/ex6/ex6.html
	NbSpams = sum([ row[1] for row in mylist]) 
	NbNoSpams = sum([ row[2] for row in mylist]) 
	V = len(dico)
	normProbs = list()
	for li in mylist:
		li[1] = (li[1] + 1)/(NbSpams + V)	#prob spam
		li[2] = (li[2] + 1)/(NbNoSpams + V)	#prob non-spam
		normProbs.append(li)
	return normProbs

def getprobas( mylistEl, dico ):
	spam = 0.0
	nonspam = 0.0
	dic = [ row[0] for row in dico ]
	#for tmp in mylist:
	index = dic.index(mylistEl)
	print "index", index
	return index

########################################################################
########################	MAIN		########################
########################################################################

featlist = ImportFile("DATA/ex6DataPrepared/train-features.txt")
lablist = ImportFile("DATA/ex6DataPrepared/train-labels.txt")

dico = uniq([ row[1] for row in featlist ])
dico.sort()
dico = zip(dico, [0.0]*len(dico), [0.0]*len(dico)) # element #spam #nonspam

lablist = ( [ row[0] for row in lablist] ) # ImportFile("DATA/ex6DataPrepared/train-labels.txt") ])
phi_y =  float(sum(lablist))/len(lablist)
lablist =  enum(lablist)

#########################################
#	constrLISTS			#
#########################################
# dico:		Nbword NbSpams nbSpams
# featlist: 	Nbmail Nbword NbIt
# lablist: 	Nbmail Spam?(1 or 0)              

Max = len(lablist)
problist = getNbSpams( dico, featlist, lablist )
dico = normProbs(problist, dico) # normalise prob as in the exercise

#########################################
#		RUN			#
#########################################

l_feattest = ImportFile("DATA/ex6DataPrepared/test-features.txt")
l_labtest = ImportFile("DATA/ex6DataPrepared/test-labels.txt")
#resu_test = ImportFile("DATA/ex6DataPrepared/test-labels.txt")


l_labtest = enum(l_labtest)

spamsou = list()
dic = [ row[0] for row in dico ]
#print dic
#sys.exit()

for ii in range(1,len(l_labtest)+1):
	probSpam = 0.0
	probNonSpam = 0.0
	for tmp in l_feattest:
		#probSpam = 0.0
		#probNonSpam = 0.0
		#print "ii", ii, tmp
		if tmp[0] == ii:
			#print "dic", dic.index(tmp[0])
			if tmp[1] in dic:
				#print "dico", dico[dic.index(tmp[1])], dic.index(tmp[1])
				#print "tmp", tmp[2], dico[dic.index(tmp[1])], dico[dic.index(tmp[1])]
				probSpam += tmp[2]*dico[dic.index(tmp[1])][1] * 1.0 	
				probNonSpam +=  tmp[2]*float( dico[dic.index(tmp[1])][2] ) 	
		print "prbas", probSpam, probNonSpam
		spamsou.append([ii, probSpam, probNonSpam])


print spamsou
print phi_y
print math.log(spamsou[0][1]*phi_y) + math.log(phi_y), math.log(spamsou[0][2]*(1-phi_y)) + math.log(1-phi_y)
finalresult = list()
for tmp in spamsou:
	if  math.log(spamsou[0][1]*phi_y) + math.log(phi_y) >= math.log(spamsou[0][2]*(1-phi_y)) + math.log(1-phi_y):
		finalresult.append( [ spamsou[0], 1 ])
	else:
		finalresult.append( [ spamsou[0], 0 ])

print finalresult

