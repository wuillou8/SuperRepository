#include <fstream>
#include <iostream>
#include <sstream>
#include <vector>
#include <string>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <typeinfo>

#include "kmean.h"
#include "utilities.cpp"

using namespace std;


//////////////////////////////////////////////////////////////////////////////////////
//	KMean Funtions								    //
//////////////////////////////////////////////////////////////////////////////////////

KMean::point KMean::gen_xy(int count, double radius)
{
	double ang, r;
	point p, pt = (point)malloc(sizeof(point_t)*count);
	//(point)new point[count];//   (point)malloc(sizeof(point_t)*count);
 
	/* note: this is not a uniform 2-d distribution */
	for (p = pt + count; p-- > pt;) {
		ang = randf(2 * M_PI);
		r = randf(radius);
		p->x = (double)( r * cos(ang));
		p->y = r * sin(ang);
	}
	
	return pt;	
}
 
KMean::point lloyd(KMean::point pts, int len, int n_cluster)
{
	int i, j, min_i;
	int changed;
 
	KMean::point p, c;
	KMean::point cent = (KMean::point)malloc(sizeof(KMean::point_t) * n_cluster);
 
	// assign init grouping randomly
	//for_len p->group = j % n_cluster;
 
	// or call k++ init
	kpp(pts, len, cent, n_cluster);
 
	do {
		// group element for centroids are used as counters
		for (c = cent, i = 0; i < n_cluster; i++, c++)
		{ c->group = 0; c->x = c->y = 0; }
		for (j = 0, p = pts; j < len; j++, p++)
		{
			c = cent + p->group;
			c->group++;
			c->x += p->x; c->y += p->y;
		}
		for (c = cent, i = 0; i < n_cluster; i++, c++)

		{ c->x /= c->group; c->y /= c->group; }
 
		changed = 0;
		// find closest centroid of each point 
		for (j = 0, p = pts; j < len; j++, p++)		
		{
			min_i = nearest(p, cent, n_cluster, 0);
			if (min_i != p->group) {
				changed++;
				p->group = min_i;
			}
		}
	} while (changed > (len >> 10)); // stop when 99.9% of points are good
 
	for ( c = cent, i = 0; i < n_cluster; i++, c++ )
	{ c->group = i; }
 
	return cent;	
}

int main( int argc,char *argv[] )
{
	// Nb of Pts, Clusters
	int nbPts, nbK;
	if( argc<=2 ) 
	{
        	printf( "Expecting 2 arguments: NbPoints NbClusters" );
	        exit(1);
	}
	nbPts = atoi( argv[1] );
	nbK = atoi( argv[2] );
	
	// Program
	KMean myKmean( nbPts, nbK );
	cout << "NbPoints: " << myKmean.m_nbPts << "NbClusters" << myKmean.m_nbK << endl;
	
	// generate random points, radius set to 10.0
	myKmean.m_randPts = myKmean.gen_xy( myKmean.m_nbPts, 10.0 );
	// generate centroids
	myKmean.m_cents = lloyd( myKmean.m_randPts, myKmean.m_nbPts, myKmean.m_nbK );
	// print eps file with the points/colors/centroids
	print_eps( myKmean.m_randPts, myKmean.m_nbPts, myKmean.m_cents, myKmean.m_nbK );
	
	return 0;

}
