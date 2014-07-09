#pragma once

template< size_t A, size_t P >
class Power
{
public:
  enum { value = A * Power< A, P - 1 >::value };
};

template< size_t A >
class Power< A, 0 >
{
public:
  enum { value = 1 };
};

template< size_t Dim >
class SpinorDim
{
public:
  enum { value = Power< 2, (Dim / 2) >::value };
};
