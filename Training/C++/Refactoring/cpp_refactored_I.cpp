#include <stdio.h>
#include <stdlib.h>
#include <iostream>

enum FeatureType {eCircle, eTriangle, eSquare,eUnknown};

class Shape {
    public:
        virtual ~Shape() {};
        virtual void draw() = 0;
};

class Circle: public Shape {
	public:
		Circle(double* _coords) : coords(_coords) 
			{};
		void draw();
	protected:
	double* coords;
};

class Polygon: public Shape {
	public: 
		Polygon(double* _edges) : edges(_edges) 
			{}
		void draw();
	protected:
	double* edges;
	int n; 
};

void Circle::draw () {
	/*** draw a Circle somehow ***/
	};

void Polygon::draw () {
	/*** draw a Polygon somehow ***/
	};

double* readPts(FILE* file, int n_pts) {
	double* pts;
	if( !(fread(&pts, sizeof(double), n_pts, file) == n_pts) ) {
		fputs ("Points not recognised",stderr); exit (3);
	}
	return pts;
};

int main(int argc, char* argv[])
{
	FeatureType type;
	Shape* obj;
	double* pts;
	FILE* file = fopen("Outprintfeats.dat", "r"); 
	if(file==NULL) {fputs ("File error",stderr); exit (1);}
	if ( fread(&type, sizeof(FeatureType), 1, file) != 1/*sizeof(FeatureType)*/ ) 
	{ fputs ("Type not readable",stderr); exit (2); }
        switch (type) {
		case eCircle: 
			obj = new Circle( readPts(file, 3) ); break;
        	case eTriangle:
			obj = new Polygon( readPts(file, 6) ); break;	
	        case eSquare: 
			obj = new Polygon( readPts(file, 8) ); break;
        	default: type = eUnknown; 
			fputs ("Type not in FeatureTypes list",stderr); exit (3);
        }
	
	return 0;
}
