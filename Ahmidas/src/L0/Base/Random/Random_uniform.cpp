#include "Random.ih"

double Base::Random::uniform()
{
  static Base::Ranlux &generator(Base::Ranlux::instance());
  return generator();
}
