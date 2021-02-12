from SnackMachine.items import Item


class itemsInvetory:
    def __init__(self):
        self.list_items = {11: Item()}

    def get_item(self, key):
        return self.list_items[key]
        pass

    def remove_item(self, item):
        self.get_item(item).remove_one_item()


