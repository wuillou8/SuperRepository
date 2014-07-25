
# In[2]:

get_ipython().magic(u'matplotlib inline')


# In[1]:

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


# In[3]:

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/00275/'+'Bike-Sharing-Dataset.zip'
Dir = 'Data/'
CopyOnlineRate( url, Dir )
Decompress( url, Dir )


# Out[3]:

#     Downloading: Data/Bike-Sharing-Dataset.zip Bytes: 279992
#           8192  [2.93%]      16384  [5.85%]      24576  [8.78%]      32768  [11.70%]      40960  [14.63%]      49152  [17.55%]      57344  [20.48%]      65536  [23.41%]      73728  [26.33%]      81920  [29.26%]      90112  [32.18%]      98304  [35.11%]     106496  [38.04%]     114688  [40.96%]     122880  [43.89%]     131072  [46.81%]     139264  [49.74%]     147456  [52.66%]     155648  [55.59%]     163840  [58.52%]     172032  [61.44%]     180224  [64.37%]     188416  [67.29%]     196608  [70.22%]     204800  [73.14%]     212992  [76.07%]     221184  [79.00%]     229376  [81.92%]     237568  [84.85%]     245760  [87.77%]     253952  [90.70%]     262144  [93.63%]     270336  [96.55%]     278528  [99.48%]     279992  [100.00%] 
#      file:  ['Readme.txt', 'day.csv', 'hour.csv']
#     

# In[5]:

import pandas as pd
'''read in the files into pandas dataframe'''
Dir = 'Data/'
dfday = pd.read_csv(Dir+'day.csv')
dfhour = pd.read_csv(Dir+'hour.csv')


# In[6]:

print dfday.head(5)
#print dfhour.head(2)


# Out[6]:

#        instant      dteday  season  yr  mnth  holiday  weekday  workingday  \
#     0        1  2011-01-01       1   0     1        0        6           0   
#     1        2  2011-01-02       1   0     1        0        0           0   
#     2        3  2011-01-03       1   0     1        0        1           1   
#     3        4  2011-01-04       1   0     1        0        2           1   
#     4        5  2011-01-05       1   0     1        0        3           1   
#     
#        weathersit      temp     atemp       hum  windspeed  casual  registered  \
#     0           2  0.344167  0.363625  0.805833   0.160446     331         654   
#     1           2  0.363478  0.353739  0.696087   0.248539     131         670   
#     2           1  0.196364  0.189405  0.437273   0.248309     120        1229   
#     3           1  0.200000  0.212122  0.590435   0.160296     108        1454   
#     4           1  0.226957  0.229270  0.436957   0.186900      82        1518   
#     
#         cnt  
#     0   985  
#     1   801  
#     2  1349  
#     3  1562  
#     4  1600  
#     

# In[7]:

import scipy
'''Analysis'''
#print dfday.describe()
print dfday.columns


# Out[7]:

#     Index([u'instant', u'dteday', u'season', u'yr', u'mnth', u'holiday', u'weekday', u'workingday', u'weathersit', u'temp', u'atemp', u'hum', u'windspeed', u'casual', u'registered', u'cnt'], dtype='object')
#     

# In[32]:

import numpy as np
''' vs Season '''
seasons = np.unique( dfday['season'] )
windspeed = np.unique( dfday['windspeed'] )
humid = np.unique( dfday['hum'] )
temper = np.unique( dfday['temp'] )
atemper = np.unique( dfday['atemp'] )
np.linspace(2.0, 3.0, num=5)
weathersit = np.unique( dfday['weathersit'] ) # [1, 2, 3]
holiday = np.unique( dfday['holiday'] ) # [0 1]
weekday = np.unique( dfday['weekday'] ) # [0 1 2 3 4 5 6]
#seasons are in [1,2,3,4]
#print seasons
for i in seasons:
    print i, np.mean( dfday[ dfday['season'] == i ]['cnt'] ),    np.std( dfday[ dfday['season'] == i ]['cnt'] )


# Out[32]:

#     1 2604.13259669 1396.06951975
#     2 4992.33152174 1691.36232198
#     3 5644.30319149 1455.91275698
#     4 4728.16292135 1694.8343366
#     

# In[33]:

print weathersit
print holiday
print weekday
#print windspeed
#print humid
#print temper
#print temper
print seasons


# Out[33]:

#     [1 2 3]
#     [0 1]
#     [0 1 2 3 4 5 6]
#     [1 2 3 4]
#     

# In[ ]:




# In[65]:

#from sklearn.feature_selection import VarianceThreshold
#X = [[0, 0, 1], [0, 1, 0], [1, 0, 0], [0, 1, 1], [0, 1, 0], [0, 1, 1]]
#sel = VarianceThreshold(threshold=(.8 * (1 - .8)))
#sel.fit_transform(X)


# In[94]:

y = dfday['cnt']
X = dfday[['season','yr','mnth','holiday','weekday','workingday','weathersit','temp','atemp','hum','windspeed']] #,'casual','registered']]
#X = dfday[['temp','atemp','hum','windspeed']]


# In[13]:

axes = pd.tools.plotting.scatter_matrix(dfday[['season','yr','mnth','holiday','weekday','workingday','weathersit','temp','atemp','hum','windspeed','cnt']], color="brown")


# Out[13]:

# image file:

# In[ ]:




# In[8]:

from sklearn.datasets import load_iris
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.ensemble import ExtraTreesClassifier
#iris = load_iris()
y = dfday['cnt']
X = dfday[['season','yr','mnth','holiday','weekday','workingday','weathersit','temp','atemp','hum','windspeed']] #,'casual','registered']]

clf = ExtraTreesClassifier()
X_new = clf.fit(X, y).transform(X)
#print X_new.shape
#print clf.feature_importances_
for n,i in enumerate(clf.feature_importances_):
    if i > 0.1:
        print n, dfday.columns[n]


# Out[8]:

#     2 season
#     7 workingday
#     8 weathersit
#     9 temp
#     10 atemp
#     

# In[ ]:




# In[96]:

from sklearn.svm import LinearSVC
#from sklearn.datasets import load_iris
#iris = load_iris()
#X, y = iris.data, iris.target
print X.shape
X_new = LinearSVC(C=0.01, penalty="l1", dual=False).fit_transform(X, y)
X_new.shape


# Out[96]:

#     (731, 11)
#     

#     (731, 4)

# In[101]:

print type(X)
print type(X_new)
print X.head(1)
X_new[0]


# Out[101]:

#     <class 'pandas.core.frame.DataFrame'>
#     <type 'numpy.ndarray'>
#        season  yr  mnth  holiday  weekday  workingday  weathersit      temp  \
#     0       1   0     1        0        6           0           2  0.344167   
#     
#           atemp       hum  windspeed  
#     0  0.363625  0.805833   0.160446  
#     

#     array([ 1.,  1.,  6.,  2.])

# In[9]:

from sklearn.datasets import make_friedman1
from sklearn.feature_selection import RFECV
from sklearn.svm import SVR
estimator = SVR(kernel="linear")
selector = RFECV(estimator, step=1, cv=5)
selector = selector.fit(X, y)
selector.support_ 
#array([ True,  True,  True,  True,  True,
#        False, False, False, False, False], dtype=bool)
selector.ranking_


# Out[9]:

#     array([1, 1, 1, 6, 2, 3, 1, 1, 1, 4, 5])

# In[12]:

for n,i in enumerate(selector.ranking_):
    if (i == 1):
        print 'YES', n, X.columns[n]
    else:
        print 'NO ', n, X.columns[n]


# Out[12]:

#     YES 0 season
#     YES 1 yr
#     YES 2 mnth
#     NO  3 holiday
#     NO  4 weekday
#     NO  5 workingday
#     YES 6 weathersit
#     YES 7 temp
#     YES 8 atemp
#     NO  9 hum
#     NO  10 windspeed
#     

# In[ ]:

2 season
7 workingday
8 weathersit
9 temp
10 atemp


# In[105]:

features = [ 'season','yr','mnth','holiday','weekday','workingday','weathersit','temp','atemp','hum','windspeed' ]
#['instant','dteday','season','yr','mnth','holiday','weekday','workingday',
#'weathersit', u'temp', u'atemp', u'hum', u'windspeed', u'casual', u'registered', u'cnt']


# In[20]:

import pylab as pl


# In[35]:

pl.subplot(1,7,1)
pl.plot(dfday['season'], dfday['cnt'], 'x')
pl.subplot(1,7,2)
pl.plot(dfday['mnth'], dfday['cnt'], 'x')
pl.subplot(1,7,3)
pl.plot(dfday['holiday'], dfday['cnt'], 'x')
pl.subplot(1,7,4)
pl.plot(dfday['weekday'], dfday['cnt'], 'x')
pl.subplot(1,7,5)
pl.plot(dfday['workingday'], dfday['cnt'], 'x')
pl.subplot(1,7,6)
pl.plot(dfday['weathersit'], dfday['cnt'], 'x')
pl.subplot(1,7,7)
pl.plot(dfday['temp'], dfday['cnt'], 'x')
#pl.show()


# Out[35]:

#     [<matplotlib.lines.Line2D at 0x1afd36b0>]

# image file:

# In[ ]:




# In[40]:

pl.subplot(1,4,1)
pl.plot(dfday['temp'], dfday['cnt'], 'x')
pl.subplot(1,4,2)
pl.plot(dfday['atemp'], dfday['cnt'], 'x')
pl.subplot(1,4,3)
pl.plot(dfday['atemp'], dfday['hum'], 'x')
pl.subplot(1,4,4)
pl.plot(dfday['atemp'], dfday['windspeed'], 'x')


# Out[40]:

#     [<matplotlib.lines.Line2D at 0x19517110>]

# image file:

# In[ ]:




# In[42]:

pl.plot(dfday['season'], dfday['cnt'], 'x')


# Out[42]:

#     [<matplotlib.lines.Line2D at 0x192df790>]

# image file:

# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:

literature:
    http://www.aaai.org/Papers/Symposia/Fall/1994/FS-94-02/FS94-02-034.pdf
        

