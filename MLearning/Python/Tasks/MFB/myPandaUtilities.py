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

def myLazyDispl(dframe):
    # Displays 10 els of the DataFrame head & tail
    print dframe.head(5)
    print "   ...  ...  ...   "
    print dframe.tail(5)

def myfilter(df,arrFilter,arrFields):
    # Filters the data frame:
    # Args:
    #   arg1: [arg1_00, arg1_01, ... , arg1_N0, arg1_N1] == the conditions on the fields (pairs are expected).
    #   arg2: [arg2_0, arg2_1, ...] == fields filtered out.
    # Usage:
    #   df = myfilter( dfff, ["Line_id",1,"Trip_id",1] == VOID, ['field1', 'field2'] == VOID)

    sizeFilter = len(arrFilter)
    sizeFields = len(arrFields)

    if np.mod(sizeFilter, 2) != 0:
        print " wrong argument number passed "
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
