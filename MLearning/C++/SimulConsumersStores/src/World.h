#pragma once

#include <iostream>
#include <cstddef>
#include <stdlib.h>

#include "LocTimeGrid.h"
#include "Random.h"
#include "Goods.h"
#include "Stores.h"
#include "Customer.h"
#include "Utilities.h"

using namespace std;

namespace WORLD {

class World {
public:
	World(size_t NgridT, size_t NgridX, size_t NgridY, size_t Ngoods, size_t Ncustoms, size_t Nstores, \
				Goods::Market& market, Customers::Customers& customs, Supply::Stores& stores);
	World( const World& other );
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
	/*ofstream& DBcustomers;
	ofstream& DBstores;*/
	size_t t;
	void describeMyself();
};

const World MakeMyWorld(size_t NgridT, size_t NgridX, size_t NgridY, size_t Ngoods, size_t Ncustoms, size_t Nstores); //, ofstream& DBcustomers, ofstream& DBstores);
const World MakeMyDBase( World& world ); //, ofstream& DBcustomers, ofstream& DBstores );
void RunWorldStory( World& world, ofstream& DBcustomers, ofstream& DBstores );
World& TimeSweep(World& world, ofstream& DBcustomers, ofstream& DBstores);
}
