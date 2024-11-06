class BalanceException(Exception): # to check if there is enough money to complete the transaction
    pass

class BankAccount:
    def __init__(self,initialAmount,acctName):
        self.balance = initialAmount # make an object
        self.name = acctName
        print(f"\nAccount '{self.name}' created . \nBalance = ${self.balance:.2f} .")
    
    def getBalance(self):
        print(f"\nAccount '{self.name}' Balance = ${self.balance:.2f} .")

    def deposit(self,amount):
        self.balance = self.balance+ amount
        # print(f"\nDeposit complete.\nAccount '{self.name}' Balance = ${self.balance:.2f} .")
        # instead of previous print => print deposit , call self.getBalance
        print(f"\nDeposit complete.")
        self.getBalance()
    
    def ViableTransaction(self,amount): # validity of process
        if self.balance >= amount:
            return
        else :
            raise BalanceException(f"Sorry , account '{self.name}' only has a balance ${self.balance:.2f}")  # error message
    

    def withdraw(self,amount):
        try:
            self.ViableTransaction(amount)
            self.balance = self.balance - amount
            print("\nWithdraw complete!")
            self.getBalance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted :\n{error}")

    def transfer(self,amount,account):
        try: 
            print("\n************\n\nbeginning transfer***********")
            self.ViableTransaction(amount) # is that amount for that account is valid or not
            self.withdraw(amount)
            account.deposit(amount)
            print("\ntransfer complete!\n\n*************")
        except BalanceException as error:
            print(f"\nTransfer interrupted : \n{error}")

class InterestRewardAcct(BankAccount): #inherite from BankAccount class all except what I write bellow
    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print("\nDeposit complete!")
        self.getBalance()

class SavingAcct(InterestRewardAcct):
    def __init__(self, initialAmount, acctName):
        super().__init__(initialAmount, acctName)
        self.fee = 5

    def withdraw(self, amount):
        try:
            self.ViableTransaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print("\nWithdraw completed")
            self.getBalance()
        
        except BalanceException as error :
            print(f"\nWithdraw interrupted : {error}")





    

    


        