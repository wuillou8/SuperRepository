#include "Writer.ih"

void Tool::IO::Lime::Writer::reserveHeader()
{
  if (!d_writeHeader)
  {
    // have to move pointer to position after record,
    // if not already done
    if (d_stream.tellp() <= d_record.recOffset)
      d_stream.seekp(d_record.recOffset + std::streampos(s_headerSize));
    return;
  }

  // d_record.offset should be zero, and position in file should be d_record.recOffset
  assert(d_stream.tellp() == d_record.recOffset);
  assert(d_record.offset == std::streampos(0));

  static int cnt(0);

//   std::cout << "now I am going to write a header of zeros! ("  << cnt ++ << ")" << std::endl;

  for (size_t ctr = 0; ctr < s_headerSize / 8; ++ctr)
    d_stream.write(s_padding, 8);
  //d_stream.flush();

  d_hasWritten = false;
}
