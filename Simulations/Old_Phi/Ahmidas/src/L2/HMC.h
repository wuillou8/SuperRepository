#pragma once

#include <L0/Base/Random.h>
#include <L0/GaugeField.h>
#include <L1/Path.h>
#include <L0/SUN.h>

template< typename Element, size_t D >
void Langevin(GaugeField< Element, D > &gf, double kappa, double step, size_t totalSweeps);


template< typename Element, size_t D >
void RandomVector(Eigen::Matrix< Element, D > &vec)

#include "Metropolis/Metropolis.template"
