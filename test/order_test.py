import unittest

from package.order import Order, make_receipt
from test.testing import create_drink


# To-do: add tests that test erroneous edge cases (Errors, not returns)
class MakeReceiptTests(unittest.TestCase):
    """Testing the function make_receipt

    Attributes
    ----------
    file_path : ./package/order.py
    """



class OrderTests(unittest.TestCase):
    """Testing the class Order

    Attributes
    ----------
    file_path : ./package/order
    """
    order = None

    def setUp(self):
        self.order = Order()

    def test_get_items(self):
        expected_result = []

        result = self.order.get_items

        self.assertEqual(result, expected_result, msg="Expect Empty")

    def test_get_total(self):
        expected_result = 0

        result = self.order.get_total

        self.assertEqual(result, expected_result)

    def test_get_num_items(self):
        expected_result = 0

        result = self.order.get_num_items

        self.assertEqual(result, expected_result)

    def test_get_receipt(self):
        expected_result = make_receipt([])

        result = self.order.get_receipt

        self.assertEqual(result, expected_result)

    def test_get_receipt_added(self):
        drink = create_drink()
        expected_result = make_receipt([drink])

        self.order.add_item(drink)
        result = self.order.get_receipt

        self.assertEqual(result, expected_result)

    def test_add_item(self):
        drink = create_drink()
        expected_result = [drink]

        self.order.add_item(drink)
        result = self.order.get_items

        self.assertEqual(result, expected_result)

    def test_remove_item(self):
        drink = create_drink()
        expected_result = [drink]

        self.order.add_item(drink)
        self.order.add_item(drink)

        self.order.remove_item(0)
        result = self.order.get_items

        self.assertEqual(result, expected_result)


tests = [OrderTests]


def create_test():
    test_suite = unittest.TestSuite()

    for test in tests:
        test_suite.addTest(test())

    return test_suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    suite = create_test()
    runner.run(suite)






