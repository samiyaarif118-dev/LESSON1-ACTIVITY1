import numpy as np 
from numpy import random

arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr)
print(arr[2,2])   #access array element
print(arr[1,1:2]) #slicing array

arr = np.array([8, 18, 28, 38, 48])
print(arr.dtype)

arr = np.array([10, 20, 30, 40, 50], dtype='S')
print(arr)
print(arr.dtype)

arr = np.array([[61, 62, 63, 64],[65, 66, 67, 68]])
print(arr.shape)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4,3)
print(newarr)

arr = np.array([11343, 1234, 2313])
for i in arr:
    print(i)

x = np.array([21, 32, 33])
y = np.array([54, 55, 56])
z = np.concatenate((x, y))
print(z)

arr = np.array([1, 2, 3, 2, 5, 2, 4, 2, 6,2, 1])
x = np.where(arr == 2)
print(x)

x = random.randint(100)
print(x)













