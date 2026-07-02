# class stats:
#   marks1=int(input("Enter marks1 of student 1 : "))
#   marks2=int(input("Enter marks2 of student 1 : "))
#   marks3=int(input("Enter marks3 of student 1 : "))
#   marks=[marks1,marks2,marks3]
#   def avg(self,marks):
#     avg=sum(self.marks)/len(marks)
#     print(avg)
#     Min=min(self.marks)
#     print(Min)
#     Max=max(self.marks)
#     print(Max)
    
# stu1=stats()
# avg=stu1.avg(stu1.marks)

class stats:
  def __init__(self,marks):
    self.marks=marks
    print("Find the avg, min and max")

  def stats(self):
    sum=0;
    for val in self.marks:
      sum+=val
    print(f"avg marks {sum/len(self.marks)}, min marks {min(self.marks)}, max marks {max(self.marks)}")
stu1=stats([23,45,67])
stu1.stats()

