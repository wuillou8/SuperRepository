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
	
	//for ( int i=0; i < myN->Noutput; ++i )	e_OutputGradients[i] = 0;
	
}

inline double NeuronesInSchool::OutputErrGrad( double desiredValue, double outputValue )
{	//return delta_k = y_k*(1.-y_k)*(d_k-y_k)
	return outputValue * ( 1 - outputValue ) * ( desiredValue - outputValue );
}

double  NeuronesInSchool::InnerErrGrad( int j )
{	//return delta_j = y_j*(1.-y_j)*sum_k( w_jk delta_k )
	double sum = 0.;
	for( int i = 0; i < myN->Noutput; ++i )
	{sum += myN->wHiddenOutput[j][i]*e_OutputGradients[i];}

	return myN->hiddenNrs[j]*( 1. - myN->hiddenNrs[j] )*sum;
}


NeuronesInSchool::~NeuronesInSchool()
{	
	delete[] d_InputHidden;	
	delete[] d_HiddenOutput;	
	delete[] e_HiddenGradients;	
	delete[] e_OutputGradients;	
}
