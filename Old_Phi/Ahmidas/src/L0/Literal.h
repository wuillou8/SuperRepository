#pragma once

#include <iostream>

#include "BaseFieldExpr.h"

template< typename VScalar >
struct Traits< Literal< VScalar > >
{
  typedef VScalar Scalar;
  typedef Literal< VScalar > InnerType;
  typedef BaseFieldExpr< Literal< VScalar > > ExprType;
  typedef VScalar ReturnType;
};

template< typename Scalar >
class Literal: public BaseFieldExpr< Literal< Scalar > >
{
  Scalar const d_scalar; // Still a value here - see if we can get it to a reference somehow!

public:
  Literal(Scalar const &scalar)
    : d_scalar(scalar)
  {}

  static Scalar const &coeff(Literal< Scalar > const *me, size_t const &index)
  {
    return me->d_scalar;
  }

  Scalar const &operator[](size_t const &index) const
  {
    return d_scalar;
  }
};

template< typename VScalar >
Literal< VScalar > N(VScalar const &scalar)
{
  return Literal< VScalar >(scalar);
}

template< typename VScalar >
struct Traits< Literal< Eigen::MatrixBase < VScalar > > >
{
  typedef VScalar Scalar;
  typedef Literal< VScalar > InnerType;
  typedef BaseFieldExpr< Literal< VScalar > > ExprType;
  typedef VScalar ReturnType;
};