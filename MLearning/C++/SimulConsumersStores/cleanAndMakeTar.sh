#!/bin/bash
rm DBases/PandaAnalysis/*pyc
rm DBases/Data/DB*
rm Release/src/*
rm Debug/src/*
rm Debug/*exe*
rm Release/*exe
tar cvf simlocafox.tar *
