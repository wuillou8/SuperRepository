#include "Writer.ih"

void IO::Lime::Writer::newRecord(std::string const &type)
{
  if (d_hasWritten)
    finalize();
  d_hasWritten = true;

  d_record = Record();
  if (!d_messageRunning)
    d_record.mesBeg = d_messageRunning = true;

  size_t typeSize = type.size() < 127 ? type.size() : 127;
  std::copy(type.c_str(), type.c_str() + typeSize, d_record.type);

  reserveHeader();
}
