#include <math.h>

#include "Random.h"

/*
 * Quick random generators
 */
namespace QuickRandom
{

void INITQuickRandom() {
	srand (0); //(NULL);
}

//Generates random double between [0,m]
double randf(double m) {
	return m * ((double) rand() ) / (double) RAND_MAX;
}

//Generates random int between [0,m]
size_t randi(size_t m) {
	return  (size_t)((double)m * rand() / (RAND_MAX - 1.));
}

double Gaussian(double m, double sigma) {
	double val1 = randf(1.);
	double val2 = randf(1.);
	return m + sigma * pow( -2.*log( val1  ), 0.5 ) * cos( 2. * M_PI * val2  );
}

double GaussianHull(double val, double m, double sigma) {
	return m + sigma * pow( -2.*log( val ), 0.5 ) * cos( 2. * M_PI * val );
}

double ExpLaw(double m) {
	return  -log( randf(1.) ) / m;
}

/* boxmuller.c Implements the Polar form of the Box-Muller
Transformation

(c) Copyright 1994, Everett F. Carter Jr.
Permission is granted by the author to use
                        this software for any application provided this
                        copyright notice is preserved.							*/

float box_mueller(float m, float s)        // normal random variate generator
{                                 			// mean m, standard deviation s
        float x1, x2, w, y1;
        static float y2;
        static int use_last = 0;

        if (use_last)                 // use value from previous call
        {
                y1 = y2;
                use_last = 0;
        }
        else
        {
                do {
                        x1 = 2.0 * randf(1.) - 1.0;
                        x2 = 2.0 * randf(1.) - 1.0;
                        //x1 = 2.0 * Base::Random::fastUniform() - 1.0;
                        //x2 = 2.0 * Base::Random::fastUniform() - 1.0;
                        w = x1 * x1 + x2 * x2;
                } while ( w >= 1.0 );

                w = sqrt( (-2.0 * log( w ) ) / w );
                y1 = x1 * w;
                y2 = x2 * w;
                use_last = 1;
        }

        return( m + y1 * s );
}

}
