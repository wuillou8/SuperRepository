// you can also use includes, for example:
// #include <algorithm>
int solution(vector<int> &A) {
	// write your code in C++98
	// 100% Solution
	int sum = 0;
	for (size_t i = 0; i < A.size(); ++i) {
		sum += A[i];
	}

	int min = abs(sum-2*A[0]);
	for (size_t i = 0; i < A.size()-1; ++i) {
	sum -= 2*A[i];
	if ( abs( sum ) < min ) {
		min = abs( sum );
	}

	}
	return min;
}
