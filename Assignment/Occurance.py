e1=int(input("Enter the element 1 : "))
e2=int(input("Enter the element 2 : "))
e3=int(input("Enter the element 3 : "))
e4=int(input("Enter the element 4 : "))
e5=int(input("Enter the element 5 : "))
list=[e1,e2,e3,e4,e5]
newlist=[]
# for i in list:
#   if i not in newlist:
#     newlist.append(i)
# # for i in newlist:
# print(newlist)
               
for i in set(list):
  count=1 
  if list.count(i):
    newlist.append(i)
    count=count+1
    print(i , "occurs", count)

