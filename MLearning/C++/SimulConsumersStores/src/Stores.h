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
	Store( LocTimeGrid::Space posSpace, size_t thresholds,
			std::vector<double> prices );
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
	std::vector<size_t> stocks; //nb of els in stock
	std::vector<int> labels;
	std::vector<Goods::Goods> storeGoods;
	size_t store_number;
	
	void describeMyself(); // not complete yet
	void IOout( ofstream& ostream, size_t time );
	
};

class Stores {
public:
	Stores(size_t Nstores);
	Stores(size_t Nstores, std::vector<Store> stores);
	virtual ~Stores();

	size_t Nstores;
	std::vector<Store> stores;
	void describeMyself();
};

//create store positions
const Store randStore(const Goods::Market& market, size_t& label);
Stores MakeSupply(size_t Nstores, const Goods::Market& market);
void ShoppingInStore(int& label, Store& store);
//"shopping" functionalities
bool findInStore(int& label, Store& store);
double priceInStore(int& label, Store& store);

}
