// erasing from multiset
#include <time.h>
#include <stdio.h>
#include <cstdlib> 
#include <ctime> 
#include <iostream>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

double sum1(vector<double>& v)
{    
    if (v.empty()) {
        return 0.0;
    }
    for(size_t i = 0; i < v.size() - 1; ++i) {
        sort(v.begin()+i, v.end());
        v[i+1] += v[i];
    }
    return v.back();
}
 
double sum2(vector<double>& v)
{    
    if (v.empty()) {
        return 0.0;
    }
    for(size_t i = 0; i < v.size() - 1; ++i) {
        partial_sort(v.begin() + i, v.begin() + i + 2, v.end());
        v[i+1] += v[i];
    }
    return v.back();
}
 
double sum3(vector<double>& v)
{    
    multiset<double> set(v.begin(), v.end());
    int n = 0;
    multiset<double>::const_iterator it;
    while (set.size() > 1) {
	//for (it=set.begin(); it!=set.end(); ++it)
    	//	std::cout << ' ' << *it;
	//printf("DBG0 %d", set.size());
        /*multi*/ multiset<double>::const_iterator itA = set.begin();
        /*multi*/ multiset<double>::const_iterator itB = ++set.begin();
        double c = *itA + *itB;
        set.erase(itA, ++itB); 
        set.insert(c);
	++n;
	
	//printf("DBG0 %d\n", set.size());
	//for (it=set.begin(); it!=set.end(); ++it)
	//	std::cout << ' ' << *it;

	//exit(1);
    }
    return !set.empty() ? *set.begin() 
                        : 0.0;
}

double sum4( vector<double>& v ) {
	double sum = 0.;
	for  ( size_t i(0); i < v.size(); ++i ) {
		sum += v[i];
	}
	return sum;
}

vector<double>  createarray( int size ) {
	vector<double> array;
	for(int i=0; i<size; i++){ 
        	array.push_back( ((double) rand() / (RAND_MAX)) + 1 );
	}
	return array;
}

int main() 
{ 
 int size;
 cout<< "how big do you want the array?" << endl;
 cin >> size;

/* int array[size];*/
vector<double> array, array1;

/***********************/
clock_t start, end;

array1 = createarray( size );
array = array1;
start = clock();
cout << "sum1: " << sum1(array) << endl;
end = clock();

cout << "Time required for execution: "
	<< (double)(end-start)/CLOCKS_PER_SEC
	<< " seconds." << "\n\n";

array = array1;
start = clock();
cout << "sum2: " << sum2(array) << endl;
end = clock();

cout << "Time required for execution: "
	<< (double)(end-start)/CLOCKS_PER_SEC
	<< " seconds." << "\n\n";

array = array1;
start = clock();
cout << "sum3: " << sum3(array) << endl;
end = clock();

cout << "Time required for execution: "
	<< (double)(end-start)/CLOCKS_PER_SEC
	<< " seconds." << "\n\n";

array = array1;
start = clock();
cout << "sum4: " << sum4(array) << endl;
end = clock();

cout << "Time required for execution: "
	<< (double)(end-start)/CLOCKS_PER_SEC
	<< " seconds." << "\n\n";


   return 0;
}
