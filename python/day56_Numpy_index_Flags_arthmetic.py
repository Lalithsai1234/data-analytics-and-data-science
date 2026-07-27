import numpy as np

# Create a 3D NumPy array:
# - First dimension = blocks
# - Second dimension = rows
# - Third dimension = columns
arr = np.array(
    [
        [
            [1, 2],
            [3, 4]
        ],
        [
            [5, 6],
            [7, 8]
        ]
    ]
)

# Print the array and its basic properties
print("arr=", arr)  # output: [[[1 2] [3 4]] [[5 6] [7 8]]]
print("arr ndim=", arr.ndim)   # number of dimensions | output: 3
print("arr shape=", arr.shape) # shape of the array | output: (2, 2, 2)

# Create another 3D array with 3 values in each inner list
# This shows that the inner lists can have different lengths in the last dimension
arr = np.array(
    [
        [
            [1, 2, 0],
            [3, 4, 0]
        ],
        [
            [5, 6, 0],
            [7, 8, 0]
        ]
    ]
)

# Print the updated array and its dimensions/shape
print("arr=", arr)  # output: [[[1 2 0] [3 4 0]] [[5 6 0] [7 8 0]]]
print("arr ndim=", arr.ndim)  # output: 3
print("arr shape=", arr.shape)  # output: (2, 2, 3)

# Indexing a 3D array follows the pattern: [block] [row] [column]
# arr[0]       -> first block
# arr[0][0]    -> first row inside the first block
# arr[0][0][0] -> first element of the first row in the first block
print("arr[0]=", arr[0])  # output: [[1 2 0] [3 4 0]]
print("arr[0][0]=", arr[0][0])  # output: [1 2 0]
print("arr[0][0][0]=", arr[0][0][0])  # output: 1
print("arr[0,0,0]=", arr[0, 0, 0])  # output: 1

 




# Examples of NumPy memory orders (for beginners):
# NumPy arrays can be stored in memory in different ways. This usually matters for
# performance and for interfacing with other libraries. The main orders:
# - C (row-major): rows are stored one after another
# - F (Fortran / column-major): columns are stored one after another
# - A: preserve existing order if possible (falls back to C)
# - K: try to preserve the memory layout of the input
arr_c = np.array([[1, 2, 3], [4, 5, 6]], order="C")
print("C order array=", arr_c)  # output: [[1 2 3] [4 5 6]]
print("C order flags=", arr_c.flags)  # flags show memory layout info | output: C_CONTIGUOUS=True, F_CONTIGUOUS=False, OWNDATA=True, WRITEABLE=True, ALIGNED=True, WRITEBACKIFCOPY=False

arr_f = np.array([[1, 2, 3], [4, 5, 6]], order="F")
print("F order array=", arr_f)  # output: [[1 2 3] [4 5 6]]
print("F order flags=", arr_f.flags)  # output: C_CONTIGUOUS=False, F_CONTIGUOUS=True, OWNDATA=True, WRITEABLE=True, ALIGNED=True, WRITEBACKIFCOPY=False

arr_a = np.array([[1, 2, 3], [4, 5, 6]], order="A")
print("A order array=", arr_a)  # output: [[1 2 3] [4 5 6]]
print("A order flags=", arr_a.flags)  # output: C_CONTIGUOUS=True, F_CONTIGUOUS=False, OWNDATA=True, WRITEABLE=True, ALIGNED=True, WRITEBACKIFCOPY=False

arr_k = np.asarray([[1, 2, 3], [4, 5, 6]], order="K")
print("K order array=", arr_k)  # output: [[1 2 3] [4 5 6]]
print("K order flags=", arr_k.flags)  # output: C_CONTIGUOUS=True, F_CONTIGUOUS=False, OWNDATA=True, WRITEABLE=True, ALIGNED=True, WRITEBACKIFCOPY=False






# Show specific flags that indicate contiguity in memory.
# C_CONTIGUOUS means the array is stored row-major without gaps.
# F_CONTIGUOUS means column-major contiguous storage.
print("arr_c.flags['C_CONTIGUOUS'] =", arr_c.flags['C_CONTIGUOUS'])  # output: True
print("arr_c.flags['F_CONTIGUOUS'] =", arr_c.flags['F_CONTIGUOUS'])  # output: False

print("arr_f.flags['C_CONTIGUOUS'] =", arr_f.flags['C_CONTIGUOUS'])  # output: False
print("arr_f.flags['F_CONTIGUOUS'] =", arr_f.flags['F_CONTIGUOUS'])  # output: True

print("arr_a.flags['C_CONTIGUOUS'] =", arr_a.flags['C_CONTIGUOUS'])  # output: True
print("arr_a.flags['F_CONTIGUOUS'] =", arr_a.flags['F_CONTIGUOUS'])  # output: False

print("arr_k.flags['C_CONTIGUOUS'] =", arr_k.flags['C_CONTIGUOUS'])  # output: True
print("arr_k.flags['F_CONTIGUOUS'] =", arr_k.flags['F_CONTIGUOUS'])  # output: False

# Example showing a non-contiguous view:
# Transposing a C-contiguous array usually produces a view that is not
# C-contiguous (it changes the memory access pattern).
mat = np.arange(6).reshape(2, 3)  # [0 1 2] and [3 4 5]
mat_t = mat.T                    # transpose -> shape becomes (3,2)
print("mat=", mat)  # output: [[0 1 2] [3 4 5]]
print("mat.flags['C_CONTIGUOUS'] =", mat.flags['C_CONTIGUOUS'])  # output: True
print("mat_t=", mat_t)  # output: [[0 3] [1 4] [2 5]]
print("mat_t.flags['C_CONTIGUOUS'] =", mat_t.flags['C_CONTIGUOUS'])  # output: False
print("mat_t.flags['F_CONTIGUOUS'] =", mat_t.flags['F_CONTIGUOUS'])  # output: True

# If you need a C-contiguous array (for example to pass to C code), make a copy
mat_t_contig = np.ascontiguousarray(mat_t)
print("mat_t_contig.flags['C_CONTIGUOUS'] =", mat_t_contig.flags['C_CONTIGUOUS'])  # output: True


a= np.array([[1,2,3]])
# b=a
# b[0]=200  #it changes the both a and b where each element was replaced by 200
# print(a)
# print(b)

b=np.array(a, copy=True) #here it creates a new array based on the value it have (like deepcopy)
b[0]=200  
print(a)  # output: [[1 2 3]]
print(b)  # output: [[200 200 200]]



# most used methods in numpy are mean, median, var, std, sum

arr= np.array([21,22,23,22,26,24,25])
print("arr=",arr)  # output: [21 22 23 22 26 24 25]
print("mean=",np.mean(arr))  # output: 23.285714285714285
print("median=", np.median(arr))  # output: 23.0
# the variance is it will take the difference of every value to the mean and square the difference and gives average of squares
# E(value-mean)**2 ==> sum of all squared difference / no of values
print("variance=", np.var(arr)) #mostly used in knn and dbscan | output: 2.7755102040816326
print("sum=", np.sum(arr))  # output: 163
# for the standard deviation you just need to square root the variance
# std=sqrt(variance)
print("Standard deviation=", np.std(arr))  # output: 1.6659862556700857

