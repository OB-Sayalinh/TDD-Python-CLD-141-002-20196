from logging import fatal

from .items import Item
from .basics import tax, RoundingMethod, RoundingFlags

round_method = RoundingMethod(RoundingFlags.Ceil | RoundingFlags.Whole | RoundingFlags.NinetyNine)

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

    price = find_price(items, taxed=False, as_string=True, b_round=False)

    taxed_price = find_price(items, as_string=True)

    receipt += "Total: ${total}\n".format(total=price)
    receipt += "Tax: {tax}%\n".format(tax=round(tax * 100, 2))
    receipt += "Final Total: ${final}\n".format(final=taxed_price)

    return receipt

def find_price(items, taxed=True, as_string=False, b_round=True):
    """

    Parameters
    ----------
    items : list of Item
    taxed : bool, optional
    as_string : bool, optional
    b_round : bool, optional

    Returns
    -------
    float : if as_string is False
    string : if as_string is True
    """
    price = 0
    for item in items:
        price += item.get_price

    if taxed:
        price *= tax + 1

    # Turns price to string
    if b_round:
        price = round_method.round(price)

    if not as_string:
        price = float(price)

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
        return find_price(self.__items__, taxed=False)

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







