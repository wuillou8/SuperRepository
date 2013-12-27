#include "World.h"

namespace WORLD
{

World::World(size_t NgridT, size_t NgridX, size_t NgridY, \
					size_t Ngoods, size_t Ncustoms, size_t Nstores, \
							const Goods::Market& market, const Customers::Customers& customs, const Supply::Stores& stores) :
		NgridT(NgridT), NgridX(NgridX), NgridY(NgridY),\
					Ngoods(Ngoods), Ncustoms(Ncustoms), Nstores(Nstores), \
								market(market), customs(customs), stores(stores), t(0)
{}

World::~World()
{}

void World::describeMyself() {
	cout << "call World" << endl;
	cout << "NgridT " << NgridT << endl;
	cout << "NgridX " << NgridX << endl;
	cout << "NgridY " << NgridY << endl;
	cout << "Ngoods " << Ngoods << endl;
	cout << "Ncustoms " << Ncustoms << endl;
	cout << "Nstores " << Nstores << endl;
	cout << "---------------------------------------market-------------------------------------------------" << endl;
	market.describeMyself();
	cout << "---------------------------------------customers-------------------------------------------------" << endl;
	customs.describeMyself();
	cout << "---------------------------------------stores-------------------------------------------------" << endl;
	stores.describeMyself();
}

const World MakeMyWorld( size_t NgridT, size_t NgridX, size_t NgridY,\
										size_t Ngoods, size_t Ncustoms, size_t Nstores ) {
	//define space-time dims
	LocTimeGrid::NgridT = NgridT;
	LocTimeGrid::NgridX = NgridX;
	LocTimeGrid::NgridY = NgridY;

	//define players
	Goods::Market market(Ngoods);
	Customers::Customers customs = Customers::MakeCustomers(Ncustoms, market);
	Supply::Stores stores = Supply::MakeSupply(Nstores, market);

	//make world
	return World( NgridT, NgridX, NgridY, \
								Ngoods, Ncustoms, Nstores, \
													market, customs, stores );
}

World& TimeSweep(World& world) {
	++world.t;
	//Goods::Goods good;
	//Customers::Customer custo;
	size_t Nstore;
	for (size_t i = 0; i < world.Ngoods; ++i) {
		//good = world.market.market[i];
		for (size_t j = 0; j < world.Ncustoms; ++j) {
			//custo = world.customs.customers[j];
			Nstore = Customers::CustomerPickAStore( world.customs.customers[j], world.market.market[i], world.stores.stores);
			//Nstore = CustomerPickAStore( custo, good , world.stores.stores); // const Supply::Stores& stores );
		}
	}

	return world;
}

}

