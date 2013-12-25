#pragma once

#include <cstddef>

#include "LocTimeGrid.h"
#include "Random.h"
#include "Goods.h"
#include "Stores.h"
#include "Customer.h"

namespace WORLD {

class World {
public:
	World(size_t NgridT, size_t NgridX, size_t NgridY, size_t Ngoods, size_t Ncustoms, size_t Nstores, \
				const Goods::Market& market, const Customers::Customers& customs, const Supply::Stores& stores);
	virtual ~World();

	//SpaceTime grid
	size_t NgridT;
	size_t NgridX;
	size_t NgridY;
	//Players
	size_t Ngoods;
	size_t Ncustoms;
	size_t Nstores;
	Goods::Market market;
	Customers::Customers customs;
	Supply::Stores stores;
	void describeMyself();

};
const World MakeMyWorld(size_t NgridT, size_t NgridX, size_t NgridY, size_t Ngoods, size_t Ncustoms, size_t Nstores);

}
