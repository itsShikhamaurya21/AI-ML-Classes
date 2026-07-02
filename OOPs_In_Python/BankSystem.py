class bank:
  name="SBI"
  def __init__(self,acc_no,acc_balance):
    self.acc_no=acc_no
    self.acc_balance=acc_balance
    print("new account created ")
  
  def deposite(self,amount):
    self.acc_balance+=amount
    print("after deposite total balanced  : ",self.acc_balance)
  
  def withdraw(self,amount):
    if(self.acc_balance>=amount):
      self.acc_balance-=amount
      print("after witrhdraw total balanced : ",self.acc_balance)
    else:
      print("insufficient amount")
user1=bank(1001,10000)
user1.deposite(2000)
user1.withdraw(5000)
