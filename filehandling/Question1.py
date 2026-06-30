# # write a  program for the given file to store each student info in dictionary and returns a list of dictionary which includes the stats of the student

User_name=input("Enter the name ")
with open("C:\\Users\\sahil\\Desktop\\AI-ML classes\\filehandling\\data.txt", "r") as f:
    for line in f:
        if line: 
            roll,name,m1,m2,m3=line.split(",")
            data={
                "Rollno":roll,
                "Name":name,
                "Marks1":int(m1),
                "Marks2":int(m2),
                "Marks3":int(m3),
                "marks":[int(m1),int(m2),int(m3)],
                "avg":(int(m1)+int(m2)+int(m3))/3

                }
            
            
            
        
            if User_name == data["Name"]:
              print(f"Rollno of {data['Name']} is {data['Rollno']}")
              print(f"Name is ",data["Name"])
              print(f"Hindi marks of {data['Name']} is ",data["Marks1"])
              print(f"Math marks of {data['Name']} is ",data["Marks2"])
              print(f"English marks of {data['Name']} is ",data["Marks3"])
              print(f"Highest marks of {data['Name']} is", max(data["marks"]))
              print(f"Average marks of {data['Name']} is", data["avg"])
            
