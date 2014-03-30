#pragma once

#include <L0/GaugeField.h>


template< typename Element, size_t D >
Field< Element, D > step(Field< Element, D > const &first, size_t nu, Base::Direction dir);

template< typename Element, size_t D >
Field< Element, D > plaquette(Field< Element, D > const &first,     // first = 1 link, second = surrounding staple
                              Field< Element, D > const &second, size_t mu, size_t nu);
template< typename Element, size_t D >
Field< Element, D > staple_up(Field< Element, D > const &first,
                              Field< Element, D > const &second, size_t mu, size_t nu);
template< typename Element, size_t D >
Field< Element, D > staple_down(Field< Element, D > const &first,
                                Field< Element, D > const &second, size_t mu, size_t nu);


template< typename Element, size_t D >
Field< Element, D > plaquette(GaugeField< Element, D > const &gf, size_t mu, size_t nu);
template <typename Element, size_t D >
Field< Element, D > staple_up(GaugeField< Element, D > const &gf, size_t mu, size_t nu);
template <typename Element, size_t D >
Field< Element, D > staple_down(GaugeField< Element, D > const &gf, size_t mu, size_t nu);



#include "Path/plaquette.template"
