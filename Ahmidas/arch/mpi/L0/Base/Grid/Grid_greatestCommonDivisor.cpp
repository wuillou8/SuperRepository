#include "Grid.ih"

namespace Base
{
size_t Grid::greatestCommonDivisor(size_t x, size_t y)
{
  size_t high = std::max(x, y);
  size_t low  = std::min(x, y);

  while (high % low)
  {
    std::swap(high, low);
    low = low % high;
  }
  return low;
}
}
