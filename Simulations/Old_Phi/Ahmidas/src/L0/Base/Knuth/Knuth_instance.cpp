#include "Knuth.ih"

Base::Knuth &Base::Knuth::instance(int seed)
{
  if (!Base::Knuth::s_instance)
    Base::Knuth::s_instance = new Base::Knuth(seed);
  else if (seed)
    Base::Knuth::s_instance->initialize(seed);

  return *Base::Knuth::s_instance;
}
