e1=int(input("Enter the element 1 : "))
e2=int(input("Enter the element 2 : "))
e3=int(input("Enter the element 3 : "))
e4=int(input("Enter the element 4 : "))
e5=int(input("Enter the element 5 : "))
list=[e1,e2,e3,e4,e5]
sum=0
max=-1
min=list[0]
for i in list:
  sum=sum+i
  if max<i:
    max=i
  if min>i:
    min=i
avg=sum/len(list)
print(avg)
print(min)
print(max)
list2=[avg,min,max]
list2.sort()
print(list2)

