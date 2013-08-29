#pragma once

#include <stdint.h>

#include <algorithm>
#include <fstream>
#include <string>
#include <vector>

#include <L0/Base/Base.h>
#include <L0/Weave.h>

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

        std::vector< std::string >    d_types; //
        std::vector< int32_t >        d_messages; //
        std::vector< uint64_t >       d_sizes; //Size of the data elements of records
        std::vector< std::streampos > d_offsets; //Offsets of the data elements of records
        std::vector< int16_t >        d_versions; //

        size_t d_currentRecord; //Index of current record
        bool d_fail; //Fail state
        bool d_messagesCorrect; //Begin and end bytes set correct?

        public:
          Reader(std::string const &filename);

          template< typename DataType >
          void read(DataType *buffer, size_t elements); //Reads elements of type Datatype into variable buffer

          void retrieveRecord(size_t const record); //Go to record with index record
          void retrieveMessageAndRecord(size_t const message, size_t const record); //Retrieve message index from record index
          void retrieveRecord(std::string const &type); //Go to record with given type

          void nextRecord(); //Go to next record
          void previousRecord(); //Go to previous record

          std::string const &filename() const; //Report filename of currently open file
          size_t records() const; //List number of records
          size_t messages() const; //Lists number of messages in the current record

          size_t currentRecord() const; //Gives the index of the current record
          size_t currentMessage() const; //Gives the index of the current message
          size_t recordSize() const; //Gives the size in bytes of the current record

          bool existsRecord(std::string const &type) const; // Check for the existence of a particular record
          size_t findRecord(std::string const &type) const; //Find the record index matching a name
          std::string const &type() const; //Lime type of currently opened record
          int16_t const &version() const; //Lime version of currently opened file

          bool good() const; //Is the reader ready to read?
          bool fail() const; //Did something fail?
          bool messagesCorrect() const; //Are begin and end bytes correctly used?

          std::streampos tellg();
          void seekg(std::streampos const offset, size_t const record);
      };
    }
  }

#include "Reader/Reader.inlines"
