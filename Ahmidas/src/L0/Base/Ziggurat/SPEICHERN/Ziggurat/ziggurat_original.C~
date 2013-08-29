# include <cstdlib>
# include <iostream>
# include <iomanip>
# include <cmath>

using namespace std;

# include "ziggurat_original.H"

static float fe[256];
static float fn[128];
static long int hz;
static unsigned long int iz;
static unsigned long int jsr = 123456789;
static unsigned long int jz;
static unsigned int ke[256];
static unsigned int kn[128];
static float we[256];
static float wn[128];

# define SHR3 ( jz=jsr, jsr^=(jsr<<13), jsr^=(jsr>>17), jsr^=(jsr<<5), jz+jsr )
# define UNI ( 0.5 + ( signed ) SHR3 * 0.2328306e-09 )
# define IUNI SHR3
# define RNOR ( hz=SHR3, iz=hz&127, ( fabs(hz)<kn[iz]) ? hz*wn[iz] : nfix() )
# define REXP ( jz=SHR3, iz=jz&255, (      jz <ke[iz]) ? jz*we[iz] : efix() )

//****************************************************************************80

float efix ( void )

//****************************************************************************80
//
//  Purpose:
//
//    EFIX generates variates when rejection occurs in the exponential code. 
//
//  Discussion:
//
//    This routine is NOT designed for direct calls by the user!
//
//  Modified:
//
//    01 May 2008
//
//  Author:
//
//    Original C version by George Marsaglia, Wai Wan Tsang.
//    C++ version by John Burkardt.
//
//  Reference:
//
//    George Marsaglia, Wai Wan Tsang,
//    The Ziggurat Method for Generating Random Variables,
//    Journal of Statistical Software,
//    Volume 5, Number 8, October 2000, seven pages.
//
//  Parameters:
//
//    Output, float EFIX, an exponential variate.
//
{ 
  float x;

  for ( ; ; ) 
  {
//
//  IZ = 0.
//
    if ( iz == 0 )
    {
      return ( 7.69711 - log ( UNI ) );
    }

    x = jz * we[iz];
    if ( fe[iz] + UNI * ( fe[iz-1] - fe[iz] ) < exp ( - x ) ) 
    {
      return x;
    }
// 
//  Initiate, try to exit the loop.
//
    jz = SHR3;
    iz = ( jz & 255 );
    if ( jz < ke[iz] ) 
    {
      return ( jz * we[iz] );
    }
  }
}
//****************************************************************************80

unsigned long int jsr_value ( void )

//****************************************************************************80
//
//  Purpose:
//
//    JSR_VALUE returns the value of the current internal seed.
//
//  Discussion:
//
//    This function provides access to the internal random number seed used
//    by the SHR3 generator.
//
//  Modified:
//
//    01 May 2008
//
//  Author:
//
//    Original C version by George Marsaglia, Wai Wan Tsang.
//    C++ version by John Burkardt.
//
//  Reference:
//
//    George Marsaglia, Wai Wan Tsang,
//    The Ziggurat Method for Generating Random Variables,
//    Journal of Statistical Software,
//    Volume 5, Number 8, October 2000, seven pages.
//
//  Parameters:
//
//    Output, unsigned long int JSR_VALUE, the current value of the seed
//    used by the SHR3 generator.
//
{
  return jsr;
}
//****************************************************************************80

float nfix ( void )

//****************************************************************************80
//
//  Purpose:
// 
//    NFIX generates variates when rejection occurs in the normal code.
//
//  Discussion:
//
//    This routine is NOT designed for direct calls by the user!
//
//  Modified:
//
//    01 May 2008
//
//  Author:
//
//    Original C version by George Marsaglia, Wai Wan Tsang.
//    C++ version by John Burkardt.
//
//  Reference:
//
//    George Marsaglia, Wai Wan Tsang,
//    The Ziggurat Method for Generating Random Variables,
//    Journal of Statistical Software,
//    Volume 5, Number 8, October 2000, seven pages.
//
//  Parameters:
//
//    Output, float NFIX, a normal variate.
//
{
  const float r = 3.442620;
  static float x;
  static float y;

  for ( ; ; )
  {
//
//  IZ = 0 handles the base strip.
//
    x = hz * wn[iz];
    if ( iz == 0 )
    { 
      do
      {
        x = - log ( UNI ) * 0.2904764; 
        y = - log ( UNI );
      }
      while ( y + y < x * x );

      return ( 0 < hz ) ? r + x : - r - x;
    }
// 
//  0 < IZ, handle the wedges of other strips.
//
    if ( fn[iz] + UNI * ( fn[iz-1] - fn[iz] ) < exp ( - 0.5 * x * x ) ) 
    {
      return x;
    }
// 
//  Initiate, try to exit the loop.
//
    hz = SHR3;
    iz = ( hz & 127 );
    if ( fabs ( hz ) < kn[iz] )
    {
      return ( hz * wn[iz] );
    }
  }
}
//****************************************************************************80

void r4_exp_setup ( void )

//****************************************************************************80
//
//  Purpose:
//
//    R4_EXP_SETUP sets data needed by R4_EXP.
//
//  Modified:
//
//    20 May 2008
//
//  Author:
//
//    Original C version by George Marsaglia, Wai Wan Tsang.
//    C++ version by John Burkardt.
//
//  Reference:
//
//    George Marsaglia, Wai Wan Tsang,
//    The Ziggurat Method for Generating Random Variables,
//    Journal of Statistical Software,
//    Volume 5, Number 8, October 2000, seven pages.
//
//  Parameters:
//
//    Global, unsigned int KE[256], data needed by R4_EXP.
//
//    Global, float FE[256], WE[256], data needed by R4_EXP.
//
{
  double de = 7.697117470131487;
  int i;
  const double m2 = 4294967296.0;
  double q;
  double te = 7.697117470131487;
  double ve = 3.949659822581572e-03;

  q = ve / exp ( - de );
  ke[0] = ( de / q ) * m2;
  ke[1] = 0;

  we[0] = q / m2;
  we[255] = de / m2;

  fe[0] = 1.0;
  fe[255] = exp ( - de );

  for ( i = 254; 1 <= i; i-- )
  {
    de = - log ( ve / de + exp ( - de ) );
    ke[i+1] = ( de / te ) * m2;
    te = de;
    fe[i] = exp ( - de );
    we[i] = de / m2;
  }
  return;
}
//****************************************************************************80

float r4_exp_value ( void )

//****************************************************************************80
//
//  Purpose:
//
//    R4_EXP_VALUE returns an exponentially distributed float.
//
//  Discussion:
//
//    The value returned is generated from a distribution on [0,+00) with density 
//    exp(-x).
//
//    The underlying algorithm is the ziggurat method.
//
//    Before calling this function, the user must call ZIGSET, supplying
//    a nonzero seed.
//
//  Modified:
//
//    01 May 2008
//
//  Author:
//
//    Original C version by George Marsaglia, Wai Wan Tsang.
//    C++ version by John Burkardt.
//
//  Reference:
//
//    George Marsaglia, Wai Wan Tsang,
//    The Ziggurat Method for Generating Random Variables,
//    Journal of Statistical Software,
//    Volume 5, Number 8, October 2000, seven pages.
//
//  Parameters:
//
//    Output, float R4_EXP_VALUE, an exponentially distributed random value.
//
{
  return REXP;
}
//****************************************************************************80

void r4_nor_setup ( void )

//****************************************************************************80
//
//  Purpose:
//
//    R4_NOR_SETUP sets data needed by R4_NOR.
//
//  Modified:
//
//    20 May 2008
//
//  Author:
//
//    Original C version by George Marsaglia, Wai Wan Tsang.
//    C++ version by John Burkardt.
//
//  Reference:
//
//    George Marsaglia, Wai Wan Tsang,
//    The Ziggurat Method for Generating Random Variables,
//    Journal of Statistical Software,
//    Volume 5, Number 8, October 2000, seven pages.
//
//  Parameters:
//
//    Global, unsigned int KN[128], data needed by R4_NOR.
//
//    Global, float FN[128], WN[128], data needed by R4_NOR.
//
{
  double dn = 3.442619855899;
  int i;
  const double m1 = 2147483648.0;
  double q;
  double tn = 3.442619855899;
  double vn = 9.91256303526217e-03;

  q = vn / exp ( - 0.5 * dn * dn );
  kn[0] = ( dn / q ) * m1;
  kn[1] = 0;

  wn[0] = q / m1;
  wn[127] = dn / m1;

  fn[0] = 1.0;
  fn[127] = exp ( - 0.5 * dn * dn );

  for ( i = 126; 1 <= i; i-- )
  {
    dn = sqrt ( - 2.0 * log ( vn / dn + exp ( - 0.5 * dn * dn ) ) );
    kn[i+1] = ( dn / tn ) * m1;
    tn = dn;
    fn[i] = exp ( - 0.5 * dn * dn );
    wn[i] = dn / m1;
  }
  return;
}
//****************************************************************************80

float r4_nor_value ( void )

//****************************************************************************80
//
//  Purpose:
//
//    R4_NOR_VALUE returns a normally distributed float.
//
//  Discussion:
//
//    The value returned is generated from a distribution with mean 0 and 
//    variance 1.
//
//    The underlying algorithm is the ziggurat method.
//
//    Before calling this function, the user must call ZIGSET, supplying
//    a nonzero seed.
//
//  Modified:
//
//    01 May 2008
//
//  Author:
//
//    Original C version by George Marsaglia, Wai Wan Tsang.
//    C++ version by John Burkardt.
//
//  Reference:
//
//    George Marsaglia, Wai Wan Tsang,
//    The Ziggurat Method for Generating Random Variables,
//    Journal of Statistical Software,
//    Volume 5, Number 8, October 2000, seven pages.
//
//  Parameters:
//
//    Output, float R4_NOR_VALUE, a normally distributed random value.
//
{
  return RNOR;
}
//****************************************************************************80

float r4_uni_value ( void )

//****************************************************************************80
//
//  Purpose:
//
//    R4_UNI_VALUE returns a uniformly distributed float.
//
//  Discussion:
//
//    Before calling this function, the user may call ZIGSET, supplying
//    a nonzero seed.
//
//  Modified:
//
//    20 May 2008
//
//  Author:
//
//    Original C version by George Marsaglia, Wai Wan Tsang.
//    C++ version by John Burkardt.
//
//  Reference:
//
//    George Marsaglia, Wai Wan Tsang,
//    The Ziggurat Method for Generating Random Variables,
//    Journal of Statistical Software,
//    Volume 5, Number 8, October 2000, seven pages.
//
//  Parameters:
//
//    Output, float R4_UNI_VALUE, a uniformly distributed random value in
//    the range [0,1].
//
{
  float value;

  jz = jsr;

  jsr = jsr ^ ( jsr << 13 );
  jsr = jsr ^ ( jsr >> 17 );
  jsr = jsr ^ ( jsr <<  5 );

  value = 0.5 + ( signed ) ( jz + jsr ) * 0.2328306e-09;

  return value;
}
//****************************************************************************80

unsigned long int shr3_value ( void )

//****************************************************************************80
//
//  Purpose:
//
//    SHR3_VALUE evaluates the SHR3 generator for unsigned long ints.
//
//  Discussion:
//
//    Before calling this function, the user may call ZIGSET, supplying
//    a nonzero seed.
//
//  Modified:
//
//    01 May 2008
//
//  Author:
//
//    Original C version by George Marsaglia, Wai Wan Tsang.
//    C++ version by John Burkardt.
//
//  Reference:
//
//    George Marsaglia, Wai Wan Tsang,
//    The Ziggurat Method for Generating Random Variables,
//    Journal of Statistical Software,
//    Volume 5, Number 8, October 2000, seven pages.
//
//  Parameters:
//
//    Output, unsigned long int SHR3_VALUE, the value of the SHR3 generator.
//
{
  return SHR3;
}
//****************************************************************************80

void timestamp ( void )

//****************************************************************************80
//
//  Purpose:
//
//    TIMESTAMP prints the current YMDHMS date as a time stamp.
//
//  Example:
//
//    31 May 2001 09:45:54 AM
//
//  Modified:
//
//    24 September 2003
//
//  Author:
//
//    John Burkardt
//
//  Parameters:
//
//    None
//
{
# define TIME_SIZE 40

  static char time_buffer[TIME_SIZE];
  const struct tm *tm;
  size_t len;
  time_t now;

  now = time ( NULL );
  tm = localtime ( &now );

  len = strftime ( time_buffer, TIME_SIZE, "%d %B %Y %I:%M:%S %p", tm );

  cout << time_buffer << "\n";

  return;
# undef TIME_SIZE
}
//****************************************************************************80

unsigned long int ul_uni_value ( void )

//****************************************************************************80
//
//  Purpose:
//
//    UL_UNI_VALUE returns a uniformly distributed unsigned long int.
//
//  Discussion:
//
//    This function provides a functional interface to the inline SHR3
//    generator.
//
//  Modified:
//
//    01 May 2008
//
//  Author:
//
//    Original C version by George Marsaglia, Wai Wan Tsang.
//    C++ version by John Burkardt.
//
//  Reference:
//
//    George Marsaglia, Wai Wan Tsang,
//    The Ziggurat Method for Generating Random Variables,
//    Journal of Statistical Software,
//    Volume 5, Number 8, October 2000, seven pages.
//
//  Parameters:
//
//    Output, unsigned long int UL_UNI_VALUE, the randomly chosen value.
//
{
  return SHR3;
}
//****************************************************************************80

void zigset ( unsigned long int jsrseed )

//****************************************************************************80
//
//  Purpose:
//
//    ZIGSET sets the seed and creates the tables for the Ziggurat method.
//
//  Discussion:
//
//    ZIGSET must be called before the exponential and normal random number
//    generators are called.
//
//  Modified:
//
//    20 May 2008
//
//  Author:
//
//    Original C version by George Marsaglia, Wai Wan Tsang.
//    C++ version by John Burkardt.
//
//  Reference:
//
//    George Marsaglia, Wai Wan Tsang,
//    The Ziggurat Method for Generating Random Variables,
//    Journal of Statistical Software,
//    Volume 5, Number 8, October 2000, seven pages.
//
//  Parameters:
//
//    Input, unsigned long int JSRSEED, the new seed for the generator.
//    JRSEED should not be zero.
//
{
  jsr = jsrseed;
//
//  Set up the tables for the normal random number generator.
//
  r4_nor_setup ( );
//
//  Set up tables for the exponential random number generator.
//
  r4_exp_setup ( );

  return;
}
