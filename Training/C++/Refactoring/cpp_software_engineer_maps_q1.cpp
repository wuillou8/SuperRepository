#include <stdio.h>
 
class Feature
{
public:
    enum FeatureType {eUnknown, eCircle, eTriangle, eSquare};
 
    Feature() : type(eUnknown), points(0) { }
 
    ~Feature()
    {
        if (points)
            delete points;
    }
 
    bool isValid() 
    {
        return type != eUnknown;
    }
 
    bool read(FILE* file)
    {        
        if (fread(&type, sizeof(FeatureType), 1, file) != sizeof(FeatureType))
            return false;
        short n = 0;
        switch (type) 
        {
        case eCircle: n = 3; break;
        case eTriangle: n = 6; break;
        case eSquare: n = 8; break;
        default: type = eUnknown; return false;
        }
        points = new double[n];
        if (!points)
            return false;
        return fread(&points, sizeof(double), n, file) == n*sizeof(double);
    }
    void draw()
    {
        switch (type)
        {
        case eCircle: drawCircle(points[0], points[1], points[2]); break;
        case eTriangle: drawPolygon(points, 6); break;
        case eSquare: drawPolygon(points, 8); break;
        }
    }
 
protected:
    void drawCircle(double centerX, double centerY, double radius);
    void drawPolygon(double* points, int size);
 
    double* points;
    FeatureType type;        
};
 
int main(int argc, char* argv[])
{
    Feature feature;
    FILE* file = fopen("features.dat", "r");
    feature.read(file);
    if (!feature.isValid())
        return 1;
    return 0;
}
