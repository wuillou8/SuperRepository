#include "Weave.ih"

Base::Weave::Weave(size_t L, size_t T)
  : d_L(L), d_T(T), d_grid(Base::Grid(L, T))
{
  d_globalVolume = d_L * d_L * d_L * d_T;
  d_localVolume = d_grid.localVolume();
  for (size_t idx = 0; idx < 4; ++idx)
  {
    // SD: this was not consistent with the scalar version,
    // since d_grid.surface() does not return the actual surface size
    // but d_grid.dimSize() does.
    // See Grid_Grid_a.cpp and
    // Weave_Weave_a.cpp in the scalar code.
    // old version:
    // d_surfaces[idx] = d_grid.surface(idx);
    // new one:
    d_surfaces[idx] = d_grid.dimSize(idx); //Surface size in direction
    d_localSize[idx] = d_grid.size(idx); //Local size in direction
  }
}
