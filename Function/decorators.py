def changecase(func):
  def inner():
    return func().upper()
  return inner

@changecase
def myfunction():
  return "Shikha MAurya"

print(myfunction())


def changecase(func):
  def inner(x):
    return func(x).lower()
  return inner

@changecase
def myfunction(x):
  return "Hello " +x

print(myfunction("Shikha"))


# multiple decorators
def changecase(func):
  @functools.wraps(func)
  def inner():
    return func().upper()
  return inner

def add(func):
  def addt():
    return "Hello "+func()+" Have a nice day"
  return addt

@changecase
@add
def myfunction():
  return "Shikha"

print(myfunction())

# after apply the decorators the original function namw is lost , so use __name__ to access the name of the original function
# and use functools.wraps to preserve the original function and docstring

print(myfunction.__name__)