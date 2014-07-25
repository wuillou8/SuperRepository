
# In[3]:

import pandas as pd
import time, datetime, json, csv , StringIO, gzip
import urllib, urllib2
import numpy as np
import matplotlib
import matplotlib.pyplot as plt


# In[4]:

''' 
    Function copying .gzip files from http://api.bitcoincharts.com/v1/csv/ 
    File copied into the directory ${Dir}/http:api.bitcoincharts.comv1csv.gz 
    EXAMPLE: PullOnlineRate('b7USD')
'''
def PullOnlineRate_gzip ( filename, Dir, Decompress = False,                     baseURL = 'http://api.bitcoincharts.com/v1/csv/', ending = '.csv.gz' ):
    
    url = baseURL + filename + ending 
    file_name = Dir+'/'+url.split('/')[-1]
    f = open(file_name, 'wb')
    u = urllib2.urlopen(url)
    meta = u.info()
    file_size = int(meta.getheaders("Content-Length")[0])
    print "Downloading: %s Bytes: %s" % (file_name, file_size)

    file_size_dl = 0
    block_sz = 8192
    while True:
        buffer = u.read(block_sz)
        if not buffer:
            break

        file_size_dl += len(buffer)
        f.write(buffer)
        status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
        status = status + chr(8)*(len(status)+1)
        print status,

    f.close()


# In[7]:

''' 
    Decompress into files into format .csv or json
    EXAMPLE: DecompressInto('b7USD.csv.gz', 'History', 'csv')
'''
def Decompress( filename, Dir ):
    
    start = time.clock()
    compressedFile = gzip.open( Dir+'/'+filename+'.csv.gz', 'rb' )
    f_out = open( Dir+'/'+filename+'.csv', 'wb' )
    f_out.writelines( compressedFile )
    f_out.close()
    elapsed = (time.clock() - start)
    print 'time for decompression: ', elapsed


def DecompressGZInto( filename, Dir, Format='csv' ):

    zfile = gzip.open(Dir+'/'+filename+'.csv.gz')
    file_name = filename[:(len(filename)-7)]
    
    ''' do DataFrame '''
    mydf = myDframe( ['unixtime', 'price', 'amount'] )
    for tm in zfile:
        mydf.Append([tm[0], tm[1], tm[2]])
    mydf.DoFrame()
    
    ''' print into files '''
    if ( Format == 'csv' ):
        mydf.PDFrame.to_csv(Dir+'/'+file_name+'.csv')
    elif (Format == 'json'):
        print Dir+'/'+filename+'.csv.gz'
        print Dir+'/'+file_name+'.json'
        mydf.PDFrame.to_json(Dir+'/'+file_name+'.json')
    else:
        print 'OutputFormat not recognised: csv OR json'
        sys.exit()


# In[9]:

''' Usage example : too slow for btcUSD
'''
Curr = 'btceUSD'
#PullOnlineRate_gzip(Curr,'History')
t_ini = time.clock()
#DecompressGZInto(Curr,'History','json')
Decompress(Curr,'History')
print time.clock() - t_ini


# Out[9]:

#     time for decompression:  49.4110690422
#     49.4114473988
#     

# In[5]:

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
            #print self.__Size, len(lst)
            sys.exit( 'error: Load PDaDFrame Failed' )

