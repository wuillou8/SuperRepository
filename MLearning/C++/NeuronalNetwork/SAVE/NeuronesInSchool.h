//#include "Neurones.h"

#include <vector>

class NeuronesInSchool
{
	private:	
	//network to be trained	
	Neurones* myN;

	//accuracy/MSE required
	double desiredAccuracy;
	
	//deltas change to weights
	double** d_InputHidden;
	double** d_HiddenOutput;

	//error gradients
	double* e_HiddenGradients; 
	double* e_OutputGradients;

	public:		
	NeuronesInSchool(Neurones* unSchooledNeurone);
	~NeuronesInSchool();


	void GetWeights();

	private:
	inline double OutputErrGrad( double desiredValue, double outputValue );
	double InnerErrGrad( int j );

};
