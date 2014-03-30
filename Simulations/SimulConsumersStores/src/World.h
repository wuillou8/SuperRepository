#pragma once

#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>
#include <stdlib.h>

#include "LocTimeGrid.h"
#include "Random.h"
#include "Goods.h"
#include "Stores.h"
#include "Customer.h"
#include "IO.h"
#include "Utilities.h"

using namespace std;

namespace WORLD {

class World {
public:
	World(size_t NgridT, size_t NgridX, size_t NgridY, size_t Ngoods, size_t Ncategs, size_t Ncustoms, size_t Nstores, \
				Goods::Market& market, Customers::Customers& customs, Supply::Stores& stores);
	World( const World& other );
	virtual ~World();

	//SpaceTime grid
	size_t NgridT;
	size_t NgridX;
	size_t NgridY;
	//Players
	size_t Ngoods;
	size_t Ncategs;
	size_t Ncustoms;
	size_t Nstores;
	Goods::Market market;
	Customers::Customers customs;
	Supply::Stores stores;
	size_t t;
	friend ostream& operator<<(ostream& os, const World& world);
	void printIO( ostream& ostream );
	void readIO2( ifstream istream );
	void readIO( ifstream& istream );
};

const World MakeMyWorld (size_t NgridT, size_t NgridX, size_t NgridY, size_t Ngoods, size_t Ncategs, size_t Ncustoms, size_t Nstores);
const World MakeMyDBase ( World& world );
void InitTest ( World& world, double price );
void RunWorldStory ( World& world, ofstream& DBcustomers, ofstream& DBstores );
void checks ( const World& world );
World& TimeSweep (World& world, ofstream& DBcustomers, ofstream& DBstores);

}
