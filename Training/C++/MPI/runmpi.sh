#!/bin/bash
mpic++ $1
#2 processors...
mpirun -np 2 a.out
