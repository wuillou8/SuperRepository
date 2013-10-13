#pragma once
#include <math.h>
#include "../EIGEN/Eigen/Dense"
#include "../EIGEN/Eigen/Core"
#include "../EIGEN/Eigen/Cholesky"

using namespace std;
using namespace Eigen;

typedef Matrix<double, Dynamic, Dynamic> Matr;
typedef Matrix<double, Dynamic, 1> Vect;


template <typename Derived>
void print_size(const EigenBase<Derived>& b)
{
  cout << "size (rows, cols): " << b.size() << " (" << b.rows()
            << ", " << b.cols() << ")" << endl;
}

