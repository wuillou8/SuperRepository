#pragma once 

#include <vector>

#include "LocTimeGrid.h"
#include "Random.h"

namespace Customers
{
//const size_t NHPars = 2; //number hidden paramters

class Customer
{
public:
	Customer(LocTimeGrid::Space loc, std::vector<double> utilparams);
	virtual ~Customer();
	
	//double Money;
	LocTimeGrid::Space locSpace;
	std::vector<double> utilparams;
	
};

/*template <LocTimeGrid::Space locSpace,int Nb>
class CustomerClusters
{};*/

Customer randCustomer( size_t NHparms ); 
inline double logit( double x );
//inline double utilityFct( , double x );
//I have been listening while working to the radio today and I focussed about the decline of the western civilization, from both french an american sides.
}