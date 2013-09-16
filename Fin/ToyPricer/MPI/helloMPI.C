// Include the MPI version 2 C++ bindings:
#include <mpi.h>
#include <iostream>
#include <string.h>

using namespace std;

int
main(int argc, char* argv[])
{
  // Initialize the MPI library:
  MPI::Init(argc, argv);

  // Get the number of processors this job is using:
  int rank = MPI::COMM_WORLD.Get_rank();

  // Get the rank of the processor this thread is running on.  (Each
  // processor has a unique rank.)
  int size = MPI::COMM_WORLD.Get_size();

  // Get the name of this processor (usually the hostname).  We call                                                      
  // memset to ensure the string is null-terminated.  Not all MPI                                                        
  // implementations null-terminate the processor name since the MPI                                                     
  // standard specifies that the name is *not* supposed to be returned                                                   
  // null-terminated.                                                                                                    
  char name[MPI_MAX_PROCESSOR_NAME];
  int len;
  memset(name,0,MPI_MAX_PROCESSOR_NAME);
  MPI::Get_processor_name(name,len);
  memset(name+len,0,MPI_MAX_PROCESSOR_NAME-len);

  cout << "hello_parallel.cc: Number of tasks="<<size<<" My rank=" << rank << " My name="<<name<<"."<<endl;

  // Tell the MPI library to release all resources it is using:
  MPI::Finalize();
  return 0;
}
