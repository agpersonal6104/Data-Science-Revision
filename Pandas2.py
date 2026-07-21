# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 16:56:44 2026

@author: emper
"""

import numpy as np
import pandas as pd

# Using Lists

student_data=[
    [100,80,10],
    [90,70,7],
    [120,100,14],
    [80,50,2]
]

df=pd.DataFrame(student_data, columns=['iq','marks','package'])
print(df)

print("--------------------------------------")

# Using Dictionary

student_dict={
    'name':['Ayush','Pratham','Singha','Satvik','Ravi'],
    'iq':[100,90,120,80,0],
    'marks':[80,70,100,50,0],
    'package':[10,7,14,2,0]
}

df2=pd.DataFrame(student_dict)
print(df2)

print(df2.values)

data=pd.read_csv(r'C:\Users\emper\Downloads\diabetes.csv')
print(data.head())
print(data.size)
print(data.shape)
print(data.describe)
print(data.index)
print(data.columns)

# Fetch single columns
print(data['Glucose'].head())
print(data[['Glucose','BloodPressure','BMI','Age','Outcome']].tail())

print('--------------------------------------')

# Selecting rows from Dataframe
#iloc: Searches using index positions
#loc: Searches using index labels

df2=df2.set_index('name')
print(df2)

print('---------------------------------------')

print(data.head())

#single row
print(data.iloc[0])
print(type(data.iloc[1]))

#multiple rows
print(data.iloc[0:5])
print(data.iloc[5:16:2])

#Fancy indexing
print(data.iloc[[0,4,5]])

print('-------------------------------------')

print(data.loc[0])
print(df2.loc['Ayush'])
print(df2.loc['Ayush':'Ravi':3])


print('----------------------------------------')

# Selecting both Rows and Cols

print(data.iloc[0:3,0:3])