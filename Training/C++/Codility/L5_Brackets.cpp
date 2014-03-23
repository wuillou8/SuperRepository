// you can also use includes, for example:
// #include <algorithm>
int solution(const string &S) {
    // write your code in C++98
    string copy(S);
    
    int pos = 0;
    while ( copy.size() > 0 ) {
        if ( copy.substr (pos, 2) == "()" ) {
            copy.erase(pos, 2);
        }
        else {
            
        }
    }
}
