#pragma once

#include <cstdlib>

namespace Base
{
class Ranlux
{
  static Ranlux *s_instance;

  double const d_delta_b;
  size_t const d_period;
  size_t const d_delta_s;
  size_t const d_lux;

  double d_state[24];

  size_t d_index;
  double d_carry;

public:
  static Ranlux &instance(int const seed = 0);
  double operator()();

  ~Ranlux();

private:
  Ranlux(int const seed);
  void initialize(int const seed = 0);
};
}

#include "Ranlux/Ranlux.inlines"
