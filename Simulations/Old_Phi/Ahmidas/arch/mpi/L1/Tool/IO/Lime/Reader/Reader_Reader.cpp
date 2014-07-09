#include "Reader.ih"

Tool::IO::Lime::Reader::Reader(std::string const &filename)
  : d_filename(filename), d_in(filename.c_str()), d_currentRecord(0),
    d_fail(false), d_messagesCorrect(true)
{
  uHeader header;
  int32_t message = -1;
  bool messageOpened = true;

  while (d_in.good())
  {
    d_in.read(header.as8, s_headerSize);

    if (!Base::bigEndian)
      Base::swapEndian(header.as32[0]);

    if (header.as32[0] != s_limeMagic)
      break; // We're done, apparently.

    if (!Base::bigEndian)
      Base::swapEndian(header.as16[2]);
    d_versions.push_back(header.as16[2]);

    if (!messageOpened)
    {
      if (header.as8[6] & s_mesBeginMask)
      {
        messageOpened = true;
        ++message;
      }
      else
        d_messagesCorrect = false;
    }

    if (messageOpened)
    {
      if (header.as8[6] & s_mesEndMask)
        messageOpened = false;
      else if (header.as8[6] & s_mesBeginMask)
        d_messagesCorrect = false;
    }

    d_messages.push_back(message);

    if (!Base::bigEndian)
      Base::swapEndian(header.as64[1]);
    d_sizes.push_back(header.as64[1]);

    d_types.push_back(std::string(&header.as8[16]));

    d_offsets.push_back(d_in.tellg());
    d_in.seekg(((d_sizes.back() + 7) / 8) * 8 , std::ios::cur);
  }
  if (!d_offsets.empty())
  {
    d_in.clear();
    d_in.seekg(d_offsets.front(), std::ios::beg);
  }
}
