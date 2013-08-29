#include "Weave.ih"

namespace Base
{
void Weave::sumOverTimeSlices(std::complex< double > const *data_send, std::complex< double > *data_recv, size_t const count) const
{
  // have to wait until all calculations are finished
  d_grid.grid().Barrier();

  // call MPI::Intracomm::Allreduce(...)
  (d_grid.grid()).Allreduce(static_cast< const void * >(data_send), static_cast< void * >(data_recv),
                            int(count*d_T), MPI::DOUBLE_COMPLEX, MPI::SUM);
}
}
