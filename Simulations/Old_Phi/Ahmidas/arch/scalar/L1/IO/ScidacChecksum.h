#pragma once

#include <L0/Field.h>

#include <cstdlib>
#include <stdint.h>

class ScidacChecksum
{
  union
  {
    uint32_t as32[2];
    uint64_t as64;
  } d_sum;

  uint32_t d_crcTable[256];

  public:
    ScidacChecksum();
    ScidacChecksum(uint64_t const &init);
    ScidacChecksum(ScidacChecksum const &other);
    void clear();

    uint64_t checksum() const;
    uint32_t lower() const;
    uint32_t upper() const;

    void aggregate(unsigned char const *data, uint32_t siteSize, uint32_t rank);

    template< typename Element >
    void calculate(Element const *data, uint32_t elemsPerSite, uint32_t numSites, uint32_t rankOffset = 0);

    bool parse(char *message);

  public:
    void createTable();
    uint32_t crc32(unsigned char const *buffer, size_t length, uint32_t crc = 0);
};

#include "ScidacChecksum/ScidacChecksum.inlines"
#include "ScidacChecksum/ScidacChecksum_calculate.template"
