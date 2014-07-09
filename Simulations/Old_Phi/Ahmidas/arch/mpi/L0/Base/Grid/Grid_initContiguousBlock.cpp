#include "Grid.ih"

namespace Base
{
void Grid::initContiguousBlock()
{
  size_t cutIdx = 0;
  while ((d_dims[cutIdx] == 1) && (cutIdx < 4))
    ++cutIdx;
  if (cutIdx < 4)
    d_contiguousBlock = dimSize(cutIdx)*d_sizes[cutIdx];
  else
    // local volume should be the same as global volume in this particular case
    d_contiguousBlock = d_localVolume;
}
}
