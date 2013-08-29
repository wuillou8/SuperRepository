#include "Writer.ih"
size_t Tool::IO::Lime::Writer::closeRecord()
{
  finalize();

  if (d_writeHeader)
  {
    // std::cout << "d_startOfNextRecord = " << d_startOfNextRecord << std::endl;
    return d_startOfNextRecord;
  }
  else return 0;
}
