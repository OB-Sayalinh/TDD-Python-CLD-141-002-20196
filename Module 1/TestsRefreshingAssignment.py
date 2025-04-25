import unittest

from RefreshingAssignment import Bases, Flavors, Order, Drink, make_receipt, prices, create_drink

# Testing


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

    def test_get_base(self):
        drink = create_drink()

        result = drink.get_base()

        self.assertEqual(result, self.__base)

    def test_get_flavors(self):
        drink = create_drink()

        result = drink.get_flavors()

        self.assertEqual(result, self.__flavors)

    def test_flavors_parameter(self):
        flavors = [Flavors.Lime]
        drink = create_drink(flavors=flavors)

        result = drink.get_flavors()

        self.assertEqual(result, flavors)

    def test_get_price(self):
        drink = create_drink()
        expected_result = prices[drink.get_base()]

        result = drink.get_price()

        self.assertEqual(result, expected_result)

    def test_get_price_added(self):
        drink = create_drink()
        flavor = Flavors.Lime
        expected_result = prices[drink.get_base()] + prices[flavor]

        drink.add_flavor(flavor)
        result = drink.get_price()

        self.assertEqual(result, expected_result)

    def test_get_name(self):
        drink = create_drink()
        expected_result = ""

        result = drink.get_name()

        self.assertEqual(result, expected_result)

    def test_name_parameter(self):
        name = "test"
        drink = create_drink(name=name)
        expected_result = name

        result = drink.get_name()

        self.assertEqual(result, expected_result)

    def test_set_flavors(self):
        flavors = [Flavors.Lime]
        drink = create_drink()

        drink.set_flavors(flavors)
        result = drink.get_flavors()

        self.assertEqual(result, flavors)

    def test_set_duplicate_flavors(self):
        flavors = [Flavors.Lime, Flavors.Lime, Flavors.Mint]
        expected_result = [Flavors.Lime, Flavors.Mint]
        drink = create_drink()

        drink.set_flavors(flavors)
        result = drink.get_flavors()

        self.assertEqual(result, expected_result)

    def test_add_flavors(self):
        flavor = Flavors.Lime
        drink = create_drink()

        drink.add_flavor(flavor)
        result = drink.get_flavors()

        self.assertEqual(result, [flavor])

    def test_duplicating_flavors(self):
        flavor = Flavors.Lime
        drink = create_drink()

        drink.add_flavor(flavor)
        drink.add_flavor(flavor)
        result = drink.get_flavors()

        self.assertEqual(result, [flavor])

    def test_num_flavors(self):
        drink = create_drink()

        result = drink.get_num_flavors()

        self.assertEqual(result, len(self.__flavors))

    def test_num_flavors_added(self):
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

