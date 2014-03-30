#include "Z2.ih"

Base::Z2 &Base::Z2::instance(double const scale, uint64_t const seed)
{
  if (!s_instance)
    s_instance = new Z2(scale, seed);
  return *s_instance;
}
