#pragma once

# include <cstdlib>
# include <iostream>
# include <iomanip>
# include <cmath>


//////////////////////////////////////////////////////////////////////////
//  The Ziggurat algo. generates randomly 				//
//  normal distributed numbers: 					//
//  http://people.sc.fsu.edu/~jburkardt/cpp_src/ziggurat/ziggurat.html  //
//////////////////////////////////////////////////////////////////////////

namespace Base
{
class Ziggurat
{
/*  static Ziggurat *s_instance;
  public:
  static Ziggurat &instance();
    double operator()();

  ~Ranlux();*/
public:
  static double r4_exp_value ( );
  static double r4_nor_value ( );
  static double efix ( );
  static double nfix ( );

private:
//  double efix ( );
  unsigned long int jsr_value ( );
//  double nfix ( );
  void r4_exp_setup ( );
//  double r4_exp_value ( );
  void r4_nor_setup ( );
  double r4_uni_value ( );
  unsigned long int shr3_value ( );
  void timestamp ( );
  unsigned long int ul_uni_value ( );
  void zigset ( unsigned long int jsrseed );
};
}

//#include "Ziggurat/Ziggurat.inlines"

