balance = float(input("enter balance: "))
deposit = float(input("enter amount: "))
balance = balance + deposit
print ("Updated balance after deposit",balance)
withdraw = float(input("enter amount to withdraw:"))
if withdraw <= balance:
    balance = balance - withdraw 
    print("amount withdrawn:",withdraw)
    print("new balance is:",balance)
else:
  print("current balance:")
