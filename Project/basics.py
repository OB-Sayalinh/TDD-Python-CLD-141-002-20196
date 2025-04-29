from enum import Enum


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


tax = 0.0725


