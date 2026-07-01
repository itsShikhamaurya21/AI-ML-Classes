

class student:
  # default constructor
  def __init__(self):
    print("new student added ")
  # parameterised constructor 
  def __init__(self,name,age,gender):
    self.name=name
    self.age=age
    self.gender=gender
    print("\n--------------new student added---------------------- ")
student1=student("Shikha",21,"Female")
print(f"\nStudent name : {student1.name}\nAge : {student1.age}\nGender : {student1.gender}")
student2=student("Sahil",23,"Male")
print(f"\nStudent name : {student2.name}\nAge : {student2.age}\nGender : {student2.gender}")
student3=student("Azan",13,"Male")
print(f"\nStudent name : {student3.name}\nAge : {student3.age}\nGender : {student3.gender}")

