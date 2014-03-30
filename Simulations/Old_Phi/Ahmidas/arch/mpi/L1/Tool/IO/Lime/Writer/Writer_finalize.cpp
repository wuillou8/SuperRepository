#include "Writer.ih"

void Tool::IO::Lime::Writer::finalize()
{

  if(!d_writeHeader || d_hasWritten)
  {
    //d_stream.flush();
    // this process has done its duty
    return;
  }

  assert(d_stream.tellp() >= d_record.recOffset);
  // size can be zero if only one process has written the current record
  // in that case we can ask the stream how many bytes have been written
  uint64_t written = 0;
  if (d_stream.tellp() > 0)
    written = d_stream.tellp() - d_record.recOffset - std::streampos(s_headerSize);
//   std::cout << "d_stream.tellp() = " << d_stream.tellp() << ", d_record.recOffset = " << d_record.recOffset << std::endl;
//   std::cout << "d_record.size = " << d_record.size << ", written = " << written << std::endl;
  // in the other case the actual record size had to be passed and is stored in d_record.size
  written = d_record.size > written ? d_record.size : written;

  d_stream.write(s_padding, (8 - (written % 8)) % 8);
  //d_stream.flush();
  d_startOfNextRecord = d_stream.tellp();

  uHeader header;
  std::fill(header.as8, header.as8 + s_headerSize, 0x00);

  header.as32[0] = s_limeMagic;
  if (!Base::bigEndian)
    Base::swapEndian(header.as32[0]);

  header.as16[2] = d_record.version;
  if (!Base::bigEndian)
    Base::swapEndian(header.as16[2]);

  header.as8[6] = d_record.mesBeg ? s_mesBeginMask : 0x00;
  header.as8[6] = header.as8[6] | (d_record.mesEnd ? s_mesEndMask : 0x00);

  header.as64[1] = written;
  if (!Base::bigEndian)
    Base::swapEndian(header.as64[1]);

  std::copy(d_record.type, d_record.type + 128, header.as8 + 16);

  // Go back and do the actual writing

  // offset is supposed to be zero or s_headerSize,
  // depending on whether Writer::seekp(streampos const) has been called
  // not the case anymore for writing of non-contiguous data
  // assert (d_record.offset == std::streampos(0) || d_record.offset == std::streampos(s_headerSize));

  // std::cout << "d_record.recOffset = " << d_record.recOffset << std::endl;

  d_stream.seekp(d_record.recOffset, std::ios::beg);
  d_stream.write(header.as8, s_headerSize);
  assert(!fail());

  //d_stream.flush();

  static int cnt(0);

//   std::cout << "now I am going to write the actual header! ("  << cnt ++ << ")" << std::endl;
//   std::cout << "---" << std::endl;
//   std::cout << std::string(header.as8, s_headerSize) << std::endl;
//   std::cout << "---" << std::endl;

  d_stream.seekp(d_startOfNextRecord, std::ios::beg);
  d_hasWritten = true;
}
