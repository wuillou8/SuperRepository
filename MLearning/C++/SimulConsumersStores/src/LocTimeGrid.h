#pragma once 

#include <cstddef> 

#include "Random.h"

namespace LocTimeGrid {
//Space-Time
static size_t NgridT;
static size_t NgridX;
static size_t NgridY;


class Space {
public:
	Space(size_t posX, size_t posY);
	Space(Space const &other);
	virtual ~Space();

	// space-time grid 
	size_t posX, posY;
	void describeMyself();
};

class Time {
public:
	Time(size_t time);
	virtual ~Time();

	// space-time grid 
	size_t time;
	void describeMyself();
};


class SpaceTime {
public:
	SpaceTime( size_t gridT, size_t gridX, size_t gridY );
	virtual ~SpaceTime();

	size_t gridT;
	size_t gridX;
	size_t gridY;
	/*Space space;
	Time time;*/
};

//spatial dist
const double distance(const Space& guy1, const Space& guy2);
//inline const double distance(const Space& guy1,const Space& guy2);
const Time randTime(size_t shift);
const Space randSpace(size_t shiftX, size_t shiftY);

}
