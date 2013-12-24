#pragma once 

#include <cstddef> 

namespace LocTimeGrid
{
//Space-Time
const static size_t Tgrid = 1000;
const static size_t Ngrid = 100;
const static size_t Nxgrid = Ngrid;
const static size_t Nygrid = Ngrid;



class Space
{
public:
	Space(size_t posX, size_t posY);
	Space(Space const &other);
	virtual ~Space();
	
	// space-time grid 
	size_t posX, posY;
};

class Time
{
public:
	Time(size_t time);
	virtual ~Time();
	
	// space-time grid 
	size_t time;
};

// space-time dist
inline const double distance(const Space& guy1,const Space& guy2);
const Time randTime(size_t shift);
const Space randSpace(size_t shiftX, size_t shiftY);

}