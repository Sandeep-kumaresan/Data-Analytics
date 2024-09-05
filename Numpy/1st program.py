import numpy as np
arr = np.array([[1,2,3],[4,5,6]])
arr1 = np.arange(4,8,1.2)
arr2 = np.arange(4, dtype = np.float64).reshape(2, 2)
print("Array is of type: ", type(arr))
print(arr1)
print(arr2)
print(arr2.ndim)# Printing array dimensions (axes)
print(arr2.shape)# Printing shape of array
print(arr2.size)# Printing size (total number of elements) of array
print(arr2.dtype)# Printing type of elements in array