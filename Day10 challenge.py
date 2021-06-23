class bank_account:
    def __init__(self):
        self.balance=0.0
        print("hello, welcome to cash deposit and withdrawal machine")
    def display(self):
        print("your current balance is:",self.balance)
class deposit(bank_account):
    def deposit1(self):
        amount=float(input("Enter amount to be deposit: "))
        self.balance+=amount
        print("Your amount",amount,"is successfully deposited in your account")
class withdrawal(deposit):
    def withdraw(self):
        amount1=float(input("enter the amount want to be withdraw:"))
        if(amount1<=self.balance):
            self.balance-=amount1
            print("Rs.",amount1,"is debited from your account")
        else:
            print("balance insufficient, please check your account balance")
k=bank_account()
k.display()
l=deposit()
l.deposit1()
m=withdrawal()
m.withdraw()