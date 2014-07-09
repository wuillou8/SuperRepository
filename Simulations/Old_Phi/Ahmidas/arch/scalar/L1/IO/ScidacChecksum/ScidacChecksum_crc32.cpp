#include "ScidacChecksum.ih"

uint32_t ScidacChecksum::crc32(unsigned char const *buffer, size_t length, uint32_t crc)
{
  crc = ~crc;
  for (size_t ctr = 0; ctr < length; ++ctr)
    crc = d_crcTable[(crc ^ buffer[ctr]) & 0xff] ^ (crc >> 8);
  return ~crc;
}
