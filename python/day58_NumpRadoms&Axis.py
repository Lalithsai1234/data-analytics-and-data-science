import numpy as np


"""Random Methods:

rand
randint
randn
choice
shuffle"""

print(np.random.rand(3)) #we need to pass the no of values needed from 0 to 1  op:[0.00670238 0.11091253 0.00419161]
print(np.random.randint(1,10,3)) #it will take (start, endpoint, no of values needed) #op:[8 5 8]
print(np.random.randn(4)) #nearest values to the 0 either '-' or '+'  op:[ 0.4367623  -0.68906548  0.75442673 -0.68440714]

arr=np.array([1,2,3,4,5])
print(np.random.choice(arr)) #takes the arr and give one option
print(np.random.choice(arr,3)) #takes thee arr and no of values needed op:[5 4 4]

np.random.shuffle(arr) #it will shuffle the original array
print(arr) #[2 4 3 5 1]



"""Max and Min with axis for 2d or more
0-- vertical
1-- horizontal
"""
arr=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(np.max(arr))#op:9
print(np.max(arr, axis=0)) # 0 for vertical op:[7 8 9]
print(np.max(arr, axis=1)) #1 for horizontal op:[3 6 9]
print(np.mean(arr)) #it will give mean of all values in arr op:5.0
print(np.mean(arr, axis=1)) #it will give array of means for each row  [2. 5. 8.]
print(np.median(arr)) #it will give the overall values of median 5.0
print(np.median(arr, axis=0)) #op:[4. 5. 6.]
## same goes for the min, var and std


"""
trigonometry in numpy we need to use radians only 
"""
arr=np.array([0,30,45,60,90])
# 180 => Pi Radians 3.14
rads=np.radians(arr)
print(rads) # op:[0.         0.52359878 0.78539816 1.04719755 1.57079633]
print(np.sin(rads)) #op:[0.         0.5        0.70710678 0.8660254  1.        ]
print(np.cos(rads))#op:[1.00000000e+00 8.66025404e-01 7.07106781e-01 5.00000000e-01 6.12323400e-17]
print(np.tan(rads))#op:[0.00000000e+00 5.77350269e-01 1.00000000e+00 1.73205081e+00   1.63312394e+16]
