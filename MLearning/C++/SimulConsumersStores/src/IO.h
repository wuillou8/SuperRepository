#pragma once

#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>
#include <stdlib.h>

#include "World.h"

using namespace std;

namespace IO {
ifstream& ReadIn( ifstream& myfile );
template<typename T>
void PrintOut(T bla);

void printheaderDBCustomers( ofstream& ostream );
void printheaderDBstores( ofstream& ostream );
}
