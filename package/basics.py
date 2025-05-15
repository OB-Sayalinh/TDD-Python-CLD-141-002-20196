import math
from enum import Enum, auto, Flag
from abc import ABC, abstractmethod


class BaseEnum(Enum):
    """Hold Data for a price and a string name

        Use Pascal case for Enum properties.

        The string value for names should be the presented text, i.e. Coke and Rum.

        Methods
        ----------
        get_price
        get_dict
    """
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

    @classmethod
    def get_dict(cls):
        all_members = {}
        for member in list(cls):
            member_dict = {'name': member.value, 'price': member.get_price}
            all_members[member.name] = member_dict
        return all_members


# Rounding


class RoundingFlags(Flag):
    """Ways of rounding.

    Use the flags in conjunction to create specific ways of rounding.

    Some flags clash as there is a non-set priority between them.

    Be warned of weird effects of clashing flags.

    Default Decimal Position is to a hundredth.

    Default type of rounding if no rounding type is set is: Round.

    Attributes
    ----------
    NoRound : int
        Skips Rounding Types & Additional Numbers.
        No rounding done.
    Round : int
        Rounding Type
        Basic rounding done to the closest number.
    Ceil : int
        Rounding Type
        Round Up.
    Floor : int
        Rounding Type
        Round Down.
    Fifths : int
        Rounding Type
        Rounds to the nearest fifth in a hundredth
    Whole : int
        Decimal Position
        Rounded to nearest whole number.
    Tenths : int
        Decimal Position
        Changes from hundredths to tenths
    Tens : int
        Decimal Position
        Changes from hundredths to tens
    Hundreds : int
        Decimal Position
        Changes from hundredths to Hundreds
    NinetyNine : int
        Additional Number
        Sets ending to 99 (Floors)
    NinetyFive : int
        Additional Number
        Sets ending to 95 (Floors)

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
    Tens = auto()
    Hundreds = auto()
    Negatives = auto()
    NoTrailingZeros = auto()
    Signed = auto()


    def do_round(self, num, trailing_count=2, add_num_place=2):
        """Round given number with flags

        Parameters
        ----------
        num : float
            Number to Round
        trailing_count : int , optional
            Amount of trailing zeroes to add
        add_num_place : int, default 2
            The decimal place to add additional numbers

        Returns
        -------
        string

        Examples
        --------
        >>> flags = RoundingFlags.Round
        ... flags.do_round(10.2339)
        10.23

        >>> flags = RoundingFlags.Ceil
        ... flags.do_round(10.2339)
        10.24

        Defaults to basic rounding when just rounding.

        >>> flags = RoundingFlags.Whole
        ... flags.do_round(10.499)
        10

        >>> flags = RoundingFlags.Floor | RoundingFlags.Whole
        ... flags.do_round(10.7339)
        11

        Goes from $10 to $9 then adds 99 cents.

        >>> flags = RoundingFlags.Round | RoundingFlags.NinetyNine
        ... flags.do_round(10.2339)
        9.99

        When wanting to ceil the result of specific number flags like NinetyNine, you need the
        rounding to be in the correct number place (in this case as a whole number).
        EQ: Lower number place + 2 = number place to round to.

        >>> flags = RoundingFlags.Ceil | RoundingFlags.Whole | RoundingFlags.NinetyFive
        ... flags.do_round(10.2339)
        10.95

        >>> flags = RoundingFlags.Tenths
        ... flags.do_round(10.2339)
        10.2

        >>> flags = RoundingFlags.Fifths
        ... flags.do_round(10.2339)
        10.25

        Odd paring of flags.

        >>> flags = RoundingFlags.Tenths | RoundingFlags.Whole
        ... flags.do_round(10.2339)
        1
        """

        trailing_zeros = True
        negatives = False
        signed = False

        if self.value & self.NoTrailingZeros.value:
            trailing_zeros = False
        if self.value & self.Negatives.value:
            negatives = True
        if self.value & self.Signed.value:
            signed = True

        rounded_num = num

        dec_places = 2

        # Rounding & Additional Numbers

        if not (self.value & self.NoRound.value):

            # Set Decimal Places

            if self.value & self.Whole.value:
                dec_places = 0
            elif self.value & self.Tenths.value:
                dec_places = 1
            elif self.value & self.Tens.value:
                dec_places = -1
            elif self.value & self.Hundreds.value:
                dec_places = -2

            # Apply Rounding Types

            if self.value & self.Round.value:
                rounded_num = round(num, dec_places)
            elif self.value & self.Ceil.value:
                rounded_num = ceil(num, dec_places)
            elif self.value & self.Floor.value:
                rounded_num = floor(num, dec_places)
            elif self.value & self.Fifths.value:
                rounded_num = round_fifths(num, dec_places)
            else:
                rounded_num = round(num, dec_places)

            # Add Additional Numbers

            if (self.value & self.NinetyNine.value) or (self.value & self.NinetyFive.value):

                # Not the same as dec_places
                dec_place = add_num_place - 2

                tens = 10 ** (-dec_place)

                use_num = rounded_num - tens

                rounded_num = floor(use_num, dec_place)

                multiplier = 10 ** (-add_num_place)

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

        # Text Formatting

        add_negative = False

        # Keep info on negative

        if self.value & self.NoRound.value:
            pass
        elif not negatives:
            if rounded_num < 0:
                rounded_num = 0.0
        else:
            if rounded_num < 0:
                add_negative = True

        return_string = str(rounded_num).replace('-', '')

        # Add trailing zeroes

        if trailing_zeros and not (self.value & self.NoRound.value) and trailing_count >= 0:

            decimal_num = get_decimals(rounded_num)

            str_rounded_dec = str(decimal_num)

            difference = trailing_count - len(str_rounded_dec)

            if difference != 0:
                if difference > 0:
                    return_string = return_string
                    for x in range(difference):
                        return_string = ''.join([return_string, "0"])
                else:
                    return_string = ''.join(return_string[:difference])

            if len(return_string.split('.')[1]) == 0:
                return_string = return_string.split('.')[0]
        # Return whole number if no trailing zeroes are to be added
        elif not self.value & self.NoRound.value and not trailing_zeros:
            return_string = return_string.split('.')[0]

        if add_negative:
            return_string = ''.join(['-',return_string])

        if signed:
            return ''.join(['$', return_string])
        else:
            return return_string


class RoundingMethod:
    """Round settings structure

    Use for rounding numbers through a set structure instead of through the enumerator for RoundingFlags.

    Still uses RoundingFlags to round but this will hold all the settings (arguments) when rounding.

    """
    def __init__(self, rounding_flags, trailing_count=2, add_num_place=2):
        """

        Parameters
        ----------
        rounding_flags : RoundingFlags
            Flags used to round.
        trailing_count : int, default 2
            Amount of trailing zeroes for decimals.
        add_num_place : int, default 2
            Decimal place for added on numbers
        """
        self.__rounding_flags__ = rounding_flags
        self.__trailing_count__ = trailing_count
        self.__add_num_place__ = add_num_place

    @property
    def get_rounding_flag(self) -> RoundingFlags:
        return self.__rounding_flags__

    @property
    def get_add_num_place(self) -> int:
        return self.__add_num_place__

    @property
    def get_trailing_count(self) -> int:
        return self.__trailing_count__

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

    def set_add_num_place(self, dec_place):
        """

        Parameters
        ----------
        dec_place : int

        Returns
        -------
        None
        """
        self.__add_num_place__ = dec_place

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
                                               self.get_add_num_place)


def get_decimals(number):
    """Get decimal numbers

    Parameters
    ----------
    number : float

    Returns
    -------
    str
    """
    str_num = str(number).split('.')
    length = len(str_num)
    if length != 2:
        return 0
    else:
        return str_num[1]

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
    return_num = float(str(number)[:dec_places-len(decimal_num)-1] + "0")
    rounded_num *= multiplier
    return_num += rounded_num

    return round(return_num, dec_places)

def round_to_multiple(number, multiple):
    """For rounding non-decimals with multiples"""
    return multiple * round(number / multiple)


# Base Item Class
class Item(ABC):

    @abstractmethod
    def get_price(self):
        raise NotImplementedError()

    @abstractmethod
    def get_name(self):
        raise NotImplementedError()

    @abstractmethod
    def get_size(self):
        raise NotImplementedError()

    @abstractmethod
    def set_name(self, name):
        raise NotImplementedError()

    @abstractmethod
    def set_size(self, size):
        raise NotImplementedError()


tax = 0.0725





