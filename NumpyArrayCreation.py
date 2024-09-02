import numpy as np
# Creating array from list with type float
a = np.array([[1,2,3],[5,6,7]],dtype ='float')
print(a)
b = np.array((1,2,4))# Creating array from tuple
print(b)
c = np.zeros((2,3))# Creating a 3X4 array with all zeros
print(c)
d = np.full((3,3),6,dtype='complex')
print(d)
e = np.random.random((2,2))
print(e)
