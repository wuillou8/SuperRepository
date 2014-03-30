#pragma once

#include <complex>
#include <eigen/Dense>
#include <L0/Base/Random.h>

namespace SUN
{
// The standard matrix operations are uploaded from the Eigen libraries.
// Matrix operations can be entered as M = M1+M2, since the compiler
// is claimed in documentation to organise optimisations.

typedef Eigen::Matrix< std::complex< double >, 1, 1 > VectorU1;
typedef Eigen::Matrix< std::complex< double >, 1, 1 > MatrixU1;

typedef Eigen::Matrix< std::complex< double >, 2, 1 > VectorSU2;
typedef Eigen::Matrix< std::complex< double >, 2, 2 > MatrixSU2;

typedef Eigen::Matrix< std::complex< double >, 3, 1 > VectorSU3;
typedef Eigen::Matrix< std::complex< double >, 3, 3 > MatrixSU3;

typedef Eigen::Matrix< std::complex< double >, 4, 1 > VectorSU4;
typedef Eigen::Matrix< std::complex< double >, 4, 4 > MatrixSU4;

typedef Eigen::Matrix< std::complex< double >, 5, 1 > VectorSU5;
typedef Eigen::Matrix< std::complex< double >, 5, 5 > MatrixSU5;

template< typename Mat >
void reunitarize(Mat &mat);

template< >
void reunitarize(MatrixU1 &mat);

template< typename Mat >
void randomize(Mat &mat);

template< typename Mat >
Mat hc(Mat const &mat);

//  template< typename Mat >
//  Mat trace(Mat const &mat);

template< typename Mat >
Mat rightMultiply(Mat  &rmat); //, Mat const &rmat);

template< typename Mat >
Mat leftMultiply(Mat  &lmat); //, Mat const &rmat);

}

static double const pi = 2 * std::asin(-1);

namespace U1
{
typedef Eigen::Matrix< std::complex< double >, 1, 1 > Vector;
typedef Eigen::Matrix< std::complex< double >, 1, 1 > Matrix;
}

namespace SU3
{
typedef Eigen::Matrix< std::complex< double >, 3, 1 > Vector;
typedef Eigen::Matrix< std::complex< double >, 3, 3 > Matrix;
}

#include "SUN/reunitarize.template"
//#include "SUN/plaquette.template"
#include "SUN/SUN.inlines"

//#include "SUN/SUN.operators.inlines"
