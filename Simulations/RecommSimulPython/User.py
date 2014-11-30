__author__ = 'jair'

import sys, random, math
import numpy as np
import pandas as pd

import MyPandasUtilities as mypd
import MyAlgebra as myalg
#----------------------------------------------------------------------------------------------------------------------#

def rand_genHist(ItemsColl, NbofEls = 10):
    '''
        gener. random history of items within Data Keyword Dictionary...
    '''
    sizeHist = random.randint(1, NbofEls)
    sizeItems = len(ItemsColl)-1
    lshist = []
    [ lshist.append(ItemsColl[random.randint(0, sizeItems)]) for i in xrange(sizeHist) ]
    return lshist

def AI_geHistory(user ,itemsCol, prefMatrix, featMatrix, NbofEls =10):
    '''
        gener. history of items based on user's preferences:
        sigmoid on the top of a Utility function with stoch. noise
    '''
    sizeHist = NbofEls #random.randint(1, NbofEls)
    #probas = map(lambda x : myalg.sigmoid(myalg.Utilityfct(user, x, psuser.PrefMatrix, psdata.kwordMatrix)), listotal)
    probas = map(lambda x : myalg.sigmoid(myalg.Utilityfct(user, x, prefMatrix, featMatrix)), itemsCol)
    lshist = []
    for i in xrange(sizeHist):
        lshist.append(myalg.userChoice(probas))
    return lshist

def vectorise0 (Idx, dframe, Dict, param = "pref"):
    '''vectorise prefs in respect with data dictionary'''
    v0 = np.zeros(len(Dict))
    if param == "pref":
        for i in dframe[dframe["idU"] == Idx]["pref"]:
            v0[np.searchsorted(Dict,i)] += 1
    '''
    elif param == "history":
        for i in dframe[dframe["idU"] == Idx]["history"]:
            v0[np.searchsorted(Dict,i)] += 1
    else:
        print "User::vectorise0 error, param not recognised"
       '''
    return v0

def vectoriseHisto (Idx, dframe, itemsList):
    '''vectorise History'''
    v0 = np.zeros(len(itemsList))
    for i in dframe[dframe["idU"] == Idx]["history"]:
        v0[np.searchsorted(itemsList,i)] += 1
    return v0

def vectoriseTF_IDF(Idx, dframe, Dict, IDFvec):
    '''compute tf-idf vector'''
    v_tf = vectorise0(Idx, dframe, Dict)
    # recall tf is term_freq/max_z term_freq (within that doc.)
    v_tf = v_tf/np.max(v_tf) #equivalent to tf
    return [ v_tf[i]*IDFvec[i] for i in (range(0, len(Dict)))]

def hackfct( dataItems, dataDict, Mode, N ):
    hacfct = Users(dataItems, dataDict, Mode, N)
    return hacfct.PrefMatrix

class Users:
    ''' class simulating users '''
    def __init__(self, dataItems, dataDict, Mode, featMatrix = None, N = 1000):
        self.N = N
        '''data dict imported for now'''
        self.Dict = dataDict
        self.NDict = len(self.Dict)
        self.__dataItems = np.sort(dataItems)
        self.LItems = len(dataItems)
        self.__DataFile = "PseudoDATA/pseudousers.csv"
        self.__dframeHeads = ["idU","pref","history"]

        if (Mode == "GenerateRand"):
            mydf = mypd.myDframe(self.__dframeHeads)
            for idx in range(0,self.N):
                rdVals = rand_genHist(self.__dataItems) #this is ~user's history of interactions
                pref = random.randint(0,self.NDict-1) #this is ~user's preference
                [ mydf.Append([idx, pref, item]) for item in rdVals ]

            mydf.DoFrame()
            self.dframe = mydf.PDFrame
            del mydf
            self.dframe.to_csv(self.__DataFile)

        elif (Mode == "Read"):
            self.dframe = pd.read_csv(self.__DataFile)
        elif (Mode == "GenerateAI"):
            '''
                hack!!! generating an instance through an external function to get the prefmatrix
                and use it for a "dynamical" generation of users history
            '''
            prefMat = hackfct(self.__dataItems, self.Dict, "GenerateRand",self.N)
            mydf = mypd.myDframe(self.__dframeHeads)
            for idx in range(0,self.N):
                rdVals = AI_geHistory( idx ,self.__dataItems, prefMat, featMatrix, NbofEls = 10)
                pref = random.randint(0,self.NDict-1) #this is ~user's preference
                [ mydf.Append([idx, pref, item]) for item in rdVals ]

            mydf.DoFrame()
            self.dframe = mydf.PDFrame
            del mydf
            self.dframe.to_csv(self.__DataFile)

        else:
            print("User::Pbm in Data Reading/Generation")
            sys.exit()

        '''data from dataframe into vector, matrices and tf_idf vectors/matrices'''
        self.PrefMatrix = self.prefsMatrix()
        self.IDFmatrix = self.prefsMatrix() #for now...
        self.IDFvector = self.compIDFvector()
        self.dataMatrix = self.dataTF_IDFMatrix()
        '''similarity("pref") matrix across data'''
        self.simDataMatTF_IDF = np.dot(self.dataMatrix, np.transpose(self.dataMatrix))
        '''history matrix across data, whereas instance<~>rating'''
        self.dataItemsHist = self.dataHistoMatrix()
        self.Clusters = self.clustersDecompo()
        #self.inClusterList

    def clustersDecompo(self):
        clustersDecompo = np.zeros(self.N)
        for i in xrange(self.PrefMatrix.shape[1]):
            for j in np.nonzero(self.PrefMatrix[:,i]):
                clustersDecompo[j] = i
        return clustersDecompo

    def TF_IDFvec(self, id):
            v = vectoriseTF_IDF(id, self.dframe, self.Dict, self.IDFvector)
            return myalg.normVec(v)

    def Histvec(self, id):
        return vectoriseHisto(id, self.dframe, self.__dataItems)

    def CreateDictionary(self):
        return np.sort(np.unique(self.dframe[self.__dframeHeads[1]])) # "kword"

    def prefsMatrix(self):
        '''computes pref matrix:'''
        IDFmat = np.zeros((self.N,self.NDict))
        for idx in xrange(0,self.N):
            for kw in self.dframe[self.dframe[self.__dframeHeads[0]] == idx][self.__dframeHeads[1]]: # "id" "history"
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

    def dataHistoMatrix(self):
        '''translates users history into numpy matrix shape NxNDict:'''
        dataMat = np.zeros((self.N, self.LItems))
        for idx in xrange(self.N):
            for n, tmp in enumerate(self.Histvec(idx)):
                dataMat[idx, n] += tmp
        return dataMat
