#include <assert.h>
#include "Stores.h"

using namespace std;

namespace Supply
{

Store::Store(LocTimeGrid::Space posSpace):
	posSpace(posSpace)
{}

Store::Store(LocTimeGrid::Space posSpace, size_t Nstock):
	posSpace(posSpace), Nstock(Nstock)
{}

Store::Store(LocTimeGrid::Space posSpace, size_t thresholds, std::vector<double> prices):
	posSpace(posSpace), thresholds(thresholds), prices(prices)
{}

Store::Store(LocTimeGrid::Space posSpace, size_t thresholds, std::vector<double> prices,\
				std::vector<size_t> stocks, std::vector<int> labels, std::vector<Goods::Goods> storeGoods):
			posSpace(posSpace), thresholds(thresholds), prices(prices),\
						stocks(stocks), labels(labels), storeGoods(storeGoods)
{}

Store::~Store()
{}

Stores::Stores(size_t NStores):
	NStores(NStores)
{}

Stores::Stores(size_t NStores, std::vector<Store> stores):
	NStores(NStores), stores(stores)
{}

Stores::~Stores()
{}

const Store randStore(const Goods::Market& market) //, double percentage) //size_t label, double var = 0.)
{
	
	size_t Ngoods = market.Ngoods;
	Random<int> shopSize(Ngoods); 										//ngoods < Ngoods
	LocTimeGrid::Space pos = LocTimeGrid::randSpace(0,0); 				//location
	size_t threshold = 4; 	//Random<int> threshold(4);					//threshold
	Random<double> pricesVar(Ngoods,1.);								//prices changes
	std::vector<double> deltaprices;
	size_t stockNb = 20;												//init stocks
	std::vector<size_t> stocks((size_t)shopSize.random[0],stockNb);		//stocks
	std::vector<Goods::Goods> storeGoods = \
						Goods::GetStore(market, (size_t)shopSize.random[0]);
	std::vector<int> labels;
	
	for (size_t i = 0 ; i < storeGoods.size(); ++i)
	{
		cout << i << " " << /*storeGoods.<<*/ endl;
		deltaprices.push_back( pricesVar.random[i] - 0.5 );
		labels.push_back( storeGoods[i].label );
	}
	
	return Store( pos, threshold, deltaprices, stocks, labels, storeGoods);
}

inline bool findinStore(int& label, Store& store)
{
	for (size_t i = 0 ; i < store.Nstock; ++i)
	{
		if ( label  == store.storeGoods[i].label )
		{return true; break;}
	}
	return false;
}	

Stores MakeSupply(const Goods::Market& market, size_t Nstores)
{
	std::vector<Store> stores;
	for (size_t i = 0; i < Nstores; ++i)
	{
		stores.push_back( randStore(market) );
	}
	return Stores(Nstores, stores);
}

}