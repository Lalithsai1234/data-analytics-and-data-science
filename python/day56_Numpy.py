import numpy as np

# Create a 3D NumPy array (simple example for beginners):
# - First dimension = blocks (like layers)
# - Second dimension = rows
# - Third dimension = columns
# Here we have 2 blocks, each block has 2 rows, each row has 2 columns.
arr = np.array([
    [
        [1, 2],  # first row of first block
        [3, 4]   # second row of first block
    ],
    [
        [5, 6],  # first row of second block
        [7, 8]   # second row of second block
    ]
])

# Print the array and its basic properties so you can see how NumPy reports them
print("arr=", arr)
print("arr ndim=", arr.ndim)   # number of dimensions (3 for a 3D array)
print("arr shape=", arr.shape) # shape = (blocks, rows, columns)

# Create another 3D array where each innermost list has 3 values
# This is just to show a different shape: now each row has 3 columns instead of 2.
arr = np.array([
    [
        [1, 2, 0],  # first row in first block (3 columns)
        [3, 4, 0]   # second row in first block
    ],
    [
        [5, 6, 0],  # first row in second block
        [7, 8, 0]   # second row in second block
    ]
])

# Print the updated array and its dimensions/shape
print("arr=", arr)
print("arr ndim=", arr.ndim)
print("arr shape=", arr.shape)

# Indexing a 3D array follows the pattern: [block] [row] [column]
# Examples (all do the same thing, different notation):
print("arr[0] = first block (a 2D array):", arr[0])
print("arr[0][0] = first row inside the first block:", arr[0][0])
print("arr[0][0][0] = first element of that row:", arr[0][0][0])
print("arr[0,0,0] = same element using comma-separated indexes:", arr[0, 0, 0])






# Examples of NumPy memory orders (for beginners):
# NumPy arrays can be stored in memory in different ways. This usually matters for
# performance and for interfacing with other libraries. The main orders:
# - C (row-major): rows are stored one after another
# - F (Fortran / column-major): columns are stored one after another
# - A: preserve existing order if possible (falls back to C)
# - K: try to preserve the memory layout of the input
arr_c = np.array([[1, 2, 3], [4, 5, 6]], order="C")
print("C order array=", arr_c)
print("C order flags=", arr_c.flags)  # flags show memory layout info

arr_f = np.array([[1, 2, 3], [4, 5, 6]], order="F")
print("F order array=", arr_f)
print("F order flags=", arr_f.flags)

arr_a = np.array([[1, 2, 3], [4, 5, 6]], order="A")
print("A order array=", arr_a)
print("A order flags=", arr_a.flags)

arr_k = np.asarray([[1, 2, 3], [4, 5, 6]], order="K")
print("K order array=", arr_k)
print("K order flags=", arr_k.flags)






# Show specific flags that indicate contiguity in memory.
# C_CONTIGUOUS means the array is stored row-major without gaps.
# F_CONTIGUOUS means column-major contiguous storage.
print("arr_c.flags['C_CONTIGUOUS'] =", arr_c.flags['C_CONTIGUOUS'])
print("arr_c.flags['F_CONTIGUOUS'] =", arr_c.flags['F_CONTIGUOUS'])

print("arr_f.flags['C_CONTIGUOUS'] =", arr_f.flags['C_CONTIGUOUS'])
print("arr_f.flags['F_CONTIGUOUS'] =", arr_f.flags['F_CONTIGUOUS'])

print("arr_a.flags['C_CONTIGUOUS'] =", arr_a.flags['C_CONTIGUOUS'])
print("arr_a.flags['F_CONTIGUOUS'] =", arr_a.flags['F_CONTIGUOUS'])

print("arr_k.flags['C_CONTIGUOUS'] =", arr_k.flags['C_CONTIGUOUS'])
print("arr_k.flags['F_CONTIGUOUS'] =", arr_k.flags['F_CONTIGUOUS'])

# Example showing a non-contiguous view:
# Transposing a C-contiguous array usually produces a view that is not
# C-contiguous (it changes the memory access pattern).
mat = np.arange(6).reshape(2, 3)  # [0 1 2] and [3 4 5]
mat_t = mat.T                    # transpose -> shape becomes (3,2)
print("mat=", mat)
print("mat.flags['C_CONTIGUOUS'] =", mat.flags['C_CONTIGUOUS'])
print("mat_t=", mat_t)
print("mat_t.flags['C_CONTIGUOUS'] =", mat_t.flags['C_CONTIGUOUS'])
print("mat_t.flags['F_CONTIGUOUS'] =", mat_t.flags['F_CONTIGUOUS'])

# If you need a C-contiguous array (for example to pass to C code), make a copy
mat_t_contig = np.ascontiguousarray(mat_t)
print("mat_t_contig.flags['C_CONTIGUOUS'] =", mat_t_contig.flags['C_CONTIGUOUS'])


