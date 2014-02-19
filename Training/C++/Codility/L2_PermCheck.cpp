// you can also use includes, for example:
// #include <algorithm>
#include <cmath>
int solution(vector<int> &A) {
	// write your code in C++98
	// 100% Solution
	long long NTot = 0, NTot2 = 0;
 
	for ( size_t i = 0; i < A.size(); ++i ) {
		NTot += ( long long ) ( i + 1 ) - A[i];
		NTot2 +=  ( long long ) pow( ( long long ) ( i + 1 ), 2) - ( long long ) pow( ( long long ) A[i], 2 );
	}
	if( (NTot == 0) && (NTot2 == 0) ) {
		return 1;
	}
	else {
		return 0;
	}
}
