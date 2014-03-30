#pragma once

#include <algorithm>
#include <iostream>
#include <complex>
#include <valarray>
#include <typeinfo>

#include <L0/BaseFieldExpr.h>
#include <L0/BinaryFieldExpr.h>
#include <L0/UnaryFieldExpr.h>
#include <L0/Literal.h>
#include <L0/Base/Base.h>
#include <L0/Weave.h>
#include <L0/SUN.h>

template< typename Element, size_t D = 4 >
class Field: public BaseFieldExpr< Field< Element, D > >
{
public:
  size_t      *d_references;
  Weave< D >  *d_weave;
  Element     *d_field;

public:
  EIGEN_MAKE_ALIGNED_OPERATOR_NEW

  // Constructors
  Field(typename Weave< D >::DimArray const &dimensions);
  Field(Element const &value, typename Weave< D >::DimArray const &dimensions);
  Field(Field< Element, D > const &other);
  Field< Element, D > &operator=(Field< Element, D > const &other);

  // Destructor
  ~Field();

  // Lazy evaluation assignment
  template< typename Derived >
  Field< Element, D > &operator=(BaseFieldExpr< Derived > const &other);

  template< typename Derived >
  Field< Element, D > &operator+=(BaseFieldExpr< Derived > const &other);

  template< typename Derived >
  Field< Element, D > &operator-=(BaseFieldExpr< Derived > const &other);


  // Access to field geometry
  size_t volume() const;
  size_t localVolume() const;
  typename Weave< D >::DimArray const &dims() const;

  // Field shifts
  Field< Element, D > &shift(size_t const &along, Base::Direction dir);

  // Element access
  Element &operator[](typename Weave< D >::DimArray const &dimensions);
  Element const &operator[](typename Weave< D >::DimArray const &dimensions) const;

  Element &operator[](size_t const &index);
  Element const &operator[](size_t const &index) const;

  Element &atEven(size_t const idx);
  Element const &atEven(size_t const idx) const;

  Element &atOdd(size_t const idx);
  Element const &atOdd(size_t const idx) const;

  Element &coeff(size_t const idx);
  Element const &coeff(size_t const idx) const;

  Element &coeff(typename Weave< D >::DimArray const &dimensions);
  Element const &coeff(typename Weave< D >::DimArray const &dimensions) const;

  // Static method used in the template evaluation mechanism
  static Element &coeff(Field< Element, D > *me, size_t const idx);
  static Element const &coeff(Field< Element, D > const *me, size_t const idx);

  // Miscellaneous methods
  void randomize();
  Element sum(); // Element summed over all sites
  Field< typename Element::Scalar, D > trace() const;
  Element *raw()
  {
    return d_field;
  }

private:
  void destroy();
  void isolate();
};

template< typename Element, size_t D >
struct Traits< Field< Element, D > >
{
  typedef Element Scalar;
  typedef Field< Element, D > InnerType;
  typedef BaseFieldExpr< Field< Element, D > > ExprType;
  typedef Element ReturnType;
};

#include "Field/Field.inlines"
#include "Field/Field_isolate.template"
#include "Field/Field_shift.template"
