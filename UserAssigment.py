class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        return self
        
    def withdraw(self, amount):
        if self.balance < amount:
            print(f"Insufficient Funds!, Balance is currently:{self.balance}. Your withdraw request of {amount} can't be completed.")
        else:
            self.balance -= amount
            return self
    def display_account_info(self):
        print(f"Account info your current balance: ${self.balance}")

    def yield_interest(self):
        self.balance = self.balance + (self.balance * self.int_rate)
        print(f"you have an interest rate of {self.int_rate}, your new balance is: ${self.balance}")
        return self
jean_account = BankAccount(0.001, 2000)
chris_account = BankAccount(0.01, 5000)

jean_account.deposit(100).deposit(200).deposit(100).withdraw(1000).yield_interest().display_account_info()
chris_account.deposit(2900).deposit(1999).withdraw(800).withdraw(400).yield_interest().display_account_info()

class User:
    def __init__(self, name, email,):
        self.name = name
        self.email = email
        self.acount_balance = BankAccount(0.02, 2000)
        

    def make_deposit(self,amount):
        self.acount_balance.balance += amount
        return self
    def make_withdraw(self, amount):
        self.acount_balance.balance -= amount
        return self
    def display_user_balance(self,acount_balance):
        self.acount_balance.balance
        return self
    # bonus have this method decrease the user's balance by the amount and add that amount to other other_user's balance
    #was not able to 
    def transfer_money(self, amount, user):
        self.amount -= amount
        user.amount += amount
        self.display_user_balance()
        user.display_user_balance()


guido = User("Guido Van Rossum", "guidoman@python.com")
marty = User("Marty Johson", "martinluis@google.com")
jake = User("Jake Lukas", "jakejumping@yallow.com")

guido.make_deposit(300).make_deposit(500).make_deposit(200).make_withdraw(400)

marty.make_deposit(400).make_deposit(400).make_withdraw(200).make_withdraw(100)

jake.make_deposit(1000).make_withdraw(300).make_withdraw(200).make_withdraw(100)

print("guido's account balance: $" + str(guido.acount_balance.balance))
print("Marty's account balance: $" + str(marty.acount_balance.balance))
print("jake's account balance: $" + str(jake.acount_balance.balance))


