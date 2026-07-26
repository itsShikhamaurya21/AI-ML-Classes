import numpy as np
print("\1D array\n")
arr=np.array([2,3,4,5,6,7])
print(arr)

print("\n2D array\n")
arr2D=np.array([[2,3,4],[9,0,8]])
print(arr2D)

print("\n3D array\n")
arr3D=np.array([
  [
    [1,2,3],[5,6,7]
  ],
  [
    [3,2,4],[1,2,3]
  ]
])
print(arr3D)

# methods --shape
print("Shape of 1D is ", arr.shape)
print("Shape of 2D is ", arr2D.shape)
print("Shape of 3D is ", arr3D.shape)

# dtype

print("type of 1D is ", arr.dtype)
print("type of 2D is ", arr2D.dtype)
print("type of 3D is ", arr3D.dtype)

# size

print("size of 1D is ", arr.size)
print("size of 2D is ", arr2D.size)
print("size of 3D is ", arr3D.size)

# ndim

print("Dimensional of 1D is ", arr.ndim)
print("Dimensional of 2D is ", arr2D.ndim)
print("Dimensional of 3D is ", arr3D.ndim)


# reshape
arr1=arr.reshape(2,3)
print(arr1)
# sum of array
print("sum ",arr.sum())
print("min ",arr.min())
print("max ",arr.max())
print("avg ",arr.mean())
print("standard deviation ",arr.std())

# indexing and slicing 

print(arr[1:])
print("Access 0 from 2D ", arr2D[1,1])
print("Slicing row 1 last two elements ",arr2D[1,1:])
print("Accessing 2 from 3Darray ",arr3D[0,0,1])
print("Slicing 2 4 in 3D array ",arr3D[1,0,1:3])

arr2=np.empty((2,2))
print(arr2)
print(type(arr2))
print(arr.astype(float))

# print(np.random,rand(2,3))


# View and copy
# Copy --- make a new array/ not affect the original array
arr=np.array([1,2,3,4,5])
x=arr.copy()
arr[0]=21

print(arr)
print(x)

# view --- make changes in original array-- it affect the original array

arr=np.array([1,2,3,4,5,6,7])
x=arr.view()
arr[0]=21
print(arr)  
print(x)  #store the original arr into it

# Every NumPy array has the attribute base that returns None if the array owns the data.

arr = np.array([1, 2, 3, 4, 5])

x = arr.copy()
y = arr.view()

print(x.base)
print(y.base)

# reshape --- 1-D to any type of D

arr=np.array([1,2,3,4,4,5,5,7,6,6,6,8])
newarr=arr.reshape(3,4)
print(newarr)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr = arr.reshape(2, -1)
print(newarr)

arr=np.array([[1,2,3,4],[5,7,8,9]])
print(arr.reshape(-1))


# loop
arr=np.array([[1,2,3,4],[5,6,7,8]])

for x in arr:
  for y in x:
    print(y)

for x in np.nditer(arr):
  print(x)

for idx,x in np.ndenumerate(arr):
  print(idx,x)

# join two 1D array
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1, arr2))

print(arr)

# join two 2 D array

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr=np.concatenate((arr1,arr2),axis=1)   # axis -1 column axis 
print(arr)

# spliting the array

arr = np.array([1, 2, 3, 4, 5])
newarr = np.array_split(arr, 3)
print(newarr)

# where-- for searching 

x=np.where(arr==4)
print(x)

# searchsorted

x=np.searchsorted(arr,4)
print(x)

# filter array

arr=np.array([41,42,43,44])
filter_arr=arr>42
newarr=arr[filter_arr]
print(filter_arr)
print(newarr)
