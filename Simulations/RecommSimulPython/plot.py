
# coding: utf-8

# In[5]:

import pylab as pl
from IPython.display import display, Math, Latex
get_ipython().magic(u'matplotlib inline')


# In[2]:

sigmoid__on = [(0.41960000000000031, 0.082993011754002532)]
random__on = [(0.34680000000000005, 0.07457720831460507)]
sigmoid__of = [(0.32800000000000007, 0.064124878167525601)]
random__of = [(0.32839999999999997, 0.057423340202395048)]

sigmoid__on.append((0.4088000000000002, 0.1125813483664146))
random__on.append((0.32539999999999997, 0.06915807978826477))
sigmoid__of.append((0.3378, 0.06834588502609355))
random__of.append((0.33620000000000005, 0.06201257936902803))

sigmoid__on.append( (0.41199999999999976, 0.086625631310830883))
random__on.append( (0.35080000000000011, 0.070677860748610669))
sigmoid__of.append( (0.32600000000000007, 0.073457470688827825))
random__of.append( (0.33839999999999998, 0.072756030677875769))

def g(arr):
    return map(lambda x: x[0]-1./3., arr)
def h(arr):
    return map(lambda x: x[1], arr)

yy = [g(sigmoid__on),g(random__on),g(sigmoid__of),g(random__of)]
err = [h(sigmoid__on),h(random__on),h(sigmoid__of),h(random__of)]


# In[6]:


x = [0,1,2] 
xx = [x, x, x, x]
pl.title("statical SALADS for SNAILS recommender")
pl.xlabel("# run")
pl.ylabel("recommender conversion percentage")
markers = ['or','ok','vk','^k']
for i in xrange(len(xx)):
    pl.plot(xx[i],yy[i],markers[i],markersize=10)
    pl.errorbar(xx[i],yy[i],yerr=err[i], linestyle="None", color="b")
pl.axhline(y=0., xmin=-0.5, xmax=1, hold=None, color='g')
pl.legend(["recomm&AIPick","","recomm&RandomPick","","Random&AIPick","","Random&RandomPick"], loc='upper right')
pl.xlim([-1,7])
pl.show()
