#include "LocTimeGrid.h"

//#include "Stores.h"

using namespace std;
namespace LocTimeGrid
{

Space::Space(size_t posX, size_t posY) :
	posX(posX), posY(posY)
	{}

Space::Space(Space const &other) :
	posX(other.posX), posY(other.posY)
	{}

Space& Space::operator =( const Space& rhs ) {
	Space( rhs.posX, rhs.posY );
	return *this;
}

bool operator==( const Space& lhs, const Space& rhs ) {
	return  (lhs.posX==rhs.posX) && (lhs.posY==rhs.posY);
}

Space::~Space()
{}

ostream& operator<<(ostream& os, const Space& space) {
    os << "class Space" << endl;
	os << "posX " << space.posX << endl;
	os << "posY " << space.posY << endl;
    return os;
}

Time::Time(size_t time) :
	time(time)
	{}

Time::~Time()
{}

ostream& operator<<(ostream& os, const Time& time) {
    os << "class Time" << endl;
	os << "time " << time << endl;
	os << "NgridT " << NgridT << endl;
    return os;
}

const double distance( const Space& guy1, const Space& guy2) {
	return	sqrt( pow( (double)guy1.posX - (double)guy2.posX, 2 ) + pow( (double)guy1.posY - (double)guy2.posY, 2 ) );
}

const Space randSpace(size_t shiftX = 0, size_t shiftY = 0) {
	//if squared grid
	size_t randSpaceX = QuickRandom::randi( NgridX );
	size_t randSpaceY = QuickRandom::randi( NgridY );
	//cout << NgridX <<" rand__________________" << randSpaceX << " " << randSpaceY << endl;
	return Space( (randSpaceX + shiftX) % NgridX, (randSpaceY + shiftY) % NgridX );
	/*else
	Random<size_t> randSpaceX(Nxgrid);
	Random<size_t> randSpaceY(Nygrid);
	return Space(randSpaceX.random[0] + shiftX, randSpaceY.random[0] + shiftY );
	*/
}

Time randTime(size_t shift = 0) {
	Random<int> randTime((int)NgridT);
	return Time((size_t)randTime.random[0] + shift);
}

}
