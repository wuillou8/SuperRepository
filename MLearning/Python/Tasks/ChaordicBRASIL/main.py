"""
@author: jair
"""
import time
import MyChaordicAnalysis
#------------------------------------------------------------------------------

infile, outfile = '../DATA/input-challenge.json', '../DATA/outputJairW.json'

reset = time.time()
analysis = MyChaordicAnalysis.MyChaordicAnalysis( infile, outfile )
readin_t = time.time() - reset
reset = time.time()
analysis.Analysis('../ANALYSIS/my_analysis.dat')
analy_t = time.time() - reset
reset = time.time()
analysis.Preprocessing('../ANALYSIS/prepatrain1.dat', \
                        '../ANALYSIS/prepatrain2.dat', \
                            '../ANALYSIS/prepatrain3.dat')
preproc_t = time.time() - reset 
reset = time.time()
analysis.fitting('noprint') #or ('Model1'), ('Model3')
fit_t = time.time() - reset
reset = time.time()
analysis.RunROCAUConModel('OUT') #or ('YES'), ('OUT')
final_t = time.time() - reset

print 'Reading time: ', readin_t
print 'Analysis time:', analy_t
print 'Processing time: ', preproc_t
print 'Fitting time: ', fit_t
print 'Finalise time: ', final_t
