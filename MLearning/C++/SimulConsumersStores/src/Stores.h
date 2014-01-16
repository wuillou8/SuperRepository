#pragma once

#include <cstddef> 
#include <vector>
#include <assert.h>
#include <stdlib.h>

#include "LocTimeGrid.h"
#include "Goods.h"
#include "Random.h"

namespace Supply {
//number of specialisations or good types

class Store {
public:
	Store( LocTimeGrid::Space posSpace );
	Store( LocTimeGrid::Space posSpace, size_t thresholds, std::vector<double> prices );
	Store( LocTimeGrid::Space posSpace, size_t Nstock );
	Store( LocTimeGrid::Space posSpace, size_t Nstock, size_t thresholds,
			std::vector<double> prices, std::vector<size_t> stocks,
			std::vector<int> labels, std::vector<Goods::Goods> storeGoods,
			size_t store_number );
	virtual ~Store();

	LocTimeGrid::Space posSpace;
	size_t Nstock;
	size_t thresholds;
	std::vector<double> prices;
	std::vector<size_t> stocks; //Nb of Els in stock
	std::vector<int> labels;
	std::vector<Goods::Goods> storeGoods;
	size_t store_number;
	
	void describeMyself(); // not complete yet
	void IOout( ofstream& ostream );
	const double getPriceWithLabel( int label ) const;
	
};

class Stores {
public:
	Stores( size_t Nstores );
	Stores( size_t Nstores, std::vector<Store> stores );
	virtual ~Stores();

	size_t Nstores;
	std::vector<Store> stores;
	void describeMyself();
	void AddStore( Store& store );
};

//create store positions
const Store randStore( const Goods::Market& market, size_t& storeNumber );
const Store MakeStore( LocTimeGrid::Space posSpace, size_t Nstock, size_t thresholds, \
					   	   	   std::vector<double> prices, std::vector<size_t> stocks, std::vector<int> labels, \
							   	   	   std::vector<Goods::Goods> storeGoods, size_t store_number );
Stores MakeSupply( size_t Nstores, const Goods::Market& market );
void ShoppingInStore( int& label, Store& store );
//"shopping" functionalities
bool findInStore( int& label, Store& store );
double priceInStore( int& label, Store& store );

}