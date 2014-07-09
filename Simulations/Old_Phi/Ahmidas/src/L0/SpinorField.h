#pragma once
#include <cmath>

#include <L0/Base/TemplateMath.h>
#include <L0/Core/Field.h>
#include <L0/Clifford.h>

static const double _pi = std::acos(-1);
static const double _pi_2 = std::asin(1);

template < typename Element, size_t D >
class SpinorField
{
  typedef Eigen::Matrix< std::complex< int >, SpinorDim< D >::value, 1 > Phase;

  Phase d_phase;
  Core::Field< Element, D > *d_fields[SpinorDim< D >::value];

public:
  EIGEN_MAKE_ALIGNED_OPERATOR_NEW

  SpinorField(typename Weave< D >::DimArray const &dims);
  SpinorField(Element const &val, typename Weave< D >::DimArray const &dims);
  SpinorField(SpinorField< Element, D > const &other);
  SpinorField(SpinorField< Element, D > const &other, typename Clifford< D >::GMatrix const &gamma);
  ~SpinorField();

  SpinorField< Element, D > &shift(size_t const &along, Base::Direction dir);

  void randomize();

  SpinorField< Element, D > &operator*=(typename Clifford< D >::GMatrix const &gamma);
  SpinorField< Element, D > &operator+=(SpinorField< Element, D > const &other);
  SpinorField< Element, D > &operator-=(SpinorField< Element, D > const &other);

  template< typename Scalar >
  SpinorField< Element, D > &operator*=(Scalar const &scalar);
};

template< typename Element, size_t D >
SpinorField< Element, D > operator*(typename Clifford< D >::GMatrix const &gamma, SpinorField< Element, D > const &spinor);

#include "SpinorField/SpinorField.inlines"
#include "SpinorField/SpinorField_SpinorField_a.template"
#include "SpinorField/SpinorField_SpinorField_b.template"
#include "SpinorField/SpinorField_SpinorField_c.template"
#include "SpinorField/SpinorField_SpinorField_d.template"
#include "SpinorField/SpinorField_~SpinorField.template"
#include "SpinorField/SpinorField_shift.template"
#include "SpinorField/SpinorField_randomize.template"
