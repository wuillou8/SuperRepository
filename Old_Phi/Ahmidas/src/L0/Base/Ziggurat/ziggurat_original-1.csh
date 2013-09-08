#!/bin/csh
#
cp ziggurat_original.H /$HOME/include
#
g++ -c -g ziggurat_original.C >& compiler.txt
if ( $status != 0 ) then
  echo "Errors compiling ziggurat_original.C."
  exit
endif
rm compiler.txt
#
mv ziggurat_original.o ~/libcpp/$ARCH/ziggurat_original.o
#
echo "Library installed as ~/libcpp/$ARCH/ziggurat_original.o"
