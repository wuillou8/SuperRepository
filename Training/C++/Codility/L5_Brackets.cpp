
// you can also use includes, for example:
#include <algorithm>
int solution(const string &S) {
    // write your code in C++98
    // 50% Solution
    string cp(S);
    size_t pos = 0, marker = 0; 
    string tmp;

    int loop=0;
    do {
        pos = 0;
        marker = cp.size();
        while ( (pos+1 < cp.size()) & (cp.size() > 0) ) {
            tmp = cp.substr (pos, 2);
            if ( tmp == "()" || tmp == "{}" || tmp == "[]") {
                cp.erase(pos, 2);
                if( pos > 0) {
                    --pos;
                }
            }
            else {
                ++pos;
            }
        }
        ++loop;

    } while ( cp.size() < marker );
    
    if ( cp.size() == 0 ) {
        return 1;
    }
    else {
        return 0;
    }
    
}
