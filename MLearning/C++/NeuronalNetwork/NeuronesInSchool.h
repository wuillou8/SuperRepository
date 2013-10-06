#include <vector>

#define LEARNINGRATE 0.001
#define MOMENTUM 0.9

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

	void setTrainingParameters( double lR, double m); //, bool batch );


	void GetWeights();

	private:
	double momentum; // = 0.9;
	double learningRate; // = 0.001;


	void BackPropagate( double* Outputs );
	inline double OutputErrGrad( double desiredValue, double outputValue );
	
	double HiddenErrGrad( int j );
	void updateWeights();

};
