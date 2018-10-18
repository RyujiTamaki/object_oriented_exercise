from coin_type import CoinType


class CoinStock:

    def __init__(self):
        self.coin_stocks = {}
        self.refund = {}
        for coin_type in CoinType:
            self.coin_stocks[coin_type] = 100
            self.refund[coin_type] = 0

    def add(self, coin_type):
        if coin_type == CoinType.YEN_100:
            self.coin_stocks[CoinType.YEN_100] += 1
        if coin_type == CoinType.YEN_500:
            self.refund[CoinType.YEN_100] += 4
            self.coin_stocks[CoinType.YEN_100] -= 4

    def decrement(self, coin_type):
        self.coin_stocks[coin_type] -= 1

    def get_quantity(self, coin_type):
        return self.coin_stocks[coin_type]

    def has_charge(self, coin_type):
        if coin_type == CoinType.YEN_100:
            return True
        if coin_type == CoinType.YEN_500:
            return True if self.get_quantity(CoinType.YEN_100) >= 4 else False

    def get_charge(self):
        charge = []
        for coin_type, coin_num in self.refund.items():
            for _ in range(coin_num):
                charge.append(coin_type)
        self.refund = {}
        return charge
