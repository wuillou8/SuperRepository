#include "ScidacChecksum.ih"

void ScidacChecksum::aggregate(unsigned char const *data, uint32_t siteSize, uint32_t rank)
{
    uint32_t crcSum = crc32(data, siteSize);

    uint32_t rank29 = rank % 29;
    uint32_t rank31 = rank % 31;

    d_sum.as32[0] ^= crcSum << rank29 | crcSum >> (32 - rank29);
    d_sum.as32[1] ^= crcSum << rank31 | crcSum >> (32 - rank31);
}

