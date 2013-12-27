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

Space::~Space()
{}

void Space::describeMyself(  ) {
	cout << "class Space" << endl;
	cout << "posX " << posX << endl;
	cout << "posY " << posY << endl;
}

void Space::IOout( ofstream& ostream ) {
	ostream << posX<<" "<<posY<<" ";
}

Time::Time(size_t time) :
	time(time)
	{}

Time::~Time()
{}

void Time::describeMyself() {
	cout << "class Time" << endl;
	cout << "time " << time << endl;
	cout << "NgridT " << NgridT << endl;
}

void Time::IOout( ofstream& ostream ) {
	ostream << time << " ";
}

const double distance( const Space& guy1, const Space& guy2) {
	return sqrt( (double)guy1.posX*guy2.posX + (double)guy1.posY*guy2.posY );
}

const Space randSpace(size_t shiftX = 0, size_t shiftY = 0) {
	//if squared grid
	/*Random<int> randSpaceX((int)NgridX);
	Random<int> randSpaceY((int)NgridY);*/
	size_t randSpaceX = QuickRandom::randi(NgridX);
	size_t randSpaceY = QuickRandom::randi(NgridY);
	/*cout << "randSpaceX_ " << randSpaceX.random[0] << endl;
	cout << "randSpaceY_ " << randSpaceY.random[0] << endl;
	cout << "randSpaceX__ " << (size_t)randSpaceX.random[0] << endl;
	cout << "randSpaceY__ " << (size_t)randSpaceY.random[0] << endl;*/
	cout << "rand__________________" << randSpaceX << " " << randSpaceY << endl;
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
