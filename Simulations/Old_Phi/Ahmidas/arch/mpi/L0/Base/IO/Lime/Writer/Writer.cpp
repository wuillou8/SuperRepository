#include "Writer.ih"

size_t const Base::IO::Lime::Writer::s_headerSize;
uint32_t const Base::IO::Lime::Writer::s_limeMagic;
char const Base::IO::Lime::Writer::s_mesBeginMask;
char const Base::IO::Lime::Writer::s_mesEndMask;
char const Base::IO::Lime::Writer::s_padding[8] = {0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00};
