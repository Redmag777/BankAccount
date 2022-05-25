class BankAccount:
    accounts = []
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        if(self.balance - amount) >= 0:
            self.balance -= amount
        else: 
            print("your balance isnt enought : Charngin a 5$ fee" )
            self.balance -= 5
    def display_account_info(self):
        print("Balance : {}".format(self.balance))
        return self
    def yield_interest(self):
        self.balance += (self.balance * self.int_rate)
        return self

Alex = BankAccount( 0.01, 0)
Nastya = BankAccount(0.01, 0)
Alex.deposit(100)
Alex.deposit(200)
Alex.deposit(300)
Alex.withdraw(300)
Alex.yield_interest()
Alex.display_account_info()
# print(Alex.balance)
Nastya.deposit(200)
Nastya.deposit(800)
Nastya.withdraw(100)
Nastya.withdraw(150)
Nastya.withdraw(300)
Nastya.withdraw(50)
Nastya.yield_interest()
Nastya.display_account_info()
# print(Nastya.balance)

@classmethod
def get_all_accounts(cls):
    for i in cls.accounts:
        i.display_account_info()