#include "ScidacChecksum.ih"

bool ScidacChecksum::parse(char *message)
{
  bool read_suma = false;
  bool read_sumb = false;
  char *pos = strtok(message, "<> \n\t");
 
  while (pos)
  {
    if (!strncmp(pos, "suma", 4))
    {
      pos = strtok(0, "<> \n\t");
      sscanf(pos, "%x", d_sum.as32);
      read_suma = true;
    }
    if (!strncmp(pos, "sumb", 4))
    {
      pos = strtok(0, "<> \n\t");
      sscanf(pos, "%x", d_sum.as32 + 1);
      read_sumb = true;
    }
    pos = strtok(0, "<> \n\t");
  }
  return (read_suma && read_sumb);
}
