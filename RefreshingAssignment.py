import unittest
from enum import Enum
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
        receipt.join(f"() : $()\n".format(item.get_name(), item.get_price()))

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


class OrderTests(unittest.TestCase):

    order = None

    def setUp(self):
        self.order = Order()

    def testGetItems(self):
        expected_result = []

        result = self.order.get_items()

        self.assertEqual(result, expected_result, msg="Expect Empty")

    def testGetTotal(self):
        expected_result = 0

        result = self.order.get_total()

        self.assertEqual(result, expected_result)

    def testGetNumItems(self):
        expected_result = 0

        result = self.order.get_num_items()

        self.assertEqual(result, expected_result)

    def testGetReceipt(self):
        expected_result = ""

        result = self.order.get_receipt()

        self.assertEqual(result, expected_result)

    def testGetReceiptAdded(self):
        drink = create_drink()
        expected_result = make_receipt([drink])

        self.order.add_item(drink)
        result = self.order.get_receipt()

        self.assertEqual(result, expected_result)

    def testAddItem(self):
        drink = create_drink()
        expected_result = [drink]

        self.order.add_item(drink)
        result = self.order.get_items()

        self.assertEqual(result, expected_result)

    def testRemoveItem(self):
        drink = create_drink()
        expected_result = [drink]

        self.order.add_item(drink)
        self.order.add_item(drink)

        self.order.remove_item(0)
        result = self.order.get_items()

        self.assertEqual(result, expected_result)


class DrinkTests(unittest.TestCase):

    __base = Bases.Water
    __flavors = []

    def testGetBase(self):
        drink = create_drink()

        result = drink.get_base()

        self.assertEqual(result, self.__base)

    def testGetFlavors(self):
        drink = create_drink()

        result = drink.get_flavors()

        self.assertEqual(result, self.__flavors)

    def testFlavorsParameter(self):
        flavors = [Flavors.Lime]
        drink = create_drink(flavors=flavors)

        result = drink.get_flavors()

        self.assertEqual(result, flavors)

    def testGetPrice(self):
        drink = create_drink()
        expected_result = prices[drink.get_base()]

        result = drink.get_price()

        self.assertEqual(result, expected_result)

    def testGetPriceAdded(self):
        drink = create_drink()
        flavor = Flavors.Lime
        expected_result = prices[drink.get_base()] + prices[flavor]

        drink.add_flavor(flavor)
        result = drink.get_price()

        self.assertEqual(result, expected_result)

    def testGetName(self):
        drink = create_drink()
        expected_result = ""

        result = drink.get_name()

        self.assertEqual(result, expected_result)

    def testNameParameter(self):
        name = "test"
        drink = create_drink(name=name)
        expected_result = name

        result = drink.get_name()

        self.assertEqual(result, expected_result)

    def testSetFlavors(self):
        flavors = [Flavors.Lime]
        drink = create_drink()

        drink.set_flavors(flavors)
        result = drink.get_flavors()

        self.assertEqual(result, flavors)

    def testSetDuplicateFlavors(self):
        flavors = [Flavors.Lime, Flavors.Lime, Flavors.Mint]
        expected_result = [Flavors.Lime, Flavors.Mint]
        drink = create_drink()

        drink.set_flavors(flavors)
        result = drink.get_flavors()

        self.assertEqual(result, expected_result)

    def testAddFlavors(self):
        flavor = Flavors.Lime
        drink = create_drink()

        drink.add_flavor(flavor)
        result = drink.get_flavors()

        self.assertEqual(result, [flavor])

    def testDuplicatingFlavors(self):
        flavor = Flavors.Lime
        drink = create_drink()

        drink.add_flavor(flavor)
        drink.add_flavor(flavor)
        result = drink.get_flavors()

        self.assertEqual(result, [flavor])

    def testNumFlavors(self):
        drink = create_drink()

        result = drink.get_num_flavors()

        self.assertEqual(result, len(self.__flavors))

    def testNumFlavorsAdded(self):
        drink = create_drink()

        drink.add_flavor(Flavors.Lime)
        result = drink.get_num_flavors()

        self.assertEqual(result, 1)


def test():
    test_suite = unittest.TestSuite()
    test_suite.addTest(OrderTests())
    test_suite.addTest(DrinkTests())

    return test_suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    suite = test()
    runner.run(suite)
