# generators are functions that can pause and resume their execution

# it returns generator object 
# code inside the function not be executed ,it works only compiled the code 

# Generators allow you to iterate over data without storing the entire dataset in memory

# it does not return anything

# use yield keyword instead of return 

# yield ka mtlb yeh fuction state ko saved kr deta hai and then jb hum function ko nnext time call krte hai too wo whi se start hoga jha wo ruk gya tha like PCB in memory allocation

def my_generator():
  yield 1
  yield 2
  yield 3

for value in my_generator():
  print(value)


def count_(n):
  count=1
  while count <=n:
    yield count
    count+=1

  for num in count_(4):
    print(num)

    # Unlike return, which terminates the function, yield pauses it and can be called multiple times.

total = sum(x * x for x in range(3))
print(total)