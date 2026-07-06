# Create a console based expense tracker program in Python that allows the user to record daily expenses and view summaries like total spending.

"""1.Add an expense with details like date, category, description,and amount 
2.view all records expense clean format 
3.calculate total spending so far 
4.exit the program gracefully when the user chooses to"""

'''Sample output 

Welcome to Expense Tracker
===========MENU==============
1.Add expense 
2.View all expenses
3. View total spending
4.exit
==============================
Enter your choice (1-4):
Enter date (DD-MM-YYYY): 05-11-2025'''

expenses=[] #list of all expenses 
print("WELCOME TO EXPENSE TRACKER")
# Add expenses 
def add_expenses():
  print("\n=============================")
  date = input("Enter date (DD-MM-YYYY): ")
  category=input("Which category(food, travel, shopping, Books) ?")
  description=input("Enter short description about your expenses : ")
  amount=float(input("Enter the amount you expend  :"))
  if amount<=0:
    print("Amount should be greater than 0 ")
    return 
  else :
    expense={
      "date":date,
      "category":category,
      "description":description,
      "amount":amount
    }

    expenses.append(expense)
    print("DONE !!!  Expenses added successfully\n")
    print("\n=============================")
    pass

# View expenses

def view_expenses():
  if len(expenses)==0:
    print("No expenses added ")
  else:
    print("=======view your expenses=======")
    count=1
    for expense in expenses:
      print("\n---------------------------------")
      print(f" Date       :    {expense['date']}")
      print(f" Category   :    {expense['category']}")
      print(f" Description:    {expense['description']}")
      print(f" Amount     :    {expense['amount']}")
      
      count=count+1

      print("\n----------------------------------")
    pass


# view total spending
def view_total_spend():
  total=0;
  for totalamount in expenses:
    total=total+totalamount["amount"]
  print("\n=============================")
  print("\n Total spend Money : \n",total)
  print("\n=============================")
  pass

      

while True:
  print("1. ADD EXPENSES :")
  print("2. VIEW ALL EXPENSES :")
  print("3. VIEW TOTAL SPENDING :")
  print("4. EXIT :")
  choice=int(input("Enter the Choice what you want to do : "))
  
  if choice==1:
    
    add_expenses()
  elif choice==2:
    view_expenses()
  elif choice==3:
    view_total_spend()
  elif choice==4:
    print("\n=====================================")
    print("Thank you for using Expense Tracker !!")
    print("\n=====================================")
    break
  else:
    print("Invalid choice ")



