//#include "NeuronesInSchool.h"

class Neurones	{
	
	friend class NeuronesInSchool;	
	
	public:

	// Nb of Els	
	int Ninput, Nhidden, Noutput;

	// Creat. / Destr.
	Neurones(int inputLay, int hiddenLay, int outputLay) : 	
		Ninput(inputLay),
		Nhidden(hiddenLay),
		Noutput(outputLay)
	{};	
	~Neurones();
	
	private:

	// "Neural grid" with three layers 	
	double* inputNrs; // input neurones 	
	double* hiddenNrs; 	
	double* outputNrs;	

	//weights	
	double** wInputHidden;	
	double** wHiddenOutput;

	public:

	Neurones NeuronalBuild();
	inline double sigmoid(double x);

	private:
	void InitWeights();
}; 


