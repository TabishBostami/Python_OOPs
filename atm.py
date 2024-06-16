class Atm:
  def __init__(self):
    self.pin = ""
    self.balance = 0

    self.menu()

  def menu(self):
    user_input = input("""
          hello how would you like to proceed.
          1. Enter 1 to create your pin.
          2. Enter 2 to deposite your money.
          3. Enter 3 to withdraw your money.
          4. Enter 4 to check balance.
          5. Enter 5 to exit.
""")  
    if user_input == "1":
      self.create_pin()
      
    elif user_input == "2":
      self.deposite()
    elif user_input =="3":
      print("withdraw")
    elif user_input == "4":
      print("checked")
    else:
      print("bye")

  def create_pin(self):
    self.pin = input("Enter your new pin")
    print("Pin set seuccessfully")

  def deposite(self):
    temp = input("Enter your pin")
    if temp == self.pin:
      amount = int(input("Enter your amount"))
      self.balance = self.balance+amount
      print("Deposite successful")
    else:
      print("Invalid pin")

  
