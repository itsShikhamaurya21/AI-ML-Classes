books=[]
while(True):
  print("1.Add book ")
  print("2.Search the book ")
  print("3.Issue book ")
  print("4.Return book ")
  print("5. Views all books ")
  print("5.Exit ")
  choice=int(input("Enter the Choice : "))
  
  match choice:
    case 1:
      print("\n-------------------ADD A BOOK-------------------------\n")
      
      title=input("Title of book : ")
      author=input("Author of book : ")
      price=float(input("Price of book : "))
      book={
        "Title":title,
        "Author":author,
        "Price":price
      }
      books.append(book)
      print("\n(:----Book added---:)\n")
      print(books)
    case 2:
      print("\n------------------Search A BOOk---------------------------\n")
      searchBook=input("Enter the book for searching : ")
      flag=False
      for book in books:
        if book["Title"].lower()==searchBook.lower():
          flag=True
          print("Book found ")
          print(book)
          break
      if not flag:
        print("Book not found ")
    case 3:
      print("\n-------------------ISSUE BOOK-------------------------------\n")
      issue=input("Enter the book you want to issued : ")
      for book in books


  
    case _:
      print("Invalid Choice ")
  print("\nThank you for using my LMS :)\n")