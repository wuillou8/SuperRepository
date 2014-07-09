#include "../IO.h"

namespace Tool
{
namespace IO
{
void saveScidac(Core::Propagator *propagator, std::vector< std::string > const &filenames);
void saveScidac(Core::StochasticPropagator< 4 > *spropagator, std::vector< std::string > const &filenames);
void saveScidac(Core::StochasticPropagator< 1 > *spropagator, std::vector< std::string > const &filenames);
}
}


void Tool::IO::save(Core::Field< QCD::Gauge > *field, std::string const &filename, filetype type)
{
  switch(type)
  {
  case fileILDG :
    // at current status, this will give an error message and
    // exit, since not implemented yet
    saveILDG(*field, filename);
    break;
  default :
    break;
  }
}

void Tool::IO::save(Core::Field< QCD::Spinor > *field, std::string const &filename, filetype type)
{
  switch(type)
  {
  case fileSCIDAC :
    saveScidac(*field, filename);
    break;
  default :
    break;
  }
}

void Tool::IO::save(Core::Propagator *propagator, std::vector< std::string> const &filenames, filetype type)
{
  switch(type)
  {
  case fileSCIDAC :
    saveScidac(propagator, filenames);
    break;
  default :
    break;
  }
}

void Tool::IO::save(Core::StochasticPropagator< 4 > *sPropagator, std::vector< std::string> const &filenames, filetype type)
{
  switch(type)
  {
  case fileSCIDAC :
    saveScidac(sPropagator, filenames);
    break;
  default :
    break;
  }
}

void Tool::IO::save(Core::StochasticPropagator< 1 > *sPropagator, std::vector< std::string> const &filenames, filetype type)
{
  switch(type)
  {
  case fileSCIDAC :
    saveScidac(sPropagator, filenames);
    break;
  default :
    break;
  }
}


// a lot of data is copied back and forth - this has to be reviewed if more efficiency is desired
void Tool::IO::saveScidac(Core::Propagator *propagator, std::vector< std::string> const &filenames)
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
        (*(itsSpinor[i])) = (*itTensor)[i];
        ++(itsSpinor[i]);
      }
      ++itTensor;
    }

    for (size_t i=0; i<12; i++)
    {
      Tool::IO::save(tmp+i, filenames[i], Tool::IO::fileSCIDAC);
    }

  }
  else
  {
    std::cerr << "Error in void Tool::IO::loadScidac(Core::Propagator *, std::vector< std::string> const &):"
              << std::endl;
    std::cerr << "filenames.size() should be 12" << std::endl;
    exit(1);
  }
}


void Tool::IO::saveScidac(Core::StochasticPropagator<4> *spropagator, std::vector< std::string> const &filenames)
{
  // would like to do this, but isolate is private
  // propagator->isolate();

  if (filenames.size() == 4)
  {
    Core::Field< QCD::Spinor > tmp [4] =
    {
      Core::Field< QCD::Spinor > (spropagator->L(), spropagator->T()),
      Core::Field< QCD::Spinor > (spropagator->L(), spropagator->T()),
      Core::Field< QCD::Spinor > (spropagator->L(), spropagator->T()),
      Core::Field< QCD::Spinor > (spropagator->L(), spropagator->T()),
    };

    Core::StochasticPropagator<4>::iterator itTensor = spropagator->begin();
    Core::Field< QCD::Spinor >::iterator itsSpinor [4] =
    {
      tmp[ 0].begin(),tmp[ 1].begin(),tmp[ 2].begin(),tmp[ 3].begin()
    };

    QCD::Spinor **spinors = new QCD::Spinor *[4];
    for (size_t i=0; i<4; i++)
      spinors[i] = NULL;

    // would like to see for loop here
    // but postfix Field::iterator operator++(int) is not implemented yet
    while (itTensor != spropagator->end())
    {
      for (size_t i=0; i<4; i++)
      {
        (*(itsSpinor[i])) = (*itTensor)[3*i];
        ++(itsSpinor[i]);
      }
      ++itTensor;
    }

    for (size_t i=0; i<4; i++)
    {
      Tool::IO::save(tmp+i, filenames[i], Tool::IO::fileSCIDAC);
    }

  }
  else
  {
    std::cerr << "Error in void Tool::IO::saveScidac(Core::Propagator *, std::vector< std::string> const &):"
              << std::endl;
    std::cerr << "filenames.size() should be 4" << std::endl;
    exit(1);
  }
}

void Tool::IO::saveScidac(Core::StochasticPropagator< 1 > *spropagator, std::vector< std::string> const &filenames)
{
  // would like to do this, but isolate is private
  // propagator->isolate();

  if (filenames.size() == 1)
  {
    Core::Field< QCD::Spinor > tmp(spropagator->L(), spropagator->T());

    Core::StochasticPropagator< 1 >::iterator itTensor = spropagator->begin();
    Core::Field< QCD::Spinor >::iterator itsSpinor = tmp.begin();

    // would like to see for loop here
    // but postfix Field::iterator operator++(int) is not implemented yet
    while (itTensor != spropagator->end())
    {
      (*itsSpinor) = (*itTensor)[0];
      ++itsSpinor;
      ++itTensor;
    }

    Tool::IO::save(&tmp, filenames[0], Tool::IO::fileSCIDAC);
  }
  else
  {
    std::cerr << "Error in void Tool::IO::saveScidac(Core::Propagator *, std::vector< std::string> const &):"
              << std::endl;
    std::cerr << "filenames.size() should be 1" << std::endl;
    exit(1);
  }
}
