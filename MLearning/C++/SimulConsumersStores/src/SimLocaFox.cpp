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
	
	/*******************
	 * bladibla *
	 * *****************/

	myInfile.close();
	myfileStore.close();
	myfileCustoms.close();

	return 0;
}
