#-------------------------------------------------------------------------------
# Name:        MyPandaUtilities
# Purpose:
#
# Author:      wuillou8
#
# Created:     25/10/2013
# Copyright:   (c) wuiljai 2013
# Licence:     <your licence>
#------------------------------------------------------------------------------
import sys
import numpy as np
import pandas as pd


def uniq(input):
  output = []
  for x in input:
    if x not in output:
      output.append(x)
  return output


#------------------------------------------------------------------------------

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

