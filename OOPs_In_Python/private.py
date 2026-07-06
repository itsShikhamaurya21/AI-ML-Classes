class login:
  def __init__(self,name,__password):
    self.name=name
    self.__password=__password

  def get_password(self):
    print(self.__password)

  def __id(self):
    print("Id is 121")

  def getId(self):
    self.__id()
    print("Call private method ")


user1=login("Shikha",1234)
user1.get_password()
user1.getId()
print(user1.name)
    