#include "Random.ih"

double Base::Random::symmetric()
{
  static Base::Ranlux &generator(Base::Ranlux::instance());
  return 1.0 - 2.0 * generator();
}
