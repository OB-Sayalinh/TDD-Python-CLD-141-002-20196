import unittest

from package.basics import RoundingFlags as rf
from package.basics import RoundingMethod, Item


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

    def test_no_round_signed(self):
        test_input = 10.9076
        flags = rf.NoRound | rf.Signed
        expected_result = ''.join(['$', str(test_input)])

        result = flags.do_round(test_input)

        self.assertEqual(result, expected_result)

    def test_signed(self):
        test_input = 10.9076
        flags = rf.Signed
        expected_result = '$10.91'

        result = flags.do_round(test_input)

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

    def test_negatives_false(self):
        test_input = -1.0
        flags = rf.Round
        expected_result = "0.00"

        result = flags.do_round(test_input)

        self.assertEqual(result, expected_result)

    def test_negatives_false2(self):
        test_input = 0.0
        flags = rf.Round
        expected_result = "0.00"

        result = flags.do_round(test_input)

        self.assertEqual(result, expected_result)

    def test_negatives_true(self):
        test_input = -1.0589
        flags = rf.Round | rf.Negatives
        expected_result = "-1.06"

        result = flags.do_round(test_input)

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

    def test_add_num_places(self):
        test_input = 256.9076
        flags = rf.NinetyNine
        expected_result = "199.00"

        result = flags.do_round(test_input, add_num_place=0)

        self.assertEqual(expected_result, result)

    def test_add_num_places2(self):
        test_input = 256.9076
        flags = rf.NinetyNine
        expected_result = "249.90"

        result = flags.do_round(test_input, add_num_place=1)

        self.assertEqual(expected_result, result)

    def test_add_num_places3(self):
        test_input = 7256.9076
        flags = rf.NinetyNine
        expected_result = "6990.00"

        result = flags.do_round(test_input, add_num_place=-1)

        self.assertEqual(expected_result, result)


class RoundingMethodTests(unittest.TestCase):
    """Test RoundingMethod Class

    Attributes
    ----------
    file_path : ./package/basics
    """

    def create_rounding_method(self, rounding_flags=rf.NoRound, trailing_count=2,
                               add_num_place=2):
        return RoundingMethod(rounding_flags=rounding_flags, trailing_count=trailing_count,
                              add_num_place=add_num_place)

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

    def test_get_add_num_place(self):
        dec_places = 2
        expected_result = dec_places

        rounder = self.create_rounding_method(add_num_place=dec_places)
        result = rounder.get_add_num_place

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

    def test_set_add_num_place(self):
        dec_place = False
        expected_result = dec_place

        method = self.create_rounding_method()
        method.set_add_num_place(dec_place)
        result = method.get_add_num_place

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


class ItemTests(unittest.TestCase):
    """Test the abstract class Item

    Only one test and that is to raise an error.

    Attributes
    ----------
    file_path : ./package/basic.py
    """
    def test_raise_type_error(self):
        with self.assertRaises(TypeError):
            item = Item()


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







