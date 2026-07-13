# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 13:16:48 2026

@author: emper
"""

import numpy as np

# Working with missing values

a=np.array([1,2,3,4,np.nan,6])
print(a)

print(np.isnan(a))

print(a[~np.isnan(a)])

# Plotting graphs using numpy
x=np.linspace(-10,10,100)
y=x;

import matplotlib.pyplot as plt

x=np.linspace(-10,10,100)
y=x**2
plt.plot(x,y)