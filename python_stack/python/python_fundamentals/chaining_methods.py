class User:
    def __init__(self, username, userbalance):
        self.name = username
        self.balance = userbalance

    def make_deposit(self, amount):
        self.balance+=amount
        return self

    def make_withdrawal(self, amount):
        self.balance-=amount
        return self
    def display_user_balance(self):
        print("Username:",self.name,",","Balance:", self.balance)
        return self
    def transfer_money(self, other_user, amount):
        self.balance-=amount
        other_user.balance+=amount
        return self

user1 = User("hasan",5000)
user2 = User("moh",6300)
user3 = User("subhi",11200)

user1.make_deposit(300).make_deposit(270).make_deposit(30).make_withdrawal(200).display_user_balance()
user2.make_deposit(30).make_deposit(200).make_withdrawal(90).make_withdrawal(15).display_user_balance()
user3.make_deposit(1200).make_withdrawal(200).make_withdrawal(300).make_withdrawal(500).display_user_balance()

user1.transfer_money(user3,14000).display_user_balance()
user3.display_user_balance()
