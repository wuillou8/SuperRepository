
# In[1]:

import pandas as pd
import json, sys
import numpy as np
import pylab as pl
import itertools
from sklearn import linear_model, datasets
from sklearn.decomposition import PCA

get_ipython().magic(u'matplotlib inline')


# In[2]:

'''
    load data
'''
file_ = 'adsquare_teaser_dataMay2014.json'
fp = open(file_)
data = json.load(fp)
dframe = pd.DataFrame( data )
print dframe.describe()


# Out[2]:

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

# In[3]:

'''
    1D plot histo
'''
pl.figure(1)
pl.hist(np.array(dframe['X1']))
pl.figure(2)
pl.hist(np.array(dframe['X2']))
pl.figure(3)
pl.hist(np.array(dframe['X3']))
pl.figure(4)
pl.hist(np.array(dframe['X4']))
pl.figure(5)
pl.hist(np.array(dframe['X5']))
pl.show()


# In[ ]:

'''
    2D plots
'''
'''
    X data against X data
'''
X1 = np.array(dframe['X1'])
X2 = np.array(dframe['X2'])
X3 = np.array(dframe['X3'])
X4 = np.array(dframe['X4'])
X5 = np.array(dframe['X5'])
pl.clf()
pl.figure(1)
pl.plot(X1,X2,"o")
pl.figure(2)
pl.plot(X1,X3,"o")
pl.figure(3)
pl.plot(X1,X4,"o")
pl.figure(4)
pl.plot(X1,X5,"o")
pl.figure(5)
pl.plot(X2,X3,"x")
pl.figure(6)
pl.plot(X2,X4,"o")
pl.figure(7)
pl.plot(X2,X5,"o")
pl.figure(8)
pl.plot(X3,X4,"o")
pl.figure(9)
pl.plot(X3,X5,"o")
pl.figure(10)
pl.plot(X4,X5,"o")
pl.show()


# In[56]:

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
    if( regr.score(X,Y) > 0.5 ):
        pl.figure(n)
        pl.scatter(X, Y,  color='black')
        pl.plot(X, regr.predict(X), color='blue', linewidth=1)
        pl.title(title+tmp)
        pl.xlabel('feature'+tmp), pl.ylabel('Earning')
        pl.legend(legend, loc='lower right')
        pl.xticks(()), pl.yticks(())
        print tmp
        
pl.show()


# Out[56]:

#     X4
#     

# image file:

# In[4]:

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

for size in xrange(2,5):
    for i in itertools.permutations(X_headers, size):  
        X = np.array(dframe[list(i)])
        db = DBSCAN(eps=0.3, min_samples=10).fit(X)
        core_samples = db.core_sample_indices_
        labels = db.labels_
        # Number of clusters in labels, ignoring noise if present.
        n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
        if (n_clusters_ > 0):
            print i, ' -*- ' , n_clusters_


# In[50]:

from scipy.stats import norm, t
import math
'''
    Compute correlation
'''
def corr(l1, l2):
    if ( len(l1) != len(l2) ):
        print 'error in correlation...'
    corr = 0
    for i in range(len(l1)):
        corr+=l1[i]*l2[i]
    return corr/len(l1)
'''
    Compute Student stat value
'''
def StudentStat(r, n):
    return r*( (n - 2) / (1-r**2))**0.5
'''
 compute Proba for H_0
 reads in two lists.
'''
def ProbH0( l1, l2 ):
    r = math.fabs( corr(l1, l2) )
    n = len(l1)-2
    return t.cdf( StudentStat(r, n) , n ) #norm.cdf( math.fabs( StudentStat(r, n) ) )

'''
    Corrects the student test for pearson correlation
    Pearson correlation is not distributed exactly as a gaussian.
    FisherZtrafo accounts for that.
    ***average is then log((1.+\rho)/(1.-\rho))
    ***std_err is \sqrt(1/(N-3))
'''
def fisherZtrafo(r):
    return .5*math.log((1+r)/(1-r))
'''
    test against zero correlation
'''
def testH_0( n, r, Zeta = 0 ):
    # test against H_0: \rho = 0.0
    testval = ( fisherZtrafo( math.fabs(r) )-fisherZtrafo( math.fabs(Zeta) ) )*( n - 3 )**.5
    if ( testval > 1.96 ):
        return False, testval
    else:
        return True, testval


print fisherZtrafo(0.75) #7469)
print testH_0(100, .35, .5)


# Out[50]:

#     0.972955074528
#     (True, -1.8108345348254946)
#     

# In[71]:

import sys
from numpy.random import rand
from sklearn.preprocessing import normalize, scale
from scipy.sparse import csr_matrix
from scipy.stats import norm
from scipy.stats.stats import pearsonr   
'''
    Normalise Data
'''
X = np.array(dframe[['X1','X2','X3','X4','X5']])
X_ = scale(X) #'''----normalize(X)----'''
X1, X2, X3, X4, X5 = X_[:,0], X_[:,1], X_[:,2], X_[:,3], X_[:,4]
Y = np.array(dframe['Earning'])
Y = scale(Y)
'''
    Analysis: against Y and data vs data
'''
data = [X1, X2, X3, X4, X5]
for _n, x in enumerate( data ):
    R, n = corr(x,Y), len(x)
    print ' Y : X'+str(_n+1) , R, testH_0( n, R )

for _n, x in enumerate( data ):
    for _m, y in enumerate( data[(_n+1):] ):
        R, n = corr(x,y), len(x)
        print ' X'+str((_n+1))+' : X'+str(_n+_m+2), R, testH_0( n, R )

#R, n = corr(X1,X3), len(X5)
#print R, testH_0( n, R )


# Out[71]:

#      Y : X1 0.0523145623828 (True, 0.5157094966126772)
#      Y : X2 0.244926747919 (False, 2.46229916534109)
#      Y : X3 -0.0148190188756 (True, 0.1459610948074279)
#      Y : X4 -0.802798595971 (False, 10.897120735948178)
#      Y : X5 0.124557158048 (True, 1.233149565310859)
#      X1 : X2 -0.10829029602 (True, 1.0707343211276015)
#      X1 : X3 0.163613441317 (True, 1.626019737905643)
#      X1 : X4 -0.0573566458612 (True, 0.5655181383821853)
#      X1 : X5 0.0678086612962 (True, 0.6688642720638669)
#      X2 : X3 -0.034497666471 (True, 0.33989749047136164)
#      X2 : X4 -0.0548236930373 (True, 0.540492699942512)
#      X2 : X5 -0.119887616723 (True, 1.1864623993689758)
#      X3 : X4 0.0705056139102 (True, 0.695553839800144)
#      X3 : X5 -0.149118339476 (True, 1.4796786392965162)
#      X4 : X5 -0.0470359649678 (True, 0.46359261378972033)
#     

# In[34]:

'''
    Check wether data correlated
    X3, X4 > 80% correlated to Earning
    X2, X3 correlated 70%
'''
import sys
#import sklearn.preprocessing.Normalizer as norma
from numpy.random import rand
from sklearn.preprocessing import normalize, scale
from scipy.sparse import csr_matrix
#from scipy.linalg import norm
from scipy.stats import norm
from scipy.stats.stats import pearsonr   
#X1, X2, X3, X4, X5 = np.array(dframe['X1']), np.array(dframe['X2']), np.array(dframe['X3']), np.array(dframe['X4']), np.array(dframe['X5'])

X = np.array(dframe[['X1','X2','X3','X4','X5']])
X_ = scale(X) #'''----normalize(X)----'''
'''
    Normalise Data
'''
X1, X2, X3, X4, X5 = X_[:,0], X_[:,1], X_[:,2], X_[:,3], X_[:,4]
Y = np.array(dframe['Earning'])
Y = scale(Y)

'''
print '12',np.sqrt(pearsonr(X1,X2)[0]**2+pearsonr(X1,X2)[1]**2)#, np.corrcoef(X1,X2)
print '13',np.sqrt(pearsonr(X1,X3)[0]**2+pearsonr(X1,X3)[1]**2)
print '14',np.sqrt(pearsonr(X1,X4)[0]**2+pearsonr(X1,X4)[1]**2)
print '15',np.sqrt(pearsonr(X1,X5)[0]**2+pearsonr(X1,X5)[1]**2)
print '23',np.sqrt(pearsonr(X2,X3)[0]**2+pearsonr(X2,X3)[1]**2)
print '24',np.sqrt(pearsonr(X2,X4)[0]**2+pearsonr(X2,X4)[1]**2)
print '25',np.sqrt(pearsonr(X2,X5)[0]**2+pearsonr(X2,X5)[1]**2)
print '34',np.sqrt(pearsonr(X3,X4)[0]**2+pearsonr(X3,X4)[1]**2)
print '35',np.sqrt(pearsonr(X3,X5)[0]**2+pearsonr(X3,X5)[1]**2)
print '45',np.sqrt(pearsonr(X4,X5)[0]**2+pearsonr(X4,X5)[1]**2)

print 'E1', np.sqrt(pearsonr(Y,X1)[0]**2+pearsonr(Y,X1)[1]**2)
print 'E2', np.sqrt(pearsonr(Y,X2)[0]**2+pearsonr(Y,X2)[1]**2)
print 'E3', np.sqrt(pearsonr(Y,X3)[0]**2+pearsonr(Y,X3)[1]**2)
print 'E4', np.sqrt(pearsonr(Y,X4)[0]**2+pearsonr(Y,X4)[1]**2)
print 'E5', np.sqrt(pearsonr(Y,X5)[0]**2+pearsonr(Y,X5)[1]**2)

for n,x in enumerate([X1, X2, X3, X4, X5]):
    pl.figure(n)
    pl.plot(x,Y,'x')
    pl.legend(['Earning vs X'+str(n+1)])

#print corr(Y,X)corr(Y,X3)
nu = X1.shape[0]
for n,x in enumerate([X1, X2, X3, X4, X5]):
    print n,' Y : X ' ,corr(x,Y), StudentStat(corr(x,Y), nu)

print '12', corr(X1,X2), StudentStat(corr(X1,X2), nu) #np.sqrt(pearsonr(X1,X2)[0]**2+pearsonr(X1,X2)[1]**2)
print '13', corr(X1,X3), StudentStat(corr(X1,X3), nu) #np.sqrt(pearsonr(X1,X3)[0]**2+pearsonr(X1,X3)[1]**2)
print '14', corr(X1,X4), StudentStat(corr(X1,X4), nu) #np.sqrt(pearsonr(X1,X4)[0]**2+pearsonr(X1,X4)[1]**2)
print '15', corr(X1,X5), StudentStat(corr(X1,X5), nu) #np.sqrt(pearsonr(X1,X5)[0]**2+pearsonr(X1,X5)[1]**2)
print '23', corr(X2,X3), StudentStat(corr(X2,X3), nu) #np.sqrt(pearsonr(X2,X3)[0]**2+pearsonr(X2,X3)[1]**2)
print '24', corr(X2,X4), StudentStat(corr(X2,X4), nu) #np.sqrt(pearsonr(X2,X4)[0]**2+pearsonr(X2,X4)[1]**2)
print '25', corr(X2,X5), StudentStat(corr(X2,X5), nu) #np.sqrt(pearsonr(X2,X5)[0]**2+pearsonr(X2,X5)[1]**2)
print '34', corr(X3,X4), StudentStat(corr(X3,X4), nu) #np.sqrt(pearsonr(X3,X4)[0]**2+pearsonr(X3,X4)[1]**2)
print '35', corr(X3,X5), StudentStat(corr(X3,X5), nu) #np.sqrt(pearsonr(X3,X5)[0]**2+pearsonr(X3,X5)[1]**2)   
print '45', corr(X4,X5), StudentStat(corr(X4,X5), nu)
'''

for n,x in enumerate([X1, X2, X3, X4, X5]):
    print ' Y : X'+str(n+1) , corr(x,Y), ProbH0(x,Y) #, StudentStat(corr(x,Y), nu)

print '12', corr(X1,X2),  ProbH0(X1,X2) #, StudentStat(corr(X1,X2), nu) #np.sqrt(pearsonr(X1,X2)[0]**2+pearsonr(X1,X2)[1]**2)
print '13', corr(X1,X3), ProbH0(X1,X3) #, StudentStat(corr(X1,X3), nu) #np.sqrt(pearsonr(X1,X3)[0]**2+pearsonr(X1,X3)[1]**2)
print '14', corr(X1,X4), ProbH0(X1,X4) #, StudentStat(corr(X1,X4), nu) #np.sqrt(pearsonr(X1,X4)[0]**2+pearsonr(X1,X4)[1]**2)
print '15', corr(X1,X5), ProbH0(X1,X5) #, StudentStat(corr(X1,X5), nu) #np.sqrt(pearsonr(X1,X5)[0]**2+pearsonr(X1,X5)[1]**2)
print '23', corr(X2,X3), ProbH0(X2,X3) #, StudentStat(corr(X2,X3), nu) #np.sqrt(pearsonr(X2,X3)[0]**2+pearsonr(X2,X3)[1]**2)
print '24', corr(X2,X4), ProbH0(X2,X4) #, StudentStat(corr(X2,X4), nu) #np.sqrt(pearsonr(X2,X4)[0]**2+pearsonr(X2,X4)[1]**2)
print '25', corr(X2,X5), ProbH0(X2,X5) #, StudentStat(corr(X2,X5), nu) #np.sqrt(pearsonr(X2,X5)[0]**2+pearsonr(X2,X5)[1]**2)
print '34', corr(X3,X4), ProbH0(X3,X4) #, StudentStat(corr(X3,X4), nu) #np.sqrt(pearsonr(X3,X4)[0]**2+pearsonr(X3,X4)[1]**2)
print '35', corr(X3,X5), ProbH0(X3,X5) #, StudentStat(corr(X3,X5), nu) #np.sqrt(pearsonr(X3,X5)[0]**2+pearsonr(X3,X5)[1]**2)   
print '45', corr(X4,X5), ProbH0(X4,X5) #, StudentStat(corr(X4,X5), nu)

#print type(X1), X1.shape
print norm.cdf(  StudentStat(.21061,600) ), norm.cdf(  StudentStat(.21061,100) )
print norm.cdf(  StudentStat(.10,100) ), StudentStat(.21061,600)


# Out[34]:

#      Y : X1 0.0523145623828 0.695544239556
#      Y : X2 0.244926747919 0.992483149794
#      Y : X3 -0.0148190188756 0.557579165678
#      Y : X4 -0.802798595971 1.0
#      Y : X5 0.124557158048 0.889176284577
#     12 -0.10829029602 0.855770786938
#     13 0.163613441317 0.946310096913
#     14 -0.0573566458612 0.712607349207
#     15 0.0678086612962 0.746486389765
#     23 -0.034497666471 0.632035051412
#     24 -0.0548236930373 0.704091069749
#     25 -0.119887616723 0.880201453609
#     34 0.0705056139102 0.75488026272
#     35 -0.149118339476 0.92863597959
#     45 -0.0470359649678 0.677221174173
#     0.999999931204 0.983528213713
#     0.840116468252 5.26843518376
#     

# In[11]:

file_ = 'adsquare_teaser_dataMay2014.json'
fp = open(file_)
data = json.load(fp)
dframe = pd.DataFrame( data )
#print dframe.describe()

X_headers = ['X1','X2','X3','X4','X5']
Y = np.array(dframe['Earning'])

X=dframe[['X1','X2','X3','X4','X5']]

pca = PCA(n_components=5)
pca.fit(X)
print pca.explained_variance_ratio_


print len(pca.transform(X))
#print pca.X_new
print pca.get_params(deep=True)
#print pca.
#print pca.whiten()
#PCA(copy=True, n_components=3, whiten=False)
#print pca.explained_variance_ratio_ #, pca.transform(X)
#print pca.components_


# Out[11]:

#     [ 0.43680576  0.24962972  0.19112526  0.11582641  0.00661286]
#     100
#     {'copy': True, 'n_components': 5, 'whiten': False}
#     

# In[ ]:

file_ = 'adsquare_teaser_dataMay2014.json'
fp = open(file_)

data = json.load(fp) #[, encoding[, cls[, object_hook[, parse_float[, parse_int[, parse_constant[, object_pairs_hook[, **kw]]]]]]]])
dframe = pd.DataFrame( data )
X_headers = ['X1','X2','X3','X4','X5']
Y = np.array(dframe['Earning'])

print Y[:3] 
print X[:3]
regr = linear_model.LinearRegression()
regr.fit(X, Y)
print label, ' --*-- ' ,regr.score(X,Y)
for size in xrange(2,5):
    for i in itertools.permutations(X_headers, size):  
        X = np.array(dframe[list(i)])
        regr = linear_model.LinearRegression()
        regr.fit(X, Y)
        if (regr.score(X,Y) > 0.65):
            print size, list(i), ' -*- ' ,regr.score(X,Y)
            
X = np.array(dframe[['X1','X2','X3','X4','X5']])
regr = linear_model.LinearRegression()
regr.fit(X, Y)
print size, list(i), ' -*- ' ,regr.score(X,Y)
'''
print dframe.head()
df = dframe[['X1','X2','X3','X4','X5']]
print type(df),df.head()
#for i in  df:
#    print i, type(i)
X = np.array(df)
regr = linear_model.LinearRegression()
regr.fit(X, Y)
regr.score(X, Y)
'''
'''
for label in ['X1','X2','X3','X4','X5']:
    X = np.array(dframe[label])
    Y = np.array(dframe['Earning'])
    regr = linear_model.LinearRegression()
    regr.fit(X, Y)
    print label, ' -*- ' ,regr.score(X,Y)
#print type(np.array(dframe['X1','X2','X3','X4','X5'])) #.head(25)))
#dframe.tail()
'''

#regr = linear_model.LinearRegression()
#regr.fit(diabetes_X_train, diabetes_y_train)
#LinearRegression(copy_X=True, fit_intercept=True, normalize=False)


# In[15]:

import numpy as np
import pylab as pl
from sklearn import svm, datasets, feature_selection, cross_validation
from sklearn.pipeline import Pipeline

###############################################################################
# Import some data to play with
digits = datasets.load_digits()
print '##################################################'
print type(digits)
print digits.data, type(digits.data)
print digits.data.shape

y = digits.target
# Throw away data, to be in the curse of dimension settings
y = y[:200]
X = digits.data[:200]
n_samples = len(y)
X = X.reshape((n_samples, -1))
# add 200 non-informative features
X = np.hstack((X, 2 * np.random.random((n_samples, 200))))


###############################################################################
# Create a feature-selection transform and an instance of SVM that we
# combine together to have an full-blown estimator

transform = feature_selection.SelectPercentile(feature_selection.f_classif)

clf = Pipeline([('anova', transform), ('svc', svm.SVC(C=1.0))])

###############################################################################
# Plot the cross-validation score as a function of percentile of features
score_means = list()
score_stds = list()
percentiles = (1, 3, 6, 10, 15, 20, 30, 40, 60, 80, 100)

for percentile in percentiles:
    clf.set_params(anova__percentile=percentile)
    # Compute cross-validation score using all CPUs
    this_scores = cross_validation.cross_val_score(clf, X, y, n_jobs=1)
    score_means.append(this_scores.mean())
    score_stds.append(this_scores.std())

pl.errorbar(percentiles, score_means, np.array(score_stds))

pl.title(
    'Performance of the SVM-Anova varying the percentile of features selected')
pl.xlabel('Percentile')
pl.ylabel('Prediction rate')

pl.axis('tight')
pl.show()


# Out[15]:

#     ##################################################
#     <class 'sklearn.datasets.base.Bunch'>
#     [[  0.   0.   5. ...,   0.   0.   0.]
#      [  0.   0.   0. ...,  10.   0.   0.]
#      [  0.   0.   0. ...,  16.   9.   0.]
#      ..., 
#      [  0.   0.   1. ...,   6.   0.   0.]
#      [  0.   0.   2. ...,  12.   0.   0.]
#      [  0.   0.  10. ...,  12.   1.   0.]] <type 'numpy.ndarray'>
#     (1797, 64)
#     

# In[76]:

from time import time
import numpy as np
import pylab as pl

from sklearn import metrics
from sklearn.cluster import KMeans
from sklearn.datasets import load_digits
from sklearn.decomposition import PCA
from sklearn.preprocessing import scale

np.random.seed(42)

digits = load_digits()
data = scale(digits.data)

n_samples, n_features = data.shape
n_digits = len(np.unique(digits.target))
labels = digits.target

sample_size = 300

print type(data)
#print data[:2]
print type(data.all), data.any
#print n_samples, n_digits, labels
'''
print("n_digits: %d, \t n_samples %d, \t n_features %d"
      % (n_digits, n_samples, n_features))
print(79 * '_')
print('% 9s' % 'init'
      '    time  inertia    homo   compl  v-meas     ARI AMI  silhouette')
'''
def bench_k_means(estimator, name, data):
    t0 = time()
    estimator.fit(data)
    print('% 9s   %.2fs    %i   %.3f   %.3f   %.3f   %.3f   %.3f    %.3f'
          % (name, (time() - t0), estimator.inertia_,
             metrics.homogeneity_score(labels, estimator.labels_),
             metrics.completeness_score(labels, estimator.labels_),
             metrics.v_measure_score(labels, estimator.labels_),
             metrics.adjusted_rand_score(labels, estimator.labels_),
             metrics.adjusted_mutual_info_score(labels,  estimator.labels_),
             metrics.silhouette_score(data, estimator.labels_,
                                      metric='euclidean',
                                      sample_size=sample_size)))
    
#KMeans(n_clusters=8, init='k-means++', n_init=10, max_iter=300, tol=0.0001, precompute_distances=True, verbose=0, random_state=None, copy_x=True, n_jobs=1)
#KMeans(n_clusters=8, init='random', n_init=5, max_iter=300, tol=0.0001, precompute_distances=True, verbose=0, random_state=None, copy_x=True, n_jobs=1)
'''
bench_k_means(KMeans(init='k-means++', n_clusters=n_digits, n_init=10),
              name="k-means++", data=data)
bench_k_means(KMeans(init='random', n_clusters=n_digits, n_init=10),
              name="random", data=data)

# in this case the seeding of the centers is deterministic, hence we run the
# kmeans algorithm only once with n_init=1
pca = PCA(n_components=n_digits).fit(data)
bench_k_means(KMeans(init=pca.components_, n_clusters=n_digits, n_init=1),
              name="PCA-based",
              data=data)
print(79 * '_')

###############################################################################
# Visualize the results on PCA-reduced data

reduced_data = PCA(n_components=2).fit_transform(data)
kmeans = KMeans(init='k-means++', n_clusters=n_digits, n_init=10)
kmeans.fit(reduced_data)

# Step size of the mesh. Decrease to increase the quality of the VQ.
h = .02     # point in the mesh [x_min, m_max]x[y_min, y_max].

# Plot the decision boundary. For that, we will assign a color to each
x_min, x_max = reduced_data[:, 0].min() + 1, reduced_data[:, 0].max() - 1
y_min, y_max = reduced_data[:, 1].min() + 1, reduced_data[:, 1].max() - 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

# Obtain labels for each point in mesh. Use last trained model.
Z = kmeans.predict(np.c_[xx.ravel(), yy.ravel()])

# Put the result into a color plot
Z = Z.reshape(xx.shape)
pl.figure(1)
pl.clf()
pl.imshow(Z, interpolation='nearest',
          extent=(xx.min(), xx.max(), yy.min(), yy.max()),
          cmap=pl.cm.Paired,
          aspect='auto', origin='lower')

pl.plot(reduced_data[:, 0], reduced_data[:, 1], 'k.', markersize=2)
# Plot the centroids as a white X
centroids = kmeans.cluster_centers_
pl.scatter(centroids[:, 0], centroids[:, 1],
           marker='x', s=169, linewidths=3,
           color='w', zorder=10)
pl.title('K-means clustering on the digits dataset (PCA-reduced data)\n'
         'Centroids are marked with white cross')
pl.xlim(x_min, x_max)
pl.ylim(y_min, y_max)
pl.xticks(())
pl.yticks(())
pl.show()
'''


# Out[76]:

#     <type 'numpy.ndarray'>
#     <type 'builtin_function_or_method'> <built-in method any of numpy.ndarray object at 0x1074F960>
#     

#     '\nbench_k_means(KMeans(init=\'k-means++\', n_clusters=n_digits, n_init=10),\n              name="k-means++", data=data)\n\nbench_k_means(KMeans(init=\'random\', n_clusters=n_digits, n_init=10),\n              name="random", data=data)\n\n# in this case the seeding of the centers is deterministic, hence we run the\n# kmeans algorithm only once with n_init=1\npca = PCA(n_components=n_digits).fit(data)\nbench_k_means(KMeans(init=pca.components_, n_clusters=n_digits, n_init=1),\n              name="PCA-based",\n              data=data)\nprint(79 * \'_\')\n\n###############################################################################\n# Visualize the results on PCA-reduced data\n\nreduced_data = PCA(n_components=2).fit_transform(data)\nkmeans = KMeans(init=\'k-means++\', n_clusters=n_digits, n_init=10)\nkmeans.fit(reduced_data)\n\n# Step size of the mesh. Decrease to increase the quality of the VQ.\nh = .02     # point in the mesh [x_min, m_max]x[y_min, y_max].\n\n# Plot the decision boundary. For that, we will assign a color to each\nx_min, x_max = reduced_data[:, 0].min() + 1, reduced_data[:, 0].max() - 1\ny_min, y_max = reduced_data[:, 1].min() + 1, reduced_data[:, 1].max() - 1\nxx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))\n\n# Obtain labels for each point in mesh. Use last trained model.\nZ = kmeans.predict(np.c_[xx.ravel(), yy.ravel()])\n\n# Put the result into a color plot\nZ = Z.reshape(xx.shape)\npl.figure(1)\npl.clf()\npl.imshow(Z, interpolation=\'nearest\',\n          extent=(xx.min(), xx.max(), yy.min(), yy.max()),\n          cmap=pl.cm.Paired,\n          aspect=\'auto\', origin=\'lower\')\n\npl.plot(reduced_data[:, 0], reduced_data[:, 1], \'k.\', markersize=2)\n# Plot the centroids as a white X\ncentroids = kmeans.cluster_centers_\npl.scatter(centroids[:, 0], centroids[:, 1],\n           marker=\'x\', s=169, linewidths=3,\n           color=\'w\', zorder=10)\npl.title(\'K-means clustering on the digits dataset (PCA-reduced data)\n\'\n         \'Centroids are marked with white cross\')\npl.xlim(x_min, x_max)\npl.ylim(y_min, y_max)\npl.xticks(())\npl.yticks(())\npl.show()\n'

# In[146]:


import numpy as np

from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.datasets.samples_generator import make_blobs
from sklearn.preprocessing import StandardScaler
import sys

##############################################################################
# Generate sample data
centers = [[1, 1], [-1, -1], [1, -1]]
X, labels_true = make_blobs(n_samples=750, centers=centers, cluster_std=0.4,
                            random_state=0)

print X
print type(X)
x, y = [tmp[0] for tmp in X], [tmp[1] for tmp in X] 
#print x
#plt.plot(x,y,'o')
print type(X), X.shape
sys.exit()

X = StandardScaler().fit_transform(X)

##############################################################################
# Compute DBSCAN
db = DBSCAN(eps=0.3, min_samples=10).fit(X)
core_samples = db.core_sample_indices_
labels = db.labels_

# Number of clusters in labels, ignoring noise if present.
n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)


print('Estimated number of clusters: %d' % n_clusters_)
print("Homogeneity: %0.3f" % metrics.homogeneity_score(labels_true, labels))
print("Completeness: %0.3f" % metrics.completeness_score(labels_true, labels))
print("V-measure: %0.3f" % metrics.v_measure_score(labels_true, labels))
print("Adjusted Rand Index: %0.3f"
      % metrics.adjusted_rand_score(labels_true, labels))
print("Adjusted Mutual Information: %0.3f"
      % metrics.adjusted_mutual_info_score(labels_true, labels))
print("Silhouette Coefficient: %0.3f"
      % metrics.silhouette_score(X, labels))

##############################################################################
# Plot result
import pylab as pl

# Black removed and is used for noise instead.
unique_labels = set(labels)
colors = pl.cm.Spectral(np.linspace(0, 1, len(unique_labels)))
for k, col in zip(unique_labels, colors):
    if k == -1:
        # Black used for noise.
        col = 'k'
        markersize = 6
    class_members = [index[0] for index in np.argwhere(labels == k)]
    cluster_core_samples = [index for index in core_samples
                            if labels[index] == k]
    for index in class_members:
        x = X[index]
        if index in core_samples and k != -1:
            markersize = 14
        else:
            markersize = 6
        pl.plot(x[0], x[1], 'o', markerfacecolor=col,
                markeredgecolor='k', markersize=markersize)

pl.title('Estimated number of clusters: %d' % n_clusters_)
pl.show()


# Out[146]:


    An exception has occurred, use %tb to see the full traceback.
    

    SystemExit
    


#     [[ 0.84022039  1.14802236]
#      [-1.15474834 -1.2041171 ]
#      [ 0.67863613  0.72418009]
#      ..., 
#      [ 0.26798858 -1.27833405]
#      [-0.88628813 -0.30293249]
#      [ 0.60046048 -1.29605472]]
#     <type 'numpy.ndarray'>
#     <type 'numpy.ndarray'> (750, 2)
#     

#     To exit: use 'exit', 'quit', or Ctrl-D.
#     

# In[ ]:



