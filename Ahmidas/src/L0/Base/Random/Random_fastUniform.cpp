#include "Random.ih"

double Base::Random::fastUniform()
{
  static Base::Knuth &generator(Base::Knuth::instance());
  return generator();
}
