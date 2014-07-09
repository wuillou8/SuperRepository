// you can also use includes, for example:
// #include <algorithm>
// 100% solution
int check ( const int &var, const vector<int> &A ) {
        size_t count(0), pos(0);
        for  ( size_t i(0); i < A.size(); ++i ) {
            if ( A[i] == var ) { ++count; pos = i;}
        }
        if ( (count > (size_t)A.size()/2) ) {
            return pos;
        }
        else {
            return -1;
        }
    }

int solution(const vector<int> &A) {
    // write your code in C++98
    size_t nbDom(1), start(0);

    // empty array?
    if (A.empty()) {
        return -1;
    }
    
    int domin(A.front());
    // if uneven number of els.
    if ( A.size() % 2 != 0 ) {
        ++start;
        if ( A.size() == 1 ) {
            return 0;
        }
    }
 
    for  ( size_t i(start); i < A.size(); i+=2 ) {
 
        if ( A[i] == A[i+1] ) {
            if( A[i] == domin ) {
                ++nbDom;
            }
            else {
                --nbDom;
                if ( nbDom < 1 ) {
                    domin = A[i];
                }
            }
        }
 
    }

    return check ( domin, A );
    }
