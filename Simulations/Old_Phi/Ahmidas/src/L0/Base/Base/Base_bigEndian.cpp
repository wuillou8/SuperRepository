#include "../Base.h"

namespace
{
// Check for endian style of the machine in use (thanks, Carsten or Marc!)
bool bigEndian()
{
  union
  {
    int l;
    char c[sizeof(int)];
  } u;

  u.l = 1;
  return (u.c[sizeof(int) - 1] == 1);
}
}

bool const Base::bigEndian = ::bigEndian();
