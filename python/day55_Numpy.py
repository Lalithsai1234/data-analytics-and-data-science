import numpy as np

# Create a 1D array with 3 elements
arr=np.array([1,2,3])

print("arr=",arr)
print("ndim=",arr.ndim)

# Create a 1D array but force it to be 5-dimensional using ndmin parameter
arr1=np.array([1,2,3,4], ndmin=5)
print("arr1=",arr1, "\nndim=",arr1.ndim)

# Check original array shape
print("arr=",arr)
print("arr shape=",arr.shape)
print("arr1=",arr1)
print("arr1 shape=",arr1.shape)

# reshape() - returns a new array with changed dimensions (doesn't modify original)
arr2=arr1.reshape(1,1,1,2,2)
print("arr2=",arr2)
print("arr2 shape=", arr2.shape)

# Check the type of the array object
print("arr type=", type(arr))

# flatten() - converts multi-dimensional array to 1D, returns NEW array (creates a copy)
flatArr=arr2.flatten()
print("faltArray from arr2=", flatArr)

# ravel() - similar to flatten() but returns a flattened view (doesn't create copy, just reference)
# However, if the array is not contiguous in memory, it returns a copy
ravelArr=arr1.ravel()
print("after ravel in 5 ndim arr1",ravelArr)  # If we change the ravelArr the original array also changes
