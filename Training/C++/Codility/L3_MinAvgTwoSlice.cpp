// you can also use includes, for example:
// #include <algorithm>
int solution(vector<int> &A) {
   // write your code in C++98
   // 100% 
   int count = 0;
    float min = 100000.0;
    for ( size_t i = 1; i < A.size()-1; ++i ) {
	// simple ugly casuistic...
        if( min >  (float)(A[i-1] + A[i])/2.0 ) {
            min = (float)(A[i-1] + A[i])/2.0;
            count = i-1;
        }
        if ( min >  (float)(A[i] + A[i+1])/2.0 ) {
            min = (float)(A[i] + A[i+1])/2.0;
            count = i;
        }
        if ( min > (float)( A[i-1] + A[i] + A[i+1])/3.0 ) {
            min = (float)(A[i-1] + A[i] + A[i+1])/3.0;
            count = i-1;            
        }
    }
    return count; 
