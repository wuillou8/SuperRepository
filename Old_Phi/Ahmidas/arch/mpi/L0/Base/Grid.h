#pragma once

#include <algorithm>
#include <cerrno>
#include <functional>
#include <iostream>

#include "mpi.h"

#include "L0/Base/Base.h"

namespace Base
{
class Grid
{
  class MPIAgent
  {
    friend class Base::Grid;

    MPIAgent(); // Protected constructor
  public:
    // This is a dummy member which helps enforcing
    // intialization of static member Grid::s_agent.
    // It is needed since compilers most likely optimize it away,
    // even though it is crucial for initializing and finalizing MPI.
    int val;
    ~MPIAgent();
  };

  static MPIAgent s_agent;

  MPI::Cartcomm d_grid;
  MPI::Cartcomm d_timeSlice;
  MPI::Cartcomm d_backbone;

  size_t d_L;
  size_t d_T;

  size_t d_dims[4]; // number of nodes in each dimension
  size_t d_sizes[4]; // local dimension sizes = L/d_dims(idx_XYZ), T/d_dims(idx_T)
  size_t d_coords[4]; // node coordinates of this node
  size_t d_surfaces[4]; // communication surfaces between nodes, for every dimension
  size_t d_dimSizes[4]; // indicates where to find the next element in a dimension (X=1, Y= sizes(idx_X) etc)

  size_t d_localVolume; //local lattice volume
  size_t d_contiguousBlock; //largest continous data block from full file

  bool d_bigEndian;

public:
  ~Grid(); //Public "destructor" for now
  Grid(size_t L, size_t T);

  MPI::Cartcomm const &grid() const; //NOTE: world? AD: No, Cartesian communicator with content of world...
  MPI::Cartcomm &timeSlice();
  MPI::Cartcomm &backbone();

  size_t rank() const; // rank of this node
  size_t rank(size_t index) const; // rank of the node holding the lattice site with index index
  size_t rank(int const *coords) const; // rank of the node with node coordinates coords

  size_t const *coords() const; // node coordinates of this node
  size_t coord(size_t idx) const; // node coordinate in dimension idx

  size_t const *dims() const; // number of nodes in each dimension
  size_t dim(size_t idx) const; // number of nodes in dimension idx

  size_t const *sizes() const; // dimension sizes on this (=every) node
  size_t size(size_t idx) const; // dimension idx size on this (=every) node

  size_t const *surfaces() const; // communication surfaces
  size_t surface(size_t idx) const; // communication surface in dimension idx

  size_t localVolume() const; // local lattice volume
  size_t totalVolume() const; // total lattice volume

  size_t const *dimSizes() const; // stepsizes to find the next element in a dimension
  size_t dimSize(size_t idx) const; // stepsize to find the next element in dimension idx

  size_t neighbour(SpaceTimeIndex idx, Direction dir) const;

  size_t bufferVolume() const;
  size_t contiguousBlock() const;

  bool bigEndian() const;

private:
  void initContiguousBlock();
  size_t greatestCommonDivisor(size_t x, size_t y);
};
}

#include "Grid/Grid.inlines"
