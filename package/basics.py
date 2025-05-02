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


class RoundingFlags(Flag):
    """Ways of rounding money.

    Since this is base around money, all strings returned are rounded at to either a hundredth or whole number.

    Must explicitly set flag for rounding type (Round, Ceil, Floor) or get '0'.

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
        Sets ending to 99 (Floors to 99)
    NinetyFive : int
        Sets ending to 95 (Floors to 95)
    Fifths : int
        Rounds to the nearest fifth in a hundredth (works with Whole).
    Tenths : int
        Changes from hundredths to tenths (works with Whole; needs a rounding type)

    Methods
    ----------
    do_round : Uses the given flags to round.
    """
    NoRound = auto()
    Round = auto()
    Whole = auto()
    Ceil = auto()
    Floor = auto()
    NinetyNine = auto()
    NinetyFive = auto()
    Fifths = auto()
    Tenths = auto()

    def do_round(self, num, trailing_count=2, trailing_zeros=True, dollar_sign=False):
        """Round given number with flags

        Parameters
        ----------
        num : float
        trailing_zeros : bool, optional
        trailing_count : int , optional
            Amount of trailing zeroes to add
        dollar_sign : bool, optional

        Returns
        -------
        string
        """

        rounded_num = num
        rounded_str = ""

        dec_places = 2

        return_string = ''

        if self.value ^ self.NoRound.value:

            if self.value & self.Whole.value:
                dec_places = 0
            elif self.value & self.Tenths.value:
                dec_places = 1

            if self.value & self.Round.value:
                rounded_num = round(num, dec_places)
            elif self.value & self.Ceil.value:
                rounded_num = ceil(num, dec_places)
            elif self.value & self.Floor.value:
                rounded_num = floor(num, dec_places)

            if (self.value & self.Tenths.value) and (self.value & self.Whole.value):
                rounded_num = round_to_multiple(rounded_num, 10)
            if self.value & self.Fifths.value:
                rounded_num = round_fifths(rounded_num, dec_places)



            if (self.value & self.NinetyNine.value) or (self.value & self.NinetyFive.value):

                rounded_num = floor(rounded_num - 1, 0)

                multiplier = 10 ** (-2)

                additive = 0

                if self.value & self.NinetyNine.value:
                    additive = 99
                elif self.value & self.NinetyFive.value:
                    additive = 95

                rounded_num += additive * multiplier
        else:
            rounded_num = num
            dec_places = 0
            return_string = str(num)

        return_string = str(rounded_num)

        if trailing_zeros and self.value ^ self.NoRound.value and trailing_count >= 0:

            decimal_num = get_decimals(rounded_num)

            str_rounded_num = str(decimal_num)

            difference = trailing_count - len(str_rounded_num)

            if difference != 0:
                if difference > 0:
                    return_string = str(rounded_num)
                    for x in range(difference):
                        return_string = ''.join([return_string, "0"])
                else:
                    return_string = str(rounded_num)[:difference - 1]
        elif not self.value & self.NoRound.value:
            return_string = return_string.split('.')[0]

        if dollar_sign:
            return ''.join(['$', return_string])
        else:
            return return_string


class RoundingMethod:
    """Round settings structure

    Use for rounding numbers through a set structure instead of through the enumerator for RoundingFlags.

    Still uses RoundingFlags to round but this will hold all the settings (arguments) when rounding.

    """
    def __init__(self, rounding_flags, trailing_count=2, trailing_zeroes=True, dollar_sign=False):
        """

        Parameters
        ----------
        rounding_flags : RoundingFlags
            Flags used to round.
        trailing_count : int
            Amount of trailing zeroes for decimals.
        trailing_zeroes : bool
            if zeroes should trail.
        dollar_sign : bool
            if dollar sign is to be added to the returned string for rounding.
        """
        self.__rounding_flags__ = rounding_flags
        self.__trailing_count__ = trailing_count
        self.__trailing_zeroes__ = trailing_zeroes
        self.__dollar_sign__ = dollar_sign

    @property
    def get_rounding_flag(self) -> RoundingFlags:
        return self.__rounding_flags__

    @property
    def get_trailing_zeroes(self) -> bool:
        return self.__trailing_zeroes__

    @property
    def get_trailing_count(self) -> int:
        return self.__trailing_count__

    @property
    def get_dollar_sign(self) -> bool:
        return self.__dollar_sign__

    def set_rounding_flags(self, flags):
        """

        Parameters
        ----------
        flags : RoundingFlags

        Returns
        -------
        None
        """
        self.__rounding_flags__ = flags

    def set_trailing_zeroes(self, zeroes):
        """

        Parameters
        ----------
        zeroes : bool

        Returns
        -------
        None
        """
        self.__trailing_zeroes__ = zeroes

    def set_trailing_count(self, count):
        """

        Parameters
        ----------
        count : int

        Returns
        -------
        None
        """
        self.__trailing_count__ = count

    def set_dollar_sign(self, set_as):
        """

        Parameters
        ----------
        set_as : bool

        Returns
        -------
        None
        """
        self.__dollar_sign__ = set_as

    def round(self, number) -> str:
        """Round using RoundingFlags property.

        Using the property rounding_flags, the method 'do_round()' is called with the other properties.

        Parameters
        ----------
        number : float

        Returns
        -------
        str
        """
        return self.get_rounding_flag.do_round(number, self.get_trailing_count,
                                               self.get_trailing_zeroes, self.get_dollar_sign)


def get_decimals(number):
    """Get decimal numbers

    Parameters
    ----------
    number : float

    Returns
    -------
    int
    """
    str_num = str(number).split('.')
    length = len(str_num)
    if length != 2:
        return 0
    else:
        return int(str_num[1])

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
    # round_num = round(round_num)
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
    # round_num = round(round_num)
    return round_num

def round_fifths(number, dec_places):
    """Rounds to nearest fifth

    Assumes given decimal length of "num" as the wanted rounding place.

    Useful when slicing to round in non-decimal numbers by multiplying the return
    number by number places and then adding.

    Higher number decimal places means further down decimals.

    Can be negative decimal numbers and works with non-decimal numbers.

    Parameters
    ----------
    number : float
    dec_places : int

    Returns
    -------
    float
    """
    # Gets the last number of the float
    decimal_num = str(get_decimals(number))
    return_num = decimal_num
    difference = dec_places - len(return_num)
    if difference > 0:
        for x in range(difference):
            return_num = ''.join([return_num, '0'])
        return_num = return_num[dec_places-1]
    else:
        return_num = return_num[dec_places-1]
    rounded_num = int(return_num)

    multiplier = 10 ** (-dec_places)

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
    return_num = float(str(number)[:dec_places-len(decimal_num)] + "0")
    rounded_num *= multiplier
    return_num += rounded_num

    return return_num

def round_to_multiple(number, multiple):
    """For rounding non-decimals with multiples"""
    return multiple * round(number / multiple)

tax = 0.0725


