#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <assert.h>
#include <map>
#include <limits>

using namespace std;

template<class K, class V>
class interval_map {
	friend void IntervalMapTest();
	private:
	std::map<K,V> m_map;

	public:
	// constructor associates whole range of K with val by inserting (K_min, val) into the map
	interval_map( V const& val) {
	m_map.insert(m_map.begin(),std::make_pair(std::numeric_limits<K>::min(),val));
	};

	// look-up of the value associated with key
	V const& operator[]( K const& key ) const {
		return ( --m_map.upper_bound(key) )->second;
	}

	// Assign function:
	// change map values within an interval defined by its boundaries
	void inline assign( K const& keyBegin, K const& keyEnd, const V& val ) {

		typename map<K,V>::iterator it;
		// I implement: assign value val to interval [keyBegin, keyEnd)
		it = m_map.find(keyEnd);
		char upperBoundVal = (--m_map.upper_bound(it->first))->second;
		// insert non specified values in the iterator at the 
		// interval boundaries, so that the iterator can be used
		it = m_map.find(keyBegin);
		if( it == m_map.end() ) {
			it = m_map.insert( std::make_pair( keyBegin, val ) ).first;
		}

		it = m_map.find(keyEnd);
		if( it == m_map.end() ) {
			it = m_map.insert( std::make_pair( keyEnd, upperBoundVal ) ).first;	
		}

		// then just iterate within the boundaries and change the values
		// this way, one simply changes m_map values.
		for (it=m_map.find(keyBegin); it!=m_map.find(keyEnd); ++it) {
			it->second = val;
		}
	}

	// create littel non-trivial <int,char> example..
	void inline genLittleExample() {
		m_map[2] = 'D';	
		m_map[4] = 'A'; 
		m_map[12] = 'C'; 
	}

};

// basical test function
void IntervalMapTest() {
	// construct an interval_map
	interval_map<int,char> test_map('A');
	// make a non-trivial example
	test_map.genLittleExample();
	// store a copy
	interval_map<int,char> test_bckup = test_map;
	
	// apply assign between fixed boundaries
	int bDown = 2;
	int bUp = 7;
	// we change the values into 'M' within the boundaries
	test_map.assign( bDown, bUp,'M');

	// basical test...
	for (int i(0); i < 100; ++i) {
		if ( !(i >= bDown && i <= bUp) ) {
			if ( !(test_map[i] == test_bckup[i]) ) {
				cout << "Test failed" << endl;
				cout << "Inegal Els: " << i << " " << test_map[i] << " " << test_bckup[i] << endl; 
	}	}	}

}

int main(int argc, char* argv[])
{
	IntervalMapTest();

return 0;	
}
