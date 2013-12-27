#include <assert.h>
#include <stdlib.h>

#include "Stores.h"

using namespace std;

namespace Supply
{

Store::Store(LocTimeGrid::Space posSpace):
	posSpace(posSpace), Nstock(), thresholds(), prices(),\
			stocks(), labels(), storeGoods(), storelabel()
{}

Store::Store(LocTimeGrid::Space posSpace, size_t Nstock):
	posSpace(posSpace), Nstock(Nstock), thresholds(), prices(),\
			stocks(), labels(), storeGoods(), storelabel()
{}

Store::Store(LocTimeGrid::Space posSpace, size_t thresholds, std::vector<double> prices):
	posSpace(posSpace), Nstock(), thresholds(thresholds), prices(prices),\
			stocks(), labels(), storeGoods(), storelabel()
{}

Store::Store(LocTimeGrid::Space posSpace, size_t Nstock, size_t thresholds, std::vector<double> prices,\
				std::vector<size_t> stocks, std::vector<int> labels, std::vector<Goods::Goods> storeGoods, size_t storelabel):
			posSpace(posSpace), Nstock(Nstock), thresholds(thresholds), prices(prices),\
						stocks(stocks), labels(labels), storeGoods(storeGoods), storelabel(storelabel)
{}

Store::~Store()
{}

void Store::describeMyself() {
	cout << "class Store" << endl;
	posSpace.describeMyself();
	cout << "Nstock " << Nstock << endl;
	cout << "thresholds " << thresholds << endl;
	cout << "storelabel " << storelabel << endl;
	for (size_t i = 0; i < prices.size(); ++i) {
		cout << "prices " << i << " " << prices[i] << endl;
		cout << "stocks " << i << " " << stocks[i] << endl;
		cout << "labels " << i << " " << labels[i] << endl;
	}
	//cout << "DBG " << storeGoods.size() << endl;
	for (size_t i = 0; i < storeGoods.size(); ++i) {
		cout << "storeGoods " << i << endl;
		storeGoods[i].describeMyself();
	}
}

Stores::Stores(size_t Nstores):
	Nstores(Nstores)
{}

Stores::Stores(size_t Nstores, std::vector<Store> stores) :
	Nstores(Nstores), stores(stores)
{}

Stores::~Stores()
{}

void Stores::describeMyself() {
	cout << "class Stores" << endl;
	cout << "Nstores" << Nstores << endl;
	for (size_t i = 0; i < stores.size(); ++i) {
		cout << "Stores " << i << endl;
		stores[i].describeMyself();
	}
}

const Store randStore(const Goods::Market& market, size_t& label) {
	//threshold fixed
	//stockInit fixed
	size_t Ngoods = market.Ngoods;
	size_t shopSize = QuickRandom::randi(Ngoods);			//ngoods <= Ngoods
	shopSize = 1;  /* to be changged later ... current simulation only */
	LocTimeGrid::Space pos = LocTimeGrid::randSpace(0,0); 	//location
	size_t threshold = 4; 	//Random<int> threshold(4);		//threshold
	Random<double> pricesVar(Ngoods,1.);					//prices changes
	std::vector<double> deltaprices;
	size_t stockNb = 20;									//init stocks
	std::vector<size_t> stocks(shopSize,stockNb);			//stocks
	std::vector<Goods::Goods> storeGoods = \
						Goods::GetStore(market, shopSize);
	std::vector<int> labels;
	
	for (size_t i = 0 ; i < storeGoods.size(); ++i)	{
		deltaprices.push_back( pricesVar.random[i] - 0.5 );
		labels.push_back( storeGoods[i].label );
	}
	return Store( pos, shopSize, threshold, deltaprices, stocks, labels, storeGoods, label);
}

Stores MakeSupply(size_t Nstores, const Goods::Market& market) {
	std::vector<Store> stores;
	for (size_t i = 0; i < Nstores; ++i) {
		stores.push_back( randStore(market, i) );
	}
	return Stores(Nstores, stores);
}

void ShoppingInStore(int& label, Store& store) {
	for (size_t i = 0 ; i < store.Nstock; ++i) {
			if ( label  == store.storeGoods[i].label ) {
				if(--(store.stocks[i]) == store.thresholds) {
					store.stocks[i] = store.thresholds + 10;
				}
			}
	}
}

bool findInStore(int& label, Store& store) {
	for (size_t i = 0 ; i < store.Nstock; ++i) {
		if ( label  == store.storeGoods[i].label ) {
			return true;
			break;
		}
	}
	return false;
}	

double priceInStore(int& label, Store& store) {
	for (size_t i = 0 ; i < store.Nstock; ++i) {
		if ( label  == store.storeGoods[i].label ) {
			return store.storeGoods[i].price;
			break;
		}
	}
	cout << " ERROR from Supply::priceInStore : goods with label expected" << endl;
	exit (EXIT_FAILURE);
}

}
