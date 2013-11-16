#-------------------------------------------------------------------------------
# Name:        myPseudoNose
# Purpose:
#
# Author:      wuiljai
#
# Created:     05/11/2013
# Copyright:   (c) wuiljai 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import sys
import numpy as np
from pandas import DataFrame
import pandas as pd


import pylab as P
import matplotlib
matplotlib.rcParams['legend.fancybox'] = True
import matplotlib.pyplot as plt
import math

from matplotlib.backends.backend_pdf import PdfPages
#-------------------------------------------------------------------------------
import myPandaUtilities
#-------------------------------------------------------------------------------
#import DBAnalytics as dba
#dba.LoadLibrary()
#import  pyquantlib as mql
#-------------------------------------------------------------------------------

def dframesDiff( dffrom, dfto ):
    ''' get differences beetween 2 dframes '''
    print dffrom.head(10)
    print dfto.head(10)
    ne_stacked = (dffrom != dfto).stack()
    changed = ne_stacked[ne_stacked]
    changed.index.names = ['id', 'col']
    diff_idxs = np.where(dffrom != dfto)
    changed_from = dffrom.values[diff_idxs]
    changed_to = dfto.values[diff_idxs]
    return changed, changed_from, changed_to

class myPseudoNose:
    ''' PseudoNode: Much better than Nose!!! '''
    def __init__(self, Dir, filesList ): #dataFile):
        # read in files and pass it into a numpy vector (first line/column removed)
        self.dir = Dir
        self.filesList = filesList
        # CritDiff differentiate dictionaries with 4 differences
        self.CritDiff = 4
        self.SetUuup()
        self.Ruuun()
        self.TearDooewneu()

    def SetUuup(self):
        self.initdf = pd.read_csv( self.dir+self.filesList[0] )

    def TearDooewneu(self):
        #print myPandaUtilities.myLazyDispl(self.initdf)
        #print self.initdf.head(20)
        #print type(self.initdf)
        #print self.initdf.iloc[3][0]
        return 0

    def Ruuun(self):
        dframeheaders = [ 'fileName','fileNum','RootNb',\
                        'RootNm','attrModif','branchWeight','from','to' ]
        mydf = myPandaUtilities.myDframe( dframeheaders )

        numTrunc = 0
        self.listTruncNbs = []
        myList = self.filesList

        while ( len(myList) > 0 ):
            dicfile = myList[0]
            dicframe = pd.read_csv(self.dir+dicfile)
            mlist = [dicfile]

            ''' Identify the affiliated files '''
            for enum, myfile in enumerate(myList[1:]):
                fileframe = pd.read_csv(self.dir+myfile)
                changed, changed_from, changed_to = \
                                    dframesDiff( dicframe, fileframe )
                if ( changed_to.size < self.CritDiff ):
                    mlist.append( myfile )

            ''' Find the best file as tree trunc      '''
            dictrunk = self.BestRoot( mlist )
            self.listTruncNbs.append( dictrunk )

            ''' Generate the data frame based on the dictrunk '''
            dicframe = pd.read_csv(self.dir+dictrunk)
            for i in range(10):
                tmp = [ dictrunk, \
                            self.filesList.index(dictrunk), \
                            numTrunc, \
                            dicfile, \
                            i, \
                            0, \
                            dicframe.iloc[i][1], \
                            dicframe.iloc[i][1] ] #changed_to[i]                   ]
                mydf.Append( tmp )


            for enum, myfile in enumerate(mlist):
                fileframe = pd.read_csv(self.dir+myfile)
                changed, changed_from, changed_to = \
                                    dframesDiff( dicframe, fileframe )

                for i in range( changed_to.size ):
                    tmp = [ myfile, \
                            self.filesList.index(myfile), \
                            numTrunc, \
                            dictrunk, \
                            changed.index[i][0], \
                            changed_to.size, \
                            changed_from[i], \
                            changed_to[i]                    ]
                    mydf.Append( tmp )

            ''' Erase files already classified/attributed to a root  '''
            #


            [ myList.pop( myList.index( tmp ) ) for tmp in mlist]
            numTrunc = numTrunc + 1



        #print mydf.inArr[1]
        #print myPandaUtilities.uniq(mydf.inArr[1])
        mydf.DoFrame()

        #pcd = myPandaUtilities.myfilter( mydf.PDFrame, ['branchWeight',0],['RootNb'])
        print 'ici', self.listTruncNbs  #mydf.PDFrame.head(10)

        #print type(mydf.DoFrame) #.head(10)
        #sys.exit()
        ''' Data analysis: summaries, ordering etc... '''
        mydf.PDFrame = self.postAnalysis(mydf.PDFrame)

        ''' Plotting '''
        print mydf.PDFrame['branchWeight'] #.head(10)
        #sys.exit()
        #self.Output( mydf.PDFrame )
        self.Plot(mydf.PDFrame, False) #True, False)
        #self.AnalysisTree( mydf.PDFrame )

    def Output(self, dframe):

        f = open('my_output.csv', 'w')
        print >> f, 'FileNumber', 'FileName',  'RootNb', 'AttributeNb' ,'from', 'to'
        for rootNb, rootNm in enumerate(self.TruncNames):
            print >> f, 'Dict rootNumber: ', rootNb,' rootName : ', rootNm
            dframe[dframe['RootNb']==rootNb][['fileName','RootNb','attrModif','from','to']].to_csv('my_output.csv', mode='a', header=False)

# ##############################################################################
################################################################################
    def AnalysisTree(self, dframe):

        for n, trunc in enumerate([0]) : #enumerate(self.listTruncNbs):
            #n = n + 1
            print n, trunc
            print self.truncCoords[n]
            print 'DBG', n


            df = dframe[dframe['RootNb']==n]
            filNames1 = []
            filCoords1 = []
            filTos1 = []
            filNames2 = []
            filCoords2 = []
            filTos2 = []
            filNames3 = []
            filCoords3 = []
            filTos3 = []
            #print df['fileName'].unique()

            for i in df['fileName'].unique():

                coords = []
                tos = []
                #myfilter(df,arrFilter,arrFields = []):
                tmp = myPandaUtilities.myfilter( df, ['fileName',i], ['fileNum','attrModif','toNb','branchWeight'] )
                #myPandaUtilities.myLazyDispl(tmp)

                if ( tmp.shape[0] == 1 ):
                    #print 'DBG0', tmp['fileNum']
                    filCoords1.append(  [ tmp['attrModif'].iloc[0] ] )
                    filTos1.append( [ tmp['toNb'].iloc[0] ] ) # tmp.iloc[:,1] #
                    filNames1.append( i )
                if ( tmp.shape[0] == 2 ):
                    filCoords2.append(  [ tmp['attrModif'].iloc[0], tmp['attrModif'].iloc[1] ]  )
                    filTos2.append( [ tmp['toNb'].iloc[0], tmp['toNb'].iloc[1]] )
                    filNames2.append( i )
                if ( tmp.shape[0] == 3 ):
                    filCoords3.append( [ tmp['attrModif'].iloc[0], tmp['attrModif'].iloc[1], tmp['attrModif'].iloc[2] ] )
                    filTos3.append( [ tmp['toNb'].iloc[0], tmp['toNb'].iloc[1], tmp['toNb'].iloc[2] ] )
                    filNames3.append( i )

            filNames = self.listTruncNbs[n]
            filCoords = [self.attrModif[:]] #
            filTos = self.truncCoords[n]

            myTree = myPandaUtilities.DataTree(  self.attrModif)
            myTree.AnalysisDic(filNames, filCoords, filTos)
            myTree.Analysis1D(filNames1, filCoords1, filTos1)
            myTree.Analysis2D(filNames2, filCoords2, filTos2)
            myTree.Analysis3D(filNames3, filCoords3, filTos3)


            print '585555555555555555555555555555555555555555555555555555555555'
            print myTree.points
            print myTree.points[36]
            print len(myTree.points)

            print myTree.AlgorithmTree()

 #[ 'fileName','fileNum','RootNb',\
 #                       'RootNm','attrModif','branchWeight','from','to' ]
################################################################################
# ##############################################################################

    def Plot(self, dframe, DisplayOrPrint = True):
        ''' General Plot '''

        for n_root, root in enumerate(self.listTruncNbs):
            dfroot = dframe[dframe['RootNb'] == n_root ]

            plt.figure(1)
            ypos = n_root
            self.x=plt.subplot(len(self.listTruncNbs),1,ypos)
            tmp = []
            [ tmp.append(str(i)) for i in  np.sort( dfroot['attrModif'].unique() ) ]

            self.x.set_xlim ( [-0.25, 10.25] )
            self.x.set_ylim ( [-0.5, len(dframe['toNb'].unique())+0.5] )
            ###############################################
            self.plotdf( n_root, dfroot )
        if DisplayOrPrint:
            self.x.show()
        else:
            self.Finalize_plot()
            plt.show()


    def plotdf(self, rootNB, df):
        ''' Subfigs Plot '''

        legend = []
        mycolors = [0, 'g', 'c', 'r','b']

        self.x.axis("off")
        self.x = plt.plot(self.attrModif,self.truncCoords[rootNB],label='root',marker=".")
        legend.append('truncDict')
        for key, grp in df.groupby(['branchWeight']):
            if ( key > 0 ):
                legend.append(key)
                print key, ' --- ' , grp
                print self.truncCoords[rootNB]
                self.x = grp.plot('attrModif','toNb',color=mycolors[key],label=key,marker="o")
                self.x.legend(legend)

        self.x =plt.legend(legend, loc='upper left',title='dics'+str(rootNB), fontsize=5,markerscale=0.1, handlelength=2)
        self.x=plt.draw()

    def Finalize_plot(self):
        pp = PdfPages('file.pdf')
        pp.savefig()
        pp.close()

    def BestRoot( self, mFile ):
        # Get the file with the smaller differences within the file set
        table = []
        for enum, tmp in enumerate(mFile):
            table.append( self.diffWeight(tmp,mFile) )
        return mFile[ table.index(min(table)) ]

    def diffWeight(self, mfile, myList):
        # Take a file and sum up the diffs found within a list
        diffWeight = 0
        dframe1 = pd.read_csv(self.dir+mfile)
        for enum, tmp in enumerate(myList[1:]):
            dframe2 = pd.read_csv(self.dir+tmp)
            changed, changed_from, changed_to = \
                           dframesDiff( dframe1, dframe2 )
            diffWeight += changed_to.size
        return diffWeight

    def postAnalysis(self, dframe):
        # summaries
        self.TruncNames =  dframe['RootNm'].unique()
        #print self.TruncNames
        #sys.exit()
        self.NbRoots = len(self.TruncNames)
        self.attrModif = np.sort(dframe['attrModif'].unique())
        self.truncCoords = [ [] for i in range(len(self.TruncNames)) ]

        ''' Modified attributes into numeroted_list '''
        df = []
        for attr in np.sort( dframe['attrModif'].unique() ):
            numerate_list = np.sort( dframe[dframe['attrModif'] == attr]['to'].unique() )
            numerate_list = np.append( numerate_list, np.sort( dframe[dframe['attrModif'] == attr]['from'].unique() ))

            ''' add dictionary Parameters '''
            for nb, dicNm in enumerate(self.TruncNames):
                rootframe = pd.read_csv(self.dir+dicNm)
                numerate_list = np.append( numerate_list, rootframe.loc[attr][1] )
            numerate_list = np.unique( numerate_list )
            print numerate_list
            ''' Parameters changed into coords/numbers '''
            tmp = dframe[dframe['attrModif'] == attr]
            tmp['toNb'] = tmp['to'].apply( \
                        lambda x: np.where( numerate_list == ''.join(x[:]) )[0][0] )
            tmp['fromNb'] = tmp['from'].apply( \
                        lambda x: np.where( numerate_list == ''.join(x[:]) )[0][0] )

            ''' comput dic. coords for the plotting '''
            for nb, dicNm in enumerate(self.TruncNames):
                rootframe = pd.read_csv(self.dir+dicNm)
                self.truncCoords[nb].append( \
                            np.where( numerate_list ==  rootframe.loc[attr][1] )[0][0] )


            df.append( tmp )
        print dframe['attrModif'].unique()
        print 'la', tmp # df
        print df, len(df)
        if (len(df) > 0):
            dframe = pd.concat( df )
        dframe = dframe.sort()
        del df
        return dframe