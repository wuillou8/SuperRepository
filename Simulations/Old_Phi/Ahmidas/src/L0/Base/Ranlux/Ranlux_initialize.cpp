#include "Ranlux.ih"

void Base::Ranlux::initialize(int const seed)
{
  if (seed)
    srand(seed);
  else
    srand(time(0));

  // Set up initial state of the system
  for (size_t ctr = 0; ctr < d_period; ++ctr)
    d_state[ctr] = std::rand() * d_delta_b;

  // Get rid of initial correlations
  for (size_t ctr = 0; ctr < 10; ++ctr)
    rand();
}
