class BankAccount:
    def __init__(self, int_rate = 0.01, balance = 0):
        self.interestrate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance+=amount
        return self

    def withdraw(self, amount):
        if self.balance - amount >0:
            self.balance-=amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance-=5
        return self

    def display_account_info(self):
        print("Balance:", self.balance)
        return self

    def yield_interest(self):
        if self.balance>0:
            self.balance= self.balance + self.balance*self.interestrate
        return self
    

class User():
    def __init__(self, username):
        self.name = username
        self.account = [BankAccount(int_rate=0.02, balance=0)]

    def create_new_account(self,int_rate,balance):
        self.account.append(BankAccount(int_rate,balance))

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        self.account.display_account_info()

    def transfer_money(self, other_user, amount):
        self.account.withdraw(amount)
        other_user.account.deposit(amount)
        return self
