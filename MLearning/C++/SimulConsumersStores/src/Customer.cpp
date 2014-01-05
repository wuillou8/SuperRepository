#include "Customer.h"
#include "Stores.h"

namespace Customers {

Customer::Customer(LocTimeGrid::Space loc, LocTimeGrid::Time time) :
		posSpace(loc), posTime(time), alpha(), beta(), cons_threshold(), customer_number()
{}

Customer::Customer(LocTimeGrid::Space loc, LocTimeGrid::Time time, double alpha) :
		posSpace(loc), posTime(time), alpha(alpha), beta(), cons_threshold(), customer_number()
{}

Customer::Customer(LocTimeGrid::Space loc, LocTimeGrid::Time time, double alpha, double beta, double cons_threshold) :
		posSpace(loc), posTime(time), alpha(alpha), beta(1.), cons_threshold(cons_threshold), customer_number()
{}

Customer::Customer(LocTimeGrid::Space loc, LocTimeGrid::Time time, double alpha, double beta, double cons_threshold, size_t customer_number) :
		posSpace(loc), posTime(time), alpha(alpha), beta(1.), cons_threshold(cons_threshold), customer_number(customer_number)
{}

Customer::~Customer()
{}

void Customer::describeMyself() {
	cout << "class Customer" << endl;
	posSpace.describeMyself();
	posTime.describeMyself();
	cout << "alpha " << alpha << endl;
	cout << "beta " << beta << endl;
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
	//if(!timedOrNot) {
	//	LocTimeGrid::Time time = LocTimeGrid::randTime(0);
	//}
	LocTimeGrid::Time time(0);
	double alpha = QuickRandom::box_mueller( 1., 0.2 );
	double beta = QuickRandom::box_mueller( 1., 0.2 );
	double const_threshold = QuickRandom::randf(1.);

	return Customer(pos, time, alpha, beta, const_threshold, custo_number);
}

Customers MakeCustomers(size_t Ncustos, const Goods::Market& market) {
	std::vector<Customer> custos;
	for (size_t i = 0; i < Ncustos; ++i) {
	custos.push_back( randCustomer(  true, i /*, Npars*/ ) );
	}
	return Customers(Ncustos, custos);
}

inline double logitFct( double x, double factor = 1. ) {
	return exp( factor*x )/( 1. + exp( factor*x ) );
}

inline double distanceFct(double x) {
	return x;
}

inline double weightNorm( const std::vector<double>& storeweights ) {
	double wNorm = 0.;
	for ( size_t i = 0 ; i < storeweights.size(); ++i ) {
		wNorm += storeweights[i];
	}
	return wNorm;
}	

inline double utilityFct( const Customer& custo, const Goods::Goods& good, const Supply::Store& store ) {
	/*
	 *	U = alpha*dist - beta*price + epsilon
	 */
	double dist = LocTimeGrid::distance( store.posSpace, custo.posSpace );

	double epsilon = QuickRandom::box_mueller( 0., 1. );
	double pInStore = store.getPriceWithLabel( good.label );
	return	custo.alpha * ( 4. - 8. * dist/LocTimeGrid::distNN )  - custo.beta * good.price * pInStore * good.categ + epsilon;
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
	std::vector<Supply::Store> storesfound = findGoodInStore( good, stores );
	std::vector<double> storeweights;
	for ( size_t i = 0 ; i < storesfound.size(); ++i ) {
		storeweights.push_back( logitFct( utilityFct( custo, good, storesfound[i] ) ) ); 
		if ( storeweights[i] != storeweights[i] ) {
			cout <<"in Customers::CustomerPickAStore: "<< storeweights[i]<<endl;
			exit (EXIT_FAILURE);
		}
	}
	return decision( storeweights );
}

inline size_t decision( const std::vector<double>& storeweights ) {
	double proba = 0.;
	double wNorm = weightNorm( storeweights );
	double choice = QuickRandom::randf(1.);
	for ( size_t i = 0 ; i < storeweights.size(); ++i ) {
			proba += storeweights[i]/wNorm;
			if( choice < proba )
			{	return i;	}
	}
	cout << " ERROR from Costumers::decision : probability not correclty handed" << endl;
	exit (EXIT_FAILURE);
}

}

