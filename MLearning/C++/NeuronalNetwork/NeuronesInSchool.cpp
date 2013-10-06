#include "NeuronesInSchool.h" 


NeuronesInSchool::NeuronesInSchool( Neurones* my_neurone ) : myN(my_neurone)
{
	//Initialises delta lists
	//--------------------------------------------------------------------------------------------------------
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
	//--------------------------------------------------------------------------------------------------------
	e_HiddenGradients = new ( double[myN->Nhidden + 1] );
	for ( int i=0; i <= myN->Nhidden; ++i ) e_HiddenGradients[i] = 0;

	e_OutputGradients = new ( double[myN->Noutput + 1] );
	for ( int i=0; i <= myN->Noutput; ++i ) e_OutputGradients[i] = 0;
}


void GetWeights()
{
	
	for ( int i=0; i < myN->Noutput; ++i )	e_OutputGradients[i] = ;
}


NeuronesInSchool::~NeuronesInSchool()
{	
	delete[] d_InputHidden;	
	delete[] d_HiddenOutput;	
	delete[] e_HiddenGradients;	
	delete[] e_OutputGradients;	
}
