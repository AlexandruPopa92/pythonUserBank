class BankAccount:
    def __init__(self,balance=0,interest_rate=0.01):
        self.balance=balance
        self.interest_rate=interest_rate
    
    def deposit(self,amount):
        self.balance += amount
        return self
    
    def withdraw(self,amount):
        self.balance-=amount
        if self.balance<=0:
            print("Insufficient funds: Charging a $5 fee")
            self.balance=self.balance-5     
            return self
        else:
            return self
    
    def display_account_info(self):
        print(f"Balance:{self.balance}\nInterest rate:{self.interest_rate}")
    
    def yield_interest(self):
        if self.balance<=0:
            print(f"Balance negative : {self.balance}")
            return self
        else:
            self.balance=self.balance+self.balance*self.interest_rate
        return self


class User:
    def __init__(self, name,last_name, email):
        self.name = name
        self.last_name= last_name
        self.email = email
        self.account = BankAccount(balance=0,interest_rate=0.01)

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self
    
    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self
    
    def display_user_balance(self):
        print(f"User: {self.name} {self.last_name}\nBalance = {self.account.balance}\n Interest = {self.account.interest_rate}")


alex=User("Alex","Popa","popa@gmail.com")
bob=User("Bob","Smith","bob@gmail.com")
alex.make_deposit(1000).make_withdrawal(50).display_user_balance()
bob.make_deposit(130).make_withdrawal(200).display_user_balance()
