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
    price = 0
    for item in items:
        flavors = "- "
        for flavor in item.get_flavors:
            flavors += flavor.name + ", "
        flavors = flavors[:-2] + ""
        receipt += "{fname} {fflavors}: ${fprice}\n".format(fname=item.get_name,
                                                            fflavors=flavors,
                                                            fprice=item.get_price)
        price += item.get_price

    receipt += "Total: ${total}\n".format(total=price)
    receipt += "Tax: ${tax}\n".format(tax=tax*100)
    receipt += "Final Total: ${final}\n".format(final=price*(tax+1))

    return receipt

def find_price(items, taxed=True):
    """

    Parameters
    ----------
    items : list of Item
    taxed : bool, optional

    Returns
    -------
    float
    """
    price = 0
    for item in items:
        price += item.get_price()

    if taxed:
        price *= tax

    return price


class Order:
    """Information on ordered items"""
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
        """

        Parameters
        ----------
        item : Item
        """
        self.__items__.append(item)

    def remove_item(self, index):
        """Pops item in the specified index

        Parameters
        ----------
        index : int
        """
        self.__items__.pop(index)







