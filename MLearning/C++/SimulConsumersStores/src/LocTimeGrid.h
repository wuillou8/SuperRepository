#pragma once 

#include <cstddef>
#include <stdlib.h>
#include <fstream>

#include "Random.h"

namespace LocTimeGrid {
//Space-Time
	const static size_t NgridX = 1000;
	const static size_t NgridY = 1000;
	const static size_t NgridT = 100;
	
//template < size_t NgridX, size_t NgridY >
class Space {
public:
	Space(size_t posX, size_t posY);
	Space(Space const &other);
	virtual ~Space();

	// space-time grid 
	size_t posX, posY;
	void describeMyself();
	void IOout( ofstream& ostream );
};

class Time {
public:
	Time(size_t time);
	virtual ~Time();

	// space-time grid 
	size_t time;
	void describeMyself();
	void IOout( ofstream& ostream );
};

//spatial dist
const double distance(const Space& guy1, const Space& guy2);
//inline const double distance(const Space& guy1,const Space& guy2);

const Space randSpace(size_t shiftX, size_t shiftY);
Time randTime(size_t shift);
}
