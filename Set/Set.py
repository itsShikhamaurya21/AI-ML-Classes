# set is the collection of unordered data , each element must be uniique and immutable 
# when we use repeated value then only one occurance of the sets will be show
# in this list and dictionary cannot be stored in a set 

set1={1,2,3,4,5,4}
print(set1)

# method 
# 1. add--- to insert the element 
set1.add(6)
print(set)
# set() is used to defined the empty set 
set2=set()     
print(set2)
print(type(set2))

set2.add(4)
set2.add(5)
set2.add(7)
print(set2)

# remove--to remove the element 
set1.remove(3)
print(set1)

# union -- to access the all element
print(set1.union(set2))

# intersection --- to access common elements 
print(set1.intersection(set2))



