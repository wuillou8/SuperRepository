#include "NeuronesInSchool.h" 


NeuronesInSchool::NeuronesInSchool( Neurones* my_neurone ) : myN(my_neurone)
{
	//Initialises delta lists
	d_InputHidden = new ( double*[myN->Ninput + 1] );
	for ( int i=0; i <= myN->Ninput; ++i )
	{
		d_InputHidden[i] = new ( double[myN->Nhidden] );
		for ( int j=0; j < myN->Nhidden; ++j ) d_InputHidden[i][j] = 0;
	}

	d_HiddenOutput = new ( double*[myN->Nhidden + 1] );
	for ( int i=0; i <= myN->Nhidden; ++i )
	{
		d_HiddenOutput[i] = new ( double[myN->Noutput] );	
		for ( int j=0; j < myN->Noutput; ++j ) d_HiddenOutput[i][j] = 0;
	}

	//create error gradient storage
	e_HiddenGradients = new ( double[myN->Nhidden + 1] );
	for ( int i=0; i <= myN->Nhidden; ++i ) e_HiddenGradients[i] = 0;

	e_OutputGradients = new ( double[myN->Noutput + 1] );
	for ( int i=0; i <= myN->Noutput; ++i ) e_OutputGradients[i] = 0;
}


void GetWeights()
{
	
	//for ( int i=0; i < myN->Noutput; ++i )	e_OutputGradients[i] = 0;
	
}

void NeuronesInSchool::setTrainingParameters( double lR, double m) //, bool batch )
{
	learningRate = lR;
	momentum = m;
	//bool useBatch = batch;
}

inline double NeuronesInSchool::OutputErrGrad( double desiredValue, double outputValue )
{	//return delta_k = y_k*(1.-y_k)*(d_k-y_k)
	return outputValue * ( 1 - outputValue ) * ( desiredValue - outputValue );
}

double  NeuronesInSchool::HiddenErrGrad( int j )
{	//return delta_j = y_j*(1.-y_j)*sum_k( w_jk delta_k )
	double Sum = 0.;
	for( int i = 0; i < myN->Noutput; ++i )
	{	Sum += myN->wHiddenOutput[j][i] * e_OutputGradients[i];	}

	return myN->hiddenNrs[j] * ( 1. - myN->hiddenNrs[j] ) * Sum;
}

void NeuronesInSchool::BackPropagate( double* Outputs )
{		
	//modify deltas between hidden/output layers
	for (int k = 0; k < myN->Noutput; k++)
	{
		//error gradient output node
		e_OutputGradients[k] = OutputErrGrad( Outputs[k], myN->outputNrs[k] );
		for (int i = 0; i <= myN->Nhidden; i++) 
		{				
			d_HiddenOutput[i][k] = learningRate * myN->hiddenNrs[i] * e_OutputGradients[k] + momentum * d_HiddenOutput[i][k];
		}
	}

	for (int k = 0; k < myN->Nhidden; k++)
	{
		//error gradient hidden node
		e_HiddenGradients[k] = HiddenErrGrad( k );
		for (int i = 0; i <= myN->Ninput; i++)
		{	
			d_InputHidden[i][k] = learningRate * myN->inputNrs[i] * e_HiddenGradients[k] + momentum * d_InputHidden[i][k];
		}
	}
	
	updateWeights();
}

void NeuronesInSchool::updateWeights()
{
	//input -> hidden weights
	for (int i = 0; i <= myN->Ninput; i++)
	{	for (int j = 0; j < myN->Nhidden; j++) 
		{
			myN->wInputHidden[i][j] += d_InputHidden[i][j];	
	}	}
	//hidden -> output weights
	for (int j = 0; j <= myN->Nhidden; j++)
	{	for (int k = 0; k < myN->Noutput; k++) 
		{					
			myN->wHiddenOutput[j][k] += d_HiddenOutput[j][k];
		}
	}
}

NeuronesInSchool::~NeuronesInSchool()
{	
	delete[] d_InputHidden;	
	delete[] d_HiddenOutput;	
	delete[] e_HiddenGradients;	
	delete[] e_OutputGradients;	
}
