# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 23:20:33 2026

@author: emper
"""

import numpy as np

#Numpy array vs Python lists

# Speed of lists

a=[i for i in range(100000)]
b=[i for i in range(100000,200000)]

c=[]

import time

start=time.time()
for i in range(len(a)):
    c.append(a[i]+b[i])
print(time.time()-start)
# Dynamic array and Referential: Item ka address store karte hain

# Speed of Numpy

a2=np.arange(100000)
b2=np.arange(100000,200000)

start=time.time()
c=a2+b2
print(time.time()-start)
#static array and item ka value store karte hain

# Memory difference

import sys

print(sys.getsizeof(a)) #python list
print(sys.getsizeof(a2)) #numpy array

print("-------------------------------------------------")

# Fancy Indexing
a1=np.arange(24).reshape(6,4)
print(a1)

print(a1[[0,2,3,5]])
print(a1[:,[0,2,3]])

print("-------------------------------------------------")

# Boolean Indexing

arr=np.random.randint(1,100,24).reshape(6,4)
print(arr)
 
# no greater than 50
print(arr>50)
print(arr[arr>50])

# greater than 50 and even
print(arr[(arr>50) & (arr%2==0)])

#find all numbers not divisible by 7
print(arr[~(arr%7==0)])