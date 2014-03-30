#include "Weave.ih"

Base::Weave::Weave(Base::Weave const &other)
  : d_L(other.d_L), d_T(other.d_T), d_grid(other.d_grid)
{
  d_globalVolume = d_L*d_L*d_L*d_T;
  d_localVolume = d_grid.localVolume();
  for (size_t idx = 0; idx < 4; ++idx)
  {
    d_surfaces[idx] = d_grid.dimSize(idx); //Surface size in direction
    // this was not consistent with scalar code
    //d_surfaces[idx] = d_grid.surface(idx); //Surface size in direction
    d_localSize[idx] = d_grid.size(idx); //Local size in direction
  }
}
