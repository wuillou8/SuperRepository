#include "Writer.ih"

void Base::IO::Lime::Writer::reserveHeader()
{
  d_record.offset = d_stream.tellp();
  for ( size_t ctr = 0; ctr < s_headerSize / 8; ++ctr)
    d_stream.write(s_padding, 8);
}
