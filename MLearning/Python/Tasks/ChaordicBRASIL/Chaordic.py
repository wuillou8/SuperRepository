# -*- coding: utf-8 -*-
"""
Created on Fri May 09 12:28:38 2014
@author: jair
"""

#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import pandas as pd
import json
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import MyPandaUtilities
import MyIO
import MyChaordicAnalysis
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

infile = 'inputtest.json'
outfile = 'testout.json'

analysis = MyChaordicAnalysis.MyChaordicAnalysis( infile )
