#include "Neurones.h"

Neurones Neurones::NeuronalBuild()
{	
	// Create Neurones	
	inputNrs = new double[Ninput + 1]; 	
	hiddenNrs = new double[Nhidden + 1]; 	
	outputNrs = new double[Noutput + 1];	
	// Initialisation	
	for ( int i=0; i < Ninput; i++ ) inputNrs[i] = 0;
	for ( int i=0; i < Nhidden; i++ ) hiddenNrs[i] = 0;
	for ( int i=0; i < Noutput; i++ ) outputNrs[i] = 0;
	// Bias neurones	
	inputNrs[Ninput] = -1;	
	hiddenNrs[Ninput] = -1;	
	//outputNrs[Ninput] = -1;
	
	// Weights	
	// Init	
	wInputHidden = new double*[Ninput + 1];	
	for ( int i=0; i <= Ninput; i++ ) 	
	{		
		wInputHidden[i] = new double[Nhidden];		
		for ( int j=0; j < Nhidden; j++ ) wInputHidden[i][j] = 0;			
	}	

	wHiddenOutput = new double*[Nhidden + 1];
	for ( int i=0; i <= Nhidden; i++ ) 	
	{		
		wHiddenOutput[i] = new double[Noutput];					

		for ( int j=0; j < Noutput; j++ ) wHiddenOutput[i][j] = 0;			
	}	
}

Neurones::~Neurones()
{	
	delete[] inputNrs;	
	delete[] outputNrs;	
	delete[] hiddenNrs;	
	delete[] wInputHidden;	
	delete[] wHiddenOutput;
}
