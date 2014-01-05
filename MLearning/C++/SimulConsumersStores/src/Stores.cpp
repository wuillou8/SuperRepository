
#include "Stores.h"

using namespace std;

namespace Supply
{

Store::Store(LocTimeGrid::Space posSpace):
	posSpace(posSpace), Nstock(), thresholds(), prices(),\
			stocks(), labels(), storeGoods(), store_number()
{}

Store::Store(LocTimeGrid::Space posSpace, size_t Nstock):
	posSpace(posSpace), Nstock(Nstock), thresholds(), prices(),\
			stocks(), labels(), storeGoods(), store_number()
{}

Store::Store(LocTimeGrid::Space posSpace, size_t thresholds, std::vector<double> prices) :
	posSpace(posSpace), Nstock(), thresholds(thresholds), prices(prices),\
			stocks(), labels(), storeGoods(), store_number()
{}

Store::Store(LocTimeGrid::Space posSpace, size_t Nstock, size_t thresholds, std::vector<double> prices,\
				std::vector<size_t> stocks, std::vector<int> labels, std::vector<Goods::Goods> storeGoods, size_t store_number) :
			posSpace(posSpace), Nstock(Nstock), thresholds(thresholds), prices(prices),\
						stocks(stocks), labels(labels), storeGoods(storeGoods), store_number(store_number)
{}

void Store::describeMyself() {
	cout << "class Store" << endl;
	posSpace.describeMyself();
	cout << "Nstock " << Nstock << endl;
	cout << "thresholds " << thresholds << endl;
	cout << "store_number " << store_number << endl;
	for (size_t i = 0; i < prices.size(); ++i) {
		cout << "prices " << i << " " << prices[i] << endl;
		cout << "stocks " << i << " " << stocks[i] << endl;
		cout << "labels " << i << " " << labels[i] << endl;
	}
	for (size_t i = 0; i < storeGoods.size(); ++i) {
		cout << "storeGoods " << i << endl;
		storeGoods[i].describeMyself();
	}
}

void Store::IOout( ofstream& ostream ) {
	for (size_t i = 0; i < Nstock; ++i) {
		ostream << store_number /*<< " " << i*/ << ", " << labels[i] << ", " << prices[i] << ", " << stocks[i] << ", ";
		posSpace.IOout(ostream); 
	}
}

const double Store::getPriceWithLabel( int label ) const {
	for( size_t i = 0; i < labels.size(); ++i ) {
		if ( labels[i] == label ) {
			return prices[i];
		}
	}
	cout<<" ERROR from Supply::Store::getPriceWithLabel : label not found"<<endl;
	exit (EXIT_FAILURE);
}

Store::~Store()
{}

Stores::Stores(size_t Nstores):
	Nstores(Nstores)
{}

Stores::Stores(size_t Nstores, std::vector<Store> stores) :
	Nstores(Nstores), stores(stores)
{}

void Stores::describeMyself() {
	cout << "class Stores" << endl;
	cout << "Nstores" << Nstores << endl;
	for (size_t i = 0; i < stores.size(); ++i) {
		cout << "Stores " << i << endl;
		stores[i].describeMyself();
	}
}

void Stores::AddStore(Store& store ) {
	Nstores++;
	store.store_number = Nstores;
	stores.push_back( store );
}

Stores::~Stores()
{}

const Store randStore(const Goods::Market& market, size_t& storeNumber) {
	//threshold fixed ...
	//stockInit fixed ...
	size_t Ngoods = market.Ngoods;
	size_t shopSize = QuickRandom::randi(Ngoods);			//ngoods <= Ngoods
	shopSize = 1;  											/* to be changged later ... current simulation only */
	LocTimeGrid::Space pos = LocTimeGrid::randSpace( LocTimeGrid::NgridX, LocTimeGrid::NgridY ); 	//location
	size_t threshold = QuickRandom::randi(4);				//threshold
	Random<double> pricesVar(Ngoods,1.);					//prices changes
	size_t stockNb = 20;									//init stocks
	std::vector<size_t> stocks((int)shopSize,(int)stockNb);	//stocks
	std::vector<Goods::Goods> storeGoods = Goods::GetStore(market, shopSize);
	std::vector<double> deltaprices;
	std::vector<int> labels;
	for (size_t i = 0 ; i < storeGoods.size(); ++i)	{
		// simulating price variations of 10%
		deltaprices.push_back( QuickRandom::GaussianHull( pricesVar.random[i], 1, 0.1 ) );
		labels.push_back( storeGoods[i].label );
	}
	return Store( pos, shopSize, threshold, deltaprices, stocks, labels, storeGoods, storeNumber);
}

const Store MakeStore( LocTimeGrid::Space posSpace, size_t Nstock, size_t thresholds, \
						std::vector<double> prices, std::vector<size_t> stocks, std::vector<int> labels, \
								std::vector<Goods::Goods> storeGoods, size_t store_number ) {
	return Store( posSpace, Nstock, thresholds, prices, stocks, labels, storeGoods, store_number);
}

Stores MakeSupply( size_t Nstores, const Goods::Market& market ) {
	std::vector<Store> stores;
	for (size_t i = 0; i < Nstores; ++i) {
		stores.push_back( randStore(market, i) );
	}
	return Stores( Nstores, stores );
}

void ShoppingInStore( int& label, Store& store ) {
	for (size_t i = 0 ; i < store.Nstock; ++i) {
			if ( label  == store.storeGoods[i].label ) {
				if(--(store.stocks[i]) == store.thresholds) 
				{	store.stocks[i] = store.thresholds + 10;	}
			}
	}
}

bool findInStore( int& label, Store& store ) {
	for (size_t i = 0 ; i < store.Nstock; ++i) {
		if ( label  == store.storeGoods[i].label ) {
			return true;
			break;
		}
	}
	return false;
}	

double priceInStore( int& label, Store& store ) {
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
