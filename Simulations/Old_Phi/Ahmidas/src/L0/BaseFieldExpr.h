#pragma once

#include <eigen/Core>

// Terminal expressions
template< typename Element, size_t D >
class Field;

template< typename Scalar >
class Literal;

// Binary expressions
template< typename Operator, typename Left, typename Right >
class BinaryFieldExpr;

// Traits
template< typename Derived >
struct Traits;

template< typename Derived >
class BaseFieldExpr
{
public:
  typename Traits< Derived >::ReturnType operator[](size_t const &index)
  {
    return Derived::coeff(reinterpret_cast<Derived*>(this), index);
  }

  typename Traits< Derived >::ReturnType const operator[](size_t const &index) const
  {
    return Derived::coeff(reinterpret_cast<Derived const *>(this), index);
  }
};

// Traits

// Generic case - type not recognized. User for recognition of Literal.
template< typename Derived >
struct Traits
{
  typedef Derived Scalar;
  typedef Literal< Derived > InnerType;
  typedef BaseFieldExpr< Literal< Derived > > ExprType;
  typedef Derived ReturnType;
};

// Case for the resolution of a BaseFieldExpr
template< typename Derived >
struct Traits< BaseFieldExpr< Derived > >
{
  typedef typename Traits< Derived >::Scalar Scalar;
  typedef Derived InnerType;
  typedef BaseFieldExpr< Derived > ExprType;
  typedef Derived ReturnType;
};
