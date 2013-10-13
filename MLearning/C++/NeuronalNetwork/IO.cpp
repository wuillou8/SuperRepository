#include <fstream>
#include <iostream>
#include <vector>
#include <string>
#include <sstream> 
#include <stdlib.h>

#include "IO.h" 


//	sstream not suited for reading doubles and I cast my strings into doubles later.
using namespace std;
/*
typedef struct {	string letter;	
			string numbers[16];
		} IO;
*/	
typedef struct {	double letter;	
			double numbers[16];
		} IOdbl;

bool ParseIO(istream &in, IOdbl &io)
{	string tmp;

	if (!getline(in, tmp, ',')) 
	{	return false;	}  
	io.letter = atof(tmp.c_str());  //io.letter;
	for(int i = 0; i < 16;++i)	
	{	
		if (!getline(in, tmp, ',')) 
		{ return false; }
		io.numbers[i] = atof(tmp.c_str());
	}	
	return true;
}

//	ReadIN
//	Read in elements file between Start and Size.
IOdbl* readIN(const char* infileName, int AnalysisStart, int AnalysisSize)
{
	istringstream iss;
	string tmp_line;
	IOdbl * input = new IOdbl[(AnalysisSize-AnalysisStart)];

	int i =  AnalysisStart;	ifstream infile( infileName, ios::in | ios::binary );	
	while( getline(infile, tmp_line) && (i < ( AnalysisSize + AnalysisStart ) ) )	
	{

		IOdbl tmp;
		iss.str (tmp_line);

		if(ParseIO(iss,tmp))
		{
			input[i] = tmp;
		}
		else
		{
			cout << "FAIL" << endl;
		}	++i;	}
	infile.close();	

	return input;
} 
