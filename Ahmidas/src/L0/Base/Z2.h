#pragma once

#include <stdint.h>
#include <iostream>
#include <iomanip>

namespace Base
{
class Z2
{
  static Z2 *s_instance;

  static uint64_t const d_mask64 = 0x8000000000000000;
  static uint64_t const d_maskPoly = 0x56C9E91ACA649B2C; // More dense polynomial

  uint64_t  d_state;

  union
  {
    double    asDouble;
    uint64_t  asUInt;
  } d_scale;

public:
  static Z2 &instance(double const scale = 1.0, uint64_t const seed = 0);
  double operator()();

  void setScale(double const scale);

private:
  Z2(double const scale, uint64_t const seed);
};
}

#include "Z2/Z2.inlines"
