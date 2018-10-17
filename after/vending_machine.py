from drink import Drink


class VendingMachine:

    def __init__(self):
        self.quantity_of_coke = 5 # コーラの在庫数
        self.quantity_of_diet_coke = 5 # ダイエットコーラの在庫数
        self.quantity_of_tea = 5 # お茶の在庫数
        self.number_of_100_yen = 10 # 100円玉の在庫
        self.charge = 0 # お釣り

    def buy(self, payment, kind_of_drink):
        '''
        ジュースを購入する.
        Parameters
        ----------
        payment            : 投入金額. 100円と500円のみ受け付ける.
        kind_of_drink: ジュースの種類. コーラ({@code Juice.COKE}),ダイエットコーラ({@code Juice.DIET_COKE},お茶({@code Juice.TEA})が指定できる.

        Returns
        -------
        指定したジュース. 在庫不足や釣り銭不足で買えなかった場合は None が返される.
        '''

        # 100円と500円だけ受け付ける
        if (payment != 100) and (payment != 500):
            self.charge += payment
            return None

        if (kind_of_drink == Drink.COKE) and (self.quantity_of_coke == 0):
            self.charge += payment
            return None
        elif (kind_of_drink == Drink.DIET_COKE) and \
                (self.quantity_of_diet_coke == 0):
            self.charge += payment
            return None
        elif (kind_of_drink == Drink.TEA) and (self.quantity_of_tea == 0):
            self.charge += payment
            return None

        # 釣り銭不足
        if payment == 500 and self.number_of_100_yen < 4:
            self.charge += payment
            return None

        if payment == 100:
            # 100円玉を釣り銭に使える
            self.number_of_100_yen += 1
        elif payment == 500:
            # 400円のお釣り
            self.charge += (payment - 100)
            # 100円玉を釣り銭に使える
            self.number_of_100_yen -= (payment - 100) / 100

        if kind_of_drink == Drink.COKE:
            self.quantity_of_coke -= 1
        elif kind_of_drink == Drink.DIET_COKE:
            self.quantity_of_diet_coke -= 1
        else:
            self.quantity_of_tea -= 1

        return Drink(kind_of_drink)

    def refund(self):
        '''
        お釣りを取り出す.

        Returns
        -------
        お釣りの金額
        '''
        result = self.charge
        self.charge = 0
        return result