#include "Writer.ih"

size_t const IO::Lime::Writer::s_headerSize;
uint32_t const IO::Lime::Writer::s_limeMagic;
char const IO::Lime::Writer::s_mesBeginMask;
char const IO::Lime::Writer::s_mesEndMask;
char const IO::Lime::Writer::s_padding[8] = {0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00};
