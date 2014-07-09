#include "Goods.h"

namespace Goods
{

Goods::Goods(double price, size_t categ, size_t label): // Goods(double price, int categ):
		price( 1.*pow(5,categ) )/*price*/, categ(categ), label(label)
{}

Goods::~Goods()
{}

ostream& operator<<(ostream& os, const Goods& goods) {
	os << "class Goods" << endl;
	os << "price " << goods.price << endl;
	os << "categ " << goods.categ << endl;
	os << "label " << goods.label << endl;
	return os;
}

Market::Market( size_t Ngoods, size_t Ncategs = 1 ) :
	Ngoods(Ngoods), Ncategs(Ncategs)
{
	market = MakeMarket( Ngoods, Ncategs );
}

Market::~Market()
{}

ostream& operator<<(ostream& os, const Market& market)
{
	os << "class Market" << endl;
	os << "Ngoods " << market.Ngoods << endl;
	for (size_t i = 0; i < market.market.size(); ++i) {
		os << "market " << i;
		os << market.market[i]; //.describeMyself();
	}
	return os;
}

const Goods randGoods ( size_t label, size_t categ = 1, double var = 0. ) {
	Random<double> randPrice( 1.*label );
	double price = var * ( randPrice.random[0] - 0.5 ) + label;
	return Goods( fabs(price), categ, label );
}

std::vector<Goods> MakeMarket( size_t NGoods, size_t Ncategs = 1 ) {
	std::vector<Goods> market;
	Goods good = randGoods(1);
	for( size_t i = 0; i < NGoods; ++i ) {
		for( size_t j = 0; j < Ncategs ; ++j ) {
			good = randGoods( i, j, 0.5 );
			market.push_back(good);
		}
	}
	return market;
}

std::vector<Goods> GetStore( const Market& market, size_t nGoods ) {
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
