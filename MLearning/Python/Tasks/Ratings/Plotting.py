# -*- coding: utf-8 -*-
"""
Created on Wed Feb 05 13:56:38 2014

@author: wuiljai
"""

class Plotting:
    '''
        Basic Analysis SuperClass:    Reading main parameters.
    '''
    def __init__( self, data ):
        
        self.legend = []

    def Init_plot( self, _title, _xaxis, _yaxis ) #line = ''):
        plt.figure()
        params = {'legend.fontsize': 6,
        'legend.linewidth': 2}
        plt.rcParams.update(params)

        plt.title( _title )
        self.legend.append( _xaxis )
        self.legend.append( _yaxis )
        plt.xlabel( _xaxis )
        plt.ylabel( _yaxis )
        #plt.xlim([-10,1010])
        #plt.ylim([-10,1010])
    #--------------------------------------------------------------------------        
        
    def Final_plot( self, _title ):
        pp = PdfPages(str(_title)+'.pdf')
        pp.savefig()
        print ' plot outputted as: '+str(_title)+'.pdf'
        pp.close()

    def Genera_plot( self, _data ):

        plt.plot( [tmp[0] for tmp in self.coordsCustos], [tmp[1] for tmp in self.coordsCustos],'*', color='r', markersize=5)
        plt.plot( [tmp[0] for tmp in self.coordsStores], [tmp[1] for tmp in self.coordsStores],'o', color='b', markersize=10)
        plt.plot( 500, 500,'o', color='r', markersize=15)
        plt.legend( legend, loc='upper right' )
        
        plt.draw()
        plt.show()
        
        
    '''
    def plotStoresCustos(self,printname=0):
        
        plt.figure()
        plt.title(' Geographical Distribution ')

        plt.xlabel(' X Coords ')
        plt.ylabel(' Y Coords ')  


        if printname != 0:
            with PdfPages( 'storesIII.pdf' ) as pdf:
                pdf.savefig()
                pdf.close()
                plt.close()
        #plt.close()
        return 0
        '''