// #include <algorithm>
#include <string>
vector<int> solution(string &S, vector<int> &P, vector<int> &Q) {
    // 66 % score...    
    vector<int> fin;
    string str;
    for ( size_t i = 0; i < P.size(); ++i ) {
        
        str = S.substr(P[i],(Q[i] - P[i] + 1));
        if (str.find('A')!=string::npos) { 
            fin.push_back(1); }
        else if (str.find('C')!=string::npos) { 
            fin.push_back(2); }
        else if (str.find('G')!=string::npos) { 
            fin.push_back(3); }
        else { 
            fin.push_back(4); }
    }
    return fin;
}
