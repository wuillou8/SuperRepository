#include <sstream>
#include <vector>
#include <string>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <typeinfo>


struct KMean {
    
    typedef struct { double x, y; int group; } point_t, *point;
   
    int m_nbPts; // Nb Points
    int m_nbK;   // Nb Clusters
    
    
    double m_radius;
    
    //
    point m_randPts;
    point m_cents;
    
    KMean( int nbPts, int nbK ) :
            m_nbPts( nbPts ),
            m_nbK( nbK )
    {};
    virtual ~KMean() {};
    
    point gen_xy( const int count, const double radius );
    point lloyd( point pts, int len, int n_cluster );
    
};