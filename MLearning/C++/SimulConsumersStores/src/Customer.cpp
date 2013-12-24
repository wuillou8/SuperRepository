#include <cmath>

#include "Customer.h"

namespace Customers
{

Customer::Customer(LocTimeGrid::Space loc, std::vector<double> utilparams):
	locSpace(loc), utilparams(utilparams)
{
}

Customer::~Customer()
{
}

Customer randCustomer( size_t NHparms )
{
	LocTimeGrid::Space pos = LocTimeGrid::randSpace(0,0); 
	Random<double> utilparams(NHparms,1.);
	return Customer(pos, utilparams.random);
}

inline double logit( double x )
{
	return exp(-x)/(1.+exp(-x));
}

}