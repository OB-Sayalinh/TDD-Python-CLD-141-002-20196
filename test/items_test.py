import unittest

from package.items import Bases, Flavors, DrinkSizes, Item, FoodSizes, Foods, Toppings, Food
from test.testing import create_drink, create_food


class ItemTests(unittest.TestCase):
    """Test the abstract class Item

    Only one test and that is to raise an error.

    Attributes
    ----------
    file_path : ./package/items.py
    """
    def test_raise_type_error(self):
        with self.assertRaises(TypeError):
            item = Item()


class DrinkTests(unittest.TestCase):
    """Test the class Drink

    Attributes
    ----------
    file_path : ./package/items.py
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
    """Test the class Food

    Attributes
    ----------
    file_path : ./package/items.py
    """
    def assume_pricing(self, item, size=None, food_choice=None, toppings=None):
        """Get info from item then assume price

            Uses getters from the item to assume price.

        Parameters
        ----------
        item : Food
        size : FoodSizes, optional
        food_choice : Foods, optional
        toppings : list of Toppings, optional

        Returns
        -------
        float
            Assumed price
        """
        price = 0.0
        if size is None:
            price += item.get_size.get_price
        else:
            price += size.get_price

        if food_choice is None:
            price += item.get_food_choice.get_price
        else:
            price += food_choice.get_price

        if toppings is None:
            for topping in item.get_toppings:
                price += topping.get_price
        else:
            for topping in toppings:
                price += topping.get_price

        return price

    # Getters

    def test_get_price(self):
        item = create_food()
        expected_result = self.assume_pricing(item)

        result = item.get_price

        self.assertEqual(result, expected_result)

    def test_get_price_added(self):
        item = create_food()
        topping = Toppings.Chili
        expected_result = self.assume_pricing(item, toppings=[topping])

        item.add_topping(topping)
        result = item.get_price

        self.assertEqual(result, expected_result)

    def test_get_price_multiple(self):
        item = create_food()
        toppings = [Toppings.Cherry, Toppings.ChocolateSauce]
        expected_result = self.assume_pricing(item, toppings=toppings)

        item.set_toppings(toppings)
        result = item.get_price

        self.assertEqual(result, expected_result)

    def test_get_price_multiple2(self):
        item = create_food()
        toppings = [Toppings.Cherry, Toppings.WhippedCream, Toppings.CaramelSauce, Toppings.ChocolateSauce]
        expected_result = self.assume_pricing(item, toppings=toppings)

        item.set_toppings(toppings)
        result = item.get_price

        self.assertEqual(result, expected_result)

    def test_get_name(self):
        name = "Food"
        item = create_food(name=name)
        expected_result = name

        result = item.get_name

        self.assertEqual(result, expected_result)

    def test_name_parameter(self):
        name = "test"
        item = create_food(name=name)
        expected_result = name

        result = item.get_name

        self.assertEqual(result, expected_result)

    def test_get_size(self):
        size = FoodSizes.Medium
        item = create_food(size=size)
        expected_result = size

        result = item.get_size

        self.assertEqual(result, expected_result)

    def test_get_food_choice(self):
        food_choice = Foods.Corndog
        item = create_food(food_choice=food_choice)
        expected_result = food_choice

        result = item.get_food_choice

        self.assertEqual(expected_result, result)

    def test_get_toppings(self):
        toppings = [Toppings.Cherry]
        item = create_food(toppings=toppings)
        expected_result = toppings

        result = item.get_toppings

        self.assertEqual(expected_result, result)

    # Setters & Misc

    def test_set_size(self):
        size = FoodSizes.Medium
        item = create_food()
        expected_result = size

        item.set_size(size)
        result = item.get_size

        self.assertEqual(result, expected_result)

    def test_set_name(self):
        name = "Food"
        item = create_food()
        expected_result = name

        item.set_name(name)
        result = item.get_name

        self.assertEqual(result, expected_result)

    def test_set_toppings(self):
        toppings = [Toppings.Cherry]
        item = create_food()
        expected_result = toppings

        item.set_toppings(toppings)
        result = item.get_toppings

        self.assertEqual(expected_result, result)

    def test_set_duplicate_toppings(self):
        toppings = [Toppings.Cherry, Toppings.Cherry, Toppings.Cherry, Toppings.CaramelSauce]
        item = create_food()
        expected_result = [Toppings.Cherry, Toppings.CaramelSauce]

        item.set_toppings(toppings)
        result = item.get_toppings

        self.assertEqual(expected_result, result)

    def test_set_food_choice(self):
        food_choice = Foods.Corndog
        item = create_food()
        expected_result = food_choice

        item.set_food_choice(food_choice)
        result = item.get_food_choice

        self.assertEqual(expected_result, result)

    def test_add_topping(self):
        toppings = [Toppings.Cherry, Toppings.ChocolateSauce]
        add_topping = Toppings.WhippedCream
        item = create_food(toppings=toppings)
        expected_result = toppings.copy()
        expected_result.append(add_topping)

        item.add_topping(add_topping)
        result = item.get_toppings

        self.assertEqual(expected_result, result)

    def test_add_duplicate_topping(self):
        toppings = [Toppings.Cherry, Toppings.ChocolateSauce]
        add_topping = Toppings.Cherry
        item = create_food(toppings=toppings)
        expected_result = toppings

        item.add_topping(add_topping)
        result = item.get_toppings

        self.assertEqual(expected_result, result)

    def test_num_toppings(self):
        toppings = [Toppings.Cherry, Toppings.ChocolateSauce]
        item = create_food(toppings=toppings)
        expected_result = 2

        result = item.get_num_toppings

        self.assertEqual(expected_result, result)

    def test_num_toppings2(self):
        toppings = [Toppings.Cherry, Toppings.ChocolateSauce]
        add_topping = Toppings.WhippedCream
        item = create_food(toppings=toppings)
        expected_result = 3

        item.add_topping(add_topping)
        result = item.get_num_toppings

        self.assertEqual(expected_result, result)

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



