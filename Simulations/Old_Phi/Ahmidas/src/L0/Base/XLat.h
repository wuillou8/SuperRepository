#pragma once

#include <sstream>

class XLat
{
  std::istringstream d_data;

public:
  XLat(char const *arg)
    : d_data(arg)
  {}

  template< typename Cast >
  operator Cast()
  {
    Cast result;
    d_data >> result;
    return result;
  }
};
