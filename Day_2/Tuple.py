tuple=(1,2,3,4,2)
print(tuple)

#   for single element tuple use , 
tuple1=(1,)
print(tuple1)
print(type(tuple1))

# 1. index method to find the element index
print(tuple.index(2))

# 2. count --count the element how many type it occurs in tuple
print(tuple.count(2)) 

# # wap a program to find the index of a number in a tuple 
e1=int(input("enter the e1 "))
e2=int(input("enter the e2 "))
e3=int(input("enter the e3 "))
e4=int(input("enter the e4 "))
e5=int(input("enter the e5 "))
key=int(input("enter the key "))
t1=(e1,e2,e3,e4,e5)
# if key in t1:
#   print("index is ",t1.index(key))
# else:
#   print("key not found")

for i in range(len(t1)):
  if t1[i]==key:
    print(i)
    break;
else:
  print("not found")


