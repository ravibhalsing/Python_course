"""
__init__ is a special method, also known as the "initializer" or
 "constructor."
 It is automatically called when an instance of a class is created.
 The primary purpose of the __init__ method is to initialize 
 the attributes of the object.

 Uses:
 1.Initializing Instance Variables
 2.Setting Default Values

self :
self is a convention used to represent the instance of the class
within a class method. It is the first parameter in the method signature,
including the __init__ method. When you define a method inside a class and
include self as its first parameter, it refers to the instance of the class.

Uses:
1.Accessing Instance Variables
2.Calling Other Methods
3.Creating and Modifying Instance Attributes
4.Creating Multiple Instances

"""

# Examples of class

class Customer:
    def __init__(self, customer_id, name):
        self.customer_id = customer_id
        self.name = name
        self.accounts = []

    def create_account(self, account_type, initial_balance):
        new_account = BankAccount(account_type, initial_balance)
        self.accounts.append(new_account)
        return new_account

    def __str__(self):
        return f"Customer ID: {self.customer_id}, Name: {self.name}"

class BankAccount:
    def __init__(self, account_type, balance=0):
        self.account_type = account_type
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(Transaction("Deposit", amount))
        return f"Deposit successful. New balance: {self.balance}"

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transactions.append(Transaction("Withdrawal", amount))
            return f"Withdrawal successful. New balance: {self.balance}"
        else:
            return "Insufficient funds."

    def get_balance(self):
        return f"Current balance: {self.balance}"

class Transaction:
    def __init__(self, transaction_type, amount):
        self.transaction_type = transaction_type
        self.amount = amount

    def __str__(self):
        return f"{self.transaction_type} of {self.amount}"

# Example Usage:
customer1 = Customer(1, "Ravi")
account1 = customer1.create_account("Savings", 1000)

print(customer1)
print(account1.get_balance())

account1.deposit(500)
account1.withdraw(200)

print(account1.get_balance())
print("Transactions:", [str(transaction) for transaction in account1.transactions])
