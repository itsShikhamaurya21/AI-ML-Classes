e1=int(input("Enter the element 1 : "))
e2=int(input("Enter the element 2 : "))
e3=int(input("Enter the element 3 : "))
e4=int(input("Enter the element 4 : "))
e5=int(input("Enter the element 5 : "))
list=[e1,e2,e3,e4,e5]
max=list[0]
secmax=list[0]
for i in list:
  if i>max:
    secmax=max
    max=i
  elif secmax!=max and secmax<i:
    secmax=i
print(max)
print(secmax)