import random, sys
import numpy as np
import Data #as *
import User #as *
import MyPandasUtilities as mypd
import MyAlgebra


def pickRand(N, liste, excluded = []):
    '''pick random item within a list where "excluded" elemenst where filtred out'''
    pickRand=[]
    liste = [x for x in liste if x not in excluded]
    pickRand.append(liste.pop(random.randint(0,len(liste)-1)))
    for n in xrange(N-1):
        pickRand.append(liste.pop(random.randint(0,len(liste)-1)))
    return pickRand

def recommender(user, cluster, usersRatingsMat, NbOfRecomm = 2):
    '''recommender "machine", doing item-based collaborative filtering'''
    Nitems = usersRatingsMat.shape[1]
    recommScores, recommList = [], []
    [recommScores.append(0) for i in xrange(NbOfRecomm)]
    recommList = pickRand(NbOfRecomm, range(usersRatingsMat.shape[1]))

    for it in xrange(Nitems):
        rec = recommenderScore(user, it, cluster, usersRatingsMat)

        if (rec > np.min(recommScores)):
            idex = recommScores.index(np.min(recommScores))
            recommList.pop(idex), recommScores.pop(idex)
            recommList.append(it), recommScores.append(rec)

    return recommScores, recommList

def recommenderScore(user, item, cluster, usersRatingsMat):
    '''Item-based recommendation score'''
    sizeCluster = cluster.shape[0]
    recommenderScore = 0.
    for j in xrange(sizeCluster):
        recommenderScore += usersRatingsMat[j, item]
    return 1.*recommenderScore/sizeCluster
