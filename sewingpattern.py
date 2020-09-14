class SewingPattern():
    def __init__(self, type, company):
        self.type = type
        self.company = company
        self.price = 21.95

    def patternsale(self, sale):
        if (self.company == sale):
            print("This pattern is on sale!")
        else:
            print("This pattern is not on sale!")

    def reducePrice(self, amount):
        self.price -= amount
        print(self.price)

simplicity8186 = SewingPattern("dress", "simplicity")
simplicity8186.patternsale("burda")
simplicity8186.patternsale("simplicity")
simplicity8186.reducePrice(5)
