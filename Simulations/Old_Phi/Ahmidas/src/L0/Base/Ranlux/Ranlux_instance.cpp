#include "Ranlux.ih"

Base::Ranlux &Base::Ranlux::instance(int const seed)
{
  if (!Base::Ranlux::s_instance)
    Base::Ranlux::s_instance = new Base::Ranlux(seed);
  else if (seed)
    Base::Ranlux::s_instance->initialize(seed);

  return *Base::Ranlux::s_instance;
}
