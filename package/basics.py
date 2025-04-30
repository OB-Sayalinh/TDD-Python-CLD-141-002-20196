import math
from enum import Enum, auto, Flag


class BaseEnum(Enum):
    """Hold Data for a price and a string name"""
    def __new__(cls, name, price=0):
        """

        Parameters
        ----------
        name : string
        price : float

        Returns
        ----------
        object
        """
        obj = object.__new__(cls)
        obj._value_ = name
        obj._price_ = price
        return obj

    @property
    def get_price(self):
        return self._price_


class RoundingMethods(Flag):
    """Ways of rounding money.

    Since this is base around money, all strings returned are rounded at to either a hundredth or whole number.

    Any returned strings are at max a decimal place of a hundredth.

    Use the flags in conjunction to create specific ways of rounding.

    Some flags clash so there is a non-set priority between them.

    Be warned of weird effects of clashing flags.

    Attributes
    ----------
    NoRound : int
        No rounding done.
    Round : int
        Basic rounding done to the closest number.
    Ceil : int
        Round Up.
    Floor : int
        Round Down.
    Whole : int
        Rounded to nearest whole number.
    NinetyNine : int
        Replaces ending with 99
    NinetyFive : int
        Replaces ending with 95
    Fifths : int
        Rounds to the nearest fifth in a hundredth (works with Whole).
    Tenths : int
        Rounds to the nearest tenth (works with Whole)

    Methods
    ----------
    do_round : Uses the given flags to round.
    """
    NoRound = 0
    Round = auto()
    Whole = auto()
    Ceil = auto()
    Floor = auto()
    NinetyNine = auto()
    NinetyFive = auto()
    Fifths = auto()
    Tenths = auto()

    def do_round(self, method, num, blank_zeroes=True, dollar_sign=False):
        """Round given number with flags

        Parameters
        ----------
        method : RoundingMethods
        num : float
        blank_zeroes : bool, optional
        dollar_sign : bool, optional

        Returns
        -------
        string
        """
        rounded_num = 0
        rounded_str = ""

        dec_places = 2

        if method in self.Whole:
            dec_places = 0
        elif method in self.Tenths:
            dec_places = 1

        if method in self.NoRound:
            pass
        elif method in self.Round:
            rounded_num = round(num, dec_places)
        elif method in self.Ceil:
            rounded_num = ceil(num, dec_places)
        elif method in self.Floor:
            rounded_num = floor(num, dec_places)

        if method in self.Tenths | self.Whole:
            rounded_num = round_to_multiple(rounded_num, 10)
        if method in self.Fifths:
            rounded_num = round_fifths(int(str(rounded_num)[-1]))





        # if method in self.NoRound:
        #     pass
        # elif method in self.Round | self.Whole:
        #     pass
        # elif method in self.Ceil | self.Whole:
        #     pass
        # elif method in self.Floor | self.Whole:
        #     pass
        # elif method in self.NinetyNine | self.Whole:
        #     pass
        # elif method in self.NinetyFive | self.Whole:
        #     pass
        # elif method in self.Fifths | self.Whole:
        #     pass
        # elif method in self.Tenths | self.Whole:
        #     pass
        #
        # if not method in self.NoRound:
        #     pass
        # elif

def floor(num, dec_places):
    """Flooring decimal numbers

    Parameters
    ----------
    num : float
    dec_places : int

    Returns
    -------

    """
    multiply = 10 ** dec_places
    round_num = num * multiply
    round_num = math.floor(round_num) / multiply
    round_num = round(round_num)
    return round_num

def ceil(num, dec_places):
    """Flooring decimal numbers

    Parameters
    ----------
    num : float
    dec_places : int

    Returns
    -------

    """
    multiply = 10 ** dec_places
    round_num = num * multiply
    round_num = math.ceil(round_num) / multiply
    round_num = round(round_num)
    return round_num

def round_fifths(number):
    """Rounds to nearest fifth

    Assumes given decimal length of "num" as the wanted rounding place.

    Useful when slicing to round in non-decimal numbers by multiplying the return
    number by number places and then adding.

    Parameters
    ----------
    number : int

    Returns
    -------
    int
    """
    # Gets the last number of the integer
    return_num = str(number)[-1]
    rounded_num = int(return_num)

    if rounded_num < 5:
        if rounded_num > 2:
            rounded_num = 5
        else:
            rounded_num = 0
    elif 5 < rounded_num <= 10:
        if rounded_num > 7:
            rounded_num = 10
        else:
            rounded_num = 5

    # Replace last integer with 0
    return_num = int(str(number)[:-1] + "0")
    return_num += rounded_num

    return return_num

def round_to_multiple(number, multiple):
    """For rounding non-decimals with multiples"""
    return multiple * round(number / multiple)


tax = 0.0725


