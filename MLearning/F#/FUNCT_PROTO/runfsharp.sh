#!/bin/bash 
rm $1.exe
fsharpc $1.fs
mono $1.exe
