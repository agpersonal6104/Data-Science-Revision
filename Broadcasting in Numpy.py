# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 19:59:56 2026

@author: emper
"""
import numpy as np


#same shape
a=np.arange(6).reshape(2,3)
b=np.arange(6,12).reshape(2,3)

print(a)
print(b)

print(a+b)

print("--------------------------------------------")

#diff shape
c=np.arange(6).reshape(2,3)
d=np.arange(3).reshape(1,3)

print(c)
print(d)

print(c+d)

print("--------------------------------------------")

# Working with missing values
e=np.arange(10)
np.sin(e)

#sigmoid (S(x)=1/(1+e^-x))
def sigmoid(array):
    return 1/(1 + np.exp(array))

f=np.arange(10)
print(sigmoid(f))

print("--------------------------------------------")

