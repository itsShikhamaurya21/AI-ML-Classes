# write a program to update student marks of a file using roll no
new_roll_No=input("Enter the roll no : ")
new_marks=input("Enter the marks ")
with open("C:\\Users\\sahil\\Desktop\\AI-ML classes\\filehandling\\data.txt","r+") as file:
  for line in file:
    if line:
      roll,name,m1,m2,m3=line.split(',')
      if roll in line:
        m1.replace(m1,new_marks)
        m2.replace(m1,new_marks)
        m3.replace(m1,new_marks)

