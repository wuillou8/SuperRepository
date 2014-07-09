#include <fstream>
#include <iostream>
#include <vector>
#include <string>
#include <sstream> 
#include <stdlib.h>

using namespace std;

typedef struct {	string letter;	
			string numbers[16];
		} IO;

bool ParseIO(istream &in, IO &io)
{	
	if (!getline(in, io.letter, ',')) 
	{ return false; }  	

	for(int i = 0; i < 16;++i)	
	{	
	if (!getline(in, io.numbers[i], ',')) { return false; }	
	}	
	return true;
}

//	ReadIN
//	Read in elements file between Start and Size.
IO* readIN(const char* infileName, int AnalysisStart, int AnalysisSize)
{		
	istringstream iss;	
	string tmp_line;
	IO * input = new IO[(AnalysisSize-AnalysisStart)];

	int i =  AnalysisStart;	ifstream infile( infileName, ios::in | ios::binary );	

	while( getline(infile, tmp_line) && (i < ( AnalysisSize + AnalysisStart ) ) )	
	{			
		IO tmp;		
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


