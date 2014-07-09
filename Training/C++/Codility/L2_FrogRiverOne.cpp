// you can also use includes, for example:
// #include <algorithm>
int solution(int X, vector<int> &A) {
    // write your code in C++98
    // 100% Test
    vector<int> pos;
    pos.assign(X,0);
    int Timer = 0;
    for ( size_t i = 0; i < A.size(); ++i ) {
        if(pos[ A[i]-1 ] == 0) {
            pos[ A[i]-1 ] = 1;
            ++Timer;
        }
        if ( Timer == X ) {
            return i;
        }
    }
    return -1;
}
