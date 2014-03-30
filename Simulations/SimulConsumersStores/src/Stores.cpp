
#include "Stores.h"

using namespace std;

namespace Supply
{

Store::Store(LocTimeGrid::Space posSpace):
	posSpace(posSpace), Nstock(), thresholds(), prices(),\
			stocks(), labels(), categs(), storeGoods(), store_number()
{}

Store::Store(LocTimeGrid::Space posSpace, size_t Nstock):
	posSpace(posSpace), Nstock(Nstock), thresholds(), prices(),\
			stocks(), labels(), categs(), storeGoods(), store_number()
{}

Store::Store(LocTimeGrid::Space posSpace, size_t thresholds, std::vector<double> prices) :
	posSpace(posSpace), Nstock(), thresholds(thresholds), prices(prices),\
			stocks(), labels(), categs(), storeGoods(), store_number()
{}

Store::Store(LocTimeGrid::Space posSpace, size_t Nstock, size_t thresholds, std::vector<double> prices,\
				std::vector<size_t> stocks, std::vector<int> labels, std::vector<int> categs, std::vector<Goods::Goods> storeGoods, size_t store_number) :
			posSpace(posSpace), Nstock(Nstock), thresholds(thresholds), prices(prices),\
						stocks(stocks), labels(labels), categs(categs), storeGoods(storeGoods), store_number(store_number)
{}

ostream& operator<<(ostream& os, const Store& store){
	os << "class Store" << endl;
	os << store.posSpace;
	os << "Nstock " << store.Nstock << endl;
	os << "thresholds " << store.thresholds << endl;
	os << "store_number " << store.store_number << endl;
	for (size_t i = 0; i < store.prices.size(); ++i) {
		os << "prices " << i << " " << store.prices[i] << endl;
		os << "stocks " << i << " " << store.stocks[i] << endl;
		os << "labels " << i << " " << store.labels[i] << endl;
		os << "categs " << i << " " << store.categs[i] << endl;
	}
	for (size_t i = 0; i < store.storeGoods.size(); ++i) {
		os << "storeGoods " << i << endl;
		os << store.storeGoods[i];
	}
    return os;
}

double Store::getPriceWithLabel( const int& label, const int& categ ) const {
	for( size_t i = 0; i < Nstock; ++i ) {
		if ( ( labels[i] == label ) && ( categs[i] == categ ) ) {
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

ostream& operator<<(ostream& os, const Stores& stores) {
	os << "class Stores" << endl;
	os << "Nstores" << stores.Nstores << endl;
	for (size_t i = 0; i < stores.stores.size(); ++i) {
		os << "Stores " << i << endl;
		os << stores.stores[i];
	}
	return os;
}


void Stores::AddStore(Store store ) {
	Nstores++;
	store.store_number = Nstores;
	cout <<"encorla"<<endl;
	stores.push_back( store );
}

Stores::~Stores()
{}

Store randStore(const Goods::Market& market, size_t& storeNumber) {
	//threshold fixed ...
	//stockInit fixed ...
	size_t Ngoods = market.Ngoods;
	size_t shopSize = market.Ngoods*market.Ncategs; //QuickRandom::randi(Ngoods);			//ngoods <= Ngoods
	//cout << "bla "<< market.Ngoods*market.Ncategs << endl;
	//exit (EXIT_FAILURE);
	//shopSize = 1;  											/* to be changged later ... current simulation only */
	LocTimeGrid::Space pos = LocTimeGrid::randSpace( LocTimeGrid::NgridX, LocTimeGrid::NgridY ); 	//location
	size_t threshold = QuickRandom::randi(4);				//threshold
	Random<double> pricesVar(Ngoods,1.);					//prices changes
	size_t stockNb = 20;									//init stocks
	std::vector<size_t> stocks((int) shopSize,(int) stockNb);	//stocks
	std::vector<Goods::Goods> storeGoods = Goods::GetStore( market, shopSize );
	std::vector<double> deltaprices;
	std::vector<int> labels, categs;
	for (size_t i = 0 ; i < storeGoods.size(); ++i)	{
		// simulating price variations of 10%
		deltaprices.push_back( QuickRandom::GaussianHull( pricesVar.random[i], 1, 0.1 ) );
		labels.push_back( storeGoods[i].label );
		categs.push_back( storeGoods[i].categ );
	}
	return Store( pos, shopSize, threshold, deltaprices, stocks, labels, categs, storeGoods, storeNumber);
}

const Store MakeStore( LocTimeGrid::Space posSpace, size_t Nstock, size_t thresholds, \
						std::vector<double> prices, std::vector<size_t> stocks, std::vector<int> labels, std::vector<int> categs,\
								std::vector<Goods::Goods> storeGoods, size_t store_number ) {
	return Store( posSpace, Nstock, thresholds, prices, stocks, labels, categs, storeGoods, store_number);
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

double priceInStore( int& label, int& categ , Store& store ) {
	for (size_t i = 0 ; i < store.Nstock; ++i) {
		if ( ( label  == store.storeGoods[i].label ) && ( categ ==  store.storeGoods[i].categ ) ) {
			return store.storeGoods[i].price;
			break;
		}
	}
	cout << " ERROR from Supply::priceInStore : goods with label expected" << endl;
	exit (EXIT_FAILURE);
}

}
