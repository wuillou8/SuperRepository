#include <fstream>
#include <iostream>
#include <vector>
#include "IO.cpp"
#include "Neurones.cpp"
#include "NeuronesInSchool.cpp"

using namespace std; 

/*template <char D>std::istream& delim(std::istream& in){  char c;  if (in >> c && c != D) in.setstate(std::ios_base::failbit);  return in;}*/

int main(int argc,char **argv)
{	
	int AnalysisStart = 0;	
	int AnalysisSize = 1000;

	IOdbl* input = readIN( "letter-recognition.data2" , 0 , 1000 );	
	
	// set neurones grid
	Neurones myNeurones( 4 , 4 , 4 );	
	myNeurones.NeuronalBuild();
	NeuronesInSchool myNeuronesInSchool( &myNeurones );
	myNeuronesInSchool.setTrainingParameters( 0.001 /*lR*/, 0.9 /*m*/);
	

	delete[] input;
}
