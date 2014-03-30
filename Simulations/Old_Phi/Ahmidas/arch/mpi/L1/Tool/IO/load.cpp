#include "../IO.h"

namespace Tool
{
namespace IO
{
void loadScidac(Core::Propagator *propagator, std::vector< std::string > const &filenames);
void loadScidac(Core::Propagator *propagator, std::vector< std::string > const &filenames, size_t const precision);
void loadScidac(Core::StochasticPropagator< 4 > *sPropagator, std::vector< std::string > const &filenames);
void loadScidac(Core::StochasticPropagator< 4 > *sPropagator, std::vector< std::string > const &filenames, size_t const precision);
void loadScidac(Core::StochasticPropagator< 1 > *sPropagator, std::vector< std::string > const &filenames);
void loadScidac(Core::StochasticPropagator< 1 > *sPropagator, std::vector< std::string > const &filenames, size_t const precision);

void load(Core::Field< QCD::Gauge > *field, std::string const &filename, filetype type)
{
  switch(type)
  {
  case fileILDG :
    // at current status, this will give an error message and
    // exit, since not implemented yet
    loadILDG(field, filename);
    break;
  default :
    break;
  }
}

void load(Core::Field< QCD::Spinor > *field, std::string const &filename, filetype type)
{
  switch(type)
  {
  case fileSCIDAC :
    loadScidac(field, filename);
    break;
  default :
    break;
  }
}

void load(Core::Field< QCD::Spinor > *field, std::string const &filename, filetype type, size_t const precision)
{
  switch(type)
  {
  case fileSCIDAC :
    loadScidac(field, filename, precision);
    break;
  default :
    break;
  }
}

void load(Core::Propagator *propagator, std::vector< std::string> const &filenames, filetype type)
{
  switch(type)
  {
  case fileSCIDAC :
    loadScidac(propagator, filenames);
    break;
  default :
    break;
  }
}

void load(Core::Propagator *propagator, std::vector< std::string> const &filenames, filetype type, size_t const precision)
{
  switch(type)
  {
  case fileSCIDAC :
    loadScidac(propagator, filenames, precision);
    break;
  default :
    break;
  }
}


void load(Core::StochasticPropagator< 4 > *sPropagator, std::vector< std::string> const &filenames, filetype type)
{
  switch(type)
  {
  case fileSCIDAC :
    loadScidac(sPropagator, filenames);
    break;
  default :
    break;
  }
}

void load(Core::StochasticPropagator< 4 > *sPropagator, std::vector< std::string> const &filenames, filetype type, size_t const precision)
{
  switch(type)
  {
  case fileSCIDAC :
    loadScidac(sPropagator, filenames, precision);
    break;
  default :
    break;
  }
}

void load(Core::StochasticPropagator< 1 > *sPropagator, std::vector< std::string> const &filenames, filetype type)
{
  switch(type)
  {
  case fileSCIDAC :
    loadScidac(sPropagator, filenames);
    break;
  default :
    break;
  }
}

void load(Core::StochasticPropagator< 1 > *sPropagator, std::vector< std::string> const &filenames, filetype type, size_t const precision)
{
  switch(type)
  {
  case fileSCIDAC :
    loadScidac(sPropagator, filenames, precision);
    break;
  default :
    break;
  }
}

// a lot of data is copied back and forth - this has to be reviewed if more efficiency is desired
void loadScidac(Core::Propagator *propagator, std::vector< std::string> const &filenames)
{
  // would like to do this, but isolate is private
  // propagator->isolate();

  if (filenames.size() == 12)
  {
    Core::Field< QCD::Spinor > tmp [12] =
    {
      Core::Field< QCD::Spinor > (propagator->L(), propagator->T()),
      Core::Field< QCD::Spinor > (propagator->L(), propagator->T()),
      Core::Field< QCD::Spinor > (propagator->L(), propagator->T()),
      Core::Field< QCD::Spinor > (propagator->L(), propagator->T()),
      Core::Field< QCD::Spinor > (propagator->L(), propagator->T()),
      Core::Field< QCD::Spinor > (propagator->L(), propagator->T()),
      Core::Field< QCD::Spinor > (propagator->L(), propagator->T()),
      Core::Field< QCD::Spinor > (propagator->L(), propagator->T()),
      Core::Field< QCD::Spinor > (propagator->L(), propagator->T()),
      Core::Field< QCD::Spinor > (propagator->L(), propagator->T()),
      Core::Field< QCD::Spinor > (propagator->L(), propagator->T()),
      Core::Field< QCD::Spinor > (propagator->L(), propagator->T())
    };

    for (size_t i=0; i<12; i++)
    {
      Tool::IO::load(tmp+i,filenames[i], Tool::IO::fileSCIDAC);
    }

    Core::Propagator::iterator itTensor = propagator->begin();
    Core::Field< QCD::Spinor >::iterator itsSpinor [12] =
    {
      tmp[ 0].begin(),tmp[ 1].begin(),tmp[ 2].begin(),
      tmp[ 3].begin(),tmp[ 4].begin(),tmp[ 5].begin(),
      tmp[ 6].begin(),tmp[ 7].begin(),tmp[ 8].begin(),
      tmp[ 9].begin(),tmp[10].begin(),tmp[11].begin()
    };

    QCD::Spinor **spinors = new QCD::Spinor *[12];
    for (size_t i=0; i<12; i++)
      spinors[i] = NULL;

    // would like to see for loop here
    // but postfix Field::iterator operator++(int) is not implemented yet
    while (itTensor != propagator->end())
    {
      for (size_t i=0; i<12; i++)
      {
        spinors[i] = new QCD::Spinor(*(itsSpinor[i]));
        ++(itsSpinor[i]);
      }
      (*itTensor) = QCD::Tensor(spinors);
      for (size_t i=0; i<12; i++)
      {
        delete spinors[i];
      }
      ++itTensor;
    }

    delete [] spinors;

  }
  else
  {
    std::cerr << "Error in void Tool::IO::loadScidac(Core::Propagator *, std::vector< std::string> const &):"
              << std::endl;
    std::cerr << "filenames.size() should be 12" << std::endl;
    exit(1);
  }
}


// a lot of data is copied back and forth - this has to be reviewed if more efficiency is desired
void loadScidac(Core::Propagator *propagator, std::vector< std::string> const &filenames, size_t const precision)
{
  // would like to do this, but isolate is private
  // propagator->isolate();

  if (filenames.size() == 12)
  {
    Core::Field< QCD::Spinor > tmp [12] =
    {
      Core::Field< QCD::Spinor > (propagator->L(), propagator->T()),
      Core::Field< QCD::Spinor > (propagator->L(), propagator->T()),
      Core::Field< QCD::Spinor > (propagator->L(), propagator->T()),
      Core::Field< QCD::Spinor > (propagator->L(), propagator->T()),
      Core::Field< QCD::Spinor > (propagator->L(), propagator->T()),
      Core::Field< QCD::Spinor > (propagator->L(), propagator->T()),
      Core::Field< QCD::Spinor > (propagator->L(), propagator->T()),
      Core::Field< QCD::Spinor > (propagator->L(), propagator->T()),
      Core::Field< QCD::Spinor > (propagator->L(), propagator->T()),
      Core::Field< QCD::Spinor > (propagator->L(), propagator->T()),
      Core::Field< QCD::Spinor > (propagator->L(), propagator->T()),
      Core::Field< QCD::Spinor > (propagator->L(), propagator->T())
    };

    for (size_t i=0; i<12; i++)
    {
      Tool::IO::load(tmp+i,filenames[i], Tool::IO::fileSCIDAC, precision);
    }

    Core::Propagator::iterator itTensor = propagator->begin();
    Core::Field< QCD::Spinor >::iterator itsSpinor [12] =
    {
      tmp[ 0].begin(),tmp[ 1].begin(),tmp[ 2].begin(),
      tmp[ 3].begin(),tmp[ 4].begin(),tmp[ 5].begin(),
      tmp[ 6].begin(),tmp[ 7].begin(),tmp[ 8].begin(),
      tmp[ 9].begin(),tmp[10].begin(),tmp[11].begin()
    };

    QCD::Spinor **spinors = new QCD::Spinor *[12];
    for (size_t i=0; i<12; i++)
      spinors[i] = NULL;

    // would like to see for loop here
    // but postfix Field::iterator operator++(int) is not implemented yet
    while (itTensor != propagator->end())
    {
      for (size_t i=0; i<12; i++)
      {
        spinors[i] = new QCD::Spinor(*(itsSpinor[i]));
        ++(itsSpinor[i]);
      }
      (*itTensor) = QCD::Tensor(spinors);
      for (size_t i=0; i<12; i++)
      {
        delete spinors[i];
      }
      ++itTensor;
    }

    delete [] spinors;

  }
  else
  {
    std::cerr << "Error in void Tool::IO::loadScidac(Core::Propagator *, std::vector< std::string> const &):"
              << std::endl;
    std::cerr << "filenames.size() should be 12" << std::endl;
    exit(1);
  }
}



void loadScidac(Core::StochasticPropagator< 4 > *sPropagator, std::vector< std::string> const &filenames)
{
  QCD::Spinor dummy;
  dummy.setToZero();

  if (filenames.size() == 4)
  {
    Core::Field< QCD::Spinor > tmp [4] =
    {
      Core::Field< QCD::Spinor > (sPropagator->L(), sPropagator->T()),
      Core::Field< QCD::Spinor > (sPropagator->L(), sPropagator->T()),
      Core::Field< QCD::Spinor > (sPropagator->L(), sPropagator->T()),
      Core::Field< QCD::Spinor > (sPropagator->L(), sPropagator->T())
    };

    for (size_t i=0; i<4; i++)
    {
      Tool::IO::load(tmp+i,filenames[i], Tool::IO::fileSCIDAC);
    }

    Core::Propagator::iterator itTensor = sPropagator->begin();
    Core::Field< QCD::Spinor >::iterator itsSpinor [4] =
    {
      tmp[0].begin(), tmp[1].begin(), tmp[2].begin(), tmp[3].begin()
    };

    QCD::Spinor **spinors = new QCD::Spinor *[12];
    for (size_t i=0; i<12; i+=3)
      spinors[i] = NULL;

    spinors[ 1] = new QCD::Spinor(dummy);
    spinors[ 2] = new QCD::Spinor(dummy);
    spinors[ 4] = new QCD::Spinor(dummy);
    spinors[ 5] = new QCD::Spinor(dummy);
    spinors[ 7] = new QCD::Spinor(dummy);
    spinors[ 8] = new QCD::Spinor(dummy);
    spinors[10] = new QCD::Spinor(dummy);
    spinors[11] = new QCD::Spinor(dummy);

    while (itTensor != sPropagator->end())
    {
      for (size_t i=0; i<4; i++)
      {
        spinors[i*3] = new QCD::Spinor(*(itsSpinor[i]));
        ++(itsSpinor[i]);
      }
      (*itTensor) = QCD::Tensor(spinors);
      for (size_t i=0; i<4; i++)
      {
        delete spinors[i*3];
      }
      ++itTensor;
    }

    delete spinors[ 1];
    delete spinors[ 2];
    delete spinors[ 4];
    delete spinors[ 5];
    delete spinors[ 7];
    delete spinors[ 8];
    delete spinors[10];
    delete spinors[11];

    delete [] spinors;

  }
  else
  {
    std::cerr << "Error in void Tool::IO::loadScidac(Core::StochasticsPropagator< 4 > *, std::vector< std::string> const &):"
              << std::endl;
    std::cerr << "filenames.size() should be 4" << std::endl;
    exit(1);
  }
}

void loadScidac(Core::StochasticPropagator< 4 > *sPropagator, std::vector< std::string> const &filenames, size_t const precision)
{
  QCD::Spinor dummy;
  dummy.setToZero();

  if (filenames.size() == 4)
  {
    Core::Field< QCD::Spinor > tmp [4] =
    {
      Core::Field< QCD::Spinor > (sPropagator->L(), sPropagator->T()),
      Core::Field< QCD::Spinor > (sPropagator->L(), sPropagator->T()),
      Core::Field< QCD::Spinor > (sPropagator->L(), sPropagator->T()),
      Core::Field< QCD::Spinor > (sPropagator->L(), sPropagator->T())
    };

    for (size_t i=0; i<4; i++)
    {
      Tool::IO::load(tmp+i,filenames[i], Tool::IO::fileSCIDAC, precision);
    }

    Core::Propagator::iterator itTensor = sPropagator->begin();
    Core::Field< QCD::Spinor >::iterator itsSpinor [4] =
    {
      tmp[0].begin(), tmp[1].begin(), tmp[2].begin(), tmp[3].begin()
    };

    QCD::Spinor **spinors = new QCD::Spinor *[12];
    for (size_t i=0; i<12; i+=3)
      spinors[i] = NULL;

    spinors[ 1] = new QCD::Spinor(dummy);
    spinors[ 2] = new QCD::Spinor(dummy);
    spinors[ 4] = new QCD::Spinor(dummy);
    spinors[ 5] = new QCD::Spinor(dummy);
    spinors[ 7] = new QCD::Spinor(dummy);
    spinors[ 8] = new QCD::Spinor(dummy);
    spinors[10] = new QCD::Spinor(dummy);
    spinors[11] = new QCD::Spinor(dummy);

    while (itTensor != sPropagator->end())
    {
      for (size_t i=0; i<4; i++)
      {
        spinors[i*3] = new QCD::Spinor(*(itsSpinor[i]));
        ++(itsSpinor[i]);
      }
      (*itTensor) = QCD::Tensor(spinors);
      for (size_t i=0; i<4; i++)
      {
        delete spinors[i*3];
      }
      ++itTensor;
    }

    delete spinors[ 1];
    delete spinors[ 2];
    delete spinors[ 4];
    delete spinors[ 5];
    delete spinors[ 7];
    delete spinors[ 8];
    delete spinors[10];
    delete spinors[11];

    delete [] spinors;

  }
  else
  {
    std::cerr << "Error in void Tool::IO::loadScidac(Core::StochasticsPropagator< 4 > *, std::vector< std::string> const &):"
              << std::endl;
    std::cerr << "filenames.size() should be 4" << std::endl;
    exit(1);
  }
}
}
}

void Tool::IO::loadScidac(Core::StochasticPropagator< 1 > *sPropagator, std::vector< std::string> const &filenames)
{
  QCD::Spinor dummy;
  dummy.setToZero();

  if (filenames.size() == 1)
  {
    Core::Field< QCD::Spinor > tmp (sPropagator->L(), sPropagator->T());

    Tool::IO::load(&tmp, filenames[0], Tool::IO::fileSCIDAC);

    Core::Propagator::iterator itTensor = sPropagator->begin();
    Core::Field< QCD::Spinor >::iterator itsSpinor = tmp.begin();

    QCD::Spinor **spinors = new QCD::Spinor *[12];

    spinors[0] = NULL;

    spinors[ 1] = new QCD::Spinor(dummy);
    spinors[ 2] = new QCD::Spinor(dummy);
    spinors[ 3] = new QCD::Spinor(dummy);
    spinors[ 4] = new QCD::Spinor(dummy);
    spinors[ 5] = new QCD::Spinor(dummy);
    spinors[ 6] = new QCD::Spinor(dummy);
    spinors[ 7] = new QCD::Spinor(dummy);
    spinors[ 8] = new QCD::Spinor(dummy);
    spinors[ 9] = new QCD::Spinor(dummy);
    spinors[10] = new QCD::Spinor(dummy);
    spinors[11] = new QCD::Spinor(dummy);

    while (itTensor != sPropagator->end())
    {
      spinors[0] = new QCD::Spinor(*itsSpinor);
      ++itsSpinor;
      (*itTensor) = QCD::Tensor(spinors);
      delete spinors[0];
      ++itTensor;
    }

    delete spinors[ 1];
    delete spinors[ 2];
    delete spinors[ 3];
    delete spinors[ 4];
    delete spinors[ 5];
    delete spinors[ 6];
    delete spinors[ 7];
    delete spinors[ 8];
    delete spinors[ 9];
    delete spinors[10];
    delete spinors[11];

    delete [] spinors;

  }
  else
  {
    std::cerr << "Error in void Tool::IO::loadScidac(Core::StochasticsPropagator< 4 > *, std::vector< std::string> const &):"
              << std::endl;
    std::cerr << "filenames.size() should be 1" << std::endl;
    exit(1);
  }
}



void Tool::IO::loadScidac(Core::StochasticPropagator< 1 > *sPropagator, std::vector< std::string> const &filenames, size_t const precision)
{
  QCD::Spinor dummy;
  dummy.setToZero();

  if (filenames.size() == 1)
  {
    Core::Field< QCD::Spinor > tmp (sPropagator->L(), sPropagator->T());

    Tool::IO::load(&tmp, filenames[0], Tool::IO::fileSCIDAC, precision);

    Core::Propagator::iterator itTensor = sPropagator->begin();
    Core::Field< QCD::Spinor >::iterator itsSpinor = tmp.begin();

    QCD::Spinor **spinors = new QCD::Spinor *[12];

    spinors[0] = NULL;

    spinors[ 1] = new QCD::Spinor(dummy);
    spinors[ 2] = new QCD::Spinor(dummy);
    spinors[ 3] = new QCD::Spinor(dummy);
    spinors[ 4] = new QCD::Spinor(dummy);
    spinors[ 5] = new QCD::Spinor(dummy);
    spinors[ 6] = new QCD::Spinor(dummy);
    spinors[ 7] = new QCD::Spinor(dummy);
    spinors[ 8] = new QCD::Spinor(dummy);
    spinors[ 9] = new QCD::Spinor(dummy);
    spinors[10] = new QCD::Spinor(dummy);
    spinors[11] = new QCD::Spinor(dummy);

    while (itTensor != sPropagator->end())
    {
      spinors[0] = new QCD::Spinor(*itsSpinor);
      ++itsSpinor;
      (*itTensor) = QCD::Tensor(spinors);
      delete spinors[0];
      ++itTensor;
    }

    delete spinors[ 1];
    delete spinors[ 2];
    delete spinors[ 3];
    delete spinors[ 4];
    delete spinors[ 5];
    delete spinors[ 6];
    delete spinors[ 7];
    delete spinors[ 8];
    delete spinors[ 9];
    delete spinors[10];
    delete spinors[11];

    delete [] spinors;

  }
  else
  {
    std::cerr << "Error in void Tool::IO::loadScidac(Core::StochasticsPropagator< 4 > *, std::vector< std::string> const &):"
              << std::endl;
    std::cerr << "filenames.size() should be 1" << std::endl;
    exit(1);
  }
}
