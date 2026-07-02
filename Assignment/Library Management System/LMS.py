
  
def add_book():
  print("================Add a new book ====================")
  book_id=input("Enter the book id : ")
  book_title=input("Enter the title : ")
  author=input("Enter the author name : ")
  price=input("Enter the price : ")
  status=input("Enter the status : ")
  with open("C:\\Users\\sahil\\Desktop\\AI-ML classes\\Assignment\\Library Management System\\Books.txt","a") as file:
    file.write(f"{book_id},{book_title},{author},{price},{status}\n")
    print("Book added successfully \n")
    print("=============================================")


def view_books():
  print("================View all books ====================")
  with open("C:\\Users\\sahil\\Desktop\\AI-ML classes\\Assignment\\Library Management System\\Books.txt","r") as file:
    for line in file:
      print(line.strip())

print("\n=============================================\n")


def search_book():
    print("================ Search a Book ====================")
    title = input("Enter the title: ")

    with open(r"C:\Users\sahil\Desktop\AI-ML classes\Assignment\Library Management System\Books.txt", "r") as file:
        found = False

        for line in file:
            line = line.strip()

            if not line:
                continue

            book_id, book_title, author, price, status = line.split(",")

            if book_title.lower() == title.lower():
                print("Book Found")  
                print(f"Book ID : {book_id}")
                print(f"Title   : {book_title}")
                print(f"Author  : {author}")
                print(f"Price   : {price}")
                print(f"Status  : {status}")
                found = True
                break

        if not found:
            print("Book not found")

    print("=================================================")

def issue_book():
  print("=================Issue a book==================")
  user_book_id=input("Enter the book id : ")
  with open("C:\\Users\\sahil\\Desktop\\AI-ML classes\\Assignment\\Library Management System\\Books.txt","r") as file:
    books=file.readlines()
  with open("C:\\Users\\sahil\\Desktop\\AI-ML classes\\Assignment\\Library Management System\\Books.txt","w") as file:
    found = False
    for line in books:
      book_id,book_title,author,price,status=line.strip().split(",")
      if book_id==user_book_id:
        if status.lower()=="available":
          file.write(f"{book_id},{book_title},{author},{price},issued\n")
          print(f"Book {book_title} issued successfully")
          found=True
          break
        else:
          print(f"Book {book_title} is already issued")
          found=True
          break
    if not found:
      print("Book not found")
print("=================================================\n")

def return_book():
  print("=================Return a book==================")
  user_book_id=input("Enter the book id : ")
  with open("C:\\Users\\sahil\\Desktop\\AI-ML classes\\Assignment\\Library Management System\\Books.txt","r") as file:
    books=file.readlines()
  with open("C:\\Users\\sahil\\Desktop\\AI-ML classes\\Assignment\\Library Management System\\Books.txt","w") as file:
    found = False
    for line in books:
      book_id,book_title,author,price,status=line.strip().split(",")
      if book_id==user_book_id:
        if status.lower()=="issued":
          file.write(f"{book_id},{book_title},{author},{price},available\n")
          print(f"Book {book_title} returned successfully")
          found=True
          break
        else:
          print(f"Book {book_title} is not issued")
          found=True
          break
    if not found:
      print("Book not found")
print("=================================================\n")

while True:
  print("1. Add a new book")
  print("2. View all books")
  print("3. Search a book")
  print("4. Issue a book")
  print("5. Return a book")
  print("6. Exit")
  choice=input("Enter your choice : ")
  if choice=="1":
    add_book()
  elif choice=="2":
    view_books()
  elif choice=="3":
    search_book()
  elif choice=="4":
    issue_book()
  elif choice=="5":
    return_book()
  elif choice=="6":
    break
  else:
    print("Invalid choice")

  

