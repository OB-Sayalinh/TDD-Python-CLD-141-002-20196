from .basics import BaseEnum
from abc import ABC, abstractmethod


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
    """Beverage with a base and flavors"""

    __price_per_additional_flavor__ = 0.15

    def __init__(self, name, base, size):
        """Create a beverage with a base and flavors

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

    def __repr__(self):

        string = "(Drink) {name}; {base}; {flavors}; {size}".format(name=self.get_name,
                                                                 base=self.get_base,
                                                                 flavors=self.get_flavors,
                                                                 size=self.get_size)
        return string

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
        price = self.__base__.get_price
        count = 0
        for flavor in self.__flavors__:
            price += flavor.get_price
            if count != 0:
                price += self.add_flavor_price
            count += 1

        price += self.__size__.get_price
        return price

    @property
    def get_name(self):
        return self.__name

    @property
    def get_size(self):
        return self.__size__

    @property
    def add_flavor_price(self):
        """Pricing for every additional flavor"""
        return self.__price_per_additional_flavor__

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

    def set_size(self, size):
        """

        Parameters
        ----------
        size : DrinkSizes
        """
        self.__size__ = size

    def set_name(self, name):
        """

        Parameters
        ----------
        name : str
        """
        self.__name = name



