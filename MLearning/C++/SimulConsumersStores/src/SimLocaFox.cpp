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
#include "World.h"
 
using namespace std;

int main() {

	ifstream myInfile ("InitializeSim.txt");
	ofstream myfileStore ("../DBases/Data/DBstore.txt");
	ofstream myfileCustoms ("../DBases/Data/DBcustoms.txt");

	/*LocTimeGrid::NgridT = 100;
	LocTimeGrid::NgridX = 100;
	LocTimeGrid::NgridY = 100;*/
	
	WORLD::World world = WORLD::MakeMyWorld( 100/*size_t NgridT*/, 100/*size_t NgridX*/, 100/*size_t NgridY*/, \
													1 /*size_t Ngoods*/, 1000/*size_t Ncustoms*/, 50/*size_t Nstores*/);
	world.describeMyself();
	cout << "-----------------------" << endl;
	//WORLD::MakeMyDBase( world, myfileCustoms, myfileStore );
	//world = WORLD::TimeSweep(world);
	WORLD::RunWorldStory( world, myfileCustoms, myfileStore );

	myInfile.close();
	myfileStore.close();
	myfileCustoms.close();


	/*double val;
	val = QuickRandom::Gaussian(1.,1.);*/
	for (size_t i = 0; i < 100; ++i) {
		cout<<i<<" "<<QuickRandom::Gaussian(1.,1.)<<endl;
	}



	return 0;
}
