#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      wuiljai
#
# Created:     18/10/2013
# Copyright:   (c) wuiljai 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import sys
import numpy as np
import pandas as pd
import pylab as P

import matplotlib
matplotlib.rcParams['legend.fancybox'] = True
import matplotlib.pyplot as plt

from matplotlib.backends.backend_pdf import PdfPages

def plotGraph(X,Y):
      fig = plt.figure()
      ### Plotting arrangements ###
      return fig



class DataAnalysis:
#
#   Basic Analysis Class:
#   Reading main parameters.
       def __init__(self,dataFile):
                # read in files and pass it into a numpy vector (first line/column removed)
                self.data = pd.read_csv(dataFile)
                self.DaysList = np.sort(self.data['DayOfWeek'].unique())
                self.LineIdList = np.sort(self.data['Line_id'].unique())
                self.DatDescr = self.data.describe()
                ##self.Ride_load = np.sort(self.data['Ride_load'].unique())


class LoadQuestionAnalysis(DataAnalysis):

        def __init__(self):
                #super(BayesSimple,self).__init__(testsample,featsSub)
                DataAnalysis.__init__(self)



def main():
    pass

if __name__ == '__main__':
    main()


dAnalys = DataAnalysis('q_result2.csv')

s = pd.Series([1,3,5,np.nan,6,8])

dates = pd.date_range('20130101',periods=6)
df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=list('ABCD'))
print df

df2 = pd.DataFrame({ 'A' : 1.,
                'B' : pd.Timestamp('20130102'),
                'C' : pd.Series(1,index=range(4),dtype='float32'),
                'D' : np.array([3] * 4,dtype='int32'),
                'E' : 'foo' })

print df2


dff = pd.read_csv('query_result.csv', index_col=False, header=0)
serie = dff.transpose()[0]

#print serie
#print dff
#**************************************************

dfff = pd.read_csv('q_result2.csv')
DaysList = np.sort(dfff['DayOfWeek'].unique())
LineIdList = np.sort(dfff['Line_id'].unique())

Ride_load = np.sort(dfff['Ride_load'].unique())

#**************************************************




print dfff.head()

print "jakoub"
print dfff[dfff['Trip_id']==16]
print dfff[dfff['Trip_id']==16]['Reven']

print "--------------------------------------------------------------"
print dfff['Line_id']

for i in dfff['Line_id'].unique():
    print "iii", i

print dfff['Line_id'].unique()[0]


print dfff[(dfff.Line_id==1) & (dfff.DayOfWeek==8)] [['Reven','Rev_km']]

print "jaja"
#print dfff['DayOfWeek'].unique(), type(dfff['DayOfWeek'].unique())[['Reven','Rev_km']]


DaysList = np.sort(dfff['DayOfWeek'].unique())

for days in DaysList:
    print dfff[(dfff.Line_id==1) & (dfff.DayOfWeek==days)]

ddf = dfff[(dfff.Line_id==1) & (dfff.DayOfWeek==days)]
print ddf[['Reven','Rev_km']].head()

print "print---------------------------------------------"

for days in DaysList:
    print dfff[(dfff.Line_id==1) & (dfff.DayOfWeek==days)].head()

print "***********************************************************"


Ride_load = np.sort(dfff['Ride_load'])
print Ride_load

#ts = pd.Series(Ride_load)
##ts = ts.cumsum()
#ts.plot()
#P.show()




x=Ride_load

# the histogram of the data with histtype='step'
n, bins, patches = P.hist(x, 50, normed=1, histtype='stepfilled')
P.setp(patches, 'facecolor', 'grey', 'alpha', 0.75)
#P.figure()

fig = P.figure()

#with backend.backend_pdf.PdfPages('foo.pdf') as pdf:
    # As many times as you like, create a figure fig and save it:
    # When no figure is specified the current figure is saved
#    pdf.savefig(fig)
#    pdf.savefig()
pp = PdfPages('foo.pdf')
pp.savefig(fig)
P.show()




#print dfff.describe()


    #[['Reven','Rev_km']]:
    # print tmp
#print dfff.Line_id[110]
# Most operations in pandas can be accomplished with operator chaining (groupby, aggregate, apply, etc)
# df.apply(lambda x: x.max() - x.min())

#print dfff.dtypes
#print dfff.describe()
#print dfff.sort(columns='line_id')  #dfff.sort_index(axis=2, ascending=False)
#print dfff.sort('line_id') #['line_id']

#-------------------------------------------------------------------------------

#print "dfff[0:3]",dfff[0:3]
#print "dfff.iloc[Rev_km]",dfff['Rev_km']    #[:] #,1:5]  #.iloc[:,0:2]

#s = pd.Series(np.random.randint(0,7,size=10))
#print s
#s.value_counts()

#ddd = pd.DataFrame(np.random.randn(10, 4))
#print ddd

#-------------------------------------------------------------------------------