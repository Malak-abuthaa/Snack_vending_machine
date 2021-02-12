from SnackMachine.Exceptoins import Execptions


class Cash:
    def __init__(self, amount, cash_type, currency, payment_method):
        if cash_type == 'c':
            self.amount = amount/100
        else:
            self.amount = amount

        self.cash_type = cash_type
        self.currency = currency
        self.payment_method = payment_method

    def get_amount(self):
        return self.amount

    def validate_payment(self):
        if self.cash_type == 'c' and self.amount not in(10, 20, 50):
            Execptions.slot_c_exception()

        elif self.cash_type == '$' and self.amount != 1:
            Execptions.slot_exception()

        elif self.cash_type == 'Note' and self.amount not in (20, 50):
            Execptions.note_exception()

        elif self.currency != 'USD':
            Execptions.currency_exception()





