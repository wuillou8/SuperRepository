// you can also use includes, for example:
// #include <algorithm>
int solution(vector<int> &A) {
    // write your code in C++98
    // 100% Score
    long long PNb = 0, numTot = 0;
    for (size_t i = 0; i < A.size(); ++i) {
        PNb = ++PNb - A[i];
        numTot += PNb * A[i];
    }
    if ( numTot > 1000000000) {
        return -1;
    }
    else {
        return numTot;
    }
}
