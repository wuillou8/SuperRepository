#include <L1/IO.h>

GaugeField< SUN::MatrixSU3, 4 > IO::loadILDG(std::string const &filename)
{
  static const size_t Nc = 3;
  static const size_t ComplexComps = 2;
  static const size_t Dims = 4;
  static const size_t DirSize = Nc * Nc * ComplexComps;
  static const size_t SiteSize = DirSize * Dims;

  Lime::Reader reader(filename);
  if(!reader.good())
  {
    std::cerr << "Error occured trying to open file: " << filename << std::endl;
    exit(EXIT_FAILURE);
  }

  ILDGinfo info(reader);

  reader.retrieveRecord("ildg-binary-data");
  if (reader.fail())
  {
    std::cerr << "Lime reader could not find a ildg-binary-data record in file: " << filename << std::endl;
    exit(EXIT_FAILURE);
  }
  assert(reader.good());

  Weave< 4 >::DimArray dims;
  dims << info.dims[0], info.dims[1], info.dims[2], info.dims[3]; 
  GaugeField< SUN::MatrixSU3, 4 > result(dims);

  size_t const numElems = SiteSize * result.volume();

  uint32_t *data32 = 0;
  uint64_t *data64 = 0;

  ScidacChecksum check;

  bool floatFlag = (info.precision.compare("32") == 0);
  if (floatFlag)
  {
    assert(numElems * sizeof(float) == reader.recordSize());
    data32 = new uint32_t[numElems];
    reader.read(data32, numElems);
    check.calculate(data32, SiteSize, result.volume());
  }
  else
  {
    assert(numElems * sizeof(double) == reader.recordSize());
    data64 = new uint64_t[numElems];
    reader.read(data64, numElems);
    check.calculate(data64, SiteSize, result.volume());
  }

  std::cerr << "Checksums for file " << filename << ".\n";
  std::cerr << "Calculated: " << std::hex << std::showbase << check.lower() << ' ' << check.upper() << std::dec << ".\n";

  if (reader.existsRecord("scidac-checksum"))
  {
     ScidacChecksum given;
     char checkString[256];
     reader.retrieveRecord("scidac-checksum");
     reader.read(checkString, reader.recordSize());
     given.parse(checkString);
     std::cerr << "Read:       " << std::hex << std::showbase << given.lower() << ' ' << given.upper() << std::dec << ".\n";
     if (given.checksum() == check.checksum())
       std::cerr << "Checksums match." << std::endl;
     else
       std::cerr << "*** WARNING! Checksums do not match. ***" << std::endl;
  }
  else
     std::cerr << "No Scidac checksum found in LIME file, so comparison not possible" << std::endl;

  if (!Base::bigEndian)
  {
    if (floatFlag)
      Base::swapEndian(data32, data32 + numElems, sizeof(float));
    else
      Base::swapEndian(data64, data64 + numElems, sizeof(double));
  }

  double *fieldPtrs[4];
  for (size_t dir = 0; dir < Dims; ++dir)
    fieldPtrs[dir] = reinterpret_cast< double* >(result[dir].raw());

  if (floatFlag)
  {
    float *data = reinterpret_cast< float* >(data32);
    for (size_t idx = 0; idx < result.volume(); ++idx, data += SiteSize, fieldPtrs[0] += DirSize, fieldPtrs[1] += DirSize, fieldPtrs[2] += DirSize, fieldPtrs[3] += DirSize)
    {
      std::copy(data + 0 * DirSize, data + 1 * DirSize, fieldPtrs[0]);
      std::copy(data + 1 * DirSize, data + 2 * DirSize, fieldPtrs[1]);
      std::copy(data + 2 * DirSize, data + 3 * DirSize, fieldPtrs[2]);
      std::copy(data + 3 * DirSize, data + 4 * DirSize, fieldPtrs[3]);
    }
    delete[] data32;
    return result;
  }

  double *data = reinterpret_cast< double* >(data64);
  for (size_t idx = 0; idx < result.volume(); ++idx, data += SiteSize, fieldPtrs[0] += DirSize, fieldPtrs[1] += DirSize, fieldPtrs[2] += DirSize, fieldPtrs[3] += DirSize)
  {
    std::copy(data + 0 * DirSize, data + 1 * DirSize, fieldPtrs[0]);
    std::copy(data + 1 * DirSize, data + 2 * DirSize, fieldPtrs[1]);
    std::copy(data + 2 * DirSize, data + 3 * DirSize, fieldPtrs[2]);
    std::copy(data + 3 * DirSize, data + 4 * DirSize, fieldPtrs[3]);
  }
//     Weave< 4 >::DimArray coord;
//     for (size_t t = 0; t < 8; t++) {
//       for (size_t z = 0; z < 8; z++) {
//         for (size_t y = 0; y < 8; y++) {
//           for (size_t x = 0; x < 8; x++) {
//               coord << t, z, y, x;
//               std::copy(data              , data +     DirSize, reinterpret_cast< double *>(&result[1][coord]));
//               std::copy(data +     DirSize, data + 2 * DirSize, reinterpret_cast< double *>(&result[2][coord]));
//               std::copy(data + 2 * DirSize, data + 3 * DirSize, reinterpret_cast< double *>(&result[3][coord]));
//               std::copy(data + 3 * DirSize, data + 4 * DirSize, reinterpret_cast< double *>(&result[0][coord]));
//             }
//           }
//         }
//       }
//     }

  delete[] data64;
  return result;
}
