from items import Item
from basics import tax

def make_receipt(items):
    """Return the receipt of all items

    Parameters
    ----------
    items : list of Item

    Returns
    -------
    string
        Formatted by name, flavors, and price
    """
    receipt = ""
    for item in items:
        flavors = "- "
        for flavor in item.get_flavors:
            flavors += flavor.name + ", "
        flavors = flavors[:-2] + ""
        receipt += "{fname} {fflavors}: ${fprice}\n".format(fname=item.get_name,
                                                            fflavors=flavors,
                                                            fprice=item.get_price)
    return receipt

def find_price(items):
    price = 0
    for item in items:
        price += item.get_price()
    return price * tax


class Order:

    def __init__(self):
        self.__items__ = []

    @property
    def get_items(self):
        return self.__items__

    @property
    def get_total(self):
        return find_price(self.__items__)

    @property
    def get_num_items(self):
        return len(self.__items__)

    @property
    def get_receipt(self):
        return make_receipt(self.__items__)

    def add_item(self, item):
        self.__items__.append(item)

    def remove_item(self, index):
        self.__items__.pop(index)
