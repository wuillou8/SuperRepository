//============================================================================
// Name        : SimLocaFox.cpp
// Author      : jw
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================
#include "Random.h"
#include "LocTimeGrid.h"
#include "Goods.h"

#include <iostream>
//#include <vector>
using namespace std;

int main() {
	

	cout << "Hello World!!!" << endl; // prints Hello World!!!
	LocTimeGrid::Space space(1, 1);
	
	Random<int> rando(50,5);
	cout << (int)rando.random[41] << " iiiciii " << rando.size << endl;
	//cout << space.posX << space.posY  << " ici " << endl;
	cout << "Hello World2!!!" << endl;
	
	/*Goods::Goods good(1.2, 2, 3);
	Goods::Goods jackson = Goods::randGoods(1);
	cout << jackson.categ << " " << jackson.label << " " << jackson.price << endl;*/
	
	//const std::vector<Goods::Goods> market = Goods::MakeMarket(10);
	int jjj = 10; 
	Goods::Market market(jjj);
	for (int i = 0 ; i < jjj ; ++i)
	{	//Goods(double price, size_t categ, size_t label)
		cout << "bla " << market.market[i].price << " " << market.market[i].categ << " " << market.market[i].label << endl;
	}
	
	cout << "=======================================================================" << endl;
	
	std::vector<Goods::Goods> jair = Goods::GetStore(market, 3);
	cout << jair[0].price << " jair.market[0].price " << endl;
	cout << jair[1].price << " jair.market[0].price " << endl;
	
	return 0;
}
