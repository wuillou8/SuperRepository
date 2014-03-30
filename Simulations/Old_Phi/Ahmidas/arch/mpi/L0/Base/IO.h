#pragma once

#include <string>
#include <L0/Base/IO/Lime/Reader.h>
#include <L0/Base/IO/Lime/Writer.h>

// Below is necessary to prevent circular including when we make IO functions friends of field.
namespace Core
{
template <typename Element, size_t L, size_t T >
class Field;
}

namespace Base
{
namespace IO
{
template <typename Element, size_t L, size_t T >
void loadILDG(Core::Field< Element, L, T > *field, std::string const &filename);

template <typename Element, size_t L, size_t T >
void saveILDG(Core::Field< Element, L, T > *field, std::string const &filename);
}
}
#include "IO/loadILDG.template"
#include "IO/saveILDG.template"
