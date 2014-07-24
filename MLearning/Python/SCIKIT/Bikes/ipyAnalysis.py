
# In[26]:

import urllib2, zipfile, gzip
import os
import os.path

def CopyOnlineRate ( url, Dir ):
    
    file_name = Dir+url.split('/')[-1]
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
    
def Decompress( url, Dir ):
    file_name = Dir+url.split('/')[-1]
    zfile = zipfile.ZipFile( file_name )
    print '\n file: ', zfile.namelist()
    # write files: ['Readme.txt', 'day.csv', 'hour.csv']
    for name in zfile.namelist():
        zfile.extract( name, Dir )


# In[28]:

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/00275/'+'Bike-Sharing-Dataset.zip'
Dir = 'Data/'
CopyOnlineRate( url, Dir )
Decompress( url, Dir )


# Out[28]:

#     Downloading: Data/Bike-Sharing-Dataset.zip Bytes: 279992
#           8192  [2.93%]      16384  [5.85%]      24576  [8.78%]      32768  [11.70%]      40960  [14.63%]      49152  [17.55%]      57344  [20.48%]      65536  [23.41%]      73728  [26.33%]      81920  [29.26%]      90112  [32.18%]      98304  [35.11%]     106496  [38.04%]     114688  [40.96%]     122880  [43.89%]     131072  [46.81%]     139264  [49.74%]     147456  [52.66%]     155648  [55.59%]     163840  [58.52%]     172032  [61.44%]     180224  [64.37%]     188416  [67.29%]     196608  [70.22%]     204800  [73.14%]     212992  [76.07%]     221184  [79.00%]     229376  [81.92%]     237568  [84.85%]     245760  [87.77%]     253952  [90.70%]     262144  [93.63%]     270336  [96.55%]     278528  [99.48%]     279992  [100.00%] 
#      file:  ['Readme.txt', 'day.csv', 'hour.csv']
#     

# In[32]:

import pandas as pd
'''read in the files into pandas dataframe'''
Dir = 'Data/'
dfday = pd.read_csv(Dir+'day.csv')
dfhour = pd.read_csv(Dir+'hour.csv')


# In[33]:

print dfday.head(2)
print dfhour.head(2)


# Out[33]:

#        instant      dteday  season  yr  mnth  holiday  weekday  workingday  \
#     0        1  2011-01-01       1   0     1        0        6           0   
#     1        2  2011-01-02       1   0     1        0        0           0   
#     
#        weathersit      temp     atemp       hum  windspeed  casual  registered  \
#     0           2  0.344167  0.363625  0.805833   0.160446     331         654   
#     1           2  0.363478  0.353739  0.696087   0.248539     131         670   
#     
#        cnt  
#     0  985  
#     1  801  
#        instant      dteday  season  yr  mnth  hr  holiday  weekday  workingday  \
#     0        1  2011-01-01       1   0     1   0        0        6           0   
#     1        2  2011-01-01       1   0     1   1        0        6           0   
#     
#        weathersit  temp   atemp   hum  windspeed  casual  registered  cnt  
#     0           1  0.24  0.2879  0.81          0       3          13   16  
#     1           1  0.22  0.2727  0.80          0       8          32   40  
#     

# In[34]:

import scipy
'''Analysis'''


# Out[34]:

#     'Analysis'

# In[ ]:



