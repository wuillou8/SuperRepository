#pragma once

#include <stdint.h>

#include <algorithm>
#include <fstream>
#include <string>
#include <vector>

#include <L0/Base/Base.h>

namespace Base
{
namespace IO
{
namespace Lime
{
class Reader
{
  static size_t const s_headerSize = 144;
  static uint32_t const s_limeMagic = 0x456789ab;
  static const char s_mesBeginMask = 0x80;
  static const char s_mesEndMask = 0x40;

  union uHeader
  {
    uint64_t as64[s_headerSize / sizeof(uint64_t)];
    uint32_t as32[s_headerSize / sizeof(uint32_t)];
    uint16_t as16[s_headerSize / sizeof(uint16_t)];
    char     as8[s_headerSize];
  };

  std::string const &d_filename;
  std::ifstream      d_in;

  std::vector< std::string >    d_types;
  std::vector< int32_t >        d_messages;
  std::vector< uint64_t >       d_sizes;
  std::vector< std::streampos > d_offsets;
  std::vector< int16_t >        d_versions;

  size_t d_currentRecord;
  bool d_fail;
  bool d_messagesCorrect;

public:
  Reader(std::string const &filename);

  template< typename DataType >
  void read(DataType *buffer, size_t elements);

  void retrieveRecord(size_t const record);
  void retrieveMessageAndRecord(size_t const message, size_t const record);

  void nextRecord();
  void previousRecord();

  std::string const &filename() const;
  size_t records() const;
  size_t messages() const;

  size_t currentRecord() const;
  size_t currentMessage() const;
  size_t recordSize() const;

  size_t findRecord(std::string const &type) const;
  std::string const &type() const;
  int16_t const &version() const;

  bool good() const;
  bool fail() const;
  bool messagesCorrect() const;

  std::streampos tellg();
  void seekg(std::streampos const offset, size_t const record);
};
}
}
}
#include "Reader/Reader.inlines"
