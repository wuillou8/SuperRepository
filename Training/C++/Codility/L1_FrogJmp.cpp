
// you can also use includes, for example:
// #include <algorithm>
int solution(int X, int Y, int D) {
	// write your code in C++98
	// 100% Solution
	long long rel = (long long) Y - X;
	long long jumpNb = ( long long) rel / D;
	long long mod = ( long long ) rel % D;
	if ( mod > 0 ) {
		return jumpNb + 1;
	}
	else {
		return jumpNb;
	}
}

