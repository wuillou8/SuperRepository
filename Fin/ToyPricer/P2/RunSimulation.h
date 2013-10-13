
enum Model {BMot, SimuSto, BlackSch, BlackSch2, BlackSchJp};

template <typename Models>
class RunSimu	{
    
    public: // Creat. / Destr.
    RunSimu(int NbRuns) : 	
        m_NbRuns(NbRuns)
        {};
    ~RunSimu();

    public:
    void MakeSimu();
    void GetVals();
    
        private:
    int m_NbRuns;
    // model Models;
    double m_averg, m_var;
};
