bool fct_m (int i,int j) { return (i<j); }
bool fct_p (int i,int j) { return (i>j); }

// you can also use includes, for example:
#include <algorithm>
int solution(vector<int> &A) {
    // write your code in C++98
    // 100% solution
    vector<int> Negs(3, 0);
    vector<int> Poss(3, -1000);
    int maxNeg(0), maxPos(-1000);
    int* val;

    for ( size_t i = 0; i < A.size(); ++i ) {
        val = &A[i];
        if ( *val < maxNeg ) {
            Negs.push_back(*val);
            sort ( Negs.begin(), Negs.end(), fct_m );
            Negs.pop_back();
            maxNeg = Negs[2];
        }
        if ( *val > maxPos )  {
            Poss.push_back(*val);
            sort ( Poss.begin(), Poss.end(), fct_p );
            Poss.pop_back();
            maxPos = Poss[2];
        }
    } 

    return max ( Poss[0]*Poss[1]*Poss[2], Negs[0]*Negs[1]*Poss[0]);
}
