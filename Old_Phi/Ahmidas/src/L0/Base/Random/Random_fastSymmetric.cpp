#include "Random.ih"

double Base::Random::fastSymmetric()
{
  return (2 * fastUniform() - 1);
}
