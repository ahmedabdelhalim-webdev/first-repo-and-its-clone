from oop_bank_accounts import *
# import module(file script name not begin with number to use its functions or classes)
hassan = BankAccount(1000,"Hassan")
li = BankAccount(2000,"li young")
dave = BankAccount(5000,"Dave")
gamil = BankAccount(9000,"gamil")

hassan.getBalance() # what is in his account
li.getBalance()
dave.getBalance()
gamil.getBalance()

hassan.deposit(5000)
li.deposit(1000)
dave.deposit(2000)
gamil.deposit(1000)

li.withdraw(5000)
gamil.withdraw(5000)

dave.transfer(5000,hassan)
gamil.transfer(17000,dave)

madbouly = InterestRewardAcct(1000,"mad")
madbouly.getBalance()
madbouly.deposit(100)
madbouly.transfer(100,li)

hamdy = SavingAcct(5000,"hamdy")
hamdy.getBalance()
hamdy.deposit(500)
hamdy.transfer(10000,li)