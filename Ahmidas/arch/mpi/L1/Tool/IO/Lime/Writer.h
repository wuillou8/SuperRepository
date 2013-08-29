#pragma once

#include <stdint.h>
#include <fstream>
#include <string>
#include <cassert>

namespace Tool
{
namespace IO
{
namespace Lime
{
class Writer
{

  static size_t const s_headerSize = 144;
  static uint32_t const s_limeMagic = 0x456789ab;
  static char const s_mesBeginMask = 0x80;
  static char const s_mesEndMask = 0x40;
  static char const s_padding[8];

  union uHeader
  {
    uint64_t as64[s_headerSize / sizeof(uint64_t)];
    uint32_t as32[s_headerSize / sizeof(uint32_t)];
    uint16_t as16[s_headerSize / sizeof(uint16_t)];
    char     as8[s_headerSize];
  };

  struct Record
  {
    char           type[128];
    uint64_t       size;
    std::streampos recOffset; // absolute offset at which the record starts
    std::streampos offset;
    int16_t        version;
    bool           mesBeg;
    bool           mesEnd;

    Record();
    Record(size_t const rOffset, size_t const recSize = 0);
  };

private:
  std::fstream   d_stream;
  std::streampos d_startOfNextRecord;
  Record         d_record;
  bool           d_hasWritten;
  bool           d_messageRunning;
  bool           d_writeHeader;

public:
  Writer(std::string const &filename, bool const writeHeader);
  ~Writer();

  void finishMessage();

  // for parallel writing also the size should be passed. If not (or zero is passed)
  // the function assumes that only onl process writes the record
  void newRecord(std::string const &type, size_t const rOffset, size_t const size = 0);

  size_t closeRecord();

  template< typename DataType >
  void write(DataType const *buffer, uint64_t elements);

  template< typename DataType >
  void write(DataType const *buffer, DataType const *finish);

  template< typename DataType >
  void fill(DataType const &buffer, uint64_t elements);

  bool fail() const;
  bool good() const;

  // sets position to offset bytes in current record
  void seekp(std::streampos const offset);

private:
  void finalize();
  void reserveHeader();
};
}
}
}

#include "Writer/Writer.inlines"
