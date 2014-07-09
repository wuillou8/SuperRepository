#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      wuillou8
#
# Created:     03/09/2013
# Copyright:   (c) wuillou8 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import io, os, csv, string, re, sys
from numpy import *

import matplotlib
matplotlib.rcParams['legend.fancybox'] = True
import matplotlib.pyplot as plt
import pylab

class Regularization1:
    def __init__(self, InfileX, InfileY, polyOrder):
        self.x_dat = loadtxt(InfileX)
        self.y_dat = loadtxt(InfileY)
        self.Order = polyOrder + 1
        self.Size = self.x_dat.shape[0]
        self.theta = 0.

    def X_theta(self):
        X_theta = list()
        for i in range(0,self.Order):
            X_theta.append(power(self.x_dat[:], i))
        return matrix(asarray(X_theta))

    def Grad_Desc(self, Lambd):
        # X := X^T
        X = self.X_theta()
        Y = transpose(matrix(self.y_dat))
        LAMBDA = zeros((self.Order,self.Order))
        fill_diagonal(LAMBDA, [0,1,1,1,1,1])
        # Implementing: \theta = \( X^TX + lambda \diag(0,1,1,1,1,1) \)^{-1} X^TY
        m = linalg.inv(X*transpose(X) + Lambd*LAMBDA)*X*Y
        self.theta = asarray( transpose( m ))[0]
        return self.theta

    def J_theta(self):
        # J_{\theta}=\frac{1}{2m} \[ \sum_{i=1}^m (h_theta(x^i) -y^i)^2 + \lambda \sum_{j=1}^n \theta_j^2 \]
        for i in range(0,self.Size):
            J_theta += power( self.h_theta(i) - self.y_dat[i] , 2.)
        return (J_theta + self.lambd*penFct())/(2*self.Size)

    def h_theta(self,dat):
        h_theta = 0.
        for n,tmp in enumerate(self.theta):
            h_theta += self.theta[n]*dat**n
        return h_theta

    def plot(self):
        pl1=plt.plot(self.x_dat,self.y_dat,'ro',label='admitted')
        x = arange(-1, 1, 0.01)
        y = map(lambda x : self.h_theta(x), x)
        plt1=plt.plot(x,y,'r--',label='fit')
        pl1=plt.draw()
        pylab.show(pl1)

################################################################################
def main():
    pass

if __name__ == '__main__':
    main()
################################################################################

l_reg1 = Regularization1("ex5Linx.dat", "ex5Liny.dat", 5)


print "theta for lambda = 0.0: ", l_reg1.Grad_Desc(0.)
l_reg1.plot()

print "theta for lambda = 1.0: ", l_reg1.Grad_Desc(1.)
l_reg1.plot()

print "theta for lambda = 10.0: ", l_reg1.Grad_Desc(10.)
l_reg1.plot()
