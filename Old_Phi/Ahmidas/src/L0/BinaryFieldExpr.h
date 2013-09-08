#pragma once

#include <typeinfo>
#include <iostream>
#include <L0/BaseFieldExpr.h>

template< typename Operator, typename Left, typename Right >
struct Traits< BinaryFieldExpr< Operator, Left, Right > >
{
  typedef typename Traits< Left >::Scalar Scalar;
  typedef BinaryFieldExpr< Operator, Left, Right > InnerType;
  typedef BaseFieldExpr< BinaryFieldExpr< Operator, Left, Right > > ExprType;
  typedef typename Eigen::ei_meta_if< !(Eigen::ei_is_arithmetic< typename Traits< Left >::Scalar >::ret), typename Traits< Left >::Scalar, typename Traits< Right >::Scalar >::ret ReturnType;
};

template< typename Operator, typename Left, typename Right >
class BinaryFieldExpr: public BaseFieldExpr< BinaryFieldExpr< Operator, Left, Right > >
{
public:
  typename Traits< Left >::ExprType  const &d_left;
  typename Traits< Right >::ExprType const &d_right;

public:
  BinaryFieldExpr(Left const &left, Right const &right)
    : d_left(left), d_right(right)
  {};

  static typename Traits< BinaryFieldExpr< Operator, Left, Right > >::ReturnType const coeff(BinaryFieldExpr< Operator, Left, Right > const *me, size_t const &index)
  {
    return Operator::coeff(index, me->d_left, me->d_right);
  }
};

struct Sum
{
  template< typename Left, typename Right >
  static typename Traits< BinaryFieldExpr< Sum, Left, Right > >::ReturnType coeff(size_t const &index, BaseFieldExpr< Left > const &left, BaseFieldExpr< Right > const &right)
  {
    return (left[index] + right[index]);
  }
};

template< typename Left, typename Right >
BinaryFieldExpr< Sum, typename Traits< Left >::ExprType, typename Traits< Right >::ExprType > operator+(BaseFieldExpr< Left > const &left, BaseFieldExpr< Right > const &right)
{
  return BinaryFieldExpr< Sum, typename Traits< Left >::ExprType, typename Traits< Right >::ExprType >
         (reinterpret_cast< typename Traits< Left >::ExprType const &>(left),  reinterpret_cast< typename Traits< Right >::ExprType const &>(right));
}

struct Product
{
  template< typename Left, typename Right >
  static typename Traits< BinaryFieldExpr< Product, Left, Right > >::ReturnType coeff(size_t const &index, Left const &left, Right const &right)
  {
    return (left[index] * right[index]);
  }
};

template< typename Left, typename Right >
BinaryFieldExpr< Product, typename Traits< Left >::ExprType, typename Traits< Right >::ExprType > operator*(BaseFieldExpr< Left > const &left, BaseFieldExpr< Right > const &right)
{
  return BinaryFieldExpr< Product, typename Traits< Left >::ExprType, typename Traits< Right >::ExprType >(reinterpret_cast< typename Traits< Left >::ExprType const &>(left),  reinterpret_cast< typename Traits< Right >::ExprType const &>(right));
}

struct Difference
{
  template< typename Left, typename Right >
  static typename Traits< BinaryFieldExpr< Difference, Left, Right > >::ReturnType coeff(size_t const &index, Left const &left, Right const &right)
  {
    return (left[index] - right[index]);
  }
};

template< typename Left, typename Right >
BinaryFieldExpr< Difference, typename Traits< Left >::ExprType, typename Traits< Right >::ExprType > operator-(BaseFieldExpr< Left > const &left, BaseFieldExpr< Right > const &right)
{
  return BinaryFieldExpr< Difference, typename Traits< Left >::ExprType, typename Traits< Right >::ExprType >(reinterpret_cast< typename Traits< Left >::ExprType const &>(left),  reinterpret_cast< typename Traits< Right >::ExprType const &>(right));
}

struct Quotient
{
  template< typename Left, typename Right >
  static typename Traits< BinaryFieldExpr< Quotient, Left, Right > >::ReturnType coeff(size_t const &index, Left const &left, Right const &right)
  {
    return (left[index] / right[index]);
  }
};

template< typename Left, typename Right >
BinaryFieldExpr< Quotient, typename Traits< Left >::ExprType, typename Traits< Right >::ExprType > operator/(BaseFieldExpr< Left > const &left, BaseFieldExpr< Right > const &right)
{
  return BinaryFieldExpr< Quotient, typename Traits< Left >::ExprType, typename Traits< Right >::ExprType >(reinterpret_cast< typename Traits< Left >::ExprType const &>(left),  reinterpret_cast< typename Traits< Right >::ExprType const &>(right));
}
