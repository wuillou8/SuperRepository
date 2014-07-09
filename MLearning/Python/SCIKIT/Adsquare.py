
## Analysis for Adsquare

# This my analysis for the adsquare Data Science Teaser.
# I am using iPython and Python packages like scikit, panda, numpy, scipy and others.
# This is a summary of the most successfull analyses and I have chosen this format because I find it
# practical to display both methods and code.

##### import libraries and some specifications:

# In[1]:

import sys, math, scipy, json, itertools, warnings
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

# In[3]:

dframe.describe()


# Out[3]:

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

# In[4]:

axes = pd.tools.plotting.scatter_matrix(dframe[['X1','X2','X3','X4','X5','Earning','Zeta']], color="brown")
#The plot below can be extended manually


# Out[4]:

# image file:

##### Correlation Analysis:

# For doing the correlation analysis, I need a few functions that I quickly design myself. 
# (I have crosschecked them against standard packages outputs). These functions are defined and commented on below.

# In[3]:

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


# In order to evaluate the best model, we will also need R2 and the adjusted R2. The squared error naturally increases if new features are added.
# This effect is accounted for by the adjusted R2.

# In[24]:

def SSreg(Y, fitY):
    return sum(map(lambda x : (x[0] - x[1])**2, zip(Y,fitY)[:]))   
def SStot(Y):
    ybar = Y.mean()
    return sum(map(lambda x : (x - ybar)**2, Y[:]))
def R2(Y,fitY):
    return 1-SSreg(Y,fitY)/SStot(Y)
''' R2 adjusted '''
def R2adj(Y,fitY,N):
    return 1.- (1.- R2(Y,fitY))*(len(Y)-1.)/(len(Y)-N-1.)
display(Math(r'R^2 \equiv 1 - {SS_{\rm res}\over SS_{\rm tot}},'))
display(Math(r'R^2_{\rm{adjusted}} = 1- (1-R^2)\cdot \frac{N - 1}{N - d_f - 1},'))
display(Math(r'with\quad SS_\text{res}=\sum_i (y_i - f_i)^2\quad and\quad SS_\text{tot}=\sum_i (y_i-\bar{y})^2.'))


# Out[24]:

# image file:

# image file:

# image file:

#     
#     

# Ftest: one-way ANOVA F-test statistic

# In[25]:

''' F-test  '''
display(Math(r'between\,\, group = \sum_i n_i(\bar{Y}_{i\cdot} - \bar{Y})^2/(K-1)')) 
display(Math(r'within \,\, group = \sum_{ij} (Y_{ij}-\bar{Y}_{i\cdot})^2/(N-K),')) 
display(Math(r'F\, =\, between\,\, group\, /\, within \,\, group.'))
def beetwGroup(arrX):
    y_i, res = [], 0.
    [ y_i.append(x_.mean()) for x_ in arrX ]
    y_bar = sum(y_i)/len(y_i)
    for i in xrange(len(y_i)):
        res += (y_i[i]- y_bar)**2 *len(arrX[i]) 
    return res / ( len(y_i)-1 )

def withinGroup(arrX):
    y_i, res, d_f = [], 0., 0
    [ y_i.append(x_.mean()) for x_ in arrX ]       
    for i in xrange(len(y_i)):
        d_f += len(arrX[i])-1
        res += sum((arrX[i][:]-y_i[i])**2)
    return res/d_f

#F = \frac{\text{explained variance}}{\text{unexplained variance}} ,
def F(arrX):
    return beetwGroup(arrX) / withinGroup(arrX)

def Ftest(arrX):
    Ftest = scipy.stats.f.cdf( F(arrX),len(arrX)-1, sum([ len(tmp)-1 for tmp in arrX ]) )
    ''' null hypothesis: same expected value '''
    if ((1. - Ftest) > 0.05):
        return Ftest #[True, Ftest]
    else:
        return Ftest #[False, Ftest]


# Out[25]:

# image file:

# image file:

# image file:

# As first step, I measure how data is correlated, first looking at correlation between the different features and earnings
# Then, I also consider powers of the features (include basical nonlinear models).

# In[226]:

'''    Preprocess Data    '''
_columns = ['Earning', 'X1', 'X2', 'X3', 'X4', 'X5', 'Zeta']
X = np.array(dframe[['X1','X2','X3','X4','X5']])
_X = scale(X) #'''----normalize X----'''
X1, X2, X3, X4, X5 = _X[:,0], _X[:,1], _X[:,2], _X[:,3], _X[:,4]
Y = scale( np.array(dframe['Earning']) )


# Measure correlations Earning VS {X1,X2,X3,X4,X5} and test Hypothesis H_0: uncorrelated data

# In[227]:

data = [X1, X2, X3, X4, X5]
print 'featureVSfeature, correlation, test uncorrelated H_0'
for _n, x in enumerate( data ):
    R, n = corr(Y,x), len(x)
    if testH_0( n, R ) == False:
        print  ' Earning : X'+str(_n+1) , R, testH_0( n, R )


# Out[227]:

#     featureVSfeature, correlation, test uncorrelated H_0
#      Earning : X2 0.244926747919 False
#      Earning : X4 -0.802798595971 False
#     

# Measure correlations between elements {X1,X2,X3,X4,X5} and test Hypothesis H_0: uncorrelated data: 

# In[228]:

print 'featureVSfeature, correlation, test uncorrelated H_0'
for _n, x in enumerate( data ):
    for _m, y in enumerate( data[(_n+1):] ):
        R, n = corr(y,x), len(x)
        if testH_0( n, R ) == False:
            print ' X'+str((_n+1))+' : X'+str(_n+_m+2), R, testH_0( n, R )


# Out[228]:

#     featureVSfeature, correlation, test uncorrelated H_0
#     

# Measure correlations Earning VS {X1,X2,X3,X4,X5} and test Hypothesis H_0: uncorrelated data for different powers of
# {X1,X2,X3,X4,X5}

# Checked is corr( Y, pow(X, N) )

# In[229]:

print  'power, featureVSfeature, correlation, test uncorrelated H_0'
for _n, x in enumerate( data ):
    for _pow in range(2,5):
        x = scale( power( x, _pow ) )
        R, n = corr(Y,x), len(x)
        if testH_0( n, R ) == False:
            print  'power', _pow, ', Y : X'+str(_n+1) , R, testH_0( n, R )


# Out[229]:

#     power, featureVSfeature, correlation, test uncorrelated H_0
#     power 2 , Y : X4 -0.199834919763 False
#     power 3 , Y : X4 -0.330585516939 False
#     power 4 , Y : X4 -0.22271889492 False
#     

#### Best model with Linear Regressions and plots:

# Based on the previous analysis, candidates for the model should contain 'x4', 'X2' or both of them.
# Below, I evaluate the models accuracies for the models fitted with linear regressions.

# In[30]:

regr = linear_model.LinearRegression()
Y = np.array(dframe[['Earning']])
models = [ ['X4'], ['X2'], ['X2','X4'], ['X1','X2','X4'], ['X2','X3','X4'], ['X2','X4','X5'],             ['X2','X3','X4','X5'], ['X1','X3','X4','X5'], ['X1','X2','X4','X5'],                 ['X1','X2','X3','X5'], ['X1','X2','X3','X4'], ['X1','X2','X3','X4','X5'] ]
print 'model  : R^2 adjusted   : my R^2         : F test         : R^2 sci-kit'
print '------------------------------------------------------------------------------------'
for tmp in models:
    X = np.array(dframe[tmp])
    regr.fit(X, Y)
    y = regr.predict(X)
    print str(tmp),':', R2adj(Y,y,len(tmp))[0],':', R2(Y,y)[0],':', Ftest([Y,y])[0],':', regr.score(X,Y)


# Out[30]:

#      model  : R^2 adjusted   : my R^2         : F test         : R^2 sci-kit
#     ------------------------------------------------------------------------------------
#     ['X4'] : 0.640857887589 : 0.644485585694 : 0.0 : 0.644485585694
#     ['X2'] : 0.0503971640078 : 0.0599891118461 : 7.51208544433e-16 : 0.0599891118461
#     ['X2', 'X4'] : 0.678478476154 : 0.684973860474 : 5.95819396427e-16 : 0.684973860474
#     ['X1', 'X2', 'X4'] : 0.675993820786 : 0.685812189853 : 5.95671231934e-16 : 0.685812189853
#     ['X2', 'X3', 'X4'] : 0.677515025719 : 0.687287297667 : 5.95410792761e-16 : 0.687287297667
#     ['X2', 'X4', 'X5'] : 0.688169589412 : 0.697618995793 : 5.9359619454e-16 : 0.697618995793
#     ['X2', 'X3', 'X4', 'X5'] : 0.689409090898 : 0.701958218538 : 5.92839010866e-16 : 0.701958218538
#     ['X1', 'X3', 'X4', 'X5'] : 0.640653699996 : 0.65517274242 : 6.01159283731e-16 : 0.65517274242
#     ['X1', 'X2', 'X4', 'X5'] : 0.685443530546 : 0.698152882847 : 8.39339816571e-16 : 0.698152882847
#     ['X1', 'X2', 'X3', 'X5'] : 0.0507166740292 : 0.0890715558866 : 1.04808863403e-15 : 0.0890715558866
#     ['X1', 'X2', 'X3', 'X4'] : 0.674591604527 : 0.687739418486 : 5.95331036477e-16 : 0.687739418486
#     ['X1', 'X2', 'X3', 'X4', 'X5'] : 0.686248639688 : 0.702094667987 : 8.38367363337e-16 : 0.702094667987
#     

# R^2 adjusted should account for the overfitting effects.
# Models found with the maximal R^2 adj. are ['X4','X2'], ['X2','X4','X5'], ['X2','X3','X4','X5'].
# Because the correlation of 'X4' and 'X2' with Y is quite clear and the increase with additional feature 
# small, my favourite model is ['X4','X2'], with parameters shown below: 

# In[51]:

Y = np.array(dframe['Earning'])
X_, X__, X___ = np.array(dframe[['X4']]), np.array(dframe[['X4','X2']]),                     np.array(dframe[['X4','X2','X3','X5']])

regr1, regr2, regr3 = linear_model.LinearRegression(), linear_model.LinearRegression(),                             linear_model.LinearRegression()
regr1.fit(X_, Y), regr2.fit(X__, Y), regr3.fit(X___,Y)
Y1D, Y2D, YmultiD = regr1.predict(X_), regr2.predict(X__), regr3.predict(X___)
err4, err42, err4235 = Y-Y1D, Y-Y2D, Y-YmultiD

title = 'plot Earning vs '
legend1, legend2, legend3 = ['1D fit X4','fitted pts'], ['2D fitted pts X4,X2'], ['2D fit error']

fig, axes = pl.subplots(figsize=(18,6))
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
title = '2D fit Error'
pl.title(title), pl.xlabel('feature X4'), pl.ylabel('Fit Error')
pl.plot(X_, err42, 'g^')
pl.legend(legend3, loc='upper right');


# Out[51]:

# image file:

# Final 2D model and its parameters:

# In[16]:

display(Math(r'Model: \quad \vec Y = \alpha \vec X_4 + \beta \vec X_2 + h,'))
display(Math(r'\alpha = '+str(regr2.coef_[0])+',')) , display(Math(r'\beta = '+str(regr2.coef_[1])+',')), display(Math(r'h = '+str(regr2.intercept_)+'.'));


# Out[16]:

# image file:

# image file:

# image file:

# image file:

#### Zeta, fits and Print data out into Json format:

# In[52]:

df = dframe.dropna()
axes = pd.tools.plotting.scatter_matrix(df[['X1','X2','X3','X4','X5','Earning','Zeta']], color="brown")


# Out[52]:

# image file:

# For Zeta, we repeat the same variance analysis as for Earning, but now earnings becomes a variable, we look at
# Zeta VS {X1,X2,X3,X4,X5,Earning}. We see that Zeta is correlated primarily with X4 and Earnings.

# In[31]:

''' preprocessing '''
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


# Out[31]:

#     featureVSfeature, correlation, test uncorrelated H_0
#     Zeta : X4 0.9142698418 False
#     Zeta : Earning -0.759428468333 False
#     power 2 Zeta : X4 0.500719178458 False
#     power 3 Zeta : X4 0.605305228444 False
#     power 4 Zeta : X4 0.455343278347 False
#     power 2 Zeta : Earning 0.445794780234 False
#     power 3 Zeta : Earning 0.497694397801 False
#     power 4 Zeta : Earning 0.521701957548 False
#     

##### Fits: 

# In[49]:

Y = np.array(df['Zeta'])
X_, X__, X___ = np.array(df[['X4']]), np.array(df[['X4','Earning']]),                     np.array(df[['X4','X1','X2','X3','X5','Earning']])
regr1, regr2, regr3 = linear_model.LinearRegression(), linear_model.LinearRegression(),                             linear_model.LinearRegression()
regr1.fit(X_, Y), regr2.fit(X__, Y), regr3.fit(X___,Y)
Y1D, Y2D, YmultiD = regr1.predict(X_), regr2.predict(X__), regr3.predict(X___)
err1D, err2D, errmultiD = Y1D-Y, Y2D-Y, YmultiD-Y

print 'model  : R^2 adjusted   : my R^2         : F test         : R^2 sci-kit'
print '------------------------------------------------------------------------------------'
print 'Y vs X4 : ', R2adj(Y,Y1D,1),':', R2(Y,Y1D),':', Ftest([Y,Y1D]),':', regr1.score(X_,Y)
print 'Y vs [X4,Earning] : ', R2adj(Y,Y2D,2),':', R2(Y,Y2D),':', Ftest([Y,Y2D]),':', regr2.score(X__,Y)
print 'Y vs [X1,X2,X3,X4,X5,Earning] : ', R2adj(Y,YmultiD,6),':', R2(Y,YmultiD),':', Ftest([Y,YmultiD]),':', regr3.score(X___,Y)

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
pl.title(title+str(' 2D fit error )')), pl.xlabel('feature X4'), pl.ylabel('2D fit error')
#pl.scatter(X_, Y,  color='black')
pl.plot(X_, err2D, 'g^' )
pl.legend(legend3, loc='lower right');


# Out[49]:

#     model  : R^2 adjusted   : my R^2         : F test         : R^2 sci-kit
#     ------------------------------------------------------------------------------------
#     Y vs X4 :  0.829051399609 : 0.835889343624 : 1.97319244073e-16 : 0.835889343624
#     Y vs [X4,Earning] :  0.823598482283 : 0.8377106037 : 2.44481043569e-16 : 0.8377106037
#     Y vs [X1,X2,X3,X4,X5,Earning] :  0.834747768478 : 0.874408304044 : 2.14646745927e-16 : 0.874408304044
#     

# image file:

# 2D model coeffs: 

# In[54]:

display(Math(r'Model: \quad \vec Y = \alpha \vec X_4 + \beta \vec {Earning} + h,'))
display(Math(r'\alpha = '+str(regr2.coef_[0])+',')) , display(Math(r'\beta = '+str(regr2.coef_[1])+',')), display(Math(r'h = '+str(regr2.intercept_)+'.'));


# Out[54]:

# image file:

# image file:

# image file:

# image file:

##### Fit the NaN in Zeta and Print data out into Json format

# Replace NaNs with fitted values and print out into file OutputJW.json

# In[90]:

_fit2D = regr2.predict(dframe[['X4','Earning']])
for i in np.where(dframe['Zeta'].isnull())[0]:
    dframe['Zeta'].iloc[i] = _fit2D[i]

_fileOut = open("OutputJW.json", "w")
_fileOut.write(dframe.reset_index().to_json())
_fileOut.close()


#### Additional analyses:

# Additional analyses investigating for more scenarios in the data.

# In[*]:

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

