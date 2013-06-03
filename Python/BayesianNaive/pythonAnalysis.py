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
		tmp_line = CorrLine( line.split() ) # file correct: fields 4 and 7 are not regular and are corrected!
		readinlines.append(tmp_line)
	return readinlines


def CorrLine( linename ):
	if len(linename) != 13:
		if linename[4] not in ['false', 'true']:
			linename.insert(3,"None")
		elif linename[8] not in ['false', 'true']:
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


#########################################
#		_main_()		#
#########################################


### IO and preparation ###
fields = ['token', 'site', 'ad', 'country', 'rtb', 'account', 'campaign', 'bannertype','spottbuy','app_id','device','token','clicks']
megaList = ImportFile("sample.tsv")


### analysis ###
nb_clicks = 0
listclicked = []
for tmp in megaList:
	if float(tmp[11]) == 1: # click?
		nb_clicks += 1
		listclicked.append(tmp)
	
# store configuations summarised to the parameters considered
clickedCoord = ClickedCoords( listclicked ) 

# store counts information within counter list
countList = []
for i in range(len(clickedCoord)):
	countList.append([0,0]) 
for run in megaList:
	tmp = SubList(run)
	if tmp in clickedCoord:
		countList[clickedCoord.index(tmp)][0] += 1
		if float(run[11]) == 1: 
			countList[clickedCoord.index(tmp)][1] += 1


# final analysis and output
for run in megaList:
	tmp = SubList(run)
	if tmp in clickedCoord:
		# probability comput. see explanations
		p_click = float(len(listclicked))/len(megaList)
		p_AgivenClick =  float(countList[clickedCoord.index(tmp)][1])/nb_clicks 
		p_A = float(countList[clickedCoord.index(tmp)][0])/(len(megaList))
		p_final = p_AgivenClick*p_click/p_A

		print run[0], p_final 
	else:
		print run[0], 0.0




