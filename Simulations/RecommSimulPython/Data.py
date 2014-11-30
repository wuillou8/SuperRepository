__author__ = 'jair'

import sys, random, math
import numpy as np
import pandas as pd

import MyPandasUtilities as mypd
import MyAlgebra as myalg
#----------------------------------------------------------------------------------------------------------------------#

def rand_genFeed(rangeEls, NbofEls = 2):
    '''generates random numbers of random numbers... '''
    size = random.randint(1, NbofEls)
    ls = []
    [ ls.append(random.randint(0, rangeEls-1)) for i in xrange(size) ]
    return np.unique(ls)

def vectorise0 (Idx, dframe, Dict):
    '''vectorise in respect with data dictionary'''
    v0 = np.zeros(len(Dict))
    for i in dframe[dframe["id"] == Idx]["kword"]:
        v0[np.searchsorted(Dict,i)] += 1
    return v0

def vectoriseTF_IDF(Idx, dframe, Dict, IDFvec):
    '''compute tf-idf vector'''
    v_tf = vectorise0(Idx, dframe, Dict)
    # recall tf is term_freq/max_z term_freq (within that doc.)
    v_tf = v_tf/np.max(v_tf) #equivalent to tf
    return [ v_tf[i]*IDFvec[i] for i in (xrange(len(Dict)))]


class PseudoData:
    ''' pseudo data for prototype '''
    def __init__(self, Mode, N = 1000, Nfeats = 10):
        self.N = N
        self.Nfeats = Nfeats
        self.__DataFile = "PseudoDATA/pseudofeeds.csv"
        self.__dframeHeads = ["id","kword"]
        if (Mode == "Generate"):
            mydf = mypd.myDframe( self.__dframeHeads )
            for idx in range(0,self.N):
                rdVals = rand_genFeed(self.Nfeats)
                [ mydf.Append([idx, tmp]) for tmp in rdVals ]

            mydf.DoFrame()
            self.dframe = mydf.PDFrame
            del mydf
            self.dframe.to_csv(self.__DataFile)

        elif (Mode == "Read"):
            self.dframe = pd.read_csv(self.__DataFile)
        else:
            print("PseudoData::Pbm in Data Reading/Generation", Mode)
            sys.exit()

        self.Dict = self.CreateDictionary() #\.sort(np.unique(self.data["kword"]))
        self.NDict = len(self.Dict)
        '''data from dataframe into vector, matrices and tf_idf vectors/matrices'''
        self.kwordMatrix = self.compPrefmatrix()
        self.IDFmatrix = self.compPrefmatrix() # for now...
        self.IDFvector = self.compIDFvector()
        self.dataMatrix = self.dataTF_IDFMatrix()
        '''similarity matrix across data'''
        self.simDataMatTF_IDF = np.dot(self.dataMatrix, np.transpose(self.dataMatrix))


    def TF_IDFvec(self, id):
        v = vectoriseTF_IDF(id, self.dframe, self.Dict, self.IDFvector)
        return myalg.normVec(v)

    def CreateDictionary(self):
        return np.sort(np.unique(self.dframe[self.__dframeHeads[1]])) # "kword"

    def compPrefmatrix(self):
        '''computes IDF matrix:'''
        IDFmat = np.zeros((self.N,self.NDict))
        for idx in xrange(0,self.N):
            for kw in self.dframe[self.dframe[self.__dframeHeads[0]] == idx][self.__dframeHeads[1]]: # "id" "kword"
                IDFmat[idx, np.searchsorted(self.Dict,kw)] = 1
        return IDFmat

    def compIDFvector(self):
        '''computes IDF vector from matrix:'''
        IDFvec = np.zeros(self.NDict)
        for idDict in xrange(0,self.NDict):
            IDFvec[idDict] = math.log(self.N/np.sum( self.IDFmatrix[:, idDict] ))
        return IDFvec

    def simTF_IDFMatrix(self):
        '''computes TFIDF similarity matrix:'''
        TF_IDFmat = np.zeros((self.N,self.N))
        for ix in xrange(self.N):
            for iy in xrange(self.N):
                v_x = self.TF_IDFvec(ix)
                v_y = self.TF_IDFvec(iy)
                TF_IDFmat[ix][iy] = Algebra.similarity0(v_x, v_y)
        return TF_IDFmat
        # if we work with metadata
        #for ix in xrange(0,self.NDict):
        #   for iy in xrange(O, self.NDict):

    def dataTF_IDFMatrix(self):
        '''translates data into tf_idf numpy matrix shape NxNDict:'''
        dataMat = np.zeros((self.N, self.NDict))
        for idx in xrange(self.N):
            for n, tmp in enumerate(self.TF_IDFvec(idx)):
                dataMat[idx, n] = tmp
        return dataMat


class Feed:
    '''class Feeds, do we need that class?'''
    def __init__(self, content):
        self._kword = self.parser(content)
        self._size = len(self._kword)

    def parser(self, content):
        return content
