#pragma once

#include <iostream>
#include <fstream>
#include <string>
#include <stdlib.h>

#include "LocTimeGrid.h"
#include "Stores.h"
#include "Customer.h"

using namespace std;

namespace Starts {

const Supply::Stores Init5StoresCross( const Goods::Market& market );
const Customers::Customers InitCustomersGrid( const Goods::Market& market, size_t resol); //, size_t ngridX, size_t ngridY );

}

namespace Checks {

void check1( const Supply::Stores& stores );
void check2( const Supply::Stores& stores, const Customers::Customers& custos );

}