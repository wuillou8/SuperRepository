__author__ = 'jair'

import sys, random, math
import pylab as pl
import numpy as np
import pandas as pd
import MyPandasUtilities as mypd
import Data, User
#----------------------------------------------------------------------------------------------------------------------#

def normVec(vec):
    return vec / np.sqrt(np.dot(vec, vec)) #np.linalg.norm(vec) #vec / np.sqrt(np.dot(vec, vec))

def similarity(vec1, vec2):
    return np.dot(vec1, vec2) / (normVec(vec1) * normVec(vec2))

##################
#pseudo AI ...

def userChoice(probas):
    '''
        pick up one particular item based on the proba
    '''
    mc = random.random()
    probas = probas / np.sum(probas)  #myalg.normVec(np.array(probas)) #normalise probas
    size, idx, probCumul = len(probas), 0, 1. #params
    for i in xrange(size):
        probCumul -= probas[i]
        if mc > probCumul:
            return i

    return size - 1

def Utilityfct(user, itemNb, prefMatrix, featMatrix):
    '''Basical utility function for user
        U = -const + alpha * (pref_user \dot feats_data) + epsilon
        epsilon is gaussian, random noise
    '''
    mu, sigma = 0, 0.5
    epsilon = np.random.normal(mu, sigma)
    #tuned by hand, I want ~90% of picking an item containing the user's favourite feature
    Utilityfct = -4.5 + 5.5*np.dot(prefMatrix[user], featMatrix[itemNb]) + epsilon
    return Utilityfct

def sigmoid(x):
  return 1. / (1. + math.exp(-x))

def plotsigmoid():
    X = np.arange(-5,5,.1)
    Y = map(lambda x : sigmoid(x), X)
    pl.plot(X,Y)
    pl.show()