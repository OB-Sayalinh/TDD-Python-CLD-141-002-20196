import unittest

import itemsTest
import orderTests

def test():
    test_suite = unittest.TestSuite()
    test_suite.addTest()

    return test_suite

if __name__ == '__main__':

    runner = unittest.TextTestRunner()
    suite = test()
    runner.run(suite)

