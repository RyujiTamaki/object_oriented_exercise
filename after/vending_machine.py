from coin_type import CoinType
from drink_stock import DrinkStock
from coin_stock import CoinStock


class VendingMachine:

    def __init__(self):
        self.drink_stock = DrinkStock() # 飲み物の在庫数
        self.coin_stock = CoinStock() # お金の在庫数

    def is_coin(self, payment):
        return payment in CoinType

    def can_buy(self, payment, drink_type):
        return self.drink_stock.has_stock(drink_type) and self.coin_stock.has_charge(payment)

    def buy(self, payment, drink_type):
        '''
        ジュースを購入する.
        Parameters
        ----------
        payment      : 投入金額. 100円と500円のみ受け付ける.
        drink_type: ジュースの種類. コーラ,ダイエットコーラ,お茶が指定できる.

        Returns
        -------
        指定したジュース. 在庫不足や釣り銭不足で買えなかった場合は None が返される.
        '''

        # 100円と500円だけ受け付ける
        if not self.is_coin(payment):
            return None

        # 飲み物, コイン在庫チェック
        if not self.can_buy(payment, drink_type):
            return None

        self.coin_stock.add(payment)
        self.drink_stock.decrement(drink_type)
        return drink_type

    def refund(self):
        '''
        お釣りを取り出す.

        Returns
        -------
        お釣りの金額
        '''
        return self.coin_stock.get_charge()
