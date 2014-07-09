#pragma once
#include <math.h>


Matr getRootGamma( int N, int Nb , Vect IniVec )
{// computing  \Gamma = \frac{1}{Nb} (X - 1_N \bar{x})^T (X - 1_N \bar{x}), whereas \bar{X} is the mean over the Nb elements.			
	Matr X(Nb, N);
	Vect avX(N), IdNb(Nb);	
	avX.setConstant(0.);
	IdNb.setConstant(1.);

	for ( int i = 0; i < N; ++i )
	{	for ( int j = 0; j < Nb; ++j )
		{	X(j,i) = Gaussian( IniVec[i], 1.);
			avX(i) += X(j,i)/(double)Nb;
	}	}
	Matr Gamma = (1./Nb) * (X - IdNb * avX.transpose()).transpose() * (X - IdNb * avX.transpose()) ;
	
	LLT<MatrixXd> lltOfA(Gamma);	// compute the Cholesky decomposition of A
	MatrixXd L = lltOfA.matrixL();  // retrieve factor L in the decomposition
	if((Gamma - L * L.transpose() ).norm() >= 1.e-06)
	{ 	
		cout <<  "Error in Cholesky" << endl;
		exit(1);
	}	
	return L; 
}

Vect GaussVect( int N, int Nb )
{
	Vect IniVec(N);	
	IniVec.setConstant(0.);
	Matr L = getRootGamma( N, Nb, IniVec );
	Vect g(N);
	for ( int i = 0; i < N; ++i )
	{	
		g(i) = Gaussian( 0, 1. );
	}
	cout << "m + AG " << endl;
	print_size(IniVec.setConstant(0.) + L*g);
	// m + AG
	return IniVec.setConstant(0.) + L*g;
}
