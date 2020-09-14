class CoffeeCup():
    def __init__(self, capacity):
        self.capacity = capacity
        self.amount = 0
    
    def fill(self):
        self.amount = self.capacity

    def empty(self):
        self.amount = 0
    
    def drink(self, amount):
        self.amount -= amount
        if (self.amount == 0):
            self.amount = 0
            print('Coffee cup is now empty')

adam_cup = CoffeeCup(8)
rome_cup = CoffeeCup(16)
elaine_cup = CoffeeCup(4)

print(rome_cup.fill())
rome_cup.empty()
rome_cup.fill()

adam_cup.fill()
adam_cup.drink(8)

