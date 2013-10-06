#include <fstream>
#include <iostream>
#include <vector>
#include <string>
#include <sstream> 
#include <stdlib.h>


using namespace std; 

/*template <char D>
std::istream& delim(std::istream& in)
{
  char c;
  if (in >> c && c != D) in.setstate(std::ios_base::failbit);
  return in;
}*/

typedef struct {
	string letter;
	string numbers[16];
} IO;


bool parseIO(istream &in, IO &io)
{	if (!getline(in, io.letter, ',')) { return false; }  
	for(int i = 0; i < 16;++i)
	{	if (!getline(in, io.numbers[i], ',')) { return false; }
	}
	return true;
}


IO* readIN(std::ifstream &in, int AnalysisStart, int AnalysisSize)
{
	istringstream iss;
	string tmp_line;
	IO * input = new IO[(AnalysisSize-AnalysisStart)];
	
	int i =  AnalysisStart;
	while( getline(in, tmp_line) && (i < ( AnalysisSize + AnalysisStart ) ) )
	{	
		IO tmp;
		iss.str (tmp_line);
		if(parseIO(iss,tmp))
		{	
			input[i] = tmp;	
		}
		else
		{	cout << "FAIL" << endl;	
		}
	++i;
	}
	
	return input;
}



int main(int argc,char **argv)
{
	int AnalysisStart = 0;
	int AnalysisSize = 1000;

	ifstream infile( "letter-recognition.data2", ios::in | ios::binary );
	IO* input = readIN(infile, 0, 1000);
	infile.close();

	delete[] input;
}
