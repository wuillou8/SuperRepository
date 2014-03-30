#pragma once

#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>
#include <stdlib.h>

#include "World.h"

using namespace std;

namespace IO {
ifstream& ReadIn( ifstream& myfile );
template<typename T>
void PrintOut(T bla);

void printheaderDBCustomers( ofstream& ostream );
void printheaderDBstores( ofstream& ostream );
}

/*
http://www.cprogramming.com/tutorial/cpreprocessor.html

String-izing Tokens
Another potentially useful macro option is to turn a token into a string containing the literal text of the token. This might be useful for printing out the token. The syntax is simple--simply prefix the token with a pound sign (#).

#define PRINT_TOKEN(token) printf(#token " is %d", token)

For instance, PRINT_TOKEN(foo) would expand to

printf("<foo>" " is %d" <foo>)

(Note that in C, string literals next to each other are concatenated, so something like "token" " is " " this " will effectively become "token is this". This can be useful for formatting printf statements.)

For instance, you might use it to print the value of an expression as well as the expression itself (for debugging purposes).

PRINT_TOKEN(x + y);
*/
