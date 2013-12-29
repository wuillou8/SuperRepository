#include "IO.h"

namespace IO {

ifstream& ReadIn( ifstream& myfile ) {
	 string line;
	 if (myfile.is_open())
	  {
	    while ( getline (myfile,line) )
	    {
	      cout << line << '\n';
	    }
	    myfile.close();
	  }
	 return myfile;
}

template<typename T>
void PrintOut(T bla) {
	cout << (string)bla << endl;
}

void printheaderDBCustomers( ofstream& ostream ) {
	ostream<<"Time, GoodsNb, price, CustoNb, PosX_cust, PosY_cust, PosX_stor, PosY_stor, Dist"<<endl;
}

void printheaderDBstores( ofstream& ostream ) {
	ostream<<"Time, StoreNb, Label_good, Prices_stor, posX, posY"<<endl;
}

}
/*
IO::IO()
{}
IO::~IO()
{}
*/
