#pragma once

namespace IO
{
  class Param
  {
    char       *d_type; //"xlf-info"
    char       *d_data; //"<nx>4</nx><ny>...

    public:
//      Message(char *type); //Create a new empty record of defined type
      Message(char *type, char *data);
      virtual ~Param();
      virtual void parse();
      virtual void generate() const;
      char const *data() const;
  };
}
