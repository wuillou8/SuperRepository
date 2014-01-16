#pragma once 

#include <cstddef> 
#include <vector>
#include <assert.h>
#include <math.h>
#include <fstream>

#include "Random.h"

namespace Goods {
//const size_t NNgoods = 10;

class Goods {
public:
	Goods(double price, size_t categ, size_t label);
	virtual ~Goods();

	double price;
	int categ;
	int label;
	void describeMyself();
	void IOout( ofstream& ostream );
	//int complements, substitutes;	//latency
};

class Market {
public:
	Market(size_t Ngoods, size_t Ncategs );
	virtual ~Market();

	size_t Ngoods;
	size_t Ncategs;
	std::vector<Goods> market;
	void describeMyself();
};

//used in Goods
const Goods randGoods(size_t label, size_t categ, double var);
std::vector<Goods> MakeMarket(size_t NGoods, size_t Ncategs);
//used in Stores
std::vector<Goods> GetStore(const Market& market, size_t nGoods);

}
