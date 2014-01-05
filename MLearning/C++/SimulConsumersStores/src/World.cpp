#include "World.h"

namespace WORLD
{

World::World( size_t NgridT, size_t NgridX, size_t NgridY, size_t Ngoods, size_t Ncategs, size_t Ncustoms, size_t Nstores, \
							Goods::Market& market, Customers::Customers& customs, Supply::Stores& stores ) :
		NgridT(NgridT), NgridX(NgridX), NgridY(NgridY),\
					Ngoods(Ngoods), Ncategs(Ncategs), Ncustoms(Ncustoms), Nstores(Nstores), \
								market(market), customs(customs), stores(stores), t(0)
{}

World::World( const World& other ) :
	NgridT(other.NgridT), NgridX(other.NgridX), NgridY(other.NgridY), \
	Ngoods(other.Ngoods), Ncategs(other.Ncategs), Ncustoms(other.Ncustoms), Nstores(other.Nstores), \
	market(other.market), customs(other.customs), stores(other.stores), t(other.t)
{}

void World::printIO( ostream& ostream ) {
	ostream << "class World" << endl;
	ostream << "NgridT," << NgridT << endl;
	ostream << "NgridX," << NgridX << endl;
	ostream << "NgridY," << NgridY << endl;
	ostream << "Ngoods," << Ngoods << endl;
	ostream << "Ncustoms," << Ncustoms << endl;
	ostream << "Nstores," << Nstores << endl;
	//market.printIO();
	//customs.printIO();
	//stores.printIO();
}

void readIO2( ifstream istream ) {
	string buff;
	istream >> buff;
	cout << "test1 " << buff <<endl;
	istream >> buff;
	cout << "test2 " << buff <<endl;
}

void World::readIO( ifstream& istream ) {
	cout << "read-world" << endl;
	string tmp;
	getline(istream,tmp,'\n');
	getline(istream,tmp,',');
	getline(istream,tmp,'\n');
	NgridT=atoi(tmp.c_str());
	getline(istream,tmp,','); getline(istream,tmp,'\n');
	NgridX=atoi(tmp.c_str());
	getline(istream,tmp,','); getline(istream,tmp,'\n');
	NgridY=atoi(tmp.c_str());
	getline(istream,tmp,','); getline(istream,tmp,'\n');
	Ngoods=atoi(tmp.c_str());
	getline(istream,tmp,','); getline(istream,tmp,'\n');
	Ncustoms=atoi(tmp.c_str());
	getline(istream,tmp,','); getline(istream,tmp,'\n');
	Nstores=atoi(tmp.c_str());
}


World::~World()
{}

void World::describeMyself() {
	cout << "call World" << endl;
	cout << "NgridX " << NgridX << endl;
	cout << "NgridY " << NgridY << endl;
	cout << "NgridT " << NgridT << endl;
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
								size_t Ngoods, size_t Ncategs, size_t Ncustoms, size_t Nstores ) {
	//define space-time dims
	/*LocTimeGrid::Dims::NgridT = NgridT;
	LocTimeGrid::Dims::NgridX = NgridX;
	LocTimeGrid::Dims::NgridY = NgridY;*/
	QuickRandom::INITQuickRandom();

	//define players
	Goods::Market market( Ngoods, Ncategs );
	//market.describeMyself();
	//exit (EXIT_FAILURE);
	//Normal config.
	/*
	Customers::Customers customs = Customers::MakeCustomers(Ncustoms, market);
	Supply::Stores stores = Supply::MakeSupply(Nstores, market);
	//place store in the grid center
	Supply::Store rand_store = Supply::randStore( market, ++Nstores );
	rand_store.posSpace.posX = 500;
	rand_store.posSpace.posY = 500;
	stores.AddStore( rand_store );
	*/

	Customers::Customers customs = Starts::InitCustomersGrid( market, 20 ); //20, LocTimeGrid::NgridX, LocTimeGrid::NgridY)
	Supply::Stores stores = Starts::Init5StoresCross(market);

	//create world
	return World( NgridT, NgridX, NgridY, \
						Ngoods, Ncategs, customs.Ncustomers, stores.Nstores, \
								market, customs, stores );
}

/*const World MakeMyDBase( World& world, ofstream& DBcustomers, ofstream& DBstores ) {
	world.DBcustomers = DBcustomers;
	world.DBstores = DBstores;
	return world;
}*/

void InitTest( World& world, double price ) {
	Supply::Stores stores = world.stores;
	world.stores.stores[0].prices[0] = price;
}

void RunWorldStory( World& world, ofstream& DBcustomers, ofstream& DBstores) {
	//make headers
	IO::printheaderDBCustomers( DBcustomers );
	IO::printheaderDBstores( DBstores );
	//run
	world.stores.stores[0].prices[0] = 1.;
	for (size_t i = 0; i < world.NgridT/*LocTimeGrid::NgridT*/; ++i){
		world = TimeSweep( world, DBcustomers, DBstores );
		cout << "world pulse " << world.t << endl;
	}
	exit (EXIT_FAILURE);
}	
	
void checks ( const World& world ) {
	/*Checks::check1( world.stores );
	Checks::check2( world.stores, world.customs );*/

}

World& TimeSweep(World& world, ofstream& DBcustomers, ofstream& DBstores) {
	++world.t;
	size_t Nstore;
	double dist;
	world.stores.stores[0].prices[0] = 10.;
	for (size_t j = 0; j < world.Ncustoms; ++j) {

		for (size_t i = 0; i < world.Ngoods*world.Ncategs; ++i) {
			Nstore = Customers::CustomerPickAStore( world.customs.customers[j], world.market.market[i], world.stores );
			dist = LocTimeGrid::distance( world.customs.customers[j].posSpace, world.stores.stores[Nstore].posSpace );

			//customers DBase
			DBcustomers<<world.t<<", ";
			world.market.market[i].IOout( DBcustomers );
			world.customs.customers[j].IOout( DBcustomers );
			DBcustomers<<Nstore<<", ";
			world.stores.stores[Nstore].posSpace.IOout( DBcustomers );
			DBcustomers<<dist<<endl;

			//stores DBase
			DBstores<<world.t<<", ";
			world.stores.stores[Nstore].IOout(DBstores);
			DBstores<<0<<endl;
		}
	}
	return world;
}

}

