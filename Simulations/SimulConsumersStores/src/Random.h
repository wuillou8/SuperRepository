#pragma once

#include <math.h>
#include <cstdlib>
#include <stdlib.h>
#include <vector>
#include <iostream>
#include <time.h>

using namespace std;

namespace QuickRandom {

void INITQuickRandom();
double randf(double m);
size_t randi(size_t m);
double Gaussian(double m, double sigma);
double GaussianHull(double val, double m, double sigma);
double ExpLaw(double m);
float box_mueller(float m, float s);

}

/*
 * General template for the generation of random numbers of different types/length
 */
template<typename T>
class Random {
public:
	Random(std::size_t size);
	Random(std::size_t size, T range);
	Random(T range);
	virtual ~Random();
	size_t size;
	T range;
	std::vector<T> random;
};

template<typename T>
Random<T>::Random(std::size_t size, T range) :
		size(size), range(range) {
	for (std::size_t i = 0; i < size; ++i) {
		random.push_back(range * rand() / (RAND_MAX - 1.));
	}
}

template<typename T>
Random<T>::Random(size_t size) :
		size(size) {
	for (size_t i = 0; i < size; ++i) {
		random.push_back((T) rand() / (RAND_MAX - 1.));
	}
}

template<typename T>
Random<T>::Random(T range) :
		size(1), range(range) {
	random.push_back(range * rand() / (RAND_MAX - 1.));
}

template<typename T>
Random<T>::~Random() {
}
/*
struct Ranbyte {

	int s[256], i,j,ss;
	size_t v;
	Ranbyte(int u) {
		v = pow(2244614371, u);
		for (size_t i = 0; i < 256, i++) {s[i] = i;}
		for (size_t i = 0; i < 256, i++) {
			ss = s[i];
			j = ( j + ss + (v >> 24)) & 
		}
	}
};*/
