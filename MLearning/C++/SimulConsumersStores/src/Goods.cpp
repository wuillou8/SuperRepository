#include "Goods.h"

namespace Goods
{

Goods::Goods(double price, size_t categ, size_t label): // Goods(double price, int categ):
		price(price), categ(categ), label(label)
{}

Goods::~Goods()
{}

void Goods::describeMyself() {
	cout << "class Goods" << endl;
	cout << "price " << price << endl;
	cout << "categ " << categ << endl;
	cout << "label " << label << endl;
}

void Goods::IOout( ofstream& ostream ) {
	ostream << label << ", "<< price << ", " ;
}

Market::Market(size_t Ngoods): 
	Ngoods(Ngoods)
{
	market = MakeMarket(Ngoods);
}

Market::~Market()
{}

void Market::describeMyself() {
	cout << "class Market" << endl;
	cout << "Ngoods " << Ngoods << endl;
	for (size_t i = 0; i < market.size(); ++i) {
		cout << "market " << i;
		market[i].describeMyself();
	}
}

const Goods randGoods(size_t label, double var = 0.) {
	size_t categ = 1;
	Random<double> randPrice(1.*label);
	double price = var * ( randPrice.random[0] - 0.5 ) + label;
	return Goods( fabs(price), categ, label);
}

std::vector<Goods> MakeMarket(size_t NGoods) {
	std::vector<Goods> market;
	Goods good = randGoods(1);
	for(size_t i = 0; i < NGoods; ++i) {
		good = randGoods(i, 0.5);
		market.push_back(good);
	}
	return market;
}

std::vector<Goods> GetStore(const Market& market, size_t nGoods) {
	//assert(nGoods < market.Ngoods); // check that the Nb goods_store < Nb Goods_market
	std::vector<Goods> GetStore;
	std::vector<Goods> my_market = market.market;
	Random<int> rando(nGoods,nGoods);
	
	for (size_t i = 0; i < nGoods; ++i)
	{
		GetStore.push_back( my_market[ rando.random[i] % my_market.size() ] );
		my_market.erase( my_market.begin() + rando.random[i] % my_market.size() );
	}
	my_market.clear();
	return GetStore;
}

}
