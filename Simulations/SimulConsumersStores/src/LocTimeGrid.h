#pragma once 

#include <cstddef>
#include <stdlib.h>
#include <iostream>
#include <fstream>
#include <cmath>

#include "Random.h"

namespace LocTimeGrid {
//Space-Time
	const static size_t NgridX = 1000;
	const static size_t NgridY = 1000;
	const static size_t NgridT = 100;//10
	const static size_t distNN = sqrt( 2.*pow(1000,2) );
	
class Space {
public:
	Space(size_t posX, size_t posY);
	Space(Space const &other);
	Space& operator=(const Space& rhs);
	virtual ~Space();

	// space-time grid 
	size_t posX, posY;
	friend ostream& operator<<(ostream& os, const Space& space);
};

bool operator==( const Space& lhs, const Space& rhs );

class Time {
public:
	Time(size_t time);
	virtual ~Time();

	// space-time grid 
	size_t time;
	friend ostream& operator<<(ostream& os, const Time& time);
};

//spatial dist
const double distance(const Space& guy1, const Space& guy2);
//inline const double distance(const Space& guy1,const Space& guy2);

const Space randSpace(size_t shiftX, size_t shiftY);
Time randTime(size_t shift);
}
