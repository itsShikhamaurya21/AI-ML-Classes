import numpy as np
# vectoraisation --modify whole array without looping 
# a=np.array([1,2,3,4])
# b=np.array([1,4,9,16])
# c=a+b
# print(c)
# print(np.sqrt(b))
# print(a*b)
# print(a-b)
# print(b/a)
# print(np.exp(b))

# # broadcasting performs operation on different shapes by automatically expanding the smaller array to match the shape of larger arrray 
# print(a+10)

# print(np.sum(a))

arr1=np.array([1,2,3,4])
arr2=np.array([[1,2,3,4],[5,6,7,8]])
print(arr1+arr2)