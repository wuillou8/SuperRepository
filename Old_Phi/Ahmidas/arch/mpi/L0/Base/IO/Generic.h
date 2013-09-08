#pragma once

#include <fstream>
#include <string>

namespace Base
{
namespace IO
{
class Generic
{
  std::ifstream d_stream;

public:
  Generic(std::string const &filename);

  template< typename DataType >
  void read(DataType *buffer, uint64_t const elements) const;

  bool fail() const;
};
}
}
#include "Generic/Generic.inlines"
