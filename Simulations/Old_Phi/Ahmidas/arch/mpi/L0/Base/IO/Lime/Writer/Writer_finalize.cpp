#include "Writer.ih"

void Base::IO::Lime::Writer::finalize()
{
  bool bigEndian = Base::bigEndian();

  uint64_t written = d_stream.tellp() - d_record.offset - 144;
  d_stream.write(s_padding, (8 - (written % 8)) % 8);
  std::streampos startOfNextRecord = d_stream.tellp();

  uHeader header;
  std::fill(header.as8, header.as8 + s_headerSize, 0x00);

  header.as32[0] = s_limeMagic;
  if (!bigEndian)
    Base::swapEndian(header.as32[0]);

  header.as16[2] = d_record.version;
  if (!bigEndian)
    Base::swapEndian(header.as16[2]);

  header.as8[6] = d_record.mesBeg ? s_mesBeginMask : 0x00;
  header.as8[6] = header.as8[6] | (d_record.mesEnd ? s_mesEndMask : 0x00);

  header.as64[1] = written;
  if (!bigEndian)
    Base::swapEndian(header.as64[1]);

  std::copy(d_record.type, d_record.type + 128, header.as8 + 16);

  // Go back and do the actual writing
  d_stream.seekp(d_record.offset, std::ios::beg);
  d_stream.write(header.as8, 144);
  d_stream.seekp(startOfNextRecord, std::ios::beg);
}
