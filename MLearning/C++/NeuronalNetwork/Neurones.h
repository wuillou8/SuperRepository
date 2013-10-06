//#include "NeuronesInSchool.h"

class Neurones	{
	private:	
	// "Neural grid" with three layers 	
	double* inputNrs; 	
	double* hiddenNrs; 	
	double* outputNrs;	

	//weights	
	double** wInputHidden;	
	double** wHiddenOutput;

	public:		
	// Nb of Els	
	int Ninput, Nhidden, Noutput;	

	Neurones(int inputLay, int hiddenLay, int outputLay) : 	
		Ninput(inputLay),
		Nhidden(hiddenLay),
		Noutput(outputLay)	{};	
	~Neurones();	
	//friend /*class*/ NeuronesInSchool;public:	
	Neurones NeuronalBuild();
}; 


