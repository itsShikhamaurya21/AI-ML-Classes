# write a program to update student marks of a file using roll no



roll=input("Enter the roll no : ")
new_marks=input("Enter the marks ")
with open("C:\\Users\\sahil\\Desktop\\AI-ML classes\\filehandling\\data.txt","r") as file:
  marks=file.readlines()
with open("C:\\Users\\sahil\\Desktop\\AI-ML classes\\filehandling\\data.txt","w") as file:
  for x in marks:
    data=x.strip().split(",")
    if(data[0]==roll):
      data[2]=new_marks
      print("marks updated successfully ")

    file.write(",".join(data)+"\n") 

#  join works as convert the list into string  

