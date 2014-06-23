#include "mpi.h"
#include <stdio.h>

int main(int argc, char **argv )
{
int done = 0, n, myid, numprocs, i, rc;
double PI = 3.14123456789;
double mypi, pi, h, sum, x, a;

MPI_Init( &argc, &argv );
MPI_Comm_rank( MPI_COMM_WORLD, &numprocs );
MPI_Comm_size( MPI_COMM_WORLD, &myid );

while(!done) {
	if (myid == 0) {
		printf(" Enter the number of intervs: (= quits) ");
		scanf("%d",&n);
	}
	MPI_Bcast(&n, 1, MPI_INT, 0, MPI_COMM_WORLD);
	if (n == 0) break;

	h = 1. / (double) n;
	sum = 0.;
	for (i = myid + 1; i <= n; i += numprocs) {
		x = h * ((double)i - .5);
		sum += 4. / (1. + x*x);	
	}
	mypi = h * sum;

MPI_Reduce(&mypi, &pi, 1, MPI_DOUBLE, MPI_SUM, 0, MPI_COMM_WORLD);


	if (myid == 0) {
		printf("pi");
	}

printf( "Hello, I am processor %d of %d\n", rank, size );
MPI_Finalize();
return 0;
}
