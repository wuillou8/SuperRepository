#include "World.h"

namespace WORLD
{

World::World( size_t NgridT, size_t NgridX, size_t NgridY, size_t Ngoods, size_t Ncustoms, size_t Nstores, \
							Goods::Market& market, Customers::Customers& customs, Supply::Stores& stores ) :
		NgridT(NgridT), NgridX(NgridX), NgridY(NgridY),\
					Ngoods(Ngoods), Ncustoms(Ncustoms), Nstores(Nstores), \
								market(market), customs(customs), stores(stores), t(0)
{}

World::World( const World& other ) :
	NgridT(other.NgridT), NgridX(other.NgridX), NgridY(other.NgridY), \
	Ngoods(other.Ngoods), Ncustoms(other.Ncustoms), Nstores(other.Nstores), \
	market(other.market), customs(other.customs), stores(other.stores), t(other.t)
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
								size_t Ngoods, size_t Ncustoms, size_t Nstores ) {
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
								market, customs, stores );
}

/*const World MakeMyDBase( World& world, ofstream& DBcustomers, ofstream& DBstores ) {
	world.DBcustomers = DBcustomers;
	world.DBstores = DBstores;
	return world;
}*/

void RunWorldStory( World& world, ofstream& DBcustomers, ofstream& DBstores) {
	//make headers
	IO::printheaderDBCustomers( DBcustomers );
	IO::printheaderDBCustomers( DBstores );
	//run
	for (size_t i = 0; i < LocTimeGrid::NgridT; ++i){
		world = TimeSweep( world, DBcustomers, DBstores );
		cout << "world pulse " << world.t << endl;
	}
	cout << "end: world pulse " << world.t << endl;
}

World& TimeSweep(World& world, ofstream& DBcustomers, ofstream& DBstores) {
	++world.t;
	size_t Nstore;
	double dist;
	for (size_t j = 0; j < world.Ncustoms; ++j) {
		for (size_t i = 0; i < world.Ngoods; ++i) {
			Nstore = Customers::CustomerPickAStore( world.customs.customers[j], world.market.market[i], world.stores );
			dist = LocTimeGrid::distance( world.customs.customers[j].posSpace, world.stores.stores[Nstore].posSpace );

			//customers DBase
			DBcustomers<<world.t<<", ";
			world.market.market[i].IOout( DBcustomers );
			world.customs.customers[j].IOout( DBcustomers );
			world.stores.stores[Nstore].posSpace.IOout( DBcustomers );
			DBcustomers<<dist<<endl;
			//stores DBase
			DBstores<<world.t<<", ";
			world.stores.stores[Nstore].IOout(DBstores);
			DBstores<<endl;
		}
	}
	return world;
}

}

