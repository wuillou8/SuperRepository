#pragma once

#include <cstdlib>

namespace Base
{
class Knuth
{
  static Knuth *s_instance;

  size_t d_next;
  size_t d_lag;

  size_t const d_max;
  int const d_seed;

  double d_state[56];

public:
  static Knuth &instance(int seed = 0);
  double operator()();

  ~Knuth();

private:
  Knuth(int const seed);
  void initialize(int seed = 0);
};
}

#include "Knuth/Knuth.inlines"
