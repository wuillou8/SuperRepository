#include "Grid.ih"

namespace Base
{
size_t Grid::rank(size_t index) const
{
  int coord[4];
  coord[idx_X] = (index %  d_L             ) / size(idx_X);
  coord[idx_Y] = (index % (d_L * d_L)      ) / (d_L * size(idx_Y));
  coord[idx_Z] = (index % (d_L * d_L * d_L)) / (d_L * d_L * size(idx_Z));
  coord[idx_T] =  index                      / (d_L * d_L * d_L * size(idx_T));
  return rank(coord);
}
}
