#pragma once

#include <eigen/Dense>
#include <L0/Base/TemplateMath.h>
#include "TIter.h"


// An indexing type for overloading
template< size_t Value >
class Index
{};

/*** START OF CLASS TENSOR ***/

template< typename Scalar, size_t Dim, size_t Rank >
class Tensor
{
public:
  typedef Eigen::Matrix< Scalar, Power< Dim, Rank >::value, 1 > VectorXs;
  typedef Eigen::Matrix< Scalar, Dim, Power< Dim, Rank - 1>::value > MatrixXs;
  typedef Eigen::Matrix< Scalar const, Dim, Power< Dim, Rank - 1>::value > CMatrixXs;

private:
  VectorXs d_data;

public:
  Tensor();
  Tensor(Scalar *array);
  Tensor(VectorXs const &vec);

  VectorXs &linear();
  VectorXs const &linear() const;

  operator VectorXs &();
  operator VectorXs const &() const;

  template< size_t Value >
  Eigen::Map< MatrixXs, 0, Eigen::Stride< Dim, 1 >, TIter< Scalar, Dim, Rank, Value > > operator[](Index< Value >);

  template< size_t Value1, size_t Value2 >
  Tensor< Scalar, Dim, Rank - 2 > trace(Index< Value1 >, Index< Value2 >) const;
};

// Tensor product: defined as a free function.
template< typename Scalar, size_t Dim, size_t Rank1, size_t Rank2 >
Tensor< Scalar, Dim, Rank1 + Rank2 > operator*(Tensor< Scalar, Dim, Rank1 > const &left, Tensor< Scalar, Dim, Rank2 > const &right);

// Specialization to cover the scalar case
template< typename Scalar, size_t Dim >
class Tensor< Scalar, Dim, 0 >
{
  typedef Eigen::Matrix< Scalar, Power< Dim, 0 >::value, 1 > VectorXs;

  Scalar d_data;

public:
  Tensor();
  Tensor(Scalar const &data);
  Tensor(Scalar *array);
  Tensor(VectorXs const &vec);

  operator Scalar&();
  operator Scalar const &() const;

  Scalar &linear();
};

#include "Tensor/Tensor.inlines"
#include "Tensor/Tensor_contract.template"
#include "Tensor/Tensor_product.template"
#include "Tensor/Tensor_trace.template"
