vector<int> solution(int N, vector<int> &A) {
    // write your code in C++98
    // Solution 100%
    vector<int> tmp;
    int maxVal = 0, threshold = 0;
    int * n; // no velocity gained from this pointer's manover...
    tmp.assign( N, 0 );
    for ( size_t i = 0; i < A.size(); ++i ) {
        n = &A[i];
        if( *n != (N+1) ) {
            tmp[*n-1] = max( threshold+1, ++tmp[*n-1] ); 
            maxVal = max( maxVal, tmp[*n-1] );
        }
        else { // trick...
            threshold = maxVal;
        }
    }
    for ( size_t i = 0; i < tmp.size(); ++i ) {
        tmp[i] = max( tmp[i], threshold );
    }
    return tmp;
}
