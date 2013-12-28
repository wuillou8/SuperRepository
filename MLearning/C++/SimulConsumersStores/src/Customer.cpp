#include "Customer.h"
#include "Stores.h"

namespace Customers {

Customer::Customer(LocTimeGrid::Space loc, LocTimeGrid::Time time, std::vector<double> utilparams) :
		posSpace(loc), posTime(time), utilparams(utilparams), priceresist(), cons_threshold()
{}

Customer::Customer(LocTimeGrid::Space loc, LocTimeGrid::Time time, std::vector<double> utilparams, double priceresist, double cons_threshold) :
		posSpace(loc), posTime(time), utilparams(utilparams), priceresist(priceresist), cons_threshold(cons_threshold)
{}

Customer::Customer(LocTimeGrid::Space loc, LocTimeGrid::Time time, std::vector<double> utilparams, double priceresist, double cons_threshold, size_t customer_number) :
		posSpace(loc), posTime(time), utilparams(utilparams), priceresist(priceresist), cons_threshold(cons_threshold), customer_number(customer_number)
{}

Customer::~Customer()
{}

void Customer::describeMyself() {
	cout << "class Customer" << endl;
	posSpace.describeMyself();
	posTime.describeMyself();
	for (size_t i = 0; i < utilparams.size(); ++i) {
		cout << "utilparams " << i << " " << utilparams[i] << endl;
	}
	cout << "priceresist " << priceresist << endl;
	cout << "cons_threshold " << cons_threshold << endl;
	cout << "customer_number " << customer_number << endl;
}

void Customer::IOout( ofstream& ostream ) {
	ostream << customer_number <<", ";
	posSpace.IOout( ostream );
}

Customers::Customers(size_t Ncustomers, std::vector<Customer> customers) :
	Ncustomers(Ncustomers), customers(customers)
{}

Customers::~Customers()
{}

void Customers::describeMyself() {
	cout << "class Customers" << endl;
	cout << "Ncustomers " << Ncustomers << endl;
	for (size_t i = 0; i < customers.size(); ++i) {
		cout << "customers " << i;
		customers[i].describeMyself();
	}
}

/*
 *	 		namespace Customers Functions
 */

Customer randCustomer(  bool timedOrNot, size_t custo_number, size_t NHparms = NHPars ) {
	LocTimeGrid::Space pos = LocTimeGrid::randSpace(0,0);
	if(!timedOrNot) {
		LocTimeGrid::Time time = LocTimeGrid::randTime(0);
	}
	LocTimeGrid::Time time(0);
	Random<double> utilparams(NHparms,1.);
	double priceresist = QuickRandom::randf(1.);
	double consthreshold = QuickRandom::randf(1.);

	return Customer(pos, time, utilparams.random, priceresist, consthreshold, custo_number);
}

Customers MakeCustomers(size_t Ncustos, const Goods::Market& market) {
	std::vector<Customer> custos;
	for (size_t i = 0; i < Ncustos; ++i) {
	custos.push_back( randCustomer(  true, i /*, Npars*/ ) );
	}
	return Customers(Ncustos, custos);
}

inline double logit( double x ) {
	return exp(-x)/(1.+exp(-x));
}

inline double distanceFct(double x) {
	return x;
}

inline double utilityFct( const Customer& custo, const Goods::Goods& good, const Supply::Store& store ) {
	double utilFct = -custo.priceresist*good.price;
	const double dist = LocTimeGrid::distance( store.posSpace, custo.posSpace );
	for ( size_t i = 0; i < NHPars; ++i ) {
		utilFct += distanceFct( custo.utilparams[i]*dist );
	}
	return utilFct;
}

std::vector<Supply::Store> findGoodInStore( const Goods::Goods& good, const Supply::Stores& stores ) {
	std::vector<Supply::Store> foundInStores;
	LocTimeGrid::Space space( 0, 0 );
	Supply::Store store( space );
	int label = good.label;
	double found;
	for (size_t i = 0; i < stores.Nstores; ++i) {
		store = stores.stores[i];
		found = Supply::findInStore( label, store );
		if( found ) {
			foundInStores.push_back( stores.stores[i] );
		}
	}
	return foundInStores;
}

size_t CustomerPickAStore( const Customer& custo, const Goods::Goods& good, const Supply::Stores& stores ) {
	std::vector<Supply::Store> found = findGoodInStore( good, stores );
	double util = 0., tmp;
	Random<double> randnoise( found.size(), 0.5 ); //approx iid values
	size_t whichOne = 0;
	for (size_t i = 0 ; i < found.size(); ++i ) {
		tmp = utilityFct( custo, good, found[i] ) + randnoise.random[i];
		if ( tmp > util ) {
			util = tmp;
			whichOne = i;
		}
	}
	return whichOne;
}

}

