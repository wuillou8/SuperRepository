
## Analysis for Adsquare

# This my analysis for the adsquare Data Science Teaser.
# I am using iPython and Python packages like scikit, panda, numpy, scipy and others.
# This is a summary of the most successfull analyses and I have chosen this format because I find it
# practical to display both methods and code.

##### import libraries and some specifications:

# In[92]:

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

# In[2]:

file_ = 'adsquare_teaser_dataMay2014.json'
dframe = pd.DataFrame( json.load(open(file_)) )


##### Summarising data: 

# In[87]:

dframe.describe()


# Out[87]:

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

# At first sight, one notice correlations for samples combinations (Earning,X4),(Zeta,X4).

# In[33]:

axes = pd.tools.plotting.scatter_matrix(dframe[['X1','X2','X3','X4','X5','Earning','Zeta']], color="brown")
#The plot below can be extended manually


# Out[33]:

# image file:

##### Correlation Analysis:

# For doing the correlation analysis, I need a few functions that I quickly design myself. 
# (I have crosschecked them against standard packages outputs). These functions are defined and commented on below.

# In[23]:

from scipy.stats import norm, t

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

'''
    Corrects the student test for pearson correlation
    Pearson correlation is not distributed exactly as a gaussian around 0 and 1.
    The Fisher z-trafo accounts for that.
    ***average is then log((1.+\rho)/(1.-\rho)), std_err is \sqrt(1/(N-3))
'''
def fisherZtrafo(r):
    if (r == 1.):
        return 1000000
    elif (r == 0.):
        return 0.
    else:
        return .5*math.log((1+r)/(1-r))
    
'''
    test Hypothesis H_0: zero correlation
'''
def testH_0( n, r, Zeta = 0 ):
    testH_0 = ( fisherZtrafo( math.fabs(r) )-fisherZtrafo( math.fabs(Zeta) ) )*( n - 3 )**.5
    if ( testH_0 > 1.96 ):
        return False
    else:
        return True


# As next step, I measure how data is correlated, first looking at correlation between the different features and earnings
# Then, I also consider powers of the features (include basical nonlinear models).

# In[25]:

'''    Preprocess Data    '''
_columns = ['Earning', 'X1', 'X2', 'X3', 'X4', 'X5', 'Zeta']
X = np.array(dframe[['X1','X2','X3','X4','X5']])
_X = scale(X) #'''----normalize X----'''
X1, X2, X3, X4, X5 = _X[:,0], _X[:,1], _X[:,2], _X[:,3], _X[:,4]
Y = scale( np.array(dframe['Earning']) )


# Measure correlations Earning VS {X1,X2,X3,X4,X5} and test Hypothesis H_0: uncorrelated data

# In[27]:

data = [X1, X2, X3, X4, X5]
print 'featureVSfeature, correlation, test uncorrelated H_0'
for _n, x in enumerate( data ):
    R, n = corr(Y,x), len(x)
    if testH_0( n, R ) == False:
        print  ' Earning : X'+str(_n+1) , R, testH_0( n, R )


# Out[27]:

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

# In[63]:

Y = np.array(dframe['Earning'])
X_, X__, X___ = np.array(dframe[['X4']]), np.array(dframe[['X4','X2']]),                     np.array(dframe[['X4','X1','X2','X3','X5']])

regr1, regr2, regr3 = linear_model.LinearRegression(), linear_model.LinearRegression(),                             linear_model.LinearRegression()
regr1.fit(X_, Y), regr2.fit(X__, Y), regr3.fit(X___,Y)
Y1D, Y2D, YmultiD = regr1.predict(X_), regr2.predict(X__), regr3.predict(X___)

print 'Y vs X1, score: ', regr1.score(X_,Y), len(regr1.coef_)
print 'Y vs [X4,X2], score: ', regr2.score(X__,Y), len(regr2.coef_)
print 'Y vs [X1,X2,X3,X4,X5], score: ', regr3.score(X___,Y), len(regr3.coef_)

title = 'plot Earning vs '
legend1, legend2, legend3 = ['1D fit','fitted pts'], ['2D fitted pts'], ['5D fitted pts']

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


# Out[63]:

#     Y vs X1, score:  0.644485585694 1
#     Y vs [X4,X2], score:  0.684973860474 2
#     Y vs [X1,X2,X3,X4,X5], score:  0.702094667987 5
#     

# image file:

# In[ ]:

Parameters of the 2D linear model: y = a*X1 + b*X2 + Id


# In[61]:

list(regr2.coef_)


# Out[61]:

#     [-12.960637179081733, 4.5855820603523032]

#### Fitting Zeta:

# In[ ]:

For Zeta, we repeat the same variance analysis as for Earning, but now earnings becomes a variable, we look at
Zeta VS {X1,X2,X3,X4,X5,Earning}. We see that Zeta is correlated primarily with X4 and Earnings.


# In[55]:

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
    x = scale( power( x, _pow ) )
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


# Out[55]:

#     featureVSfeature, correlation, test uncorrelated H_0
#     Zeta : X4 0.617877940651 False
#     Zeta : Earning 0.466334697707 False
#     power 2 Zeta : X4 0.500719178458 False
#     power 3 Zeta : X4 0.605305228444 False
#     power 4 Zeta : X4 0.455343278347 False
#     power 2 Zeta : Earning 0.445794780234 False
#     power 3 Zeta : Earning 0.497694397801 False
#     power 4 Zeta : Earning 0.521701957548 False
#     

##### Fits: 

# In[93]:


Y = np.array(df['Zeta'])
X_, X__, X___ = np.array(df[['X4']]), np.array(df[['X4','Earning']]),                     np.array(df[['X4','X1','X2','X3','X5','Earning']])
regr1, regr2, regr3 = linear_model.LinearRegression(), linear_model.LinearRegression(),                             linear_model.LinearRegression()
regr1.fit(X_, Y), regr2.fit(X__, Y), regr3.fit(X___,Y)
Y1D, Y2D, YmultiD = regr1.predict(X_), regr2.predict(X__), regr3.predict(X___)

print 'Y vs X1, score: ', regr1.score(X_,Y), len(regr1.coef_)
print 'Y vs [X4,Earning], score: ', regr2.score(X__,Y), len(regr2.coef_)
print 'Y vs [X1,X2,X3,X4,X5,Earning], score: ', regr3.score(X___,Y), len(regr3.coef_)

title = 'plot Zeta vs '
legend1, legend2, legend3 = ['1D fit','fitted pts'], ['2D fitted pts'], ['5D fitted pts']

fig, axes = pl.subplots(figsize=(14,5))
pl.subplot(1,3,1)
pl.title(title+str(' 1D fit')), pl.xlabel('feature X4'), pl.ylabel('Earning')
pl.scatter(X_, Y,  color='black')
pl.plot(X_, regr1.predict(X_), color='blue', linewidth=1)
pl.plot(X_, Y1D, 'r*' )
pl.legend(legend1, loc='lower right')

pl.subplot(1,3,2)
pl.title(title+str(' 2D fit')), pl.xlabel('feature X4'), pl.ylabel('Zeta')
pl.scatter(X_, Y,  color='black')
pl.plot(X_, Y2D, 'bx' )
pl.legend(legend2, loc='lower right');

pl.subplot(1,3,3)
pl.title(title+str(' 5D fit')), pl.xlabel('feature X4'), pl.ylabel('Zeta')
pl.scatter(X_, Y,  color='black')
pl.plot(X_, YmultiD, 'gx' )
pl.legend(legend3, loc='lower right');


# Out[93]:

#     Y vs X1, score:  0.835889343624 1
#     Y vs [X4,Earning], score:  0.8377106037 2
#     Y vs [X1,X2,X3,X4,X5,Earning], score:  0.874408304044 6
#     

# image file:

# 2D model coeffs: 

# In[65]:

list(regr2.coef_)


# Out[65]:

#     [0.23184589621746463, 0.0010111624214806207]

##### Fit the NaN in Zeta and Print data out into Json format

# In[ ]:

#regr = linear_model.LinearRegression()
#x_ = np.array(df[['X4','Earning']])
#regr.fit(x_, Y)

Yout = regr3.predict(X___)

pl.scatter( x4, Yout, color='black' )
pl.scatter( X4, Yout, color='blue' )
pl.scatter( X4, Yout, color='purple' )
#pl.plot( X4, regr.predict(X4), color='green', linewidth=1) 

NaNsList = np.where(dframe['Zeta'].isnull())[0]

#fill the NaN with the regression model
for i in NaNsList:
    dframe['Zeta'].iloc[i] = y[i]

tmp = dframe.reset_index().to_json()
text_file = open("Output.json", "w")
text_file.write(tmp)
text_file.close()


#### Additional analyses:

# In[ ]:

Additional analyses investigating for more scenarios in the data.


# In[14]:

'''
    Check for clusters
    no clusters found
'''
from sklearn.datasets.samples_generator import make_blobs
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import DBSCAN
from sklearn import metrics

X_headers = ['Earning','X1','X2','X3','X4','X5']
X = np.array(dframe[['Earning','X1','X2','X3','X4','X5']])
X = StandardScaler().fit_transform(X)
##############################################################################
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


# Out[14]:

#     No Clusters found
#     

# In[6]:

import sys
df = dframe.dropna()
'''
    Normalise Data
'''
X = np.array(df[['X1','X2','X3','X4','X5','Earning','Zeta']])
X_ = scale(X) #'''----normalize(X)----'''
X1, X2, X3, X4, X5, E, Z = X_[:,0], X_[:,1], X_[:,2], X_[:,3], X_[:,4], X_[:,5], X_[:,6]
Y = scale( np.array(df[['Earning']]) )
'''
    Analysis: against Y and data vs data
'''
data = [X1, X2, X3, X4, X5, Z]
for _n, x in enumerate( data ):
    for _pow in range(1,2):
        x = scale( power( x, _pow ) )
        R, n = corr(x,Y), len(x)
        print  'power ', _pow, ' Y : X'+str(_n+1) , R, testH_0( n, R )

for _n, x in enumerate( data ):
    for _m, y in enumerate( data[(_n+1):] ):
        R, n = corr(x,y), len(x)
        print ' X'+str((_n+1))+' : X'+str(_n+_m+2), R, testH_0( n, R )


# Out[6]:

#     power  1  Y : X1 [-0.1225373] (True, 0.5906364088585154)
#     power  1  Y : X2 [ 0.4046124] (False, 2.058140830904867)
#     power  1  Y : X3 [ 0.1292908] (True, 0.6235469336418955)
#     power  1  Y : X4 [-0.85485866] (False, 6.109543500593257)
#     power  1  Y : X5 [ 0.07928568] (True, 0.38104054527871484)
#     power  1  Y : X6 [-0.75942847] (False, 4.771197320101307)
#      X1 : X2 -0.207274073467 (True, 1.0086658068270948)
#      X1 : X3 0.0185716276655 (True, 0.08907663934285416)
#      X1 : X4 0.2659976675 (True, 1.3071124035897612)
#      X1 : X5 0.36898618752 (True, 1.8571809223517113)
#      X1 : X6 0.28466416443 (True, 1.403980829486632)
#      X2 : X3 0.18644002031 (True, 0.9047165160483944)
#      X2 : X4 -0.260367680859 (True, 1.2781024594847337)
#      X2 : X5 0.00268982031161 (True, 0.01289995615351149)
#      X2 : X6 -0.196858662259 (True, 0.9565883326556353)
#      X3 : X4 -0.00990782887303 (True, 0.04751783294143396)
#      X3 : X5 -0.00203807548954 (True, 0.009774280212961183)
#      X3 : X6 -0.08260234145 (True, 0.39705160916381266)
#      X4 : X5 0.0473394389496 (True, 0.22720179660094275)
#      X4 : X6 0.9142698418 (False, 7.44765509683277)
#      X5 : X6 0.216220005745 (True, 1.0535833038878122)
#     

# In[104]:

title, legend= 'plot Zeta vs ', ['fit']

X_headers = ['X1','X2','X3','X4','X5','Earning']
Y = np.array(df['Zeta'])

# Plot outputs
for n, tmp in enumerate(X_headers): 
    X = np.array(df[[tmp]])
    # Create linear regression object
    regr = linear_model.LinearRegression()
    # Train the model using the training sets
    regr.fit(X, Y)
    if( regr.score(X,Y) > 0.05 ):
        pl.figure(n)
        pl.scatter(X, Y,  color='black')
        pl.plot(X, regr.predict(X), color='blue', linewidth=1)
        pl.title(title+tmp)
        pl.xlabel('feature '+tmp), pl.ylabel('Zeta')
        pl.legend(legend, loc='lower right')
        pl.xticks(()), pl.yticks(())
        print regr.score(X,Y), tmp
        
#x4x = np.array(df[['X4']])      
X = np.array(df[['X4','X2']])
regr.fit(X, Y)
x1 = regr.predict(X)
print regr.score(X,Y)
pl.plot(X, x1, color='blue', linewidth=1)


X = np.array(df[['X4','X2','X3','X1','X5','Earning']])
regr.fit(X, Y)
x2 = regr.predict(X)
print regr.score(X,Y)
pl.plot(X, x2, color='green', linewidth=1)


#X = np.array(df[['X4']])
#regr.fit(X, Y)
#x3 = regr.predict(X)
#print regr.score(X,Y)
#pl.plot(X, x3, color='red', linewidth=1)


# Out[104]:

#     0.0810336865106 X1
#     0.835889343624 X4
#     0.576731598515 Earning
#     0.837709132552
#     0.874408304044
#     

#     [<matplotlib.lines.Line2D at 0x12297390>,
#      <matplotlib.lines.Line2D at 0x12205730>,
#      <matplotlib.lines.Line2D at 0x125d8c30>,
#      <matplotlib.lines.Line2D at 0x125d8230>,
#      <matplotlib.lines.Line2D at 0x125d8350>,
#      <matplotlib.lines.Line2D at 0x125d88b0>]

# image file:

# image file:

# image file:

# In[117]:

'''
    load data
'''
file_ = 'adsquare_teaser_dataMay2014.json'
data = json.load( open(file_) )
dframe = pd.DataFrame( data )
print dframe.describe()
'''
    predict Zeta
'''
regr = linear_model.LinearRegression()
#fit
X = np.array( df[['X4','X2','X3','X1','X5','Earning']] )
Y = np.array( df[['Zeta']] )
regr.fit(X, Y)
Y_ = regr.predict(X)
#prevision
x = np.array(dframe[['X4','X2','X3','X1','X5','Earning']])
y = regr.predict(x)

X4 = np.array( df[['X4']] )
x4 = np.array( dframe[['X4']] )

x_ = np.array(df[['X4']])
regr.fit(x_, Y)
y_ = regr.predict(x_)

pl.scatter( x4, y, color='black' )
pl.scatter( X4, Y, color='blue' )
pl.scatter( X4, Y_, color='purple' )
pl.plot( X4, regr.predict(X4), color='green', linewidth=1) 

NaNsList = np.where(dframe['Zeta'].isnull())[0]

#fill the NaN with the regression model
for i in NaNsList:
    dframe['Zeta'].iloc[i] = y[i]

tmp = dframe.reset_index().to_json()
text_file = open("Output.json", "w")
text_file.write(tmp)
text_file.close()


# Out[117]:

#               Earning       Index          X1          X2          X3          X4          X5       Zeta
#     count  100.000000  100.000000  100.000000  100.000000  100.000000  100.000000  100.000000  26.000000
#     mean    68.987725   49.500000   11.036567    3.429383    1.066958   -1.625202    6.665725   0.008950
#     std    207.069287   29.011492    6.639703    9.099960    1.611464   12.649626    8.888543   3.178287
#     min   -441.872612    0.000000   -2.868187  -13.615200   -1.909986  -23.268849  -16.501386  -5.737756
#     25%    -53.370111   24.750000    6.166075   -3.367730   -0.202271  -12.698001    0.451811  -2.118379
#     50%     71.848425   49.500000   11.110337    2.057958    1.236681   -2.898435    7.078727  -0.531868
#     75%    206.180674   74.250000   16.332492   11.564573    2.064181    9.628537   12.921400   1.479583
#     max    485.608414   99.000000   23.837957   23.377158    5.298393   23.530120   24.825712   6.653498
#     

#     C:\Python27\lib\site-packages\pandas\core\config.py:570: DeprecationWarning: height has been deprecated.
#     
#       warnings.warn(d.msg, DeprecationWarning)
#     

# image file:

# In[53]:

file_ = 'adsquare_teaser_dataMay2014.json'
fp = open(file_)
data = json.load(fp)
dframe = pd.DataFrame( data )

regr = linear_model.LinearRegression()
#X = np.array(dframe[['X1','X2','X3','X4','X5']])
X = np.array(dframe[['X2','X4']])
X = np.array(dframe[['X2']])
Y = np.array(dframe['Earning'])
print type(Y)


for tmp in ['X1','X2','X3','X4','X5']:
    X = np.array(dframe[[tmp]])
    regr.fit(X, Y)
    print tmp, ' --*-- ' ,regr.score(X,Y)

#print dframe.head(25) #.notnull()
#print dframe.dropna() #notnull()
#regr.fit(X4,Y)
#print ' --*-- ' ,regr.score(X4,Y) 


# Out[53]:

#     <type 'numpy.ndarray'>
#     X1  --*--  0.00273681343731
#     X2  --*--  0.0599891118461
#     X3  --*--  0.000219603320435
#     X4  --*--  0.644485585694
#     X5  --*--  0.015514485621
#     

# In[ ]:

'''
    2D plots Earnings vs X's & fits
    
    I found that 'X4' and Earning have some kind of linear relation
    score 64%
'''

title, legend= 'plot Earning vs ', ['fit']

X_headers = ['X1','X2','X3','X4','X5']
Y = np.array(dframe['Earning'])

# Plot outputs
for n, tmp in enumerate(X_headers): 
    X = np.array(dframe[[tmp]])
    # Create linear regression object
    regr = linear_model.LinearRegression()
    # Train the model using the training sets
    regr.fit(X, Y)
    if( regr.score(X,Y) > 0.05 ):
        pl.figure(n)
        pl.scatter(X, Y,  color='black')
        pl.plot(X, regr.predict(X), color='blue', linewidth=1)
        pl.title(title+tmp)
        pl.xlabel('feature'+tmp), pl.ylabel('Earning')
        pl.legend(legend, loc='lower right')
        pl.xticks(()), pl.yticks(())
        print tmp
        
pl.show()


# In[ ]:

'''
# Plot outputs
for n, tmp in enumerate(X_headers): 
    X = np.array(dframe[[tmp]])
    # Create linear regression object
    regr = linear_model.LinearRegression()
    # Train the model using the training sets
    regr.fit(X, Y)
    if( regr.score(X,Y) > 0.05 ):
        pl.figure(n)
        pl.scatter(X, Y,  color='black')
        pl.plot(X, regr.predict(X), color='blue', linewidth=1)
        pl.title(title+tmp)
        pl.xlabel('feature '+tmp), pl.ylabel('Zeta')
        pl.legend(legend, loc='lower right')
        pl.xticks(()), pl.yticks(())
        print regr.score(X,Y), tmp

X = np.array(dframe[['X1','X2','X3']])
regr.fit(X,Y)
print regr.coef_
'''

