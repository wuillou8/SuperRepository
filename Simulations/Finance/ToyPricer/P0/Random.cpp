#pragma once
#include <math.h>


double randf(double m)
{	return m * rand() / (RAND_MAX - 1.); 
}

double Gaussian(double m, double sigma)
{	return m + sigma * pow( -2.*log( randf(1.) ), 0.5 ) * cos( 2. * M_PI * randf(1.) );
}

double ExpLaw(double m)
{	return  -log( randf(1.) ) / m;	
}

double PoissonLaw(double lambda)
{	double u = randf(1.);
	double a = exp(-lambda);
	int n = 0;
	
	while( u > a ){
		u = u * randf(1.);
		n++;
	}
	return n;
}
