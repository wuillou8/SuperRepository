#pragma once

#include <string>
#include <vector>
#include <iostream>

#include <L0/Weave.h>
#include <L0/GaugeField.h>
#include <L1/IO/Lime.h>
#include <L1/IO/ScidacChecksum.h>

namespace IO
{
  struct ILDGinfo
  {
    std::string version;
    std::string field;
    std::string precision;
    size_t      dims[4];

    ILDGinfo(IO::Lime::Reader &reader);
  };

  GaugeField< SUN::MatrixSU3, 4 >  loadILDG(std::string const &filename);
}
