# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 23:35:14 2026

@author: emper
"""

import numpy as np
import pandas as pd

# Series from list

#String
country=['India','USA','Nepal','Srilanka']
print(pd.Series(country))

#Integer
run=[13,25,100,33,54]
print(pd.Series(run))

#Custom Index
marks=[67,57,95,89,100]
subjects=['Physics','Chemistry','Maths','English','Computer']

table1=pd.Series(marks, index=subjects, name='Ayush ke Marks!')
print(table1)

# Series from Dictionary
marks={
       'Physics':67,
       'Maths':95,
       'Chemistry':57
}

table2=pd.Series(marks)
print(table2)