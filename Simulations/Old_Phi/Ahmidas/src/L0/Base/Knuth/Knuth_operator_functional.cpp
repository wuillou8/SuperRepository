#include "Knuth.ih"

double Base::Knuth::operator()()
{
  if (++d_next == 56)
    d_next = 0;

  if (++d_lag == 56)
    d_lag = 0;

  d_state[d_next] = d_state[d_next] - d_state[d_lag];
  if (d_state[d_next] < 0.0)
    d_state[d_next] += 1.0;
  return d_state[d_next];
}
