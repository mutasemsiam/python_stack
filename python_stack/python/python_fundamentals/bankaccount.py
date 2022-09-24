class BankAccount:
    def __init__(self, int_rate = 0.01, balance = 0) -> None:
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


account1 = BankAccount(0.07, 9000)
account2 = BankAccount(0.03, 1400)

account1.deposit(500).deposit(1000).deposit(1000).withdraw(500).yield_interest().display_account_info()
account2.deposit(100).deposit(200).withdraw(400).withdraw(50).withdraw(50).withdraw(100).yield_interest().display_account_info()

