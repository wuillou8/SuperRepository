// you can also use includes, for example:
// #include <algorithm>
int solution(vector<int> &A) {
    // write your code in C++98
    // 100% Version
    int NTot = 0;
    for ( size_t i = 0; i < A.size()+1; ++i ) {
        NTot += (i+1);
    }    
    for ( size_t i = 0; i < A.size(); ++i ) {
        NTot -= A[i];
    }
    return NTot;
}

