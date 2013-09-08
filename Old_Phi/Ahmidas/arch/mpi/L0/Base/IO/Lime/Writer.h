#pragma once

#include <fstream>
#include <string>

namespace Base
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
    std::streampos offset;
    int16_t        version;
    bool           mesBeg;
    bool           mesEnd;

    Record();
  };

private:
  std::ofstream     d_stream;
  Record            d_record;
  bool              d_hasWritten;
  bool              d_messageRunning;

public:
  Writer(std::string const &filename);
  ~Writer();

  void finishMessage();
  void newRecord(std::string const &type);

  template< typename DataType >
  void write(DataType *buffer, uint64_t elements);

  bool fail() const;
  bool good() const;

private:
  void finalize();
  void reserveHeader();
};
}
}
}
#include "Writer/Writer.inlines"
#include "Writer/Writer_write.template"
