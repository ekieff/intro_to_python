class BankAccount():
    def __init__(self, type):
        self.type = type
        self.balance = 0
        self.overdraft_fees = 0
    def deposit(self, amount):
        self.balance += amount
    
    def withdrawal(self, amount):
        self.balance -= amount  