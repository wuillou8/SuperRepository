
import SoundSegment

import csv
from scipy.cluster.vq import kmeans, vq
import numpy as np

class SoundSegmentsDatabase:
        def __init__(self):
                self.segments = []
                self.records = None
                self.databasePath = None
                self.codeBook = None
                #feature vectors of all sound segments:
                #a1,a2
                #       frame1
                #       frame2
                #       frame3
                self.__featureVectors = None
                pass
                
        def readCsvSourceFile(self, filename):
                reader = csv.reader(open(filename, "rb"), delimiter=',', quoting=csv.QUOTE_NONE)
                
                #header = []
                self.records = []
                #fields = 3
                
                #if thereIsAHeader: header = reader.next()
                
                for row, record in enumerate(reader):
                #    if len(record) != fields:
                #        print ("Skipping malformed record %i, contains %i fields (%i expected)" %
                #            (record, len(record), fields))
                #    else:
                        self.records.append(record)
                
        def setCodebook(self, codesCount):
                self.__setFeatureVectors()
                [self.codeBook, self.codeBookError]=kmeans(self.__featureVectors,codesCount)
                self.__emptyFeatureVectors()
                
        def __setFeatureVectors(self):
                first=True
                for rec in self.segments:
                        if first:
                                data=rec.featureVectors.transpose()
                                first=False
                        else:
                                data=np.vstack((data,rec.featureVectors.transpose()))
                self.__featureVectors=data
                
        def __emptyFeatureVectors(self):
                self.__featureVectors=None
                
        def printAll(self, p_filename):
                from matplotlib.backends.backend_pdf import PdfPages
                
                pp = PdfPages(p_filename)
                
                for i in range(0,len(self.segments)):
                        print("printing %s" % self.segments[i].label)
                        figure=self.segments[i].drawAll()
                        figure.suptitle(('%s: %s \n %s' % (self.records[i][0], self.records[i][3], self.records[i][2])), fontsize=12)
                        figure.savefig(pp, format='pdf')
                        figure.clf()
                
                pp.close()
