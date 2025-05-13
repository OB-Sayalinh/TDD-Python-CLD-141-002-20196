import unittest

from package.drink import Bases, Flavors, DrinkSizes
from test.testing import create_drink


class DrinkTests(unittest.TestCase):
    """Test the class Drink

    Attributes
    ----------
    file_path : ./package/drink.py
    """
    __base = Bases.Water
    __flavors = []

    # Getters & Parameters

    def test_get_base(self):
        drink = create_drink()

        result = drink.get_base

        self.assertEqual(result.value, self.__base.value)

    def test_get_flavors(self):
        drink = create_drink()

        result = drink.get_flavors

        self.assertEqual(result, self.__flavors)

    def test_flavors_parameter(self):
        flavors = [Flavors.Lime]
        drink = create_drink(flavors=flavors)

        result = drink.get_flavors

        self.assertEqual(result, flavors)

    def test_get_price(self):
        drink = create_drink()
        expected_result = DrinkSizes.Small.get_price

        result = drink.get_price

        self.assertEqual(result, expected_result)

    def test_get_price_added(self):
        drink = create_drink()
        flavor = Flavors.Lime
        expected_result = DrinkSizes.Small.get_price

        drink.add_flavor(flavor)
        result = drink.get_price

        self.assertEqual(result, expected_result)

    def test_get_price_multiple(self):
        drink = create_drink()
        flavors = [Flavors.Lime, Flavors.Mint]
        expected_result = DrinkSizes.Small.get_price + drink.add_flavor_price

        drink.set_flavors(flavors)
        result = drink.get_price

        self.assertEqual(result, expected_result)

    def test_get_price_multiple2(self):
        drink = create_drink()
        flavors = [Flavors.Lime, Flavors.Mint, Flavors.Cherry, Flavors.Strawberry]
        expected_result = DrinkSizes.Small.get_price + drink.add_flavor_price * 3

        drink.set_flavors(flavors)
        result = drink.get_price

        self.assertEqual(result, expected_result)

    def test_get_name(self):
        drink = create_drink()
        expected_result = ""

        result = drink.get_name

        self.assertEqual(result, expected_result)

    def test_name_parameter(self):
        name = "test"
        drink = create_drink(name=name)
        expected_result = name

        result = drink.get_name

        self.assertEqual(result, expected_result)

    def test_get_size(self):
        size = DrinkSizes.Small
        drink = create_drink(size=size)
        expected_result = size

        result = drink.get_size

        self.assertEqual(result, expected_result)

    def test_get_num_flavors(self):
        drink = create_drink()

        result = drink.get_num_flavors

        self.assertEqual(result, len(self.__flavors))

    def test_get_num_flavors_added(self):
        drink = create_drink()

        drink.add_flavor(Flavors.Lime)
        result = drink.get_num_flavors

        self.assertEqual(result, 1)

    # Setters & Misc

    def test_set_name(self):
        name = "Jenry"
        item = create_drink()
        expected_result = name

        item.set_name(name)
        result = item.get_name

        self.assertEqual(result, expected_result)

    def test_set_size(self):
        size = DrinkSizes.Large
        item = create_drink()
        expected_result = size

        item.set_size(size)
        result = item.get_size

        self.assertEqual(result, expected_result)

    def test_set_flavors(self):
        flavors = [Flavors.Lime]
        drink = create_drink()

        drink.set_flavors(flavors)
        result = drink.get_flavors

        self.assertEqual(result, flavors)

    def test_set_duplicate_flavors(self):
        flavors = [Flavors.Lime, Flavors.Lime, Flavors.Mint]
        expected_result = [Flavors.Lime, Flavors.Mint]
        drink = create_drink()

        drink.set_flavors(flavors)
        result = drink.get_flavors

        self.assertEqual(result, expected_result)

    def test_add_flavors(self):
        flavor = Flavors.Lime
        drink = create_drink()

        drink.add_flavor(flavor)
        result = drink.get_flavors

        self.assertEqual(result, [flavor])

    def test_add_duplicating_flavors(self):
        flavor = Flavors.Lime
        drink = create_drink()

        drink.add_flavor(flavor)
        drink.add_flavor(flavor)
        result = drink.get_flavors

        self.assertEqual(result, [flavor])


tests = [DrinkTests]

def create_test():
    test_suite = unittest.TestSuite()

    for test in tests:
        test_suite.addTest(test())

    return test_suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    suite = create_test()
    runner.run(suite)



