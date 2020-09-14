class BankAccount():
    def __init__(self, type, pin):
        self.type = type
        self.balance = 0
        self.overdraft_fees = 0
        self.pin = pin
    def deposit(self, amount):
        self.balance += amount
    
    def withdrawal(self, amount, pin_from_user):
        if(self.pin == pin_from_user):
            
            if(self.balance < amount):
                print("Sorry, you don't have that amount in your account.")
                return 
            elif (self.balance == amount):
                self.balance -= amount
                print("You are now empty")
            else:
                self.balance -= amount
                print("Current balance is now {}".format(self.balance))
        else:
            print('The pin number is incorrect, try again')

        # if (self.balance <0):
        #     self.overdraft_fees += 36
        # return amount

    def change_pin(self, pin):
        self.pin = pin
        print(f"The new pin number is {self.pin}")

elaine_checking = BankAccount("checking", 1234)
print("my new account is a {} account".format(elaine_checking.type))

elaine_checking.deposit(3000)
# print("My current balance is ${}".format(elaine_checking.balance))

elaine_checking.withdrawal(1500, 20)
# print("My current balance is ${}".format(elaine_checking.balance))

elaine_checking.withdrawal(2000, 1234)
print("My overdraft fee is currently {}".format(elaine_checking.overdraft_fees))

elaine_checking.change_pin(4000)
print("My new pin is {}".format(elaine_checking.pin))