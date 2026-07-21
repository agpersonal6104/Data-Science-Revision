# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 21:25:03 2026

@author: emper
"""
import numpy as np
import pandas as pd

movies=pd.read_csv(r"C:\Users\emper\Downloads\bollywood.csv",index_col='movie')
print(type(movies))
print(movies.head())

# etween: checks for a condition between elements mentioned
# Clip: Converts all values to a range
#subs.clip(100,200)

#drop_duplicates
temp=pd.Series([1,1,2,2,3,3,4,4])
print(temp.drop_duplicates())
print(temp.drop_duplicates(keep='last'))
print(temp.duplicated())

print('-----------------------------------')

temp2=pd.Series([1,3,np.nan,3,np.nan,5,6,4,np.nan])
print(temp2.isnull())
temp2=temp2.dropna()
print(temp2)

print('-----------------------------------')

temp3=pd.Series([1,3,np.nan,3,np.nan,5,6,4,np.nan])
temp3=temp3.fillna(temp.mean())
print(temp3)

# Checks whether multiple values are present
#df.isin([49.99])

# apply: Help to apply custom logic in the series
print(movies)
#movies.apply(lambda x : x.split()[0].upper())

#copy
print(temp)
new=temp.head()
print(new)
new[0]=100;
print(temp)
#head and tail give view of the data/ they are not repllicas or copies, so it will reflect back to original

new2=temp.head().copy()
new2[1]=100
print(temp)
#Use Copy to prevent problems in main data