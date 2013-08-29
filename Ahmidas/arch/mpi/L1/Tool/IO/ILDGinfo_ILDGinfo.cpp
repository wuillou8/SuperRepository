#include "ILDGinfo.ih"

// Unfortunately, ETMC used to include spurious spaces in its ILDG header. We'll have to strip those out.

inline char *realFront(char *string)
{
  return string + std::strspn(string, " \t");
}

inline size_t realLen(char *string)
{
  return std::strcspn(realFront(string), " \t");
}

Tool::IO::ILDGinfo::ILDGinfo(Tool::IO::Lime::Reader &reader)
{
  reader.retrieveRecord(reader.findRecord("ildg-format"));
  assert(reader.good());

  char *ildgCStr = new char[reader.recordSize()];
  reader.read(ildgCStr, reader.recordSize());

  // We use the C tokenize capabilities to parse this string
  char *pch;
  pch = std::strtok(ildgCStr, "<>");
  if (std::strncmp(pch, "?xml", 4))
    return;

  // We've removed the XML header, now we can set up a state machine to parse the file
  while ((pch = std::strtok(0, "<>")))
  {
    if (std::strncmp(pch, "ildgFormat", 10))
      continue; // Unknown info string, just go on

    while ((pch = std::strtok(0, "<>")))
    {
      if (!std::strncmp(pch, "/ildgFormat", 11))
        break;
      if (!std::strncmp(pch, "version", 7))
      {
        while ((pch = std::strtok(0, "<>")))
        {
          if (!std::strncmp(pch, "/version", 8))
            break;
          version.assign(realFront(pch), realLen(pch));
        }
        continue;
      }
      if (!std::strncmp(pch, "field", 5))
      {
        while ((pch = std::strtok(0, "<>")))
        {
          if (!std::strncmp(pch, "/field", 6))
            break;
          field.assign(realFront(pch), realLen(pch));
        }
        continue;
      }
      if (!std::strncmp(pch, "precision", 9))
      {
        while ((pch = std::strtok(0, "<>")))
        {
          if (!std::strncmp(pch, "/precision", 10))
            break;
          precision.assign(realFront(pch), realLen(pch));
        }
        continue;
      }
      if (!std::strncmp(pch, "lx", 2))
      {
        while ((pch = std::strtok(0, "<>")))
        {
          if (!std::strncmp(pch, "/lx", 3))
            break;
          dims[Base::idx_X] = atoi(realFront(pch));
        }
        continue;
      }
      if (!std::strncmp(pch, "ly", 2))
      {
        while ((pch = std::strtok(0, "<>")))
        {
          if (!std::strncmp(pch, "/ly", 3))
            break;
          dims[Base::idx_Y] = atoi(realFront(pch));
        }
        continue;
      }
      if (!std::strncmp(pch, "lz", 2))
      {
        while ((pch = std::strtok(0, "<>")))
        {
          if (!std::strncmp(pch, "/lz", 3))
            break;
          dims[Base::idx_Z] = atoi(realFront(pch));
        }
        continue;
      }
      if (!std::strncmp(pch, "lt", 2))
      {
        while ((pch = std::strtok(0, "<>")))
        {
          if (!std::strncmp(pch, "/lt", 3))
            break;
          dims[Base::idx_T] = atoi(realFront(pch));
        }
        continue;
      }
    }
    break;
  }
  delete[] ildgCStr;
}
