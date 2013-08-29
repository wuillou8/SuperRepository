#pragma once

#include <algorithm>
#include <complex>
#include <mpi.h>

#include <L0/Base/Base.h>
#include <L0/Base/Grid.h>


// This particular version of Weave is tailored for an MPI setup.
namespace Base
{
class Weave
{
  size_t  d_surfaces[4];
  size_t  d_localSize[4];
  size_t  d_L;
  size_t  d_T;
  size_t  d_localVolume;
  size_t  d_globalVolume;

public:
  Grid d_grid;

  Weave(size_t const L, size_t const T);
  Weave(Weave const &other);
  Weave &operator=(Weave const &other);

  size_t L() const;
  size_t T() const;
  size_t localVolume() const;
  size_t localSurface(Base::SpaceTimeIndex idx) const;
  size_t localSpatialVolume() const;
  size_t dim(Base::SpaceTimeIndex idx) const;
  size_t localSize(Base::SpaceTimeIndex idx) const;
  size_t globalVolume() const;

  size_t rank() const;
  size_t rank(size_t index) const; // rank of the node holding the lattice site with index index
  size_t rank(size_t const *coords) const; // rank of the node with site coordinates coords

  double sum(double result) const;

  template< typename Element >
  void fieldShift(Base::SpaceTimeIndex const idx, Base::Direction const dir, Element *field, size_t const *offsets) const;

  size_t globalCoordToLocalIndex(size_t const x, size_t const y, size_t const z) const;
  size_t globalCoordToLocalIndex(size_t const x, size_t const y, size_t const z, size_t const t) const;

  void sumOverTimeSlices(std::complex< double > const *data_send,
                         std::complex< double > *data_recv, size_t const count=1) const;

  // a wrapper for the MPI::Barrier function
  void barrier() const;

  template< typename Element >
  void broadcast(Element *data, size_t const count, int root) const;

  template< typename Element >
  void sendRecv(Element const * data_send, Element * data_recv, size_t const count, int source, int destination);

  template< typename Element >
  void allReduce(Element const *data_send, Element *data_recv, size_t const count=1) const;

  void allReduce(std::complex< double > const *data_send, std::complex< double > *data_recv, size_t const count=1) const;
  void allReduce(double const *data_send, double *data_recv, size_t const count=1) const;

  bool isLocallyAvailable(size_t const x, size_t const y, size_t const z) const;
  bool isLocallyAvailable(size_t const x, size_t const y, size_t const z, size_t const t) const;

  bool isRoot() const;

private:
  size_t fromGlobal(size_t const x, Base::SpaceTimeIndex const idx) const;
};
}

#include "Weave/Weave.inlines"
#include "Weave/Weave_fieldShift.template"
