#include <math.h>

#include "Random.h"

/*
 * Quick random generators
 */
namespace QuickRandom
{
//Generates random double between [0,m]
double randf(double m) {
	return (double)m * rand() / (RAND_MAX - 1.);
}

//Generates random int between [0,m]
size_t randi(size_t m) {
	return  (size_t)((double)m * rand() / (RAND_MAX - 1.));
}

double Gaussian(double m, double sigma) {
	return m + sigma * pow( -2.*log( randf(1.) ), 0.5 ) * cos( 2. * M_PI * randf(1.) );
}

double ExpLaw(double m) {
	return  -log( randf(1.) ) / m;
}

}
