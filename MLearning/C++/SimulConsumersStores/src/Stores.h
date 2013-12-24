#pragma once

#include <cstddef> 
#include <vector>

#include "LocTimeGrid.h"
#include "Goods.h"
#include "Random.h"

namespace Supply
{
//number of specialisations or good types

class Store
{
public:
	Store(LocTimeGrid::Space posSpace);
	Store(LocTimeGrid::Space posSpace, size_t thresholds, std::vector<double> prices);
	Store(LocTimeGrid::Space posSpace, size_t Nstock);
	Store(LocTimeGrid::Space posSpace, size_t thresholds, std::vector<double> prices,\
			std::vector<size_t> stocks, std::vector<int> labels, std::vector<Goods::Goods> storeGoods);
	virtual ~Store();
	
	LocTimeGrid::Space posSpace;
	size_t Nstock;
	size_t thresholds;
	std::vector<double> prices;
	std::vector<size_t> stocks; //nb of els in stock
	std::vector<int> labels;
	std::vector<Goods::Goods> storeGoods;
};

class Stores
{
public:
	Stores(size_t NStores);
	Stores(size_t NStores, std::vector<Store> stores);
	virtual ~Stores();
	
	size_t NStores;
	std::vector<Store> stores;
};

// create store positions
const Store randStore(const Goods::Market& market); 
inline bool findinStore(int& label, Store& store);
Stores MakeSupply(const Goods::Market& market, size_t Nstores);

}