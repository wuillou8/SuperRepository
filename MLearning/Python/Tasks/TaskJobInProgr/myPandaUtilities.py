#-------------------------------------------------------------------------------
# Name:        MyPandaUtilities
# Purpose:
#
# Author:      wuillou8
#
# Created:     25/10/2013
# Copyright:   (c) wuiljai 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import sys
import numpy as np
import pandas as pd


def uniq(input):
  output = []
  for x in input:
    if x not in output:
      output.append(x)
  return output


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def myLazyDispl(dframe):
    # Displays 10 els of the DataFrame head & tail
    if (dframe.shape[0] >= 10):
        print dframe.head(5)
        print "   ...  ...  ...   "
        print dframe.tail(5)
    else:
        print dframe.head()

def myfilter(df,arrFilter,arrFields = []):
    ''' Filters the data frame:
        Args:
        arg1: [arg1_00, arg1_01, ... , arg1_N0, arg1_N1] == the conditions on the fields (pairs are expected).
        arg2: [arg2_0, arg2_1, ...] == fields filtered out.
        Usage:
        df = myfilter( dfff, ["Line_id",1,"Trip_id",1] == VOID, ['field1', 'field2'] == VOID) '''

    sizeFilter = len(arrFilter)
    sizeFields = len(arrFields)

    if np.mod(sizeFilter, 2) != 0:
        print ' wrong argument number passed '
        sys.exit(0)

    if sizeFilter != 0:
        #iterative filtering
        for n_i in range(0,sizeFilter/2):
            field1 = arrFilter[2*n_i]
            field2 = arrFilter[2*n_i+1]
            df = df[ df[field1] == field2 ]

    if sizeFields == 0:
        return df
    else:
        return df[arrFields]

def FilterInput(In, Range):
    # check Input content against array of expected values
    if (In not in Range):
        sys.exit( "Comput Mode must be in " + str(Range))
    return In

def dframesDiff( dffrom, dfto ):
    ''' get differences beetween 2 dframes '''
    #print dffrom.head(10)
    #print dfto.head(10)
    ne_stacked = (dffrom != dfto).stack()
    changed = ne_stacked[ne_stacked]
    changed.index.names = ['id', 'col']
    diff_idxs = np.where(dffrom != dfto)
    changed_from = dffrom.values[diff_idxs]
    changed_to = dfto.values[diff_idxs]
    return changed, changed_from, changed_to



''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class myDframe:
    '''
        Generic class to init/load Panda Dataframe
    '''
    def __init__(self, args):
        self.__args = args
        self.__Size = len(args)
        self.__inArr = [ [] for tmp in range(self.__Size) ]

    def Append(self, arr):
        self.__Check(arr)
        [ self.__inArr[idx].append(arr[idx]) for idx in range(self.__Size) ]

    def DoFrame(self):
        DoFrame = {}
        [ DoFrame.update( {self.__args[idx] : self.__inArr[idx]} ) for idx in range(self.__Size) ]
        self.PDFrame = pd.DataFrame( DoFrame )
        del self.__inArr
        del DoFrame

    def __Check(self, lst):
        if (len(lst) != self.__Size):
            sys.exit( 'error: Load PDaDFrame Failed (myPandaUtilities::myDframe)' )


class DataTree:
    '''
        DataTree
    '''
    def __init__( self, COORDS):

        self.COORDS = COORDS
        # grid
        self.Max = 25
        self.grid = np.zeros( ( self.Max, len(self.COORDS) ) )
        self.gridWght = np.zeros( ( self.Max, len(self.COORDS) ) )
        self.points = []


    def AnalysisDic( self, listFiles, listCoords, listToNbs ):
        print 'dico: '
        self.listFiles = listFiles
        self.listCoords = listCoords
        self.listToNbs = listToNbs

        self.points.append( [0,self.listCoords,self.listToNbs,0] )

        #print self.listFiles
        #print 'coords', self.listCoords
        #print 'destins', self.listToNbs
        #print 'tests', self.listToNbs[1]

    def Analysis1D( self, listFiles, listCoords, listToNbs ):
        #print 'dico 1D: dico'
        self.listFiles1 = listFiles
        self.listCoords1 = listCoords
        self.listToNbs1 = listToNbs

        for i in range(len(self.listFiles1)):
            self.points.append( [1,self.listCoords1[i],self.listToNbs1[i],i] )

        print self.listFiles1
        print 'coords1', self.listCoords1
        print 'destins1', self.listToNbs1

    def Analysis2D( self, listFiles, listCoords, listToNbs ):
        #print 'dico 2D: dico'
        self.listFiles2 = listFiles
        self.listCoords2 = listCoords
        self.listToNbs2 = listToNbs

        for i in range(len(self.listFiles2)):
            self.points.append( [2,self.listCoords2[i],self.listToNbs2[i],i] )

        print self.listFiles2
        print 'coords2', self.listCoords2
        print 'destins2', self.listToNbs2

    def Analysis3D( self, listFiles, listCoords, listToNbs ):
        #print 'dico 3D: dico'
        self.listFiles3 = listFiles
        self.listCoords3 = listCoords
        self.listToNbs3 = listToNbs

        for i in range(len(self.listFiles3)):
            self.points.append( [3,self.listCoords3[i],self.listToNbs3[i],i] )
        print self.listFiles3
        print 'coords3', self.listCoords3
        print 'destins3', self.listToNbs3
'''
    def AlgorithmTree(self):
        AlgorithmTree = []
        tmp = self.Dist(36, 35)
        print tmp
        print self.Dist(36, 35)
        self.InitFilter()

    def InitFilter(self):
        InitFilter = []
        L = len(points)
        for i in range(L):

            if ( i < (len(points)-1) ): # and i not eq j
                count = 0
                for j in range(points):

                    if self.Dist( i, j ) == 1:
                        count += 1
                if ( count == 0  ):
                    points.pop(i)
                if ( count > 1 ):
                    InitFilter.append(i)

        print 'get rid of ', L - len(points[])
        return InitFilter



    def LookForTrees(self):
        L = len(points)
        for i in range(L):
            for j in range(points):
                if (i != j):
                    if self.Dist( i, j ) == 1:
                        link i,j dir



        # fpr j in range(points):




    def Dist(self, Npoint1, Npoint2):
        print self.points[Npoint1], self.points[Npoint2]
        if ( len( self.points[Npoint1][1] ) > len( self.points[Npoint2][1] ) ):
            self.distance( Npoint1, Npoint2 )
        else:
            self.distance( Npoint2, Npoint1 )

    def distance(self, Npoint1, Npoint2):
        # distance bool ( 0 = False / 1 = True )
        #if ( (self.points[Npoint1][0] == 3) & (self.points[Npoint2][0] == 1) ):
        if ( self.points[Npoint1][0] == self.points[Npoint2][0] ):
            distance = 0
            print 'la0'
            return 0
        else:
            distance = 0
            pt1coor = self.points[Npoint1][1]
            pt2coor = self.points[Npoint2][1]
            pt1 = self.points[Npoint1][2]
            pt2 = self.points[Npoint2][2]
            print 'la'
            for i in pt1coor:
                if ( i in pt2coor ):
                    if ( pt1[pt1coor.index(i)] != pt2[pt2coor.index(i)] ):
                        distance += 1
            print 'distance', distance
            if distance == 1:
                print 'ici'
                distance = 1
            else:
                distance = 0

        return distance
'''



        #for coord1 in Npoint1:
        #    for coord2 in Nbpoint2:
        #return 0
    #self.points.append( [0,self.listCoords,self.listToNbs,0] )





