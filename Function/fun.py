# def sum(a,b):
#   return a+b
# print(sum(2,3))

# # wap to create function to calculate the avg of the list entered by the user 

# e1=int(input("enter the e1 "))
# e2=int(input("enter the e2 "))
# e3=int(input("enter the e3 "))
# e4=int(input("enter the e4 "))
# e5=int(input("enter the e5 "))
# li=[e1,e2,e3,e4,e5]
# sum=0
# for i in range(len(li)):
#   sum=sum+li[i]
# print(sum)


# def avg(sum):
#   avg=sum/len(li)
#   return avg
# print("Average is ",avg(sum))

n=int(input("Enter the number "))

# def factorial(n):
#   fact=1
#   for i in range(1,n+1):
#     fact=fact*i
#   return fact
# print(factorial(n))


def fibonaaci(n):
  f0=0
  f1=1
  for i in range(1,n+1):
    print(f0, end=" " )
    c=f0+f1
    f0=f1
    f1=c
fibonaaci(n)