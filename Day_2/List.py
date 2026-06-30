# list=[3,4,11,9]
# # list method 

# # 1. append --- add the element on last of the list
# list.append(10)
# print(list)

# # 2. sort ---- for sorting the method always in ascending order 
# list.sort()
# print(list)

# # 3. reverse ---- for reversing the list 
# list.reverse()
# print(list)

# # 4. insert---to add the element on the particular index 
# list.insert(2,5)
# print(list) 

# # 5. pop --- pass the index which you want to delete 
# list.pop(2)
# print(list)

# # 6. remove ---pass the value and it delete first occurance 
# list.remove(3)
# print(list)


  # set function in python is create a set of element which are unique 
  # split method is used to break a string into a list of substring based on a specified delimeter 


# wAP to check list contain a palindrome of element or not 

e1=int(input("enter the num "))
e2=int(input("enter the num "))
e3=int(input("enter the num "))
e4=int(input("enter the num "))
e5=int(input("enter the num "))
li=[e1,e2,e2,e3,e4]
li1=li.copy()
li.reverse()
if li==li1:
  print("palindrome")
else:
  print("not palindrome ")