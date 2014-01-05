//============================================================================
// Name        : SimLocaFox.cpp
// Author      : jw
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================
#include <iostream>
#include <fstream>

#include "Random.h"
#include "LocTimeGrid.h"
#include "Goods.h"
#include "IO.h"
#include "World.h"

 
using namespace std;

int main(int argc, char **argv) {

	ifstream myInfile ("InitializeSim.txt");
	ofstream myfileStore ("../DBases/Data/DBstore.txt");
	ofstream myfileCustoms ("../DBases/Data/DBcustoms.txt");
	ofstream testfile ("../DBases/Data/testfile.txt");
	//ifstream test2file ("../DBases/Data/testfile.txt");
	//ifstream test22file ("../DBases/Data/testfile.txt");

	/*LocTimeGrid::NgridT = 100;
	LocTimeGrid::NgridX = 100;
	LocTimeGrid::NgridY = 100;*/
	
	WORLD::World world = WORLD::MakeMyWorld( 5/*size_t NgridT*/, 100/*size_t NgridX*/, 100/*size_t NgridY*/, \
													1 /*size_t Ngoods*/, 3 /*Ncategories*/, 5000/*size_t Ncustoms*/, 50/*size_t Nstores*/);
	world.describeMyself();
	cout << "start-----------------------start " << world.stores.Nstores  <<endl;

	WORLD::InitTest( world, 1. );
	WORLD::RunWorldStory( world, myfileCustoms, myfileStore );
	WORLD::checks( world );

	myInfile.close();
	myfileStore.close();
	myfileCustoms.close();
	testfile.close();

	return 0;
}
