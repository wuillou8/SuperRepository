#pragma once

#include <cstddef> 
#include <vector>
#include <assert.h>
#include <stdlib.h>
#include <iostream>

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
			std::vector<int> labels, std::vector<int> categs, std::vector<Goods::Goods> storeGoods,
			size_t store_number );
	virtual ~Store();

	// getters/setters
	double getPriceWithLabel( const int& label, const int& categ ) const;
	//const LocTimeGrid::Space& posSpace() const { return this->posSpace(); };
	//void posSpace(std::string const& var) :  posSpace(var) {};
/*
	const size_t& getNstock() const { return Nstock; };
	void setNstock(size_t const& var) :  Nstock(var) {};
	const size_t& getthreshold() const { return thresholds; };
	void setthreshold(size_t const& var) :  thresholds(var) {};
	const std::vector<double>& getprices() const { return prices; };
	void setprices(std::vector<double> const& var) :  prices(var) {};
	const std::vector<size_t>& getstocks() const { return stocks; };
	void setstocks(std::vector<size_t> const& var) : stocks(var) {};
	const std::vector<int>& getlabels() const { return labels; };
	void setlabels(std::vector<int> const& var) : labels(var) {};
	const std::vector<int>& getcategs() const { return categs; };
	void setcategs(std::vector<int> const& var) : categs(var) {};
	const std::vector<Goods::Goods>& getstoreGoods() const { return storeGoods; };
	void setstoreGoods(std::vector<Goods::Goods> const& var) : storeGoods(var) {};
	const size_t& getstore_number() const { return store_number; };
	void setstore_number(size_t const& var) : store_number(var) {};
*/
//private:
	LocTimeGrid::Space posSpace;
	size_t Nstock;
	size_t thresholds;
	std::vector<double> prices;
	std::vector<size_t> stocks; //Nb of Els in stock
	std::vector<int> labels;
	std::vector<int> categs;
	std::vector<Goods::Goods> storeGoods;
	size_t store_number;
	
	friend ostream& operator<<(ostream& os, const Store& store);
};

class Stores {
public:
	Stores( size_t Nstores );
	Stores( size_t Nstores, std::vector<Store> stores );
	virtual ~Stores();

	size_t Nstores;
	std::vector<Store> stores;
	friend ostream& operator<<(ostream& os, const Stores& stores);
	void AddStore( Store store );

};

//create store positions
Store randStore( const Goods::Market& market, size_t& storeNumber );
const Store MakeStore( LocTimeGrid::Space posSpace, size_t Nstock, size_t thresholds, \
					   	   	   std::vector<double> prices, std::vector<size_t> stocks, std::vector<int> labels, \
					   	   	std::vector<int> categs, std::vector<Goods::Goods> storeGoods, size_t store_number );
Stores MakeSupply( size_t Nstores, const Goods::Market& market );
void ShoppingInStore( int& label, Store& store );
//"shopping" functionalities
bool findInStore( int& label, Store& store );
double priceInStore( int& label, int& categ, Store& store );

}
