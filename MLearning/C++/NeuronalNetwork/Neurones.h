#include "NeuronesInSchool.h"

//class NeuronesInSchool;


class Neurones
{
private:
	// "Neural grid" with three layers
 	double* inputNrs;
 	double* hiddenNrs;
 	double* outputNrs;

	// Nb of Els
	int Ninput, Nhidden, Noutput;

	//weights
	double** wInputHidden;
	double** wHiddenOutput;

public:	
	Neurones(int inputLay, int hiddenLay, int outputLay) : 
		Ninput(inputLay),
		Nhidden(hiddenLay),
		Noutput(outputLay)
	{};
	~Neurones();

	//friend /*class*/ NeuronesInSchool;

public:
	Neurones NeuronalBuild();

};
