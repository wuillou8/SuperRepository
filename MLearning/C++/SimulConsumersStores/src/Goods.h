#pragma once 

#include <cstddef> 
#include <vector>

namespace Goods
{
//const size_t NNgoods = 10;

class Goods 
{
public:
	Goods(double price, size_t categ, size_t label);
	//Goods(double price, int categ);
	//virtual ~Goods();
	
	double price;
	int categ;
	int label;
	//int complements, substuitutes;
	//latency
};

class Market
{
public:	
	Market(size_t Ngoods);
	//virtual ~Market();
	
	size_t Ngoods;
	std::vector<Goods> market;
};

//used in Goods
const Goods randGoods(size_t label, double var);
std::vector<Goods> MakeMarket(size_t NGoods);

//used in Stores
std::vector<Goods> GetStore(const Market& market, size_t nGoods);

}