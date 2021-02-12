class Item:
    def __init__(self, code=11, name='snack', price=10, qty=1):
        self.code = code
        self.name = name
        self.price = price
        self.qty = qty

    def get_code(self):
        return self.code

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def get_qty(self):
        return self.qty

    def set_code(self, code):
        self.code = code

    def set_name(self, name):
        self.name = name

    def set_price(self,price):
        self.price = price

    def set_qty(self, qty):
        self.qty = qty

    def remove_one_item(self):
        self.qty -= 1



