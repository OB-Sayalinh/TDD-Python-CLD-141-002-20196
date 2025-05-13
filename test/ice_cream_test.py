import unittest
from sys import flags

from test.testing import create_ice_cream
from package.ice_cream import IceCream, Additionals, Flavors, IceCreamSizes


class IceCreamTests(unittest.TestCase):
    """Test the class IceCream

    Attributes
    ----------
    file_path : ./package/ice_cream.py
    """
    def assume_pricing(self, item, size=None, flavors=None, additionals=None):
        """Get info from item then assume price

            Uses getters from the item to assume price.

        Parameters
        ----------
        item : Food
        size : IceCreamSizes, optional
        flavors : Foods, optional
        additionals : list of Additionals, optional

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

        if flavors is None:
            for flavor in item.get_flavors:
                price += flavor.get_price
        else:
            for flavor in flavors:
                price += flavor.get_price

        if additionals is None:
            for topping in item.get_additionals:
                price += topping.get_price
        else:
            for topping in additionals:
                price += topping.get_price

        return price

    # Getters

    def test_get_price(self):
        item = create_ice_cream()
        expected_result = self.assume_pricing(item)

        result = item.get_price

        self.assertEqual(expected_result, result)

    def test_get_price_added(self):
        item = create_ice_cream()
        topping = Additionals.WhippedCream
        expected_result = self.assume_pricing(item, additionals=[topping])

        item.add_flavor(topping)
        result = item.get_price

        self.assertEqual(expected_result, result)

    def test_get_price_multiple_additionals(self):
        item = create_ice_cream()
        additionals = [Additionals.Cherry, Additionals.ChocolateSauce]
        expected_result = self.assume_pricing(item, additionals=additionals)

        item.set_additionals(additionals)
        result = item.get_price

        self.assertEqual(expected_result, result)

    def test_get_price_multiple_additionals2(self):
        item = create_ice_cream()
        additionals = [Additionals.Cherry, Additionals.WhippedCream,
                       Additionals.CaramelSauce, Additionals.ChocolateSauce]
        expected_result = self.assume_pricing(item, additionals=additionals)

        item.set_additionals(additionals)
        result = item.get_price

        self.assertEqual(expected_result, result)

    def test_get_price_multiple_flavors(self):
        size = IceCreamSizes.DoubleScoop
        item = create_ice_cream(size=size, auto_size=False)
        flavors = [Flavors.MintChocolateChip, Flavors.Smore]
        expected_result = self.assume_pricing(item, flavors=flavors)

        item.set_flavors(flavors)
        result = item.get_price

        self.assertEqual(expected_result, result)

    def test_get_price_multiple_flavors2(self):
        size = IceCreamSizes.QuadrupleScoop
        item = create_ice_cream(size=size, auto_size=False)
        flavors = [Flavors.MintChocolateChip, Flavors.Smore,
                   Flavors.MintChocolateChip, Flavors.ButterPecan]
        expected_result = self.assume_pricing(item, flavors=flavors)

        item.set_flavors(flavors)
        result = item.get_price

        self.assertEqual(expected_result, result)

    def test_get_price_multiple(self):
        size = IceCreamSizes.QuadrupleScoop
        item = create_ice_cream(size=size, auto_size=False)
        additionals = [Additionals.Cherry, Additionals.WhippedCream,
                       Additionals.CaramelSauce, Additionals.ChocolateSauce]
        flavors = [Flavors.MintChocolateChip, Flavors.Smore,
                   Flavors.MintChocolateChip, Flavors.ButterPecan]
        expected_result = self.assume_pricing(item, additionals=additionals, flavors=flavors)

        item.set_flavors(flavors)
        item.set_additionals(additionals)
        result = item.get_price

        self.assertEqual(expected_result, result)

    def test_get_name(self):
        name = "IceCream"
        item = create_ice_cream(name=name)
        expected_result = name

        result = item.get_name

        self.assertEqual(expected_result, result)

    def test_get_max_flavors(self):
        size = IceCreamSizes.Scoop
        item = create_ice_cream(size=size)
        expected_result = size.get_max_scoops

        result = item.get_max_flavors

        self.assertEqual(expected_result, result)

    def test_get_max_flavors2(self):
        size = IceCreamSizes.DoubleScoop
        item = create_ice_cream(size=size, auto_size=False)
        expected_result = size.get_max_scoops

        result = item.get_max_flavors

        self.assertEqual(expected_result, result)

    def test_name_parameter(self):
        name = "test"
        item = create_ice_cream(name=name)
        expected_result = name

        result = item.get_name

        self.assertEqual(expected_result, result)

    def test_get_size(self):
        size = IceCreamSizes.DoubleScoop
        item = create_ice_cream(size=size, auto_size=False)
        expected_result = size

        result = item.get_size

        self.assertEqual(expected_result, result)

    def test_get_size_automated(self):
        flavors = [Flavors.Banana, Flavors.ButterPecan]
        item = create_ice_cream(flavors=flavors)
        expected_result = IceCreamSizes.DoubleScoop

        result = item.get_size

        self.assertEqual(expected_result, result)

    def test_get_flavors(self):
        flavors = [Flavors.Banana]
        item = create_ice_cream(flavors=flavors, auto_size=False)
        expected_result = flavors

        result = item.get_flavors

        self.assertEqual(expected_result, result)

    def test_get_additionals(self):
        additionals = [Additionals.Cherry]
        item = create_ice_cream(additionals=additionals)
        expected_result = additionals

        result = item.get_additionals

        self.assertEqual(expected_result, result)

    def test_get_num_additionals(self):
        additionals = [Additionals.Cherry, Additionals.ChocolateSauce]
        item = create_ice_cream(additionals=additionals)
        expected_result = 2

        result = item.get_num_additionals

        self.assertEqual(expected_result, result)

    def test_get_num_additionals2(self):
        additionals = [Additionals.Cherry, Additionals.ChocolateSauce]
        add_additional = Additionals.WhippedCream
        item = create_ice_cream(additionals=additionals)
        expected_result = 3

        item.add_additional(add_additional)
        result = item.get_num_additionals

        self.assertEqual(expected_result, result)

    def test_get_num_flavors(self):
        flavors = [Flavors.Chocolate, Flavors.Banana]
        item = create_ice_cream(flavors=flavors)
        expected_result = 2

        result = item.get_num_flavors

        self.assertEqual(expected_result, result)

    def test_get_num_flavors2(self):
        flavors = [Flavors.Chocolate, Flavors.Banana]
        add_flavor = Flavors.MintChocolateChip
        item = create_ice_cream(size=IceCreamSizes.TripleScoop, flavors=flavors, auto_size=False)
        expected_result = 3

        item.add_flavor(add_flavor)
        result = item.get_num_flavors

        self.assertEqual(expected_result, result)

    # Setters & Misc

    def test_set_size(self):
        size = IceCreamSizes.DoubleScoop
        item = create_ice_cream()
        expected_result = size

        result1 = item.set_size(size)
        result2 = item.get_size

        self.assertTrue(result1)
        self.assertEqual(expected_result, result2)

    def test_set_size_overfilled(self):
        size = IceCreamSizes.Scoop
        flavors = [Flavors.Banana, Flavors.ButterPecan]
        item = create_ice_cream(flavors=flavors)
        expected_result = IceCreamSizes.DoubleScoop

        item.set_size(size)
        result = item.get_size

        self.assertEqual(expected_result, result)

        result = item.set_size(size)

        self.assertFalse(result)

    def test_set_name(self):
        name = "IceCream"
        item = create_ice_cream()
        expected_result = name

        item.set_name(name)
        result = item.get_name

        self.assertEqual(expected_result, result)

    def test_set_additionals(self):
        additionals = [Additionals.Cherry]
        item = create_ice_cream()
        expected_result = additionals

        item.set_additionals(additionals)
        result = item.get_additionals

        self.assertEqual(expected_result, result)

    def test_set_duplicate_additionals(self):
        additionals = [Additionals.Cherry, Additionals.Cherry, Additionals.Cherry, Additionals.CaramelSauce]
        item = create_ice_cream()
        expected_result = [Additionals.Cherry, Additionals.CaramelSauce]

        item.set_additionals(additionals)
        result = item.get_additionals

        self.assertEqual(expected_result, result)

    def test_set_flavors(self):
        flavors = [Flavors.Banana]
        item = create_ice_cream()
        expected_result = flavors

        item.set_flavors(flavors)
        result = item.get_flavors

        self.assertEqual(expected_result, result)

    def test_set_flavors_max(self):
        size = IceCreamSizes.Scoop
        flavors = [Flavors.Banana, Flavors.Chocolate]
        item = create_ice_cream(size=size)
        expected_result = [flavors[0]]

        item.set_flavors(flavors)
        result = item.get_flavors

        self.assertEqual(expected_result, result)

    def test_add_flavor(self):
        size = IceCreamSizes.DoubleScoop
        flavors = [Flavors.Banana]
        flavor = Flavors.Chocolate
        item = create_ice_cream(flavors=flavors, size=size, auto_size=False)
        expected_result = flavors.copy()
        expected_result.append(flavor)

        item.add_flavor(flavor)
        result = item.get_flavors

        self.assertListEqual(expected_result, result)

    def test_add_flavor2(self):
        size = IceCreamSizes.DoubleScoop
        flavors = [Flavors.Banana]
        flavor = Flavors.Chocolate
        item = create_ice_cream(flavors=flavors, size=size, auto_size=False)
        expected_result = flavors.copy()
        expected_result.append(flavor)

        item.add_flavor(flavor)
        result = item.get_flavors

        self.assertListEqual(expected_result, result)

    def test_add_flavor_max(self):
        size = IceCreamSizes.Scoop
        flavors = [Flavors.Banana]
        flavor = Flavors.Chocolate
        item = create_ice_cream(flavors=flavors, size=size)
        expected_result = flavors

        item.add_flavor(flavor)
        result = item.get_flavors

        self.assertListEqual(expected_result, result)

        result = item.add_flavor(flavor)

        self.assertFalse(result)

    def test_add_additional(self):
        additionals = [Additionals.Cherry, Additionals.ChocolateSauce]
        add_additional = Additionals.WhippedCream
        item = create_ice_cream(additionals=additionals)
        expected_result = additionals.copy()
        expected_result.append(add_additional)

        item.add_additional(add_additional)
        result = item.get_additionals

        self.assertListEqual(expected_result, result)

    def test_add_duplicate_additional(self):
        additionals = [Additionals.Cherry, Additionals.ChocolateSauce]
        add_additional = Additionals.Cherry
        item = create_ice_cream(additionals=additionals)
        expected_result = additionals

        item.add_additional(add_additional)
        result = item.get_additionals

        self.assertEqual(expected_result, result)


tests = [IceCreamTests]

def create_test():
    test_suite = unittest.TestSuite()

    for test in tests:
        test_suite.addTest(test())

    return test_suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    suite = create_test()
    runner.run(suite)


