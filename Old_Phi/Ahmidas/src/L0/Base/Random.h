#pragma once

#include <cstdlib>

namespace Base
{
namespace Random
{
double uniform();
double symmetric();
double fastUniform();
double fastSymmetric();
void setRange(size_t const min, size_t const max);
size_t range();
void setZ2Scale(double const scale);
double Z2();
double Gaussian();
}
}
