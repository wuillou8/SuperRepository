#pragma once

#include "TTemplate.h"

// And a generic iterator type. Let's make this one a free class, since it's pretty generic.
template< typename Scalar, size_t Dim, size_t Rank, size_t Index1, size_t Index2 = Rank >
class TIter
{
  Scalar const * const d_base;
  size_t d_offset;

public:
  TIter(Scalar const * const base, size_t offset = 0);
  //operator Scalar*() const;

  // This is the replacement for a pointer: the dereferencing doesn't change the value of the pointer itself.
  Scalar &operator*() const;
  Scalar &operator[](size_t index) const;

  TIter< Scalar, Dim, Rank, Index1, Index2 > &operator++();
  TIter< Scalar, Dim, Rank, Index1, Index2 > operator++(int);

  TIter< Scalar, Dim, Rank, Index1, Index2 > &operator--();
  TIter< Scalar, Dim, Rank, Index1, Index2 > operator--(int);

  // We need a full implementation of pointer arithmetic still...
  size_t operator-(TIter< Scalar, Dim, Rank, Index1, Index2 > const &other) const;
  TIter< Scalar, Dim, Rank, Index1, Index2 > operator-(size_t shift) const;
  TIter< Scalar, Dim, Rank, Index1, Index2 > operator+(size_t shift) const;

  TIter< Scalar, Dim, Rank, Index1, Index2 > &operator-=(size_t shift);
  TIter< Scalar, Dim, Rank, Index1, Index2 > &operator+=(size_t shift);

private:
  size_t reindex(size_t index) const;
};

template< typename Scalar, size_t Dim, size_t Rank, size_t Index1, size_t Index2 >
inline TIter< Scalar, Dim, Rank, Index1, Index2 >::TIter(Scalar const * const base, size_t offset)
  : d_base(base), d_offset(offset)
{}

template< typename Scalar, size_t Dim, size_t Rank, size_t Index1, size_t Index2 >
inline TIter< Scalar, Dim, Rank, Index1, Index2 > &TIter< Scalar, Dim, Rank, Index1, Index2 >::operator++()
{
  ++d_offset;
  return *this;
}

template< typename Scalar, size_t Dim, size_t Rank, size_t Index1, size_t Index2 >
inline TIter< Scalar, Dim, Rank, Index1, Index2 > TIter< Scalar, Dim, Rank, Index1, Index2 >::operator++(int)
{
  ++d_offset;
  return TIter< Scalar, Dim, Rank, Index1, Index2 >(d_base, d_offset - 1);
}

template< typename Scalar, size_t Dim, size_t Rank, size_t Index1, size_t Index2 >
inline TIter< Scalar, Dim, Rank, Index1, Index2 > &TIter< Scalar, Dim, Rank, Index1, Index2 >::operator--()
{
  --d_offset;
  return *this;
}

template< typename Scalar, size_t Dim, size_t Rank, size_t Index1, size_t Index2 >
inline TIter< Scalar, Dim, Rank, Index1, Index2 > TIter< Scalar, Dim, Rank, Index1, Index2 >::operator--(int)
{
  --d_offset;
  return TIter(d_base, d_offset + 1);
}

// We want to specialize the function below, for Index == Rank - 1 and Index = 0?!
template< typename Scalar, size_t Dim, size_t Rank, size_t Index1, size_t Index2 >
size_t TIter< Scalar, Dim, Rank, Index1, Index2 >::reindex(size_t index) const
{
  size_t result = (index % Dim) * ((Power< Dim, Index1 >::value + Power< Dim, Index2 >::value) % Power< Dim, Rank >::value);
  index /= Dim;
  size_t stride = 1;
  while (index)
  {
    if (stride == Power< Dim, Index1 >::value || stride == Power< Dim, Index2 >::value)
    {
      stride *= Dim;
      continue;
    }
    result += (index % Dim) * stride;
    index /= Dim;
    stride *= Dim;
  }
  return result;
}

// template< typename Scalar, size_t Dim, size_t Rank, size_t Index1, size_t Index2 >
// TIter< Scalar, Dim, Rank, Index1, Index2 >::operator Scalar*() const
// {
//   // This cast is ugly, but for some reason Eigen seems to be designed like this...
//   return const_cast< Scalar* >(d_base + reindex(d_offset));
// }

template< typename Scalar, size_t Dim, size_t Rank, size_t Index1, size_t Index2 >
Scalar &TIter< Scalar, Dim, Rank, Index1, Index2 >::operator*() const
{
  return const_cast< Scalar& >(d_base[reindex(d_offset)]);
}

template< typename Scalar, size_t Dim, size_t Rank, size_t Index1, size_t Index2 >
Scalar &TIter< Scalar, Dim, Rank, Index1, Index2 >::operator[](size_t index) const
{
//   std::cerr << "From " << index << " comes " << reindex(index) << std::endl;
  return const_cast< Scalar& >(d_base[reindex(d_offset + index)]);
}

template< typename Scalar, size_t Dim, size_t Rank, size_t Index1, size_t Index2 >
inline size_t TIter< Scalar, Dim, Rank, Index1, Index2 >::operator-(TIter< Scalar, Dim, Rank, Index1, Index2 > const &other) const
{
  return (d_offset - other.d_offset); // Only makes sense if the base is the same, but that is never checked with pointers either.
}

template< typename Scalar, size_t Dim, size_t Rank, size_t Index1, size_t Index2 >
inline TIter< Scalar, Dim, Rank, Index1, Index2 > TIter< Scalar, Dim, Rank, Index1, Index2 >::operator-(size_t shift) const
{
  return TIter< Scalar, Dim, Rank, Index1, Index2 >(d_base, d_offset - shift);
}

template< typename Scalar, size_t Dim, size_t Rank, size_t Index1, size_t Index2 >
inline TIter< Scalar, Dim, Rank, Index1, Index2 > TIter< Scalar, Dim, Rank, Index1, Index2 >::operator+(size_t shift) const
{
  return TIter< Scalar, Dim, Rank, Index1, Index2 >(d_base, d_offset + shift);
}

template< typename Scalar, size_t Dim, size_t Rank, size_t Index1, size_t Index2 >
inline TIter< Scalar, Dim, Rank, Index1, Index2 > &TIter< Scalar, Dim, Rank, Index1, Index2 >::operator-=(size_t shift)
{
  d_offset -= shift;
  return *this;
}

template< typename Scalar, size_t Dim, size_t Rank, size_t Index1, size_t Index2 >
inline TIter< Scalar, Dim, Rank, Index1, Index2 > &TIter< Scalar, Dim, Rank, Index1, Index2 >::operator+=(size_t shift)
{
  d_offset += shift;
  return *this;
}
