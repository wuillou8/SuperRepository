


class dataEntry
{
public:	
	double* pattern;	//input patterns
	double* target;		//target result
public:	
	dataEntry(double* p, double* t): pattern(p), target(t) 
	{}	
	~dataEntry()
	{				
		delete[] pattern;
		delete[] target;
	}
};

class trainingDataSet
{
public:

	std::vector<dataEntry*> trainingSet;
	std::vector<dataEntry*> generalizationSet;
	std::vector<dataEntry*> validationSet;

	trainingDataSet(){}
	
	void clear()
	{
		trainingSet.clear();
		generalizationSet.clear();
		validationSet.clear();
	}
};


