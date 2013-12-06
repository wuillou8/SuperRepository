#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      wuiljai
#
# Created:     18/11/2013
# Copyright:   (c) wuiljai 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import sys, string

#-General Utility Fcts----------------------------------------------------------

''' local utility lambda                                                     '''
__parseStr = lambda x: x.isalpha() and x or x.isdigit() and \
                            int(x) or x.isalnum() and x or \
                            len(set(string.punctuation).intersection(x)) == 1 and \
                            x.count('.') == 1 and float(x) or x

def findRange( array ):
    ''' fct checks if panda series elements are floats,
        if yes, it translates it into range(min, max, incr), if possible...  '''

    try:
        array = [ float(__parseStr(array[i])) for i in range(len(array)) ]
        array.sort()
    except:
        return False

    N = len(array)-1
    Min = array[0]
    Max = array[N]
    incr = ( Max - Min ) / N

    for i in range(N):
        if array[i] != Min + i*incr:
            return False

    return  Min, Max, incr

def FilterInput(In, Range):
    # check Input content against array of expected values
    if (In not in Range):
        sys.exit( "Comput Mode must be in " + str(Range))
    return In