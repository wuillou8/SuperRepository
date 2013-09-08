#pragma once

#include <complex>
#include <eigen/Dense>

#include <L0/Base/TemplateMath.h>

static const std::complex< int > _ci0 = std::complex< int >(0, 0);
static const std::complex< int > _ci1 = std::complex< int >(1, 0);
static const std::complex< int > _ciI = std::complex< int >(0, 1);


// First define the generic case, which we'll use as the matrix dimension > 16
// At this point, there is no advantage to using fixed size matrices any more.
template< size_t dim >
class Clifford
{
public:
  typedef Eigen::Matrix< std::complex< int >, SpinorDim< dim >::value, SpinorDim< dim >::value > GMatrix;

private:
  static GMatrix *s_gamma;
  static GMatrix *s_cconj;
  static GMatrix *s_chiral;

  static void generateGamma();
  static void generateCconj();
  static void generateChiral();

public:
  static GMatrix const *gamma();
  static GMatrix const *cconj();
  static GMatrix const *chiral();
  static GMatrix const identity();
};

template< size_t Dim >
typename Clifford< Dim >::GMatrix *Clifford< Dim >::s_gamma = 0;

template< size_t Dim >
typename Clifford< Dim >::GMatrix *Clifford< Dim >::s_cconj = 0;

template< size_t Dim >
typename Clifford< Dim >::GMatrix *Clifford< Dim >::s_chiral = 0;

template< size_t Dim >
typename Clifford< Dim >::GMatrix const inverse(typename Clifford< Dim >::GMatrix const &gamma)
{
  return gamma.inverse();
}

#include "Clifford/Clifford.inlines"

#include "Clifford/Clifford_gamma.template"
#include "Clifford/Clifford_cconj.template"
#include "Clifford/Clifford_chiral.template"

#include "Clifford/Clifford_generateGamma.template"
#include "Clifford/Clifford_generateCconj.template"
#include "Clifford/Clifford_generateChiral.template"
