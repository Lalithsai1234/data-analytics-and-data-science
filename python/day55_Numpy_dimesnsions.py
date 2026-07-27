import numpy as np

# Create a 1D array with 3 elements
arr=np.array([1,2,3])

print("arr=",arr)  # [1 2 3]
print("ndim=",arr.ndim)  # 1

# Create a 1D array but force it to be 5-dimensional using ndmin parameter
arr1=np.array([1,2,3,4], ndmin=5)
print("arr1=",arr1, "\nndim=",arr1.ndim)  # 5D array, ndim=5

# Check original array shape
print("arr=",arr)  # [1 2 3]
print("arr shape=",arr.shape)  # (3,)
print("arr1=",arr1)  # 5D array
print("arr1 shape=",arr1.shape)  # (1, 1, 1, 1, 4)

# reshape() - returns a new array with changed dimensions (doesn't modify original)
arr2=arr1.reshape(1,1,1,2,2)
print("arr2=",arr2)  # 5D array reshaped to (1,1,1,2,2)
print("arr2 shape=", arr2.shape)  # (1, 1, 1, 2, 2)

# Check the type of the array object
print("arr type=", type(arr))  # <class 'numpy.ndarray'>

# flatten() - converts multi-dimensional array to 1D, returns NEW array (creates a copy)
flatArr=arr2.flatten()
print("faltArray from arr2=", flatArr)  # [1 2 3 4]

# ravel() - similar to flatten() but returns a flattened view (doesn't create copy, just reference)
# However, if the array is not contiguous in memory, it returns a copy
ravelArr=arr1.ravel()
print("after ravel in 5 ndim arr1",ravelArr)  # [1 2 3 4] - If we change the ravelArr the original array also changes
