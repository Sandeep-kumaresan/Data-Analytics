import numpy as np
# Creating array from list with type float
a = np.array([[1,2,3],[5,6,7]],dtype ='float')
print(a)
b = np.array((1,2,4))# Creating array from tuple
print(b)
c = np.zeros((2,3))# Creating a 3X4 array with all zeros
print(c)
d = np.full((3,3),4,dtype='complex')
print(d)
e = np.random.random((2,2))
print(e)
f = np.arange(1,10,0.2)
print(f)
g = np.linspace(5,15,9)#splitting equal parts
print(g)
arr = np.array([[1, 2, 3, 4],
                [5, 2, 4, 2],
                [1, 2, 0, 1]])
newarr = arr.reshape(2, 2, 3)
print(newarr)
arr = np.array([[1, 2, 3], [4, 5, 6]])
flat_arr = arr.flatten()
print(flat_arr)