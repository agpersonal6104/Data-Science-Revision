# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 15:31:35 2026

@author: emper
"""
import numpy as np
# Indexing and Slicing in python

a1=np.arange(10)
a2=np.arange(12).reshape(3,4)
a3=np.arange(8).reshape(2,2,2)

print(a1[-1])
print(a3[1,0,1])
print(a3[0,1,1])

print(a1[2:5])
print(a1[2:5:2])

print(a2[2,:])
print(a2[:,1])
print(a2[1:,1:3])

print(a2[::2,::3 ]) # print element on corners
print(a2[::2,1::2])
print(a2[1,::3])
print(a2[0:2,1:])

a4=np.arange(27).reshape(3,3,3)

print(a4[1,:,:])
print(a4[1])

for i in a1:
    print(i)
    
for i in a2:
    print(i)
    
for i in a3:
    print(i)
    
for i in np.nditer(a3):
    print(i)
    
    
# Reshaping

print(np.transpose(a2)) #transpose
print(a2.T)

#revel: COnverts n dim array to 1d array
print(a3.ravel())

print("-----------------------------")

# Stacking

a4=np.arange(12).reshape(3,4)
a5=np.arange(12,24).reshape(3,4)

print(a4)
print(a5)
#horizontal stacking
print(np.hstack((a4,a5)))

#vertically stacking
print(np.vstack((a4,a5)))

print("-----------------------------")

# Splitting

print(np.hsplit(a4,2))
print(np.vsplit(a5,3))



