from drink_type import DrinkType


class DrinkStock:

    def __init__(self):
        self.drink_stocks = {}
        for drink_type in DrinkType:
            self.drink_stocks[drink_type] = 100

    def decrement(self, drink_type):
        self.drink_stocks[drink_type] -= 1

    def get_quantity(self, drink_type):
        return self.drink_stocks[drink_type]

    def has_stock(self, drink_type):
        return True if self.get_quantity(drink_type) > 1 else False
