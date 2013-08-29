#include "Grid.ih"

namespace Base
{
Grid::Grid(size_t L, size_t T)
  : d_L(L), d_T(T)
{
  // NOTE This forces intialization of s_agent - should be really fixed.
  s_agent.val++;

  size_t gridSize = static_cast< size_t >(MPI::COMM_WORLD.Get_size());
  if (totalVolume() % gridSize) // No balanced distribution available
  {
    std::cerr << "total volume = " << totalVolume() << " # cpus = "
              << gridSize << " => no balanced distribution available. Aborting." << std::endl;
    MPI::COMM_WORLD.Abort(EDEADLK);
  }

  d_localVolume = totalVolume() / gridSize;
  // Compute the gcd using the Euclidian algorithm
  d_dims[idx_T] = greatestCommonDivisor(T, gridSize);

  // The other nodes should be used to divide the spatial part
  {
    size_t spatSize = gridSize / d_dims[idx_T];
    size_t fac[3] = {1, 1, 1};

    size_t idx = 0;
    size_t div = 2;

    // We prime factorize the remainder and distribute the factors
    while (spatSize != 1)
    {
      if (spatSize % div)
      {
        ++div;
        continue;
      }
      spatSize /= div;
      fac[idx++] *= div;
      idx %= 3;
    }

    d_dims[idx_Z] = fac[0];
    d_dims[idx_Y] = fac[1];
    d_dims[idx_X] = fac[2];
  }

  d_sizes[idx_X] = d_L / d_dims[idx_X];
  d_sizes[idx_Y] = d_L / d_dims[idx_Y];
  d_sizes[idx_Z] = d_L / d_dims[idx_Z];
  d_sizes[idx_T] = d_T / d_dims[idx_T];

  // With the dimensions determined, we create a Cartesian communicator
  {
    bool wrap[] = {true, true, true, true};
    int intGrid[4];
    for (size_t idx = 0; idx < 4; ++idx)
      intGrid[idx] = int(d_dims[idx]);

    d_grid = MPI::COMM_WORLD.Create_cart(4 /* ndims */, intGrid, wrap, true /* reorder */);

    bool boolGrid[4] = {false, false, false, false};
    boolGrid[idx_T] = true;
    d_timeSlice = d_grid.Sub(boolGrid);
    d_backbone = d_grid.Split(d_timeSlice.Get_rank(), 0); // We'll leave the rank in standard order

    d_grid.Get_coords(d_grid.Get_rank(), 4, intGrid);
    for (size_t idx = 0; idx < 4; ++idx)
      d_coords[idx] = size_t(intGrid[idx]);
  }

  // Calculate and store the dimensional size for the distribution just constructed
  d_dimSizes[idx_X] = 1;
  d_dimSizes[idx_Y] = d_sizes[idx_X];
  d_dimSizes[idx_Z] = d_dimSizes[idx_Y] * d_sizes[idx_Y];
  d_dimSizes[idx_T] = d_dimSizes[idx_Z] * d_sizes[idx_Z];

  // We want to make sure the setup is consistent, since errors here will be hard
  // enough to trace as it is...
  assert((d_dimSizes[idx_T] * d_sizes[idx_T]) == d_localVolume);

  initContiguousBlock();
  // Finally, we'd like to know the 3D surface of each dimension,
  // and the largest surface over which we will be using communication
  for (size_t ctr = 0; ctr < 4; ++ctr)
    d_surfaces[ctr] = d_localVolume / d_sizes[ctr];
}

}
