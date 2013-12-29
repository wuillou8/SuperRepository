#pragma once 

#include <vector>
#include <cstddef>
#include <fstream>

#include "LocTimeGrid.h"
#include "Random.h"
#include "Goods.h"
#include "Stores.h"

namespace Customers {
//number hidden parameters characterising a customer Util. function
const size_t NHPars = 1;

class Customer {
public:
	Customer(LocTimeGrid::Space loc, LocTimeGrid::Time time, double utilparam);
	Customer(LocTimeGrid::Space loc, LocTimeGrid::Time time, double utilparam, double priceresist,  double cons_threshold);
	Customer(LocTimeGrid::Space loc, LocTimeGrid::Time time, double utilparam, double priceresist,  double cons_threshold, size_t customer_number);
	virtual ~Customer();

	LocTimeGrid::Space posSpace;
	LocTimeGrid::Time posTime;
	double utilparam;//std::vector<double>
	double priceresist;
	double cons_threshold;
	size_t customer_number;
	void describeMyself();
	void IOout( ofstream& ostream );
};

class Customers {
public:
	Customers(size_t Ncustomers, std::vector<Customer> customers);
	virtual ~Customers();

	size_t Ncustomers;
	std::vector<Customer> customers;
	void describeMyself();
};

/*template <LocTimeGrid::Space locSpace,int Nb>
 class CustomerClusters
 {};*/

Customer randCustomer(bool timedOrNot, size_t custo_number, size_t NHparms);
Customers MakeCustomers(size_t Ncustos, const Goods::Market& market);

inline double logitFct( double x, double factor );
inline double distanceFct( double x );
inline double utilityFct( const Customer& custo, const Goods::Goods& good, const Supply::Store& store );

std::vector<Supply::Store> findGoodInStore( int& label, const Supply::Stores& stores );
//bool GoShopping?(const Customrer& custo);
size_t CustomerPickAStore( const Customer& custo, const Goods::Goods& good, const Supply::Stores& stores );
inline size_t decision( const std::vector<double>& storeweights );
inline double weightNorm( const std::vector<double>& storeweights );

}
