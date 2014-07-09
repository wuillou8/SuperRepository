#include "Knuth.ih"
#include <iostream>

void Base::Knuth::initialize(int seed)
{
  if (!seed)
    seed = std::time(0);

  double filler = static_cast< double >(std::abs(d_seed - seed) % d_max) / d_max;

  d_state[55] = filler;
  double current = 1.0 / d_max;
  for (size_t ctr = 0; ctr < 55; ++ctr)
  {
    size_t idx = (21 * ctr) % 55;
    d_state[idx] = current;
    current = filler - current;
    if (current < 0.0)
      current += 1.0;
    filler = d_state[idx];
  }

  for (size_t cycle = 0; cycle < 4; ++cycle)
    for (size_t ctr = 0; ctr < 56; ++ctr)
    {
      d_state[ctr] -= d_state[1 + (ctr + 30) % 55];
      if (d_state[ctr] < 0.0)
        d_state[ctr] += 1.0;
    }

  d_next = 0;
  d_lag = 31;
}
