# File handling is used to create, read, write, append, and delete files
# file handling in python is interacting with files to read data and write data on them 
# python provide several built in functions and methods for crating,opening , reatng and writing and closing the file 

# Types of files 
# 1. Text file----.txt, .docx, .csv, .py  
# 2. Binary file --- .png, .jpg, .mp3

# python can be used to perform read and write operation on both types of files 

# Steps 
# 1. OPEN A FILE ---    file  = open("filename.txt","mode")
            # modes ---
            # r = for reading only the file pointer is placed at beginning of the file((by default)) --- rt means r --- it by default read the text file 
            # rb = open a file only binary file , file pointer is placed at the beginning of the file.
            # r+ = perform read and write operation only on text file 
            # rb+ = perform read and write operation on binary file 
            # w = overwrite the file if the file exist / open for writing , truncating the file first , if file not exist it will create new file 
            # a = open for writing, appending to the end of the file if exist 
            # t = opening the text file 
            # b = opening the binary file 
            # w+ = open both for reading and writing 
            # x = create a new file and open it for writing  

# file = open("C:\\Users\\sahil\\Desktop\\AI-ML classes\\filehandling\\Screenshot 2026-06-22 102759.png", "rb")
# file.write("Artificial Intelligence ")
# print(file.closed)
# print(file.read())

# with open("C:\\Users\\sahil\\Desktop\\AI-ML classes\\filehandling\\demo.text","r+") as f:
#   print(f.read())

with open("C:\\Users\\sahil\\Desktop\\AI-ML classes\\filehandling\\demo.text","r+") as f:
  data=f.write("String is changed ")
  print(data)
#   f.tell() #moving pointer to beginning
  print(f.tell())


# with open("C:\\Users\\sahil\\Desktop\\AI-ML classes\\filehandling\\demo.text","r+") as f:
#   data=f.read()
#   print(data)
# list=['a','e','i','o','u','A','E','I','O','U']
# count =0
# for i in data:
#   if i in list:
#     count=count+1
  
# print(count)

# with open("C:\\Users\\sahil\\Desktop\\AI-ML classes\\filehandling\\demo.text","r+") as f:
#   line_no=1
#   for line in f:
#     if line_no%2==0:
#       print(line.strip())   #strip method removes the unnecessary lines that takes automatically by the python such as \n,\t
#     line_no+=1
# Write a fuction to seacrh a word in particular file
# write a program to update student marks of a file using roll no
# write a  program for the given file to store each student info in dictionary and returns a list of dictionary which includes the stats of the student
# create a small project of library management system that includes add book,search book, borrow and return book 
# data={}
# with open("C:\\Users\\sahil\\Desktop\\AI-ML classes\\filehandling\\data.txt","r") as f:
#   for line in f:
#     key,value=line.strip().split(":")
#     data[key]=value
# print(data)

# data = {}
# User_name=input("Enter the name ")
# with open("C:\\Users\\sahil\\Desktop\\AI-ML classes\\filehandling\\data.txt", "r") as f:
#     for line in f:
#         if line: 
#             roll,name,m1,m2,m3=line.split(",")
#             data={
#                 "Rollno":roll,
#                 "Name":name,
#                 "Marks1":int(m1),
#                 "Marks2":int(m2),
#                 "Marks3":int(m3),
#                 "marks":[int(m1),int(m2),int(m3)],
#                 "avg":(int(m1)+int(m2)+int(m3))/3

#                 }
            
            
            
        
#             if User_name == data["Name"]:
#               print(f"Rollno of {data['Name']} is {data['Rollno']}")
#               print(f"Name is ",data["Name"])
#               print(f"Hindi marks of {data['Name']} is ",data["Marks1"])
#               print(f"Math marks of {data['Name']} is ",data["Marks2"])
#               print(f"English marks of {data['Name']} is ",data["Marks3"])
#               print(f"Highest marks of {data['Name']} is", max(data["marks"]))
#               print(f"Average marks of {data['Name']} is", data["avg"])
            
              
            

# print(data)

 

#  we have to import os module to delete a file using python 
# import os 
# os.remove(file_name)
 
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





