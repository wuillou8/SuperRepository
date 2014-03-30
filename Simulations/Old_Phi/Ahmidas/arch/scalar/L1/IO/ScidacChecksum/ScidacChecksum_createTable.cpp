#include "ScidacChecksum.ih"

// Produces a lookup table for crc32 checksum calculations
// Checked against known standard crc32 table, found to be working correctly

void ScidacChecksum::createTable()
{
  uint32_t const poly = 0xedb88320; // Defines crc polynomial (0, 1, 2, 4, 5, 7, 8, 10, 11, 12, 16, 22, 23, 26)
  for (uint32_t ctr = 0; ctr < 256; ++ctr)
    d_crcTable[ctr] = ctr;

  for (uint32_t ctr = 0; ctr < 256; ++ctr)
    for (uint32_t shift = 0; shift < 8; ++shift)
      d_crcTable[ctr] = (d_crcTable[ctr] & 1) ? ((d_crcTable[ctr] >> 1) ^ poly) : d_crcTable[ctr] >> 1;
}
