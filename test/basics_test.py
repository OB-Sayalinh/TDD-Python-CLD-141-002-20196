import unittest

from package.basics import RoundingFlags as rf
from package.basics import RoundingMethod


class RoundingFlagsTests(unittest.TestCase):
    """Test RoundingFlags Enum Class

    Attributes
    ----------
    file_path : ./package/basics.py
    """
    def test_no_round(self):
        test_input = 10.9076
        flags = rf.NoRound
        expected_result = str(test_input)

        result = flags.do_round(test_input)

        self.assertEqual(result, expected_result)

    def test_no_round_sign(self):
        test_input = 10.9076
        flags = rf.NoRound
        expected_result = ''.join(['$', str(test_input)])

        result = flags.do_round(test_input, dollar_sign=True)

        self.assertEqual(result, expected_result)

    def test_basic_round(self):
        test_input = 10.9076
        flags = rf.Round
        expected_result = "10.91"

        result = flags.do_round(test_input)

        self.assertEqual(result, expected_result)

    def test_floor(self):
        test_input = 10.9076
        flags = rf.Floor
        expected_result = "10.90"

        result = flags.do_round(test_input)

        self.assertEqual(result, expected_result)

    def test_ceil(self):
        test_input = 10.9016
        flags = rf.Ceil
        expected_result = "10.91"

        result = flags.do_round(test_input)

        self.assertEqual(result, expected_result)

    def test_whole_round(self):
        test_input = 10.9076
        flags = rf.Whole
        expected_result = "11"

        result = flags.do_round(test_input, trailing_count=0)

        self.assertEqual(result, expected_result)

    def test_trailing_zeroes(self):
        test_input = 10.10
        flags =  rf.Round
        expected_result = "10.10"

        result = flags.do_round(test_input)

        self.assertEqual(result, expected_result)

    def test_trailing_zeroes2(self):
        test_input = 10.10
        flags =  rf.Round
        expected_result = "10.100"

        result = flags.do_round(test_input, trailing_count=3)

        self.assertEqual(result, expected_result)

    def test_no_negatives_true(self):
        test_input = -1.0
        flags = rf.Round
        expected_result = "0.00"

        result = flags.do_round(test_input)

        self.assertEqual(result, expected_result)

    def test_no_negatives_true2(self):
        test_input = 0.0
        flags = rf.Round
        expected_result = "0.00"

        result = flags.do_round(test_input)

        self.assertEqual(result, expected_result)

    def test_no_negatives_false(self):
        test_input = -1.0589
        flags = rf.Round
        expected_result = "-1.06"

        result = flags.do_round(test_input, trailing_count=2,no_negatives=False)

        self.assertEqual(result, expected_result)

    def test_ninety_nine(self):
        test_input = 10.9076
        flags =  rf.NinetyNine
        expected_result = "9.99"

        result = flags.do_round(test_input)

        self.assertEqual(result, expected_result)

    def test_ninety_five(self):
        test_input = 10.9076
        flags =  rf.NinetyFive
        expected_result = "9.95"

        result = flags.do_round(test_input)

        self.assertEqual(result, expected_result)

    def test_fifths(self):
        test_input = 10.9376
        flags =  rf.Fifths
        expected_result = "10.95"

        result = flags.do_round(test_input)

        self.assertEqual(result, expected_result)

    def test_tenths(self):
        test_input = 10.9076
        flags = rf.Tenths
        expected_result = "10.9"

        result = flags.do_round(test_input, trailing_count=1)

        self.assertEqual(result, expected_result)

    def test_ceil_whole_ninety_nine(self):
        test_input = 10.9016
        flags = rf.Ceil | rf.Whole | rf.NinetyNine
        expected_result = "10.99"

        result = flags.do_round(test_input)

        self.assertEqual(result, expected_result)

    def test_floor_whole_ninety_nine(self):
        test_input = 10.9016
        flags = rf.Floor | rf.Whole | rf.NinetyNine
        expected_result = "9.99"

        result = flags.do_round(test_input)

        self.assertEqual(result, expected_result)

    def test_tens(self):
        test_input = 13.9076
        flags = rf.Tens
        expected_result = "10.00"

        result = flags.do_round(test_input)

        self.assertEqual(result, expected_result)

    def test_hundreds(self):
        test_input = 256.9076
        flags = rf.Hundreds
        expected_result = "300.00"

        result = flags.do_round(test_input)

        self.assertEqual(result, expected_result)


class RoundingMethodTests(unittest.TestCase):
    """Test RoundingMethod Class

    Attributes
    ----------
    file_path : ./package/basics
    """

    def create_rounding_method(self, rounding_flags=rf.NoRound, trailing_count=2,
                               trailing_zeroes=True, dollar_sign=False, no_negatives=True):
        return RoundingMethod(rounding_flags=rounding_flags, trailing_count=trailing_count,
                              trailing_zeroes=trailing_zeroes, dollar_sign=dollar_sign,
                              no_negatives=no_negatives)

    def test_get_rounding_flags(self):
        rounding_flags = rf.Round
        expected_result = rounding_flags

        result = self.create_rounding_method(rounding_flags).get_rounding_flag

        self.assertEqual(expected_result, result)

    def test_get_trailing_count(self):
        trailing_count = 5
        expected_result = trailing_count

        result = self.create_rounding_method(trailing_count=trailing_count).get_trailing_count

        self.assertEqual(expected_result, result)

    def test_get_trailing_zeroes(self):
        trailing_zeroes = False
        expected_result = trailing_zeroes

        result = self.create_rounding_method(trailing_zeroes=trailing_zeroes).get_trailing_zeroes

        self.assertEqual(expected_result, result)

    def test_get_dollar_sign(self):
        dollar_sign = True
        expected_result = dollar_sign

        result = self.create_rounding_method(dollar_sign=dollar_sign).get_dollar_sign

        self.assertEqual(expected_result, result)

    def test_get_no_negatives(self):
        no_negatives = False
        expected_result = no_negatives

        result = self.create_rounding_method(no_negatives=no_negatives).get_no_negatives

        self.assertEqual(expected_result, result)

    def test_set_rounding_flags(self):
        rounding_flags = rf.Round
        expected_result = rounding_flags

        method = self.create_rounding_method()
        method.set_rounding_flags(rounding_flags)
        result = method.get_rounding_flag

        self.assertEqual(expected_result, result)

    def test_set_trailing_count(self):
        trailing_count = 5
        expected_result = trailing_count

        method = self.create_rounding_method()
        method.set_trailing_count(trailing_count)
        result = method.get_trailing_count

        self.assertEqual(expected_result, result)

    def test_set_trailing_zeroes(self):
        trailing_zeroes = False
        expected_result = trailing_zeroes

        method = self.create_rounding_method()
        method.set_trailing_zeroes(trailing_zeroes)
        result = method.get_trailing_zeroes

        self.assertEqual(expected_result, result)

    def test_set_dollar_sign(self):
        dollar_sign = True
        expected_result = dollar_sign

        method = self.create_rounding_method()
        method.set_dollar_sign(dollar_sign)
        result = method.get_dollar_sign

        self.assertEqual(expected_result, result)

    def test_set_no_negatives(self):
        no_negatives = False
        expected_result = no_negatives

        method = self.create_rounding_method()
        method.set_no_negatives(no_negatives)
        result = method.get_no_negatives

        self.assertEqual(expected_result, result)

    def test_round(self):
        """
        Notes
        _____
        RoundingFlagsTest has further in-depth testing of rounding
        """
        rounding_flags = rf.Round
        num = 10.9079
        expected_result = '10.91'

        method = self.create_rounding_method(rounding_flags)
        result = method.round(num)

        self.assertEqual(expected_result, result)


tests = [RoundingFlagsTests, RoundingMethodTests]

def create_test():
    test_suite = unittest.TestSuite()

    for test in tests:
        test_suite.addTest(test())

    return test_suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    suite = create_test()
    runner.run(suite)







