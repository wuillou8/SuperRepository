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
#include "World.h"

#include <iostream>
//#include <vector>
using namespace std;

int main() {

	WORLD::World world = WORLD::MakeMyWorld( 100/*size_t NgridT*/, 100/*size_t NgridX*/, 100/*size_t NgridY*/, \
													1/*size_t Ngoods*/, 10/*size_t Ncustoms*/, 3/*size_t Nstores*/);
	world.describeMyself();

	return 0;
}
