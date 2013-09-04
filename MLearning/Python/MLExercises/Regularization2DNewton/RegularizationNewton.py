#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      wuiljai
#
# Created:     04/09/2013
# Copyright:   (c) wuiljai 2013
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
    def __init__(self, InfileX, InfileY, polyOrder):
        self.x_dat = loadtxt(InfileX,delimiter=',',unpack=True)
        self.y_dat = loadtxt(InfileY)
        self.Order = polyOrder + 1
        self.Dim = self.x_dat.shape[0]
        self.Size = self.x_dat.shape[1]
        self.test = asarray(matrix(self.x_dat))
        self.X = combinate(asarray(matrix(self.x_dat)),self.Order, self.Size)
        self.Y = self.y_dat
        self.N_theta = self.X.shape[1]
        # initial theta as zeros
        self.theta = zeros(self.N_theta)
        self.LAMBDA = eye(self.N_theta) ; self.LAMBDA[0][0] = 0.
        self.Lambd = 0.

    def h_theta(self,idx):
        return 1./(1.+exp(-dot(asarray(self.X)[idx],transpose(self.theta))))

    def H_theta(self):
        return 1./(1.+exp(-dot(asarray(self.X)[:],transpose(self.theta))))

    def J_theta(self):
        # Cost Function:
        # \frac{1}{m} \sum_i^m \[ -y^i log(h_{\theta}(x^i) - (1-y^i)log(1-h_{\theta}(x^i)) +
        # \lambda * \sum_i^N (\theta^i)^2 \]
        J_theta = 0.
        self.lambd = 0.
        for i in range(0,self.Size):
            J_theta -= self.Y[i]*log(self.h_theta(i)) + (1-self.Y[i])*log(1.-self.h_theta(i))
        return (2*J_theta + self.Lambd*dot(self.theta[1:], transpose(self.theta[1:])))/(2.*self.Size)

    def D_J_theta(self):
        # gradient of J_theta
        D_J_theta = []
        tmp = zeros(self.N_theta)
        for j in range(0,self.Size):
            print "bla", squeeze(asarray(self.X[j]))*(self.h_theta(j)-self.Y[j]) #*squeeze(asarray(self.X[j]))
        print "bli" ,  dot(transpose(self.H_theta()[:]-self.Y[:]), squeeze(asarray(self.X[:])))
        pass
        #for i in range(0,self.N_theta):
        #    D_J_theta.append( #1./(self.Size) * \
        #        sum((self.h_theta(i)-self.Y[i]) ) )#*squeeze(asarray(self.X[i])) + dot(self.LAMBDA, transpose(self.theta)) ))
        #return  array(D_J_theta)

    def H_I(self): # Hessian: \frac{1}{m} \sum_i^m \[ h_{\theta}(x^i) (1-h_{\theta}(x^i)) x^i (x^i)^T \]
        H = matrix(zeros((self.N_theta,self.N_theta)))
        for i in range(0,self.Size):
            H += (1./self.Size)*self.h_theta(i)*(1.0-self.h_theta(i)) \
                *dot( transpose(matrix(self.X[i])), matrix(self.X[i])) \
                + self.Lambd*self.LAMBDA
        return H.I

    def Grad_Desc(self, Lambd):
        self.Lambd = Lambd
        print "grad", matrix(self.D_J_theta())
        self.theta = self.theta - squeeze( asarray( dot( self.H_I(), transpose(matrix(self.D_J_theta()))) ))
        return self.theta

    def plot(self):
        dat_0 = [l_reg.x_dat[0][l_reg.y_dat[:] == 0],l_reg.x_dat[1][l_reg.y_dat[:] == 0]]
        dat_1 = [l_reg.x_dat[0][l_reg.y_dat[:] == 1],l_reg.x_dat[1][l_reg.y_dat[:] == 1]]
        pl1=plt.plot(dat_0[0],dat_0[1],'ro',label='y=0')
        pl1=plt.plot(dat_1[0],dat_1[1],'g^',label='y=1')
        pl1=plt.title('Student exams scores && logistic regression')
        pl1=plt.xlabel('U')
        pl1=plt.ylabel('V')
        pl1=plt.legend()
        pl1=plt.draw()
        pylab.show(pl1)

################################################################################
def main():
    pass

if __name__ == '__main__':
    main()
################################################################################

l_reg = Regularization("ex5Logx.dat", "ex5Logy.dat",5) # 5 for the poly_order

# Run
print "grad", l_reg.D_J_theta()
#for i in range(0,1):
    #print "J", l_reg.J_theta()
    #print( "---*-Ite #%s : Theta = %s , J = %s " % (i, l_reg.theta , l_reg.J_theta()))
    #theta_in = l_reg.theta
    #l_reg.Grad_Desc(0)
    #d_theta = theta_in - l_reg.theta
    #if( std(d_theta) <= 1.e-10 ):
    #    print "---*-Algorithm converged after %s Iteration" % i
    #    print "---*-theta_conv = %s , J_theta = %s" % (l_reg.theta, l_reg.J_theta())
	#	#l_Reg.plot()
    #    sys.exit()
