import unittest
from enum import Enum, StrEnum
from venv import create


# Drink Enums

class Bases(Enum):
    Water = 'water',
    Sbrite = 'sbrite',
    Pokeacola = 'pokeacola',
    MrSalt = 'mr. salt',
    HillFog = 'hill fog',
    LeafWine = 'Leaf Wine'


class Flavors(Enum):
    Lemon = 'lemon',
    Cherry = 'cherry',
    Strawberry = 'strawberry',
    Mint = 'mint',
    Blueberry = 'blueberry',
    Lime = 'lime'




# Prices


prices = {
    Bases.Water : 1,
    Bases.MrSalt : 1,
    Bases.Sbrite: 1,
    Bases.HillFog: 1,
    Bases.LeafWine: 1,
    Bases.Pokeacola: 1,
    Flavors.Lime : 1,
    Flavors.Mint : 1,
    Flavors.Lemon : 1,
    Flavors.Cherry : 1,
    Flavors.Blueberry : 1,
    Flavors.Strawberry : 1,
}

tax = 0.0675

def find_price(items):
    price = 0
    for item in items:
        price += prices[item]
    return price * tax

# Making A Receipt

def make_receipt(items):
    receipt = ""

    for item in items:
        flavors = "- "
        for flavor in item.get_flavors():
            flavors += flavor.name + ", "
        flavors = flavors[:-2] + ""
        receipt += "{fname} {fflavors}: ${fprice}\n".format(fname=item.get_name(),
                                                                        fflavors=flavors,
                                                                        fprice=item.get_price())

    return receipt


# Main Classes


class Order:

    def __init__(self):
        self.__items__ = []

    def get_items(self):
        return self.__items__

    def get_total(self):
        return find_price(self.__items__)

    def get_num_items(self):
        return len(self.__items__)

    def get_receipt(self):
        return make_receipt(self.__items__)

    def add_item(self, item):
        self.__items__.append(item)

    def remove_item(self, index):
        self.__items__.pop(index)


class Drink:

    def __init__(self, name, base):
        self.__base__ = base
        self.__flavors__ = []
        self.__name = name

    def get_base(self):
        return self.__base__

    def get_flavors(self):
        return self.__flavors__

    def get_num_flavors(self):
        return len(self.__flavors__)

    def get_price(self):
        price = prices[self.__base__]
        for flavor in self.__flavors__:
            price += prices[flavor]

        return price

    def get_name(self):
        return self.__name

    def set_flavors(self, flavors):
        temp_flavors = []
        for flavor in flavors:
            if not temp_flavors.count(flavor):
                temp_flavors.append(flavor)
        self.__flavors__ = temp_flavors

    def add_flavor(self, flavor):
        if not self.__flavors__.count(flavor):
            self.__flavors__.append(flavor)


# Testing

def create_drink(name="", base=Bases.Water, flavors=None):
    if flavors is None:
        flavors = []
    drink = Drink(name, base)
    drink.set_flavors(flavors)
    return drink



if __name__ == '__main__':
    order = Order()

    drink1 = create_drink(name="Baja Blast", flavors=[Flavors.Lime, Flavors.Lemon])

    drink2 = create_drink(name="Sparkles", flavors=[Flavors.Cherry, Flavors.Blueberry, Flavors.Strawberry])

    order.add_item(drink1)

    order.add_item(drink2)

    print(order.get_receipt())
