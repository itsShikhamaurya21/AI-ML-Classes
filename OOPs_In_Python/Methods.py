class car:
  brand="BMW"
  def __init__(self,model,color,price):
    self.model=model
    self.color=color
    self.price=price
    print("new car added ")
  
  def available_car(self):
    if(self.color=="red"):
      print("Available")
    else:
      print("Not available")

car1=car("B3001","red",10000000)
car1.available_car()
car2=car("B3002","blue",1000000)
car2.available_car()