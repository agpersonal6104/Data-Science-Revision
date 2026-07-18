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

table2=pd.Series(marks,name="Ayush ke marks!")
print(table2)

# Attributes
print(table2.size)
print(table2.dtype)
print(table2.name)
print(table2.is_unique)
print(table2.index)
print(table2.values)

# Series using CSV
df=pd.read_csv(r'C:\Users\emper\Downloads\bollywood.csv',index_col='movie')
print(type(df))
df=df.squeeze()
print(type(df))

print("----------------------------------")

# Series Methods

print(df.head())
print("----------------------------------")
print(df.tail())
print("----------------------------------")
print(df.sample(5)) #random selection
print("----------------------------------")
print(df.value_counts()) # Frequency in descending order
print("----------------------------------")
print(df.sort_values().head(1).values[0]) # Sort values
print("----------------------------------")
print(df.sort_index()) # Sort index

print("----------------------------------")

# Series Maths functions

print(df.count())
print(df.sum())
# product, mean, median and mode, min/max can be applied to int

print("----------------------------------")
print(df.describe)

print("----------------------------------")

# Series Indexing
x=pd.Series([12,13,14,35,34,57,59,79])
print(x[1]) #series only works in +ve indexing
print(df.iloc[0])