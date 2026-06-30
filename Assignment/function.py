# f(x)=x*x + 2x and g(x)=x+3

# def f1(x):
#   return x*x+2*x

# def g1(x):
#   return x+3

# print(f1(g1(2)))


# list comprehension

# l1=[10,20,30]
# l2=[x+2 for x in l1 ]
# print(l2)

l=[1,2,3,4,5,6,7,8,9,10]
l2=[x*x for x in l if x%2==0]
print(l2)
