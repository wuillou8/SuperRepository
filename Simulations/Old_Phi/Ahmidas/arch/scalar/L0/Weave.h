#pragma once

#include <assert.h>
#include <complex>
#include <cstring>

#include <eigen/Dense>

#include <L0/Base/Base.h>

template < size_t D >
class Weave
{
public:
  typedef Eigen::Array< size_t, D, 1 > DimArray;

private:
  DimArray d_dims;
  DimArray d_off;
  Eigen::Array< size_t, D + 1, 1 > d_surf;

public:
  EIGEN_MAKE_ALIGNED_OPERATOR_NEW

  Weave(DimArray const &dims);
  Weave(Weave const &other);
  Weave &operator=(Weave const &other);

  size_t localVolume() const;
  size_t localDim(size_t const &idx) const;
  size_t localSurface(size_t const &idx) const;

  size_t dim(size_t const &idx) const;
  DimArray const &dims() const;
  size_t volume() const;

  size_t rank() const;
  size_t rank(size_t index) const; // rank of the node holding the lattice site with index index
  size_t rank(DimArray const &dims) const; // rank of the node with node coordinates coords

  template< typename Element >
  void fieldShift(size_t const &along, Base::Direction dir, Element *field);

  size_t coordToIndex(DimArray const &coord) const;
  size_t physIdx(size_t const &index) const;

  size_t physEvenOddIdx(size_t const index, bool const odd) const;

  template< typename Element >
  Element globalSum(Element elem) const
  {
    return elem;
  }
};

#include "Weave/Weave.inlines"
#include "Weave/Weave_Weave.template"
#include "Weave/Weave_operatorassign.template"
#include "Weave/Weave_coordToIndex.template"
#include "Weave/Weave_physEvenOddIdx.template"
