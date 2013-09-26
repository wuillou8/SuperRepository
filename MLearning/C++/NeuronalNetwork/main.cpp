#include <fstream>
#include <iostream>
#include <vector>
/*
#include <string>
#include <sstream> 
#include <stdlib.h>
*/
#include "IO.cpp"
#include "Neurones.cpp"
#include "NeuronesInSchool.cpp"

using namespace std; 

/*template <char D>
std::istream& delim(std::istream& in)
{
  char c;
  if (in >> c && c != D) in.setstate(std::ios_base::failbit);
  return in;
}*/

int main(int argc,char **argv)
{
	int AnalysisStart = 0;
	int AnalysisSize = 1000;

	IO* input = readIN("letter-recognition.data2", 0, 1000);
	
	Neurones myNeurones(2,2,2);
	myNeurones.NeuronalBuild();
	
	delete[] input;
}
