#pragma once

#include <typeinfo>
#include <iostream>
#include <L0/BaseFieldExpr.h>

template< typename Operator, typename Arg >
class UnaryFieldExpr;

template< typename Operator, typename Arg >
struct Traits< UnaryFieldExpr< Operator, Arg > >
{
  typedef typename Traits< Arg >::Scalar Scalar;
  typedef UnaryFieldExpr< Operator, Arg > InnerType;
  typedef BaseFieldExpr< UnaryFieldExpr< Operator, Arg > > ExprType;
  typedef typename Traits< Arg >::Scalar ReturnType;
};

template< typename Operator, typename Arg >
class UnaryFieldExpr: public BaseFieldExpr< UnaryFieldExpr< Operator, Arg > >
{
  typename Traits< Arg >::ExprType  const &d_arg;

public:
  UnaryFieldExpr(Arg const &arg)
    : d_arg(arg)
  {};

  static typename Traits< UnaryFieldExpr< Operator, Arg > >::ReturnType const coeff(UnaryFieldExpr< Operator, Arg > const *me, size_t const &index)
  {
    return Operator::coeff(index, me->d_arg);
  }
};

class Adjoint
{
public:
  template< typename Arg >
  static typename Traits< Arg >::Scalar coeff(size_t const &index, BaseFieldExpr< Arg > const &arg)
  {
    return (arg[index].adjoint().eval());
  }
};

template< typename Arg >
UnaryFieldExpr< Adjoint, typename Traits< Arg >::ExprType > adjoint(BaseFieldExpr< Arg > const &arg)
{
  return UnaryFieldExpr< Adjoint, typename Traits< Arg >::ExprType >(reinterpret_cast< typename Traits< Arg >::ExprType const &>(arg));
}

struct Minus
{
  template< typename Arg >
  static typename Traits< Arg >::Scalar coeff(size_t const &index, BaseFieldExpr< Arg > const &arg)
  {
    return (-arg[index]).eval();
  }
};

template< typename Arg >
UnaryFieldExpr< Minus, typename Traits< Arg >::ExprType > operator-(BaseFieldExpr< Arg > const &arg)
{
  return UnaryFieldExpr< Minus, typename Traits< Arg >::ExprType >(reinterpret_cast< typename Traits< Arg >::ExprType const &>(arg));
}
