#include <algorithm>
 
bool myfunction (int i,int j) { return (i<j); }
 
int solution(const vector<int> &A) {
// write your code in C++98
#include <algorithm>
 
bool myfunction (int i,int j) { return (i<j); }

int solution(const vector<int> &A) {
// write your code in C++98
// 100% solution
    int counter;
    if ( A.size() == 0 ) {
        return 0;
    }
    else {
        counter = 1;
    }
 
    vector<int> copy(A);
    sort ( copy.begin(), copy.end() ); //, myfunction );
    for ( size_t i = 1; i < copy.size(); ++i ) {
        if ( copy[i-1] != copy[i] ) {
            ++counter;
        } 
    }
    
    return counter;
} 

