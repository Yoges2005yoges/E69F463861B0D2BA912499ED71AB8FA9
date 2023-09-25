class BankAccount:
  def __init__(self, account_number,account_holder_name, initial_balance=0.0):
self.__account_number=account_number
self.__account_holder_name=account_holder_name
self.__account_holder_name=account_holder_name
self.__account_balance=initial_balance
  def deposite(self,amount):
    if amount>0:
      self.__account_balance+=amount
      print("Deposited  ₹{}. New balance: ₹{}".format(amount,self.__account_balance))
    else:
      print("Invalid deposit amount.")
      
  def withdraw(self,amount):
    if amount>0 and amount<=self.__account_balance:
      self.__account_balance-=amount
      print("withdraw₹{}.Newbalance:₹{}". format(amount,self.__account_balance))
    else:
      print("Invalid withdraw amount or insufficient balance.")

  def display_balance(self):
    print("Account balance for {} (account #{}):₹{}".format(self.__account_holder_name,self.__account_number,self.__account_balance))

account=BankAccount(account_number="123456789",account_holder_name="Maha",initial_balance=5000.0)

account.display_balance()
account.deposite(500.0)
account.withdraw(200.0)
account.withdraw(20000.0)
account.display_balance()