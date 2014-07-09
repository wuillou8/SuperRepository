#include "Weave.ih"

size_t Base::Weave::rank(size_t const *coords) const
{
  int mpi_coord[4];
  size_t size;
  for (size_t idx = 0; idx < 4; ++idx)
  {
    size = idx == Base::idx_T ? d_T : d_L;
    mpi_coord[idx] = static_cast< int >(coords[idx] / (size / d_grid.dim(idx)));
  }
  return d_grid.rank(mpi_coord);
}
