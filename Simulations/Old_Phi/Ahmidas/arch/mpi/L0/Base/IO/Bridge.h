#pragma once

#include <L0/Core/Field.h>
namespace Base
{
namespace IO
{
template< typename IOClass, typename Element, size_t L, size_t T >
class Bridge
{
  friend class Core::Field< Element, L, T >;

  IOClass                      &d_io;
  Core::Field< Element, L, T > &d_field;

private:
  Bridge(IOClass &io, Core::Field< Element, L, T > &field);
  void loadDataFromIO();
  void saveDataToIO();
};
}
}
#include "Bridge/Bridge_loadDataFromIO.template"

