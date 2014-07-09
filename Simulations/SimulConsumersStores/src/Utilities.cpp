#include "Utilities.h"

namespace Starts {

// Function placing 5 stores in the 4 corners + in the middle.
const Supply::Stores Init5StoresCross( const Goods::Market& market ) {
	std::vector<double> prices (3,1.);
	//store in the center
	size_t nstores(0);
	Supply::Stores stores( 0 );
	Supply::Store rand_store = Supply::randStore( market, nstores );
	rand_store.prices = prices;
	rand_store.posSpace.posX = LocTimeGrid::NgridX/2;
	rand_store.posSpace.posY = LocTimeGrid::NgridY/2;
	cout<<stores;
	stores.AddStore( rand_store );

	rand_store = Supply::randStore( market, ++nstores );
	rand_store.prices = prices;
	rand_store.posSpace.posX = LocTimeGrid::NgridX;
	rand_store.posSpace.posY = 0;
	stores.AddStore( rand_store );
	
	rand_store = Supply::randStore( market, ++nstores );
	rand_store.prices = prices;
	rand_store.posSpace = LocTimeGrid::Space( 0, LocTimeGrid::NgridY );
	rand_store.posSpace.posX = 0;
	rand_store.posSpace.posY = LocTimeGrid::NgridY;
	stores.AddStore( rand_store );

	return stores;
}

const Customers::Customers InitCustomersGrid(const Goods::Market& market, size_t resol ) { //, size_t ngridX = LocTimeGrid::NgridX, size_t ngridY = LocTimeGrid::NgridY) {
	size_t custoNb = 0;
	Customers::Customer custo(LocTimeGrid::Space(0,0), LocTimeGrid::Time(0));
	std::vector<Customers::Customer> custos;
	for (size_t i = 0; i < LocTimeGrid::NgridX/resol+1; ++i){
		for (size_t j = 0; j < LocTimeGrid::NgridY/resol+1; ++j){
			custo = Customers::randCustomer( true, ++custoNb, Customers::NHPars );
			custo.posSpace.posX = i*resol;
			custo.posSpace.posY = j*resol;
			custos.push_back( custo ); 		
		}
	}
	return Customers::Customers( custoNb, custos );
}
		
}

namespace Checks {

//check that all the stores are at the same dist...
void check1( const Supply::Stores& stores ) {
	Supply::Store storeO = stores.stores[0];
	
	for ( size_t i = 1; i < stores.Nstores ; ++i ) {
		cout<<i<<" "<<LocTimeGrid::distance( storeO.posSpace, stores.stores[i].posSpace )<<endl;
	}
}
//check distance with all customers...
void check2( const Supply::Stores& stores, const Customers::Customers& custos ) {
	double tmp = 0.;
	for ( size_t i = 1; i < stores.Nstores ; ++i ) {
		tmp = 0.;
		for ( size_t j = 1; j < custos.Ncustomers ; ++j  ) {
			tmp += LocTimeGrid::distance( custos.customers[j].posSpace , stores.stores[i].posSpace ); 
		}
		cout <<"store "<<stores.stores[i].posSpace.posX<<" "<<stores.stores[i].posSpace.posX<<" "<<i<<" "<<tmp<<endl;
	}
	cout<<"custos.Ncustomers "<<custos.Ncustomers<<endl;
	cout<<"custos.size "<<custos.customers.size()<<endl;

	size_t resol = 20;
	size_t count = 0;
	for ( size_t i = 1; i < stores.Nstores ; ++i ) {
		tmp = 0.;
		for (size_t _i = 0; _i < LocTimeGrid::NgridX/resol+1; ++_i){
			for (size_t _j = 0; _j < LocTimeGrid::NgridY/resol+1; ++_j){
				tmp += LocTimeGrid::distance( stores.stores[i].posSpace, LocTimeGrid::Space( _i*resol, _j*resol ) );
				
	cout<<count<<" "<<custos.customers[count].posSpace.posX<<" "<<custos.customers[count].posSpace.posY<<endl;
	cout<<i<<" "<<_i*resol<<" pos "<<_j*resol<<endl;
	cout << LocTimeGrid::Space( _i*resol, _j*resol ).posX << " "<< LocTimeGrid::Space( _i*resol, _j*resol ).posY << endl;
	cout << custos.customers[count].posSpace.posX << " " << custos.customers[count].posSpace.posY <<endl;
	
				if ( !(LocTimeGrid::Space( _i*resol, _j*resol ) == custos.customers[count].posSpace) ) {
					cout<<" STOP "<<endl; 
					cout<<count<<" "<<custos.customers[count].posSpace.posX<<" "<<custos.customers[count].posSpace.posY<<endl;
					cout<<i<<" "<<_i*resol<<" pos "<<_j*resol<<endl;
					cout<<"stop"<<endl;
					exit (EXIT_FAILURE);
				}
				count++;

			}
		}
		count=0;
		cout <<"2_store "<<stores.stores[i].posSpace.posX<<" "<<stores.stores[i].posSpace.posX<<" "<<i<<" "<<tmp<<endl;
	} 
	
	count = 0;
	for (size_t i = 0; i < LocTimeGrid::NgridX/resol+1; ++i){
				for (size_t j = 0; j < LocTimeGrid::NgridY/resol+1; ++j){
					++count;	
		}		}
	
	cout << "count " << count << endl;

	int cadI(0), cadII(0), cadIII(0), cadIV(0);
	for ( size_t i = 0; i < custos.customers.size() /*Ncustomers*/ ; ++i ) {

		if( (custos.customers[i].posSpace.posX < 500) && (custos.customers[i].posSpace.posY < 500) )
		{	cadI++;	}
		if( (custos.customers[i].posSpace.posX > 500) && (custos.customers[i].posSpace.posY < 500) )
		{	cadII++;	}
		if( (custos.customers[i].posSpace.posX < 500) && (custos.customers[i].posSpace.posY > 500) )
		{	cadIII++;	}
		if( (custos.customers[i].posSpace.posX > 500) && (custos.customers[i].posSpace.posY > 500) )
		{	cadIV++;	}
		
	}
	cout << cadI<<" "<< cadII<<" "<<cadIII<<" "<<cadIV<<endl;
	
}
		
}
