#include "Ranlux.ih"

double Base::Ranlux::operator()()
{
  for (size_t ctr = 0; ctr < d_lux; ++ctr)
  {
    if (++d_index == d_period)
      d_index = 0;
    d_state[d_index] -= d_state[(d_index + d_delta_s) % d_period] + d_carry;
    if (d_state[d_index] < 0.0)
    {
      d_carry = d_delta_b;
      d_state[d_index] += 1.0;
    }
    else
      d_carry = 0.0;
  }
  return d_state[d_index];
}
