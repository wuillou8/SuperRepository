__author__ = 'jair'

import sys, random, math
import pylab as pl
import numpy as np
import Data #as *
import User #as *
import MyPandasUtilities as mypd
import MyAlgebra as myalg
import MyRecomm as myrec

################################
##      glob vars             ##
################################
nFeats = 10
nItems = 100
nUsers = 50

nbRuns = 10
#random.seed(17)


###############################
# user data interaction fcts ##
###############################
def run0(modeUserChoice, recommOnOff):
    '''
        runs the interaction user//data//recommender
        mode: "sigmoid" or "random"
    '''
    stat = []
    for i in xrange(nbRuns):
        psdata = Data.PseudoData("Generate", nItems)
        psuser = User.Users(range(psdata.N), psdata.Dict, "GenerateAI", psdata.kwordMatrix, nUsers)

        statRec = 0
        for user in xrange(psuser.N):
            if recommOnOff == "on":
                #extract users's cluster
                pref = np.nonzero(psuser.PrefMatrix[0])[0][0]
                cluster = np.nonzero(psuser.PrefMatrix[:,pref])[0]
                scores, prelistRecomm = myrec.recommender(user, cluster, psuser.dataItemsHist)
            elif recommOnOff == "off":
                prelistRecomm = myrec.pickRand(2, range(psdata.N))

            prelistRandom = myrec.pickRand(4, range(psdata.N), prelistRecomm)
            listotal = prelistRandom + prelistRecomm
            if len(mypd.uniq(listotal)) != len(listotal):
                print "duplicated items", prelistRandom , prelistRecomm
                sys.exit(1)
            #else:
            #    print "pass"

            probas = map(lambda x : myalg.sigmoid(myalg.Utilityfct(user, x, psuser.PrefMatrix, psdata.kwordMatrix)), listotal)

            if modeUserChoice == "sigmoid":
                picked = listotal[myalg.userChoice(probas)]
            elif modeUserChoice == "random":
                picked = myrec.pickRand(1, listotal)[0]

            if picked in prelistRecomm:
                statRec += 1

        print i, "stat: ", modeUserChoice, recommOnOff, 1.*statRec/psuser.N
        stat.append(1.*statRec/psuser.N)
    return np.mean(stat), np.std(stat)

def run1(modeUserChoice, recommOnOff):
    '''
        Dynamical version:
        runs the interaction user//data//recommender
        mode: "sigmoid" or "random"
    '''
    psdata = Data.PseudoData("Generate", nItems)
    psuser = User.Users(range(psdata.N), psdata.Dict, "GenerateAI", psdata.kwordMatrix, nUsers)
    stat = []
    for sweep in xrange(nbRuns):

        statRec = 0
        for user in xrange(psuser.N):
            if recommOnOff == "on":
                #extract users's cluster
                pref = np.nonzero(psuser.PrefMatrix[0])[0][0]
                cluster = np.nonzero(psuser.PrefMatrix[:,pref])[0]
                scores, prelistRecomm = myrec.recommender(user, cluster, psuser.dataItemsHist)
            elif recommOnOff == "off":
                prelistRecomm = myrec.pickRand(2, range(psdata.N))

            prelistRandom = myrec.pickRand(4, range(psdata.N), prelistRecomm)
            listotal = prelistRandom + prelistRecomm
            if len(mypd.uniq(listotal)) != len(listotal):
                print "duplicated items", prelistRandom , prelistRecomm
                sys.exit(1)
            #else:
            #    print "pass"

            probas = map(lambda x : myalg.sigmoid(myalg.Utilityfct(user, x, psuser.PrefMatrix, psdata.kwordMatrix)), listotal)

            if modeUserChoice == "sigmoid":
                picked = listotal[myalg.userChoice(probas)]
            elif modeUserChoice == "random":
                picked = myrec.pickRand(1, listotal)[0]

            psuser.dataItemsHist[user,picked] += 1
            if picked in prelistRecomm:
                statRec += 1

        print sweep, "stat: ", modeUserChoice, recommOnOff, 1.*statRec/psuser.N
        print "max ", np.max(psuser.dataItemsHist)
        stat.append(1.*statRec/psuser.N)
    return np.mean(stat), np.std(stat)

##########################################
### MAIN                                ##
##########################################
psdata = Data.PseudoData("Generate", nItems, nFeats)
#psdata = Data.PseudoData("Read", nItems)

#psuser = User.Users(range(psdata.N), psdata.Dict, "GenerateAI", psdata.kwordMatrix, nUsers)
#psuser = User.Users(range(psdata.N), psdata.Dict, "GenerateRand", None, nUsers)
#psuser = User.Users(range(psdata.N), psdata.Dict, "Read", None, nUsers)

statsigmoid1 = run1("sigmoid", "on")
#statsrandom1 = run0("random", "on")

#statsigmoid2 = run0("sigmoid", "off")
#statsrandom2 = run0("random", "off")

print "sigmoid__on", statsigmoid1 #, np.mean(statsigmoid)
#print "random__on", statsrandom1 #, np.mean(statsrandom)

#print "sigmoid__of", statsigmoid2 #, np.mean(statsigmoid)
#print "random__of", statsrandom2 #, np.mean(statsrandom)