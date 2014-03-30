#pragma once

#include <L1/IO/Param.h>

namespace IO
{
  class ildgFormat : public Param
  {
    static char *s_start = "<ildgFormat xmlns=\"http://www.lqcd.org/ildg\"xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"        xsi:schemaLocation=\"http://www.lqcd.org/ildg filefmt.xsd\">";
    static char *s_end = "</ildgFormat>";
    public :
      size_t       nx;
      size_t       ny;
      size_t       nz;
      size_t       nt;
      size_t       precision;
      std::string *d_field;
      std::string *d_version;


      virtual void parse();
      virtual void generate() const;
      char const *data() const;
  }
}