from package.basics import BaseEnum
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
    HillFog = 'Hill Fog'
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

        string = "(Drink) {name}; {base}; {flavors}; {size}; {price}".format(name=self.get_name,
                                                                base=self.get_base,
                                                                flavors=self.get_flavors,
                                                                size=self.get_size,
                                                                price=self.get_price
                                                                )
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
        if not type(flavors) is list:
            raise TypeError()
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


# Food


class Foods(BaseEnum):
    Hotdog = 'Hotdog', 2.30
    Corndog = "Corndog", 2.00
    IceCream = "Ice Cream", 3.00
    OnionRings = "Onion Rings", 1.75
    FrenchFries = "French Fries", 1.50
    TaterTots = "Tater Tots", 1.70
    NachoChips = "Nacho Chips", 1.90


class Toppings(BaseEnum):
    Cherry = "Cherry", 0.00
    WhippedCream = "Whipped Cream", 0.00
    CaramelSauce = "Caramel Sauce", 0.50
    ChocolateSauce = "Chocolate Sauce", 0.50
    NachoCheese = "Nacho Cheese", 0.30
    Chili = "Chili", 0.60
    BaconBits = "Bacon Bits", 0.30
    Ketchup = "Ketchup", 0.00
    Mustard = "Mustard", 0.00


class FoodSizes(BaseEnum):
    Small = "Small", 0.00
    Medium = "Medium", 0.00
    Large = "Large", 0.00
    Mega = "Mega", 0.00


class Food(Item):
    """Food item with a choice of food and toppings"""
    def __init__(self, name, size, food_choice):
        """Create a beverage with a base and flavors

        Parameters
        ----------
        name : string
        size : DrinkSizes
        food_choice : Foods
        """
        self.__name = name
        self.__size__ = size

        self.__food_choice__ = food_choice
        self.__toppings__ = []

    def __repr__(self):

        string = "(Food) {name}; {food_choice}; {toppings}; {size}; {price}".format(name=self.get_name,
                                                                food_choice=self.get_food_choice,
                                                                toppings=self.get_toppings,
                                                                size=self.get_size,
                                                                price=self.get_price)
        return string

    @property
    def get_food_choice(self):
        return self.__food_choice__

    @property
    def get_toppings(self):
        return self.__toppings__

    @property
    def get_num_toppings(self):
        return len(self.__toppings__)

    @property
    def get_price(self):
        price = self.__food_choice__.get_price
        count = 0

        for topping in self.__toppings__:
            price += topping.get_price

        price += self.__size__.get_price
        return price

    @property
    def get_name(self):
        return self.__name

    @property
    def get_size(self):
        return self.__size__

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

    def set_food_choice(self, food_choice):
        self.__food_choice__ = food_choice

    def set_toppings(self, toppings):
        """Set the flavors

        Parameters
        ----------
        toppings : list of Toppings
        """
        temp_toppings = []
        for topping in toppings:
            if not temp_toppings.count(topping):
                temp_toppings.append(topping)
        self.__toppings__ = temp_toppings

    def add_topping(self, topping):
        """Add a singular flavor

        Parameters
        ----------
        topping : Toppings
        """
        if not self.__toppings__.count(topping):
            self.__toppings__.append(topping)













