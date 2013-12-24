#include "LocTimeGrid.h"
#include "Random.h"

namespace LocTimeGrid
{

Space::Space(size_t posX, size_t posY):
	posX(posX), posY(posY)
	{}
Space::Space(Space const &other):
	posX(other.posX), posY(other.posY)
	{}
	
Space::~Space()
{}

Time::Time(size_t time):
	time(time)
	{}

Time::~Time()
{}

inline const double distance( const Space& guy1, const Space& guy2)
{
	return (double)guy1.posX*guy2.posX + (double)guy1.posY*guy2.posY;
}

const Time randTime(size_t shift = 0)
{
	Random<int> randTime(Tgrid);
	return Time((size_t)randTime.random[0] + shift);
}

const Space randSpace(size_t shiftX = 0, size_t shiftY = 0)
{
	//if squared grid
	Random<int> randSpace(2,(int)Ngrid);
	return Space((size_t)randSpace.random[0] + shiftX, (size_t)randSpace.random[1] + shiftY );
	/*else
	Random<size_t> randSpaceX(Nxgrid);
	Random<size_t> randSpaceY(Nygrid);
	return Space(randSpaceX.random[0] + shiftX, randSpaceY.random[0] + shiftY );
	*/
}

}