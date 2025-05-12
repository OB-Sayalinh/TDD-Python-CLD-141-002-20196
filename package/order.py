from basics import tax, RoundingMethod, RoundingFlags, Item
from package.food import Food
from package.drink import Drink

untaxed_rounding = RoundingMethod(RoundingFlags.Ceil | RoundingFlags.Whole | RoundingFlags.NinetyNine)
taxed_rounding = RoundingMethod(RoundingFlags.Fifths)

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
    item_rounding = RoundingMethod(RoundingFlags.Ceil)
    receipt = ''
    price = 0
    for count in range(len(items)):
        item = items[count]
        add_str = ''
        if type(item) is Drink:
            flavors = ''
            for flavor in item.get_flavors:
                flavors = ''.join([flavors, flavor.name, ', '])
            flavors = flavors[:-2]
            price = item_rounding.round(item.get_price)
            add_str = ''.join([add_str, '{name} ({base}) {flavors}: ${price}' \
                            .format(name=item.get_name,
                            base = item.get_base.value,
                            flavors=flavors,
                            price=price)])
        elif type(item) is Food:
            toppings = ''
            for topping in item.get_toppings:
                toppings = ''.join([toppings, topping.name, ', '])
            toppings = toppings[:-2]
            price = item_rounding.round(item.get_price)
            add_str = ''.join([add_str, '{name} ({food_choice}) {toppings}: ${price}' \
                            .format(name=item.get_name,
                            food_choice=item.get_food_choice.value,
                            toppings=toppings,
                            price=price)])

        receipt = ''.join([receipt, add_str])

        if not count == len(items):
            receipt = ''.join([receipt, '\n'])

    price = find_price(items, taxed=False, as_string=True, b_round=True)

    taxed_price = find_price(items, as_string=True)

    receipt = ''.join([receipt, 'Total: ${total}\n'.format(total=price)])
    receipt = ''.join([receipt, 'Tax: {tax}%\n'.format(tax=round(tax * 100, 2))])
    receipt = ''.join([receipt, 'Final Total: ${final}\n'.format(final=taxed_price)])

    return receipt

def find_price(items, taxed=True, as_string=False, b_round=True,
               before_tax_rounding=None, after_tax_rounding=None):
    """

    Parameters
    ----------
    items : list of Item
    taxed : bool, default True
    as_string : bool, default False
    b_round : bool, default True
    before_tax_rounding : RoundingMethod, optional
    after_tax_rounding : RoundingMethod, optional

    Returns
    -------
    float : if as_string is False
    string : if as_string is True
    """
    if before_tax_rounding is None:
        before_tax_rounding = untaxed_rounding
    if after_tax_rounding is None:
        after_tax_rounding = taxed_rounding

    price = 0
    for item in items:
        price += item.get_price

    # Returns as string
    if b_round:
        price = before_tax_rounding.round(price)

    # Returns as string
    if taxed:
        price = float(price)
        price *= tax + 1
        price = after_tax_rounding.round(price)

    if not as_string:
        price = float(price)
    else:
        price = str(price)

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







