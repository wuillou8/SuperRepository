#pragma once

#include <L0/Base/Random.h>
#include <L0/GaugeField.h>
#include <L1/Path.h>

template< typename Element, size_t D >
void Metropolis(GaugeField< Element, D > &gf, double kappa, double step, size_t totalSweeps);


#include "Metropolis/Metropolis.template"
