#!/bin/bash 
echo "run python analysis"
time  ./Debug/simlocaFox.exe
time /cygdrive/c/Python27/python.exe DBases/PandaAnalysis/DataBase.py
