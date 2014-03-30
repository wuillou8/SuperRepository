#include "Z2.ih"

Base::Z2::Z2(double const scale, uint64_t const seed)
  : d_state(seed)
{
  d_scale.asDouble = scale;
  if (!d_state)
  {
    srand(time(0));
    d_state = rand();
    for (size_t ctr = 0; ctr < 256; ++ctr)
      operator()(); // There will be patches of single sign at the start
  }
}
