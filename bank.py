class User:
    bank_name = "Chase"

    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdrawal(self, amount):
        self.account_balance -= amount

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount

    def display_user_balance(self):
        print(self.name)
        print(self.account_balance)


duy = User("Duy Pham", "dcatp408@gmail.com")
cat = User("Cat Pham", "phamsee@gmail.com")
danh = User("Danh Pham", "phamooooo@gmail.com")

duy.make_deposit(100)
duy.make_deposit(50)
duy.make_deposit(200)
duy.make_withdrawal(140)
duy.transfer_money(danh, 100)
print(duy.display_user_balance())

cat.make_deposit(1000)
cat.make_deposit(300)
cat.make_withdrawal(200)
cat.make_withdrawal(50)
print(cat.display_user_balance())

danh.make_deposit(5000)
danh.make_withdrawal(50)
danh.make_withdrawal(75)
print(danh.display_user_balance())
