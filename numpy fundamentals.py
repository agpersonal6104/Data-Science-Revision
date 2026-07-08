import numpy as np

# Numpy 1D array
a=np.array([1,2,3])
print(a) # Scaler Vector

# 2D and 3D array
b=np.array([[1,2,3],[4,5,6]])
print(b) # Matrix

c=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(c) # Tensor

# Datatype
d=np.array([1,2,3],dtype=float)
e=np.array([0,1,2],dtype=bool)
print(d)
print(e)

# np.arange
print(np.arange(1,11,2))

# reshape
print(np.arange(1,13 ).reshape(3,4))

# np.ones & np.zeros
f=np.ones((3,4))
g=np.zeros((2,2))
print(f)
print(g)

# Random
print(np.random.random((2,3)))

# Linearly spaced: Distributes points with equal distances between two points
h=np.linspace(-10, 10,10, dtype=int)
print(h)

# Identity Matrix
print(np.identity(3))


# Array Attributes

a1=np.arange(10)
a2=np.arange(12,dtype=float ).reshape(3,4)
a3=np.arange(8).reshape(2,2,2)

print(a1.ndim)
print(a2.ndim)
print(a3.ndim)

print(a1.shape)
print(a2.shape)
print(a3.shape)

print(a1.size)
print(a2.size)
print(a3.size)

print(a1.itemsize)
print(a2.itemsize)
print(a3.itemsize)

print(a1.dtype)
print(a2.dtype)


# Changing datatype
print(a3.dtype)
print(a3.astype(np.int32).dtype)


#Array Operations

a1=np.arange(12).reshape(3,4)
a2=np.arange(12,24 ).reshape(3,4)

# Scaler Operations
print(a1*4) #Arithematic
print(a2>15) #Realational

# Vector Operations
print(a1/a2) #arithematic


# Array Functions
a1=np.random.random((3,3))
a1=np.round(a1*100)
print(a1)

print(np.sum(a1))
print(np.prod(a1))

# 0->col && 1->row
print(np.max(a1,axis=0))
print(np.min(a1,axis=0))

print(np.mean(a1,axis=1))
print(np.median(a1))
print(np.std(a1,axis=1))
print(np.var(a1,axis=1))


#
