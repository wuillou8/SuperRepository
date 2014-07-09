#pragma once
#include <math.h>

Vect BMotion(int N)
{
	Vect BM(N);
	BM(0)=0.;
	for ( int i = 1; i < N; ++i ){
		BM(i) = BM(i-1) + Gaussian( 0., 1.);	
	}
	return BM;
}

Vect SimuStocha(int N)
{//	Simple stochastic process
 //	S_{n+1}=S_n + d_t*b + sigma*g_n*d_t^{1/2}	
 //     d_t = 1, b, g_n const
	Vect SimuS(N);
	SimuS(0)=0.;
	double b = 0.01; 
	double sigm = 1.;
	for ( int i = 1; i < N; ++i ){
		SimuS(i) = SimuS(i-1) + b + sigm * Gaussian( 0., 1.);	
	}
	return SimuS;
}

Vect BlackScholes(int N)
{//	Black-Scholes: dX = x(r*dt + sigma dW) 
 //	Euler Method: S_{n+1}=S_n(1 + r*d_t + sigma*g_n*d_t^{1/2})	
 //     d_t = 1, r, g_n const
	Vect BS(N);
	BS(0)=1.;
	double d_t = 0.01;
	double b = 1; 
	double sigm = 1.;
	for ( int i = 1; i < N; ++i ){
		BS(i) = BS(i-1)*(1. + b * d_t + sigm * Gaussian( 0., 1. )*pow(d_t,0.5));	
	}
	return BS;
}

Vect BlackScholes2(int N)
{//	Black-Scholes: dX = x(r*dt + sigma dW) 
 //	Method: S_{n}=S_0 exp( (r- sigma^2/2.) * t + sigma*\sum_i  g_i )	
 //     d_t = 1, r, g_n const
	Vect BS2(N), g(N);
	BS2(0) = 1.;
	double d_t = 0.01;
	double b = 0.1; 
	double sigm = 1.;
	g(0) = 0.;
	for ( int i = 1; i < N; ++i ){
		g(i) += g(i-1) + Gaussian( 0., 1. );
		BS2(i) = BS2(0)*exp( ( b - pow(sigm,2.)/2. ) * i * d_t + sigm * g(i) * pow(d_t, 0.5) );
	}
	return BS2;
}

Vect BlackScholesJump(int N)
{//	Black-Scholes: dX = x(r*dt + sigma dW) 
 //	Euler Method: S_{n+1}=S_n(1 + r*d_t + sigma*g_n*d_t^{1/2})	
 //     d_t = 1, r, g_n const
	Vect JBS(N), g(N);
	JBS(0)=1.;
	double d_t = 1.;
	double b = 1; 
	//JUMPS/////
	int Nbj;
	double sigm = 1.;
	double lambda = 0.1;
	g(0) = 0.;
	////////////
	for ( int i = 1; i < N; ++i ){
		g(i) += g(i-1) + Gaussian( 0., 1. );
		JBS(i) = JBS(0)*exp( ( b - pow(sigm,2.)/2. ) * i * d_t + sigm * g(i) * pow(d_t, 0.5) );
		
		Nbj = PoissonLaw(lambda);
		for (int nj = 0; nj < Nbj; ++nj)
		{
			JBS(i) *= (1. + randf(1.0));
		}
	}
	return JBS;
}

