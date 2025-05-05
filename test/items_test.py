import unittest

from package.items import Bases, Flavors, DrinkSizes, Item, FoodSizes, Foods, Toppings
from test.testing import create_drink, create_food


class ItemTests(unittest.TestCase):

    def test_raise_type_error(self):
        with self.assertRaises(TypeError):
            item = Item()


class DrinkTests(unittest.TestCase):

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

    def test_num_flavors(self):
        drink = create_drink()

        result = drink.get_num_flavors

        self.assertEqual(result, len(self.__flavors))

    def test_num_flavors_added(self):
        drink = create_drink()

        drink.add_flavor(Flavors.Lime)
        result = drink.get_num_flavors

        self.assertEqual(result, 1)


class FoodTests(unittest.TestCase):

    # Getters

    def test_get_price(self):
        item = create_food()
        expected_result = DrinkSizes.Small.get_price

        result = item.get_price

        self.assertEqual(result, expected_result)

    def test_get_price_added(self):
        item = create_food()
        topping = Toppings.Chili
        expected_result = FoodSizes.Small.get_price + topping.get_price

        item.add_topping(topping)
        result = item.get_price

        self.assertEqual(result, expected_result)

    def test_get_price_multiple(self):
        item = create_food()
        toppings = [Flavors.Lime, Flavors.Mint]
        toppings_price = 0
        for topping in toppings:
            toppings_price += topping.get_price
        expected_result = DrinkSizes.Small.get_price + toppings_price

        item.set_toppings(toppings)
        result = item.get_price

        self.assertEqual(result, expected_result)

    def test_get_price_multiple2(self):
        item = create_food()
        toppings = [Toppings.Cherry, Toppings.Whipped, Toppings.CaramelSauce, Toppings.ChocolateSauce]
        toppings_price = 0
        for topping in toppings:
            toppings_price += topping.get_price
        expected_result = FoodSizes.Small.get_price + toppings_price

        item.set_toppings(toppings)
        result = item.get_price

        self.assertEqual(result, expected_result)

    def test_get_name(self):
        item = create_food()
        expected_result = ""

        result = item.get_name

        self.assertEqual(result, expected_result)

    def test_name_parameter(self):
        name = "test"
        item = create_food(name=name)
        expected_result = name

        result = item.get_name

        self.assertEqual(result, expected_result)

    def test_get_size(self):
        size = FoodSizes.Small
        item = create_food(size=size)
        expected_result = size

        result = item.get_size

        self.assertEqual(result, expected_result)

    def test_get_food_choice(self):
        pass

    def test_get_toppings(self):
        pass

    # Setters & Misc

    def test_set_size(self):
        pass

    def test_set_name(self):
        pass

    def test_set_toppings(self):
        pass

    def test_set_duplicate_toppings(self):
        pass

    def test_set_food_choice(self):
        pass

    def test_add_topping(self):
        pass

    def test_add_duplicate_topping(self):
        pass

    def test_num_toppings(self):
        pass

    def test_num_toppings2(self):
        pass

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

