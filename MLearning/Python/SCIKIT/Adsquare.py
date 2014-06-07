
## Analysis for Adsquare

# This my analysis for the adsquare Data Science Teaser.
# I am using iPython and Python packages like scikit, panda, numpy, scipy and others.
# This is a summary of the most successfull analyses and I have chosen this format because I find it
# practical to display both methods and code.

##### import libraries and some specifications:

# In[6]:

import sys, math, json, itertools, warnings
import pandas as pd
import numpy as np
import pylab as pl
from sklearn import linear_model, datasets
from sklearn.decomposition import PCA
from sklearn.preprocessing import  scale
from IPython.display import display, Math, Latex

warnings.simplefilter(action = "ignore", category = FutureWarning)
warnings.simplefilter(action = "ignore", category = DeprecationWarning)
get_ipython().magic(u'matplotlib inline')


##### load data:

# In[142]:

file_ = 'adsquare_teaser_dataMay2014.json'
dframe = pd.DataFrame( json.load(open(file_)) )


##### Summarising data: 

# In[8]:

dframe.describe()


# Out[8]:

#               Earning       Index          X1          X2          X3          X4          X5       Zeta
#     count  100.000000  100.000000  100.000000  100.000000  100.000000  100.000000  100.000000  26.000000
#     mean    68.987725   49.500000   11.036567    3.429383    1.066958   -1.625202    6.665725   0.008950
#     std    207.069287   29.011492    6.639703    9.099960    1.611464   12.649626    8.888543   3.178287
#     min   -441.872612    0.000000   -2.868187  -13.615200   -1.909986  -23.268849  -16.501386  -5.737756
#     25%    -53.370111   24.750000    6.166075   -3.367730   -0.202271  -12.698001    0.451811  -2.118379
#     50%     71.848425   49.500000   11.110337    2.057958    1.236681   -2.898435    7.078727  -0.531868
#     75%    206.180674   74.250000   16.332492   11.564573    2.064181    9.628537   12.921400   1.479583
#     max    485.608414   99.000000   23.837957   23.377158    5.298393   23.530120   24.825712   6.653498

# plotting: Earning, X1, X2, X3, X4, X5, Zeta vs itself

# At first sight, one notice correlations for samples combinations (Earning,X4), (Zeta,X4).

# In[144]:

axes = pd.tools.plotting.scatter_matrix(dframe[['X1','X2','X3','X4','X5','Earning','Zeta']], color="brown")
#The plot below can be extended manually


# Out[144]:

# image file:

##### Correlation Analysis:

# For doing the correlation analysis, I need a few functions that I quickly design myself. 
# (I have crosschecked them against standard packages outputs). These functions are defined and commented on below.

# In[141]:

''' quick power x_array -> x_array**2 '''
def power( np_arr, N ):
    power = []
    [ power.append(tmp**N) for tmp in np_arr ] 
    return np.array( power )
''' quick equal for lists with O(1e-16) precision '''
def equal(l_a, l_b):
    for i in xrange(len(l_a)):
        if not abs(l_a[i] - l_b[i]) < 1e-6:
            return False
    return True
''' Correlation for normalised data (lists) '''
def corr(l1, l2):
    if not equal([len(l1),l1.mean(),l2.mean(),l1.std(),l2.std()],[len(l2),0.,0.,1.,1.]):
        print 'error in corr::input'
        sys.exit()
    return np.dot( l1, l2 )/len(l1)
''' Corrects the student test for pearson correlation
    Pearson correlation is not distributed exactly as a gaussian around 0 and 1.
    The Fisher z-trafo accounts for that.
    ***average is then log((1.+\rho)/(1.-\rho)), std_err is \sqrt(1/(N-3)) '''
def fisherZtrafo(r):
    if (r == 1.):
        return 1000000
    elif (r == 0.):
        return 0.
    else:
        return .5*math.log((1+r)/(1-r))
''' test Hypothesis H_0: zero correlation '''
def testH_0( n, r, Zeta = 0 ):
    testH_0 = ( fisherZtrafo( math.fabs(r) )-fisherZtrafo( math.fabs(Zeta) ) )*( n - 3 )**.5
    if ( testH_0 > 1.96 ):
        return False
    else:
        return True


# As next step, I measure how data is correlated, first looking at correlation between the different features and earnings
# Then, I also consider powers of the features (include basical nonlinear models).

# In[10]:

'''    Preprocess Data    '''
_columns = ['Earning', 'X1', 'X2', 'X3', 'X4', 'X5', 'Zeta']
X = np.array(dframe[['X1','X2','X3','X4','X5']])
_X = scale(X) #'''----normalize X----'''
X1, X2, X3, X4, X5 = _X[:,0], _X[:,1], _X[:,2], _X[:,3], _X[:,4]
Y = scale( np.array(dframe['Earning']) )


# Measure correlations Earning VS {X1,X2,X3,X4,X5} and test Hypothesis H_0: uncorrelated data

# In[11]:

data = [X1, X2, X3, X4, X5]
print 'featureVSfeature, correlation, test uncorrelated H_0'
for _n, x in enumerate( data ):
    R, n = corr(Y,x), len(x)
    if testH_0( n, R ) == False:
        print  ' Earning : X'+str(_n+1) , R, testH_0( n, R )


# Out[11]:

#     featureVSfeature, correlation, test uncorrelated H_0
#      Earning : X2 0.244926747919 False
#      Earning : X4 -0.802798595971 False
#     

# Measure correlations between elements {X1,X2,X3,X4,X5} and test Hypothesis H_0: uncorrelated data: 

# In[28]:

print 'featureVSfeature, correlation, test uncorrelated H_0'
for _n, x in enumerate( data ):
    for _m, y in enumerate( data[(_n+1):] ):
        R, n = corr(y,x), len(x)
        if testH_0( n, R ) == False:
            print ' X'+str((_n+1))+' : X'+str(_n+_m+2), R, testH_0( n, R )


# Out[28]:

#     featureVSfeature, correlation, test uncorrelated H_0
#     

# Measure correlations Earning VS {X1,X2,X3,X4,X5} and test Hypothesis H_0: uncorrelated data for different powers of
# {X1,X2,X3,X4,X5}

# Checked is corr( Y, pow(X, N) )

# In[29]:

print  'power, featureVSfeature, correlation, test uncorrelated H_0'
for _n, x in enumerate( data ):
    for _pow in range(2,5):
        x = scale( power( x, _pow ) )
        R, n = corr(Y,x), len(x)
        if testH_0( n, R ) == False:
            print  'power', _pow, ', Y : X'+str(_n+1) , R, testH_0( n, R )


# Out[29]:

#     power, featureVSfeature, correlation, test uncorrelated H_0
#     power 2 , Y : X4 -0.199834919763 False
#     power 3 , Y : X4 -0.330585516939 False
#     power 4 , Y : X4 -0.22271889492 False
#     

##### Fits, Linear Regressions:

# Even though the X1,X3,X5 features can statistically be considered indep. of Earning, I found the
# best regression score as all {X1,X2,X3,X5} were included. The algorithm is a standard last square linear regression.

# In[137]:

Y = np.array(dframe['Earning'])
X_, X__, X___ = np.array(dframe[['X4']]), np.array(dframe[['X4','X2']]),                     np.array(dframe[['X4','X1','X2','X3','X5']])

regr1, regr2, regr3 = linear_model.LinearRegression(), linear_model.LinearRegression(),                             linear_model.LinearRegression()
regr1.fit(X_, Y), regr2.fit(X__, Y), regr3.fit(X___,Y)
Y1D, Y2D, YmultiD = regr1.predict(X_), regr2.predict(X__), regr3.predict(X___)

print 'Y vs X1, score: ', regr1.score(X_,Y), len(regr1.coef_)
print 'Y vs [X4,X2], score: ', regr2.score(X__,Y), len(regr2.coef_)
print 'Y vs [X1,X2,X3,X4,X5], score: ', regr3.score(X___,Y), len(regr3.coef_)

title = 'plot Earning vs '
legend1, legend2, legend3 = ['1D fit X4','fitted pts'], ['2D fitted pts X4,X2'], ['5D fitted pts']

fig, axes = pl.subplots(figsize=(14,5))
pl.subplot(1,3,1)
pl.title(title+str(' 1D fit')), pl.xlabel('feature X4'), pl.ylabel('Earning')
pl.scatter(X_, Y,  color='black')
pl.plot(X_, regr1.predict(X_), color='blue', linewidth=1)
pl.plot(X_, Y1D, 'r*' )
pl.legend(legend1, loc='upper right')

pl.subplot(1,3,2)
pl.title(title+str(' 2D fit')), pl.xlabel('feature X4'), pl.ylabel('Earning')
pl.scatter(X_, Y,  color='black')
pl.plot(X_, Y2D, 'bx' )
pl.legend(legend2, loc='upper right');

pl.subplot(1,3,3)
pl.title(title+str(' 5D fit')), pl.xlabel('feature X4'), pl.ylabel('Earning')
pl.scatter(X_, Y,  color='black')
pl.plot(X_, YmultiD, 'gx' )
pl.legend(legend3, loc='upper right');


# Out[137]:

#     Y vs X1, score:  0.644485585694 1
#     Y vs [X4,X2], score:  0.684973860474 2
#     Y vs [X1,X2,X3,X4,X5], score:  0.702094667987 5
#     

# image file:

# Parameters of the 2D linear model: 

# In[138]:

display(Math(r'Model: \quad \vec Y = \alpha \vec X_4 + \beta \vec X_2 + h,'))
display(Math(r'\alpha = '+str(regr2.coef_[0])+',')) , display(Math(r'\beta = '+str(regr2.coef_[1])+',')), display(Math(r'h = '+str(regr2.intercept_)+'.'));


# Out[138]:

# image file:

# image file:

# image file:

# image file:

#### Fitting Zeta:

# In[ ]:

For Zeta, we repeat the same variance analysis as for Earning, but now earnings becomes a variable, we look at
Zeta VS {X1,X2,X3,X4,X5,Earning}. We see that Zeta is correlated primarily with X4 and Earnings.


# In[134]:

''' preprocessing '''
df = dframe.dropna()
_headers = ['X1','X2','X3','X4','X5','Earning']
_X = scale(np.array(df[['X1','X2','X3','X4','X5','Earning']]))
Y = scale( np.array(df['Zeta']) )
X1, X2, X3, X4, X5, E = _X[:,0], _X[:,1], _X[:,2], _X[:,3], _X[:,4], _X[:,5]

''' Same analysis as above '''
data = [X1, X2, X3, X4, X5, E]
print 'featureVSfeature, correlation, test uncorrelated H_0'
for _n, x in enumerate( data ):
    R, n = corr(Y,x), len(x)
    if testH_0( n, R ) == False:
        print  'Zeta : '+str(_headers[_n]) , R, testH_0( n, R )
        
''' checking powers of X1,X2, .. '''
for _n, x in enumerate( data ):
    for _pow in range(2,5):
        x = scale( power( x, _pow ) )
        R, n = corr(Y,x), len(x)
        if testH_0( n, R ) == False:
            print  'power', _pow, 'Zeta : '+str(_headers[_n]) , R, testH_0( n, R )


# Out[134]:

#     featureVSfeature, correlation, test uncorrelated H_0
#     Zeta : X4 0.951561682841 False
#     Zeta : Earning -0.73608208576 False
#     power 3 Zeta : X4 0.311662793951 False
#     power 4 Zeta : X4 0.221332188038 False
#     power 3 Zeta : Earning 0.263160233415 False
#     power 4 Zeta : Earning 0.269084471723 False
#     

##### Fits: 

# In[135]:

Y = np.array(df['Zeta'])
X_, X__, X___ = np.array(df[['X4']]), np.array(df[['X4','Earning']]),                     np.array(df[['X4','X1','X2','X3','X5','Earning']])
regr1, regr2, regr3 = linear_model.LinearRegression(), linear_model.LinearRegression(),                             linear_model.LinearRegression()
regr1.fit(X_, Y), regr2.fit(X__, Y), regr3.fit(X___,Y)
Y1D, Y2D, YmultiD = regr1.predict(X_), regr2.predict(X__), regr3.predict(X___)

print 'Y vs X1, score: ', regr1.score(X_,Y), len(regr1.coef_)
print 'Y vs [X4,Earning], score: ', regr2.score(X__,Y), len(regr2.coef_)
print 'Y vs [X1,X2,X3,X4,X5,Earning], score: ', regr3.score(X___,Y), len(regr3.coef_)

title = 'Zeta( '
legend1, legend2, legend3 = ['1D fit','fitted pts'], ['2D fitted pts'], ['5D fitted pts']

fig, axes = pl.subplots(figsize=(18,6))
pl.subplot(1,3,1)
pl.title(title+str(' 1D fit )')), pl.xlabel('feature X4'), pl.ylabel('Earning')
pl.scatter(X_, Y,  color='black')
pl.plot(X_, regr1.predict(X_), color='blue', linewidth=1)
pl.plot(X_, Y1D, 'r*' )
pl.legend(legend1, loc='lower right')

pl.subplot(1,3,2)
pl.title(title+str(' 2D fit )')), pl.xlabel('feature X4'), pl.ylabel('Zeta')
pl.scatter(X_, Y,  color='black')
pl.plot(X_, Y2D, 'bx' )
pl.legend(legend2, loc='lower right')

pl.subplot(1,3,3)
pl.title(title+str(' 5D fit )')), pl.xlabel('feature X4'), pl.ylabel('Zeta')
pl.scatter(X_, Y,  color='black')
pl.plot(X_, YmultiD, 'gx' )
pl.legend(legend3, loc='lower right');


# Out[135]:

#     Y vs X1, score:  0.905469636251 1
#     Y vs [X4,Earning], score:  0.907648241144 2
#     Y vs [X1,X2,X3,X4,X5,Earning], score:  0.960316681916 6
#     

# image file:

# 2D model coeffs: 

# In[136]:

display(Math(r'Model: \quad \vec Y = \alpha \vec X_4 + \beta \vec {Earning} + h,'))
display(Math(r'\alpha = '+str(regr2.coef_[0])+',')) , display(Math(r'\beta = '+str(regr2.coef_[1])+',')), display(Math(r'h = '+str(regr2.intercept_)+'.'));


# Out[136]:

# image file:

# image file:

# image file:

# image file:

##### Fit the NaN in Zeta and Print data out into Json format

# We correct the NaNs with the 2D linear model defined above.

# In[101]:

title, legend = 'Zeta( X4 )', ['data avail.','2D fitted pts (X4,Earning)','1D fit (X4)']
pl.figure(figsize=(10, 6))

pl.plot(np.array(df[['X4']]), np.array(df[['Zeta']]), 'bo')
pl.plot( np.array(dframe[['X4']]), regr2.predict(dframe[['X4','Earning']]), 'rx' )
pl.plot( np.array(df[['X4']]), regr.predict(np.array(df[['X4']])), 'b--')
pl.xlabel('X4'), pl.ylabel('Zeta')
pl.title(title), pl.legend(legend, loc='lower right');


# Out[101]:

# image file:

# Replace NaNs with fitted values and print out into file OutputJW.json

# In[90]:

_fit2D = regr2.predict(dframe[['X4','Earning']])
for i in np.where(dframe['Zeta'].isnull())[0]:
    dframe['Zeta'].iloc[i] = _fit2D[i]

_fileOut = open("OutputJW.json", "w")
_fileOut.write(dframe.reset_index().to_json())
_fileOut.close()


#### Additional analyses:

# In[ ]:

Additional analyses investigating for more scenarios in the data.


# In[139]:

'''     Check for clusters   '''
from sklearn.datasets.samples_generator import make_blobs
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import DBSCAN
from sklearn import metrics

X_headers = ['Earning','X1','X2','X3','X4','X5']
X = np.array(dframe[['Earning','X1','X2','X3','X4','X5']])
X = StandardScaler().fit_transform(X)

# Compute DBSCAN
_cluster = False
for size in xrange(2,5):
    for i in itertools.permutations(X_headers, size):  
        X = np.array(dframe[list(i)])
        db = DBSCAN(eps=0.3, min_samples=10).fit(X)
        core_samples = db.core_sample_indices_
        labels = db.labels_
        # Number of clusters in labels, ignoring noise if present.
        n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
        if (n_clusters_ > 0):
            _cluster = True
            print i, ' -*- ' , n_clusters_
            
if ( _cluster == False ):
    print 'No Clusters found'


# Out[139]:

#     No Clusters found
#     
