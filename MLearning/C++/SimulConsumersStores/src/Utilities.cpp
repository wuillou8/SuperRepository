#include "Utilities.h"

namespace Utilities {

void printheaderDBCustomers( ofstream& ostream ) {
	ostream<<"Time, GoodsNb, price, CustoNb, PosX_cust, PosY_cust, PosX_stor, PosY_stor, Dist"<<endl;
}

void printheaderDBstores( ofstream& ostream ) {
	ostream<<"Time, StoreNb, Label_good, Prices_stor, posX, posY"<<endl;
}

void PrintOut(string bla) {
	cout << bla << endl;
}
}
