# lambda arguments :expression

x=lambda a,b,c: a*b*c
print(x(5,5,4))

# why we use 
# lambda function is a anomyous function in this we have declare any number of arguments but it ghas only one expresssion 

# the power of lambda is better shown when we use it in another function

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

# map(), filter(), sorted()

list1=[1,2,3,4]
double=list(map(lambda a: a*2,list1))
print(double)

list1=[1,2,3,4]
double=list(filter(lambda a: a%2!=0,list1))
print(double)

words=["apple","pie","bananna","cherry"]
sorted=sorted(words,key=lambda x:len(x))
print(sorted)

list1=[5,2,9,4]
double=sorted(list1,key=lambda x:len(x))
print(double)