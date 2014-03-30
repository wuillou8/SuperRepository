#include <L0/SUN.h>
#include <L0/GaugeField.h>
#include <L1/Path.h>
#include <L2/Metropolis.h>

#include <iostream>

#include <L0/Base/XLat.h>
#include <L1/IO.h>
#include <L0/Base/BoxMueller.h>
#include <L0/Base/Ziggurat.h>



#define GAUGEGROUP SUN::MatrixSU3

static const size_t Dim = 4;
static const size_t Nc = 3;
static const size_t PlaqNr = Dim * (Dim - 1);

int main(int argc, char **argv)
{

for (int idx = 0; idx < 10000000; ++idx)
  {
//    std::cout /*<< idx << " "*/ << Base::BoxMueller::box_mueller(0.0, 1.0) << std::endl;
	std::cout << Base::Ziggurat::r4_exp_value ( ) << std::endl;
  }

/*  GaugeField< SUN::MatrixSU3, 4 > myField = IO::loadILDG(argv[1]);

  for (size_t idx = 0; idx < myField.volume(); ++idx)
  {
    SUN::reunitarize(myField[0][idx]);
    SUN::reunitarize(myField[1][idx]);
    SUN::reunitarize(myField[2][idx]);
    SUN::reunitarize(myField[3][idx]);
  }

  std::complex< double > plaq;
  for (size_t mu = 0; mu < 4; ++mu)
    for (size_t nu = 0; nu < 4; ++nu)
    {
      if (mu == nu)
        continue;
      plaq += plaquette(myField, mu, nu).sum().trace();
    }
  plaq /= (Nc * PlaqNr * myField.volume());

  Weave< Dim >::DimArray coord = Weave< Dim >::DimArray::Constant(0);

  std::cout << myField[0][coord] << '\n' << std::endl;
  std::cout << myField[1][coord] << '\n' << std::endl;
  std::cout << myField[2][coord] << '\n' << std::endl;
  std::cout << myField[3][coord] << '\n' <<  std::endl;

  std::cout << "Plaquette: " << plaq << std::endl;
*/
  return 0;
}
