import numpy as np
"""
Array Creation methods:
arange()
ones()
zeros()
full()
eye()
linspace()
reshape()
flatten()
"""

arr=np.arange(1,11)#this methods works as range which have(start, stop,skip)
print("arange =",arr)

arr=np.arange(1,11).reshape(2,5)
print("arange and reshape=",arr)


arr=np.ones(5)
print("ones without specified dtype=",arr)

arr=np.ones(5,dtype=int)
print("ones with specified dtype=",arr)

arr=np.ones((2,5),dtype=int) #arr=np.ones(2,5,dtype=int) gives an error bcz we need to pass as a single argument
print("ones in 2d",arr)


arr=np.zeros((2,3), dtype=int) #zeroes works as ones we need to specify dtype and if 2d we need give in argument
print("zeroes in 2d", arr)


arr=np.full(5,7) #you must give two arguments 
print("full=", arr)#it will generate the array with specified value 


arr=np.eye(3,3)
print("eye=\n",arr) #it will generate the 1 in diagonal 00 to 11

arr=np.eye(3,3, dtype=int)
print("eye with dtype=\n",arr)


arr=np.linspace(1,10,5) #it will take (start, stop(includes), parts )
print("linspace=", arr) #linspace= [ 1.    3.25  5.5   7.75 10.  ]

arr=np.linspace(1,10,5, dtype=int) #it will take (start, stop(includes), parts )
print("linspace=", arr) #linspace= [ 1    3      5   7     10  ]


arr=np.array([1,2,3,4,5,6,7,8,9])
arr=arr.reshape(3,3) #it will returns the array doesn't change the original
print("reshaping the array=\n", arr)


arr=arr.flatten()
print("flatten=",arr) #makes the any dimensions array into 1d


### Arithmetic

arr=np.array([1,2,3,4,5,6,7,8])
arr=arr+4 #we don't need to use for to access the each element in numpy with any +,-,*,/,%,//
print("arr+4=", arr) # arr+4= [ 5  6  7  8  9 10 11 12]

arr=np.array([1,2,3,4,5,6])
arr1=np.array([3,4,5,6,7,8])

print(np.add(arr,arr1))#[ 4  6  8 10 12 14]
print(np.subtract(arr1,arr))#[2 2 2 2 2 2]
print(np.multiply(arr, arr1))#[ 3  8 15 24 35 48]
print(np.divide(arr, arr1))#[0.33333333 0.5        0.6        0.66666667 0.71428571 0.75      ]
print(np.floor_divide(arr,arr1))#[0 0 0 0 0 0]
print(np.mod(arr,arr1))#[1 2 3 4 5 6]
print(np.power(arr, arr1))#[      1      16     243    4096   78125 1679616]



### comparison

print(arr<5) #[ True  True  True  True False False]
print(arr<arr1) # [ True  True  True  True  True  True]

##Filtering
print(arr[arr<5]) #[1 2 3 4] only satisfied will be return in a array


### All Comparison Operator Methods in NumPy

arr=np.array([1,2,3,4,5,6])
arr1=np.array([3,4,5,6,7,8])

print(np.less(arr, arr1)) #element-wise less than (<)
print(np.less_equal(arr, arr1)) #element-wise less than or equal (<=)
print(np.greater(arr, arr1)) #element-wise greater than (>)
print(np.greater_equal(arr, arr1)) #element-wise greater than or equal (>=)
print(np.equal(arr, arr1)) #element-wise equal (==)
print(np.not_equal(arr, arr1)) #element-wise not equal (!=)
print(np.logical_and(arr<4, arr1>3)) #logical AND
print(np.logical_or(arr<2, arr1>7)) #logical OR
print(np.logical_not(arr<4)) #logical NOT


## Slicing
#arr=[1,2,3,4,5,6]
print(arr[3]) #4
print(arr[-1]) #6
print(arr[1:3]) # [2 3]
print(arr[-1:0:-1]) #[6 5 4 3 2]
print(arr[:0:-1]) #[6 5 4 3 2] works same
print(arr[::-1]) #reverse the array


##sorting
arr=[4,6,7,89,13,4,6]
arr=np.sort(arr) 
print("sorting the array=",arr ) # [ 4  4  6  6  7 13 89]

arr=np.array([
    [1,2,3],
    [5,6,7],
    [8,9,10]
])
print(arr[1,2]) #7
print(arr[::2,::2]) #[[ 1  3] [ 8 10]]
print(arr[0:-1,1:-1]) #[[2] [6]]


##transpose
print(arr.T) #[[ 1  5  8][ 2  6  9] [ 3  7 10]]


##aggregate methods


print(np.max(arr))  #10
print(np.min(arr)) #1
print(np.argmax(arr)) #8
print(np.argmin(arr)) #0