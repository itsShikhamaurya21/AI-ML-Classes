# Recursion--its a technique where function call itself to solve  a problem by breaking down into smaller similar sub problem instead of utilising loops to repeat an action , recursion pushes active function instances into python internal call stack*** 

# base case (stopping condition for recursion ) return frm the function 
# it prevents from the infinite loop it returns immediately without making another responsive call 

# def view (n):
#   if n==0: return 1
#   print(n)
#   view(n-1)
# view(4)

# n=int(input("Enter the number "))
# def factorial(n):
#   if(n==0): return 1
#   return n*factorial(n-1)
# print(factorial(n))

# def sum(n):
#   if(n==0): return 0
#   return n+sum(n-1)
# print(sum(n))

# def test(x=[]):
#   x.append(1)
#   return x

# print(test())
# print(test())

x=int(input("Enter the number "))
def fibonacci(x):
  if x<=1: return x
  return fibonacci(x-1)+fibonacci(x-2)

for i in range(x):
  print(fibonacci(i),end=" ")
fibonacci(x)

#