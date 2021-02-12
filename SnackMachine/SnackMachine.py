from SnackMachine.State import *
from SnackMachine.cash import Cash
from SnackMachine.items_inventory import itemsInvetory


class SnackMachine:
    def __init__(self):
        self.state=Ready(self)
        self.items = itemsInvetory()
        self.amount = 0
        self.selected_item = None

    def set_selected_item(self, code):
        self.selected_item = self.items.get_item(code)

    def get_selected_item(self):
        return self.selected_item

    def add_cash(self, amount, cash_type, currency, payment_method):
        cash = Cash(amount, cash_type, currency, payment_method)
        if cash.validate_payment():
            self.amount = cash.get_amount()
            return True
        else:
            return False

    def set_collected_cash(self, amount):
        self.amount= amount

    def set_state(self, state):
        self.state = state

    def get_state(self):
        return self.state

    def calculate_change(self):
        return   int(self.get_selected_item().get_price()) - self.amount

    def remove_item(self):
        self.items.remove_item(self.selected_item)

    def get_collected_cash(self):
        return self.amount

    def collection_cash(self,  amount, cash_type, currency, payment_method):
        self.state.collection_cash( amount, cash_type, currency, payment_method)

    def return_change(self, ):
        self.state.return_change()

    def drop_item(self):
        self.state.drop_item()

    def cancel_process(self):
        self.state.cancel_process()


