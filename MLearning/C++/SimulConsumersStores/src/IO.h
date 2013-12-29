#pragma once

#include <iostream>
#include <fstream>
#include <string>
#include <stdlib.h>

using namespace std;

namespace IO {

ifstream& ReadIn( ifstream& myfile );
template<typename T>
void PrintOut(T bla);

void printheaderDBCustomers( ofstream& ostream );
void printheaderDBstores( ofstream& ostream );

}

/*class IO
{
public:
	IO();
	virtual ~IO();
};*/
