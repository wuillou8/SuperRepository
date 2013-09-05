#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      wuillou8
#
# Created:     04/09/2013
# Copyright:   (c) wuillou8 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import io, os, csv, string, re, sys
from numpy import *

import matplotlib
matplotlib.rcParams['legend.fancybox'] = True
import matplotlib.pyplot as plt
import pylab

def combinate(Matr,N,L):
    # generate the combinations (x,y) = (1,x,y,x^2,xy,y^2,..,y^N)
    combinate=[]
    for idx in range(0,L):
        tmp = [1.]
        for i in range(1,N+1):
            for j in range(0,i+1):
                tmp.append( Matr[0][idx]**(i-j)*Matr[1][idx]**j )
        combinate.append(tmp)
    return matrix(combinate)


class Regularization:
    ############################################################################
    #       Class: Regularised Logistic Regression for 2D data                 #
    ############################################################################
    def __init__(self, InfileX, InfileY, polyOrder):
        self.x_dat = loadtxt(InfileX,delimiter=',',unpack=True)
        self.y_dat = loadtxt(InfileY)
        self.Order = polyOrder + 1
        # Preparation
        self.Dim = self.x_dat.shape[0]
        self.Size = self.x_dat.shape[1]
        self.X = combinate(asarray(matrix(self.x_dat)),self.Order, self.Size)
        self.Y = self.y_dat
        self.N_theta = self.X.shape[1]
        # Initial theta/lambda as zeros
        self.theta = zeros(self.N_theta)
        self.Lambd = 0.
        # LAMBDA = diag(0.,1.,1.,...,1.)
        self.LAMBDA = eye(self.N_theta) ; self.LAMBDA[0][0] = 0.

    def H_theta(self,idx=None):
        if idx == None:
            return 1./(1.+exp(-dot(asarray(self.X)[:],transpose(self.theta))))
        else:
            return 1./(1.+exp(-dot(asarray(self.X)[idx],transpose(self.theta))))

    def J_theta(self):
        # Cost Function: \frac{1}{m} \sum_i^m \[ -y^i log(h_{\theta}(x^i) - (1-y^i)log(1-h_{\theta}(x^i))
        # + \lambda * \sum_i^N (\theta^i)^2 \]
        J_theta = 0.
        self.lambd = 0.
        for i in range(0,self.Size):
            J_theta -= self.Y[i]*log(self.H_theta(i)) + (1-self.Y[i])*log(1.-self.H_theta(i))
        return (2*J_theta + self.Lambd*dot(self.theta[1:], transpose(self.theta[1:])))/(2.*self.Size)

    def D_J_theta(self):
        # Gradient of J_theta:
        # \nabla_{\theta} J_{\theta} = \frac{1}{m}*\sum_i^{m} h_theta(x^i)(1-h_theta(x^i) x^i*(x^i)^T
        tmp = zeros(self.N_theta)
        D_J_theta =  dot( transpose(self.H_theta()[:]-self.Y[:]), squeeze(asarray(self.X[:])) ) \
            + self.Lambd*dot(self.LAMBDA, transpose(self.theta) )
        return array(D_J_theta)/self.Size

    def H_I(self):
        # Hessian: \frac{1}{m} \sum_i^m \[ h_{\theta}(x^i) (1-h_{\theta}(x^i)) x^i (x^i)^T \]
        H = matrix(zeros((self.N_theta,self.N_theta)))
        for i in range(0,self.Size):
            H += self.H_theta(i)*(1.0-self.H_theta(i)) * dot( transpose(matrix(self.X[i])), matrix(self.X[i]))
        H += self.Lambd*self.LAMBDA
        return linalg.inv(H/self.Size)

    def Grad_Desc(self, Lambd):
        # Gradient Descent: \theta = \theta - H^{-1} * \nabla_{\theta} J_{\theta}
        self.Lambd = Lambd
        self.theta = self.theta - squeeze( asarray( dot( self.H_I(), transpose(matrix(self.D_J_theta()))) ))
        return self.theta

    def Z_theta(self, delta):
        # fct X : z=\theta^T*X
        # prepare the grid
        x = arange(-1., 1.5, delta)
        y = arange(-1., 1.5, delta)
        X, Y = meshgrid(x, y)
        print X, Y, len(X.flat)
        x = squeeze(reshape(X,len(X.flat)))
        y = squeeze(reshape(Y,len(Y.flat)))
        size = x.shape[0]
        # compute z=\theta^T*X and re-put it on the grid
        z=combinate(asarray([x,y]),self.Order,size)
        z=dot(asarray(z)[:],transpose(self.theta))
        Z=reshape(z,X.shape)
        return plt.contour(X,Y,Z)

    def plot(self):
        dat_0 = [l_reg.x_dat[0][l_reg.y_dat[:] == 0],l_reg.x_dat[1][l_reg.y_dat[:] == 0]]
        dat_1 = [l_reg.x_dat[0][l_reg.y_dat[:] == 1],l_reg.x_dat[1][l_reg.y_dat[:] == 1]]
        pl1=plt.plot(dat_0[0],dat_0[1],'ro',label='y=0')
        pl1=plt.plot(dat_1[0],dat_1[1],'g^',label='y=1')
        pl1=plt.title('Regularised Logistic Regression: Lambda = ' + str(self.Lambd) )
        pl1=plt.xlabel('U')
        pl1=plt.ylabel('V')
        pl1=plt.legend()
        CS=self.Z_theta(0.1)
        pl1=plt.clabel(CS,[0.], fontsize=10)
        pl1=plt.draw()
        #pylab.show(pl1)

################################################################################
def main():
    pass

if __name__ == '__main__':
    main()
################################################################################
#Initialisation
l_reg = Regularization("ex5Logx.dat", "ex5Logy.dat",5) # 5 for the poly_order
N_IterMax = 50

#Run
for Num, mylambda in enumerate([0.,1.,10.]):
    l_reg.Lambd = mylambda #mylambda
    l_reg.theta = zeros(l_reg.N_theta)

    for i in range(0,N_IterMax):
        print( "---*-Ite #%s : J = %s " % (i, l_reg.J_theta()))
        theta_in = l_reg.theta
        l_reg.Grad_Desc(mylambda)
        d_theta = theta_in - l_reg.theta
        if( std(d_theta) <= 1.e-10 ):
            print "---*-For lambda = %s, Algorithm converged after %s Iteration" % ( mylambda,i )
            print "---*-  J_conv = %s, theta_conv = %s " % ( l_reg.J_theta(), l_reg.theta )
            break
        elif ( i == (N_IterMax-1) ):
            print "---*-Convergence Failed for lambda = %s after %s Iterations" % (l_reg.Lambd,N_IterMax)
            sys.exit(1)
   # Plots: Figs with contours for Lambda rates (after and if convergence)
    pylab.figure(Num)
    l_reg.plot()

#Show plots
pylab.show()
