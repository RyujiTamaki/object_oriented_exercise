class Drink:
    COKE = 0
    DIET_COKE = 1
    TEA = 2

    def __init__(self, kind):
        self.kind = kind

    def get_kind(self):
        return self.kind