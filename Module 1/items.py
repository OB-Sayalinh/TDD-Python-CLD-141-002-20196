from basics import BaseEnum
from abc import ABC, abstractmethod


# Base Item Class
class Item(ABC):

    @abstractmethod
    def get_price(self):
        pass

    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_size(self):
        pass

# Drinks


class Bases(BaseEnum):
    Water = 'Water'
    Sbrite = 'Sbrite'
    Pokeacola = 'Pokeacola'
    MrSalt = 'Mr. Salt'
    HillFog = 'hill fog'
    LeafWine = 'Leaf Wine'


class Flavors(BaseEnum):
    Lemon = 'Lemon',
    Cherry = 'Cherry',
    Strawberry = 'Strawberry',
    Mint = 'Mint',
    Blueberry = 'Blueberry',
    Lime = 'Lime'


class DrinkSizes(BaseEnum):
    Small = "Small", 1.50
    Medium = "Medium", 1.75
    Large = "Large", 2.05
    Mega = "Mega", 2.15


class Drink(Item):
    """Create a beverage with a base and flavors"""
    def __init__(self, name, base, size):
        """

        Parameters
        ----------
        name : string
        base : Bases
        size : DrinkSizes
        """
        self.__base__ = base
        self.__flavors__ = []
        self.__name = name
        self.__size__ = size

    @property
    def get_base(self):
        return self.__base__

    @property
    def get_flavors(self):
        return self.__flavors__

    @property
    def get_num_flavors(self):
        return len(self.__flavors__)

    @property
    def get_price(self):
        super().get_price()
        price = self.__base__.get_price
        for flavor in self.__flavors__:
            price += flavor.get_price

        price += self.__size__.get_price
        return price

    @property
    def get_name(self):
        super().get_name()
        return self.__name

    @property
    def get_size(self):
        return self.__size__

    def set_flavors(self, flavors):
        """Set the flavors

        Parameters
        ----------
        flavors : list of Flavors
        """
        temp_flavors = []
        for flavor in flavors:
            if not temp_flavors.count(flavor):
                temp_flavors.append(flavor)
        self.__flavors__ = temp_flavors

    def add_flavor(self, flavor):
        """Add a singular flavor

        Parameters
        ----------
        flavor : Flavors
        """
        if not self.__flavors__.count(flavor):
            self.__flavors__.append(flavor)
