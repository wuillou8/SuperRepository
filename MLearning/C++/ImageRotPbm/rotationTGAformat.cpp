#include <fstream>
#include <iostream>
#include <vector>
#include <string>

using namespace std;

typedef short int* Byte;

typedef struct
{
    unsigned char IDLength;
    unsigned char ColMType;
    unsigned char picType;
    short int colourMap;
    short int XOrig;
    short int YOrig;
    short int imageWidth;
    short int imageHeight;	
    unsigned char pixSize; 
    unsigned char imageDescr;
} TGAFILE;

/*std::ifstream&*/void ReadTGAHeader(std::ifstream& in, const TGAFILE& tgaFile)
{
	in.read ((char*)(&tgaFile.IDLength), 1);
	in.read ((char*)(&tgaFile.ColMType), 1);
	in.read ((char*)(&tgaFile.picType), 1);
	in.read ((char*)(&tgaFile.colourMap), 5);
	in.read ((char*)(&tgaFile.XOrig), 2);
	in.read ((char*)(&tgaFile.YOrig), 2);
	in.read ((char*)(&tgaFile.imageWidth), 2);
	in.read ((char*)(&tgaFile.imageHeight), 2);
	in.read ((char*)(&tgaFile.pixSize), 1);
	in.read ((char*)(&tgaFile.imageDescr), 1);
	//return in;
}

/*std::ofstream&*/void WriteTGAHeader(std::ofstream& out, const TGAFILE& tgaFile)
{
	out.write ((char*)(&tgaFile.IDLength), 1);
	out.write ((char*)(&tgaFile.ColMType), 1);
	out.write ((char*)(&tgaFile.picType), 1);
	out.write ((char*)(&tgaFile.colourMap), 5);
	// Output changed for the rotation //*
	out.write ((char*)(&tgaFile.XOrig), 2);
	out.write ((char*)(&tgaFile.imageWidth), 2); //*
	out.write ((char*)(&tgaFile.imageHeight), 2); //*
	out.write ((char*)(&tgaFile.imageWidth), 2); //*
	out.write ((char*)(&tgaFile.pixSize), 1);
	out.write ((char*)(&tgaFile.imageDescr), 1);
	//return out;
}

int main(int argc,char **argv)
{
	TGAFILE tgaFile;
	int imageSize, colorMode; 
	int nxyGrid, nxGrid, nyGrid, coordGrid; 
	vector<Byte> bytes;
	Byte tmp; 

	// Basic IO Error handling
	if(argc != 3+1)
	{	cout << "!!!expected input: <program> <input_image.tga> <output_image.tga> left|right " << argc << endl; 
	 	exit (EXIT_FAILURE);
	}

    	ifstream in;
	in.open (argv[1], ios::in | ios::binary);
	ofstream out;
	out.open (argv[2], ios::out | ios::binary);

	cout << "---------------------- Handle Header ---------------------"<< endl;
	ReadTGAHeader(in, tgaFile); 
	WriteTGAHeader(out, tgaFile);
	cout << "---------------------- Handle Figure ----------------------"<< endl;
	// Initialisation
	nxGrid = (int)tgaFile.imageWidth;
	nyGrid = (int)tgaFile.imageHeight;
	nxyGrid = nxGrid * nyGrid;
	// "Colormode" for Image Descriptor = 32 computed as spec.in the docu.
	colorMode = (int)tgaFile.pixSize / 8;
    	imageSize =  nxyGrid * colorMode;    
    	// ReadIn Fig
    	int i = 0;
    	while (in.good() && i < nxyGrid)
    	{
    		in.read ((char*)(&tmp), colorMode);//myheader.ColMType)
        	bytes.push_back(tmp);
		++i;
    	}
	// Rotate & print Fig
	if((string)argv[3] == "right") // 90° rotation to the right
	{	for (int y = 0; y < nxGrid; ++y)
		{	for (int x = 0 ; x < nyGrid; ++x)
			{
				coordGrid = (nyGrid-1-x)*(nxGrid) + y; 
				out.write ((char*)(&bytes[coordGrid]),colorMode);
		}	}
	}
	else if((string)argv[3] == "left") // 90° rotation to the left
	{	for (int y = 0; y < nxGrid; ++y)
		{	for (int x = 0 ; x < nyGrid; ++x)
			{
				coordGrid = x*(nxGrid) + (nxGrid-1-y); 
				out.write ((char*)(&bytes[coordGrid]),colorMode);
		}	}
	}
	else
	{	cout << "!!!argv[3] must be in left|right " <<endl; 
		exit (EXIT_FAILURE);
	}

	cout << "---------------------- Finalise      ----------------------"<< endl;
	while (in.good())
	{
		in.read ((char*)(&tmp), colorMode);
		out.write ((char*)(&tmp), colorMode);
	}
	out.close();
	in.close();
}


