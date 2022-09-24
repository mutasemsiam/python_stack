class User:
    def __init__(self, username, userbalance):
        self.name = username
        self.balance = userbalance

    def make_deposit(self, amount):
        self.balance+=amount

    def make_withdrawal(self, amount):
        self.balance-=amount

    def display_user_balance(self):
        print("Username:",self.name,",","Balance:", self.balance)

    def transfer_money(self, other_user, amount):
        self.balance-=amount
        other_user.balance+=amount

user1 = User("hasan",5000)
user2 = User("moh",6300)
user3 = User("subhi",11200)
# user1.make_deposit(300)
# user1.make_deposit(270)
# user1.make_deposit(30)
# user1.make_withdrawal(200)
# user1.display_user_balance()

# user2.make_deposit(30)
# user2.make_deposit(200)
# user2.make_withdrawal(90)
# user2.make_withdrawal(15)
# user2.display_user_balance()

# user3.make_deposit(1200)
# user3.make_withdrawal(200)
# user3.make_withdrawal(300)
# user3.make_withdrawal(500)
# user3.display_user_balance()

# user1.transfer_money(user3,14000)
# user1.display_user_balance()
# user3.display_user_balance()

