# Search a word in a particular file
word=input("Enter the word :")
flag=False
with open("C:\\Users\\sahil\\Desktop\\AI-ML classes\\filehandling\\data.txt", "r") as file:
   for line in file:
      if word in line:
         flag=True
         print("Found",line.strip())
if flag==False:
   print("Not found")