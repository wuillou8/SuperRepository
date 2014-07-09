#include <fstream>
#include <iostream>
#include <sstream>
#include <vector>
#include <string>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include "P0/Random.cpp"

#include "EIGEN/Eigen/Dense"
#include "P0/EigenFcts.cpp"

#include "P0/GaussianVec.cpp"
#include "P0/BMotion.cpp"

#include "P2/RunSimulation.cpp"


using namespace std;
using namespace Eigen;


int main( int argc,char *argv[] )
{
	/*
	for (int i = 0; i < 100; ++i)
	{
	cout << "Random " << randf(1.) << endl;
	cout << "Gaussian " <<  Gaussian(0., 1.) << endl;
	cout << "ExpLaw, m=1. " << ExpLaw(1.) << endl;
	cout << "Vector GaussianLaw \n" <<  GaussVect( 3, 100 ) << endl;
	}
	cout << "BM: " << BMotion(100) << endl;
	*/
	//cout << "BM: " << SimuStocha(10000) << endl;
	//cout << "Black-Scholes: " << BlackScholes2(1000) << endl;
	for (int i = 0; i < 100; ++i)
	{
		cout << "Poisson: " <<  PoissonLaw(1.011) << endl;
	}
	return 0;
}
