from abc import abstractmethod


class State:
    def __init__(self, snack_machine):
        self.snack_machine = snack_machine

    @abstractmethod
    def collection_cash(self, amount, cash_type, currency, payment_method):
        pass

    @abstractmethod
    def return_change(self):
        pass

    @abstractmethod
    def drop_item(self):
        pass

    @abstractmethod
    def cancel_process(self):
        pass


class Ready(State):

    def __init__(self, snack_machine):
        super(Ready, self).__init__(snack_machine)

    def collection_cash(self, amount, cash_type, currency, payment_method):

        if not self.snack_machine.add_cash(amount, cash_type, currency, payment_method):
            self.snack_machine.set_state(CancelState(self.snack_machine))
            self.snack_machine.cancel_process()

    def return_change(self):
        self.snack_machine.set_state(ReturnChargeSate(self.snack_machine))
        self.snack_machine.return_change()

    def drop_item(self):
        print("you cannot drop item")

    def cancel_process(self):
        self.snack_machine.set_state(CancelState(self.snack_machine))
        self.snack_machine.cancelProcess()


class ReturnChargeSate(State):

    def __init__(self, snack_machine):
        super(ReturnChargeSate, self).__init__(snack_machine)

    def collection_cash(self, amount, cash_type, currency, payment_method):
        print("you cannot insert money in money return process")

    def return_change(self):
        change = self.snack_machine.calculate_change()
        self.snack_machine.set_state(DropItemState(self.snack_machine))
        print(change , 'amount of money returned')
        self.snack_machine.drop_item()

    def drop_item(self):
        print("unable to  drop item now in money return process")

    def cancel_process(self):
        print(" unable cancel process now in money return process")


class DropItemState(State):

    def __init__(self, snack_machine):
        super(DropItemState, self).__init__(snack_machine)

    def collection_cash(self, amount, cash_type, currency, payment_method):
        print("Unable to  insert money in drop item process")

    def return_change(self):
        print("Unable to return money in drop item process")

    def drop_item(self):
        self.snack_machine.remove_item()
        print(self.snack_machine.get_selected_item().get_name(), 'item is dropping ')
        self.snack_machine.set_state(Ready(self.snack_machine))

    def cancel_process(self):
        print("Unable to cancel process in drop item process")


class CancelState(State):
    def __init__(self, snack_machine):
        super(CancelState, self).__init__(snack_machine)

    def collection_cash(self, amount, cash_type, currency, payment_method):
        print("Unable to  insert money in cancel  process")

    def return_change(self):
        print("Unable to return money in cancel process")

    def drop_item(self):
        print("unable to drop item now in money return process")

    def cancel_process(self):
        print("return ", self.snack_machine.get_collected_cash())
        self.snack_machine.set_collected_cash(0)
        self.snack_machine.set_state(Ready(self.snack_machine))
