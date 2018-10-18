from vending_machine import VendingMachine
from drink_type import DrinkType
from coin_type import CoinType

if __name__ == '__main__':
    vendingMachine = VendingMachine()
    drink = DrinkType.COKE
    coin = CoinType.YEN_500
    myDrink = vendingMachine.buy(coin, drink)
    charge = vendingMachine.refund()
    print(myDrink)
    print(charge)
