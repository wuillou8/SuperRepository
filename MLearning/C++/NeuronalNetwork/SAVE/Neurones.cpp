#include <math.h>
#include "Neurones.h"

using namespace std; 

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

	InitWeights();
}

inline double Neurones::sigmoid( double x )
{
	//sigmoid fct°
	return 1./(1.+exp(-x));
}	

void Neurones::InitWeights( )
{
	//set range
	double rH = 1/sqrt( (double) Ninput);
	double rO = 1/sqrt( (double) Nhidden);
	
	//set weights: input and hidden 		
	for(int i = 0; i <= Ninput; i++)
	{	for(int j = 0; j < Nhidden; j++) 
		{	//set weights to random values
			wInputHidden[i][j] = ( ( (double)(rand()%100)+1)/100  * 2. * rH ) - rH;			
		}	
	}
	for(int i = 0; i <= Nhidden; i++)
	{	for(int j = 0; j < Noutput; j++) 
		{	//set weights to random values
			wHiddenOutput[i][j] = ( ( (double)(rand()%100)+1)/100 * 2. * rO ) - rO;
		}	
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
