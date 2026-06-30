n=int(input("enter the number "))
f0=0
f1=1
for i in range(n):
  print(f0 ,end=" ")
  f2=f0+f1
  f0=f1
  f1=f2
  # f0,f1=f1,f0+f1
  
   