#include "World.h"

namespace WORLD
{

World::World(size_t NgridT, size_t NgridX, size_t NgridY, \
					size_t Ngoods, size_t Ncustoms, size_t Nstores, \
							const Goods::Market& market, const Customers::Customers& customs, const Supply::Stores& stores) :
		NgridT(NgridT), NgridX(NgridX), NgridY(NgridY),\
					Ngoods(Ngoods), Ncustoms(Ncustoms), Nstores(Nstores), \
								market(market), customs(customs), stores(stores)
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
	cout << "----------------------------------------------------------------------------------------" << endl;
	market.describeMyself();
	cout << "----------------------------------------------------------------------------------------" << endl;
	customs.describeMyself();
	cout << "----------------------------------------------------------------------------------------" << endl;
	stores.describeMyself();
}

const World MakeMyWorld(size_t NgridT, size_t NgridX, size_t NgridY,\
										size_t Ngoods, size_t Ncustoms, size_t Nstores) {
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



}

