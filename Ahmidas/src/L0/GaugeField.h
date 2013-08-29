#pragma once

#include<L0/Field.h>

template < typename Element, size_t D >
class GaugeField
{
  Field< Element, D > *d_fields[D];

public:
  //Constructors
  GaugeField(typename Weave< D >::DimArray const &dims);
  GaugeField(Element const &val, typename Weave< D >::DimArray const &dims);
  GaugeField(Field< Element, D > const &field);
  GaugeField(GaugeField const &other);

  // Destructor
  ~GaugeField();

  // Coefficient access operators (obtain a field in particular direction)
  Field< Element, D > &operator[](size_t idx);
  Field< Element, D > const &operator[](size_t idx) const;

  // Field shift methods
  GaugeField< Element, D > &shift (int const &dim);

  // Miscellaneous methods
  void randomize();
  typename Weave< D >::DimArray const &dims() const;
  size_t volume() const;
};

#include "GaugeField/GaugeField.inlines"
