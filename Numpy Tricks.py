# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 00:01:19 2026

@author: emper
"""

import numpy as np

# np.sort: Returns a sorted copy of an array

a=np.random.randint(1,100,15)
print(a)
a=np.sort(a)
print(a)


# np.append: adds values alonged the mentioned axis of an array
print(np.append(a,200))

# np.concat: Concatinate a sequence of arrays along a given axis
c=np.arange(6).reshape(2,3)
d=np.arange(6,12).reshape(2,3)
print(c)
print(d)

print(np.concat((c,d),axis=0))
print(np.concat((c,d),axis=1))# use instead of vstack and hstack

# np.unique: We can get unique values from the array
e=np.array([1,1,2,3,3,4,3,5,5,6,6])
f=np.array([[1,2,3,1],[1,2,3,2]])

print(e)
print(f)

print(np.unique(e))
print(np.unique(f))

# np.where: returns the indices of the element where the given codition is stsisfied
print(a)
print(np.where(a>50))

print(np.where(a>50,0,a)) #replace 50 with 0

# np.argmax: returns indices of the max element in an axis
# np.argmin: ""min""
# np.cumsum: calculate cumulative sum
# np.cumprod: calculate cumulative product

# np.percentile

print(a)
print(np.percentile(a, 100))

print("----------------------")

# np.corrcoef() : return pearsons product moment correlation coefficients
#0-no corelation, 1-+ve corelation, -1: -ve corelation

sal=np.array([20000,40000,25000,35000,60000])
exp=np.array([1,3,2,4,2])
print(np.corrcoef(sal,exp))

# np.isin(): Checks for multiple ele in an array return boolean.

# np.flip: reverses order of array on axis preserving shape.

# np.put(): Replaces specific ele with a given value.

# np.delete(): returns new array with deletion of subarray along mentioned axis.
delete=np.array([1,2,4,2,4])
print(delete)
print(np.delete(delete,[1,2]))
# 