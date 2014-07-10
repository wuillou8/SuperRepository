
###### Load libs:

# In[1]:

import sys, math, scipy, json, itertools, warnings
import pandas as pd
import numpy as np
import pylab as pl
from sklearn import linear_model, datasets
from sklearn.decomposition import PCA
from sklearn.preprocessing import scale
from IPython.display import display, Math, Latex
from matplotlib.backends.backend_pdf import PdfPages

warnings.simplefilter(action = "ignore", category = FutureWarning)
warnings.simplefilter(action = "ignore", category = DeprecationWarning)
get_ipython().magic(u'matplotlib inline')


###### Load Data:

# In[5]:

dataFile_ = 'Trading\\trades.json'
dframe =  pd.DataFrame( json.load(open(dataFile_)) )

''' extract Asks&Bids '''
dframeAsks = dframe[dframe['Type']==0]
dframeBids = dframe[dframe['Type']==1]

''' load Depth::Asks & Bids separately '''
asksFile_ = 'Trading\\btcusdAsks.json'
dfasks = pd.DataFrame( json.load(open(asksFile_)) )
bidsFile_ = 'Trading\\btcusdBids.json'
dfbids = pd.DataFrame( json.load(open(bidsFile_)) )

''' Data Summary '''
dframe.describe()


# Out[5]:

#                  Amount        Price              Tid         Type
#     count  2.000000e+03  2000.000000      2000.000000  2000.000000
#     mean   1.172246e-01   458.126833  40044692.062000     0.656500
#     std    3.197781e-01     4.323213     43442.240417     0.474995
#     min    1.000000e-08   452.442000  39922594.000000     0.000000
#     25%    1.681400e-02   455.000000  40023197.250000     0.000000
#     50%    3.877070e-02   456.526000  40063410.500000     1.000000
#     75%    9.537685e-02   461.002000  40065430.750000     1.000000
#     max    6.323270e+00   468.000000  40121542.000000     1.000000

# In[6]:

dframe.head() 


# Out[6]:

#          Amount  Price       Tid             Timestamp  Type
#     0  0.018406  458.0  40121542  2014-07-09T08:42:13Z     0
#     1  0.010599  458.0  40121541  2014-07-09T08:42:12Z     1
#     2  0.041238  458.9  40121436  2014-07-09T08:32:07Z     0
#     3  0.028762  458.9  40121435  2014-07-09T08:32:06Z     0
#     4  0.040000  458.9  40120872  2014-07-09T08:13:26Z     1

# In[7]:

dframe.tail()


# Out[7]:

#             Amount    Price       Tid             Timestamp  Type
#     1995  0.039515  462.227  39923327  2014-07-04T21:56:05Z     0
#     1996  0.013546  462.227  39923325  2014-07-04T21:56:04Z     0
#     1997  0.012222  462.227  39923299  2014-07-04T21:55:22Z     0
#     1998  0.026904  462.700  39922674  2014-07-04T21:45:36Z     1
#     1999  0.000318  462.700  39922594  2014-07-04T21:45:04Z     0

###### Summary:     Data contains ~4 days     data size 184 kB     ==> 25000 kB a year (1.5*365/4*184)

# In[3]:

fig, axes = pl.subplots(figsize=(14,7))
pl.subplot(1,2,1)
title = ' Bids & Asks '
legend = ['Asks','Bids']
pl.plot(dframeAsks['Price'],'g-')
pl.plot(dframeBids['Price'],'b-')

pl.title(title)
pl.ylabel('Price'), pl.xlabel('TradeNb')
pl.legend(legend, loc='upper left')
pl.subplot(1,2,2)
title = ' Bids & Asks '
legend = ['Asks','Bids']
pl.plot(dframeAsks['Amount'],'m-')
pl.plot(dframeBids['Amount'],'r-')
pl.title(title)
pl.ylabel('Amount'), pl.xlabel('TradeNb')
pl.legend(legend, loc='upper left');


# Out[3]:

# image file:

# In[6]:

#dfBids.head()
#dfBids.tail()
x = pd.datetime(2014, 7, 8, 11, 1)
y = pd.datetime(2014, 7, 8, 6, 30)
z = pd.datetime(2014, 7, 8, 10, 0)
print x, y
#print xx, yy
#print dfBids.ix[z]


# Out[6]:


    ---------------------------------------------------------------------------
    NameError                                 Traceback (most recent call last)

    <ipython-input-6-e496e4f999f0> in <module>()
          6 print x, y
          7 #print xx, yy
    ----> 8 print dfBids.ix[z]
    

    NameError: name 'dfBids' is not defined


#     2014-07-08 11:01:00 2014-07-08 06:30:00
#     

# In[7]:

dfBids.head()


# Out[7]:


    ---------------------------------------------------------------------------
    NameError                                 Traceback (most recent call last)

    <ipython-input-7-97c90e048e54> in <module>()
    ----> 1 dfBids.head()
    

    NameError: name 'dfBids' is not defined


# In[ ]:

df['20130419':'20130422']


# In[42]:

print dfbids.head()
print dfbids.tail()


# Out[42]:

#          Amount    Price
#     0  0.716445  452.603
#     1  0.669000  452.443
#     2  1.000000  452.442
#     3  0.203254  452.441
#     4  1.010245  452.000
#            Amount    Price
#     145  0.340000  322.000
#     146  0.300000  321.002
#     147  0.019019  321.000
#     148  5.540900  320.000
#     149  0.035118  319.000
#     

# In[43]:

dframe.head()


# Out[43]:

#          Amount                  Date  Item    Price  PriceCurrency       Tid  Type
#     0  0.165436  2014-07-08T11:01:08Z     0  457.497              1  40098326     0
#     1  0.049866  2014-07-08T11:01:07Z     0  457.497              1  40098322     1
#     2  0.016774  2014-07-08T11:00:01Z     0  452.603              1  40098300     0
#     3  0.055912  2014-07-08T11:00:00Z     0  452.603              1  40098299     0
#     4  0.232969  2014-07-08T11:00:00Z     0  452.603              1  40098296     0

# In[16]:

dFile_ = 'Trading\\trades3.json'
df =  pd.DataFrame( json.load(open(dFile_)) )
''' extract Asks&Bids '''
dfAsks = df[df['Type']==0]
dfBids = df[df['Type']==1]


# In[21]:

df.head()


# Out[21]:

#          Amount  Price       Tid             Timestamp  Type
#     0  0.018406  458.0  40121542  2014-07-09T08:42:13Z     0
#     1  0.010599  458.0  40121541  2014-07-09T08:42:12Z     1
#     2  0.041238  458.9  40121436  2014-07-09T08:32:07Z     0
#     3  0.028762  458.9  40121435  2014-07-09T08:32:06Z     0
#     4  0.040000  458.9  40120872  2014-07-09T08:13:26Z     1

# In[24]:

fig, axes = pl.subplots(figsize=(14,7))
pl.subplot(1,2,1)
title = ' Bids & Asks '
legend = ['Asks','Bids']
pl.plot(dfAsks['Price'],'r-')
pl.plot(dfBids['Price'],'b-')

pl.title(title)
pl.ylabel('Price'), pl.xlabel('TradeNb')
pl.legend(legend, loc='upper left')
pl.subplot(1,2,2)
title = ' Bids & Asks '
legend = ['Asks','Bids']
pl.plot(dfAsks['Amount'],'m-')
pl.plot(dfBids['Amount'],'g-')
pl.title(title)
pl.ylabel('Amount'), pl.xlabel('TradeNb')
pl.legend(legend, loc='upper left')

pp = PdfPages('foo.pdf')
fig.savefig(pp, format='pdf') 
pp.close();


# Out[24]:

# image file:

# In[20]:

df[df['Tid']==40107964]


# Out[20]:

#           Amount    Price       Tid             Timestamp  Type
#     38  0.077634  459.997  40107964  2014-07-08T20:17:11Z     1

# In[ ]:



