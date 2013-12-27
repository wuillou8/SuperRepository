#include "World.h"

namespace WORLD
{

World::World( size_t NgridT, size_t NgridX, size_t NgridY, size_t Ngoods, size_t Ncustoms, size_t Nstores, \
							Goods::Market& market, Customers::Customers& customs, Supply::Stores& stores, \
									ofstream& DBcustomers, ofstream& DBstores) :
		NgridT(NgridT), NgridX(NgridX), NgridY(NgridY),\
					Ngoods(Ngoods), Ncustoms(Ncustoms), Nstores(Nstores), \
								market(market), customs(customs), stores(stores), t(0), \
										DBcustomers(DBcustomers), DBstores(DBstores)
{}

World::World( const World& other ) :
	NgridT(other.NgridT), NgridX(other.NgridX), NgridY(other.NgridY), \
	Ngoods(other.Ngoods), Ncustoms(other.Ncustoms), Nstores(other.Nstores), \
	market(other.market), customs(other.customs), stores(other.stores), DBcustomers(other.DBcustomers), DBstores(other.DBstores)
{}

/*World::World( const World& world, const ofstream& DBcustomers, const ofstream& DBstores ) :
	DBcustomers(DBcustomers), DBstores(DBstores)
{World::World(world);}*/

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

const World MakeMyWorld( size_t NgridT, size_t NgridX, size_t NgridY, \
								size_t Ngoods, size_t Ncustoms, size_t Nstores, \
										ofstream& DBcustomers, ofstream& DBstores) {
	//define space-time dims
	/*LocTimeGrid::Dims::NgridT = NgridT;
	LocTimeGrid::Dims::NgridX = NgridX;
	LocTimeGrid::Dims::NgridY = NgridY;*/

	//define players
	Goods::Market market(Ngoods);
	Customers::Customers customs = Customers::MakeCustomers(Ncustoms, market);
	Supply::Stores stores = Supply::MakeSupply(Nstores, market);

	//make world
	return World( NgridT, NgridX, NgridY, \
						Ngoods, Ncustoms, Nstores, \
								market, customs, stores, \
										DBcustomers, DBstores);
}

/*const World MakeMyDBase( World& world, ofstream& DBcustomers, ofstream& DBstores ) {
	world.DBcustomers = DBcustomers;
	world.DBstores = DBstores;
	return world;
}*/

void RunWorldStory( World& world ) {
	for (size_t i = 0; i < LocTimeGrid::NgridT; ++i){
		world = TimeSweep( world );
	}
	cout << "end: world pulse " << world.t << endl;
}

World& TimeSweep(World& world) {
	++world.t;
	size_t Nstore;
	double dist;
	for (size_t j = 0; j < world.Ncustoms; ++j) {
		for (size_t i = 0; i < world.Ngoods; ++i) {
			Nstore = Customers::CustomerPickAStore( world.customs.customers[j], world.market.market[i], world.stores );
			cout  << " customer " << j << " goods " << i << " store " << Nstore << endl;
			
			dist = LocTimeGrid::distance( world.customs.customers[j].posSpace, world.stores.stores[Nstore].posSpace );
			cout << "dist: " << dist << endl;
		}
	}
	return world;
}

}

