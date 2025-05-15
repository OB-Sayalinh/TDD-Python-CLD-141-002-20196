from package.basics import BaseEnum, Item


class Flavors(BaseEnum):
    MintChocolateChip = 'Mint Chocolate Chip', 4.00
    Chocolate = "Chocolate", 3.00
    VanillaBean = "Vanilla Bean", 3.00
    Banana = "Banana", 3.50
    ButterPecan = "Butter Pecan", 3.50
    Smore = "S'more", 4.00


class Additionals(BaseEnum):
    Cherry = "Cherry", 0.00
    WhippedCream = "Whipped Cream", 0.00
    CaramelSauce = "Caramel Sauce", 0.50
    ChocolateSauce = "Chocolate Sauce", 0.50
    Storios = "Storios", 1.00
    DigDogs = "Dig Dogs", 1.00
    TandT = "T&T's", 1.00
    CookieDough = "Cookie Dough", 1.00
    Pecans = "Pecans", 0.50


class IceCreamSizes(BaseEnum):
    """

    Attributes
    ----------
    get_max_scoops
    get_default_scoops
        returns dictionary of scoop count to a size
    """
    Scoop = "Scoop", 1, 0.00
    DoubleScoop = "Double Scoop", 2, 0.00
    TripleScoop = "Triple Scoop", 3, 0.00
    QuadrupleScoop = "Quadruple Scoop", 4, 0.00
    PentaScoop = "Penta Scoop", 5, 0.00
    SenaryScoop = "Senary Scoop", 6, 0.00
    Sundae = "Sundae", 3, 0.00

    # def __init__(self, name, max_scoops, price=0):
    #     super().__init__(name, max_scoops, price=0)
    #

    def __new__(cls, name, max_scoops, price=0):
        """

        Parameters
        ----------
        name : str
        price : float
        max_scoops : int
        """
        member = object.__new__(cls)
        member._value_ = name
        member._max_scoops_ = max_scoops
        member._price_ = price
        return member

    @property
    def get_max_scoops(self) -> int:
        return self._max_scoops_

    def get_default_scoops(self):
        """Get Scoops to Default to

        An amount of scoops up to 6 (including) has a default size.

        A scoop of 0 defaults to the 1 option.

        Returns
        -------
        dict of int : size
        """
        return {
            0 : self.Scoop,
            1 : self.Scoop,
            2 : self.DoubleScoop,
            3 : self.TripleScoop,
            4 : self.QuadrupleScoop,
            5 : self.PentaScoop,
            6 : self.SenaryScoop
        }

    @classmethod
    def get_dict(cls):
        all_members = {}
        for member in list(cls):
            member_dict = {'name': member.value, 'price': member.get_price, 'scoops': member.get_max_scoops}
            all_members[member.name] = member_dict
        return all_members

class IceCream(Item):
    """IceCream item with a choice of food and additionals"""
    def __init__(self, name, size, flavors, auto_size=True):
        """Create an Ice Cream with flavors and additions

        Parameters
        ----------
        name : string
        size : IceCreamSizes
        flavors : list of Flavors
        auto_size : bool default True
            automatically set the size
        """
        self.__name = name
        if auto_size:
            self.__size__ = IceCreamSizes.get_default_scoops(size)[len(flavors)]
        else:
            self.__size__ = size

        self.__flavors__ = flavors
        self.__additionals__ = []

    def __repr__(self):

        string = "(IceCream) {name}; {flavors}; {additionals}; {size}; {price}".format(name=self.get_name,
                                                                flavors=self.get_flavors,
                                                                additionals=self.get_additionals,
                                                                size=self.get_size,
                                                                price=self.get_price)
        return string

    # Getters

    @property
    def get_flavors(self):
        return self.__flavors__

    @property
    def get_additionals(self):
        return self.__additionals__

    @property
    def get_num_additionals(self):
        return len(self.__additionals__)

    @property
    def get_num_flavors(self):
        return len(self.__flavors__)

    @property
    def get_price(self):
        price = 0

        for flavor in self.__flavors__:
            price += flavor.get_price

        for additional in self.__additionals__:
            price += additional.get_price

        price += self.__size__.get_price
        return price

    @property
    def get_name(self):
        return self.__name

    @property
    def get_size(self):
        return self.__size__

    @property
    def get_max_flavors(self):
        return self.__size__.get_max_scoops

    # Setter and Misc

    def set_size(self, size):
        """

        Parameters
        ----------
        size : IceCreamSizes
        """
        if self.get_num_flavors >= size.get_max_scoops:
            return False
        else:
            self.__size__ = size
            return True

    def set_name(self, name):
        """

        Parameters
        ----------
        name : str
        """
        self.__name = name

    def set_flavors(self, flavors):
        if len(flavors) > self.get_max_flavors:
            self.__flavors__ = flavors[:-len(flavors) + 1]
        else:
            self.__flavors__ = flavors

    def add_flavor(self, flavor):
        if len(self.__flavors__) >= self.get_max_flavors:
            return False
        else:
            self.__flavors__.append(flavor)
            return True

    def set_additionals(self, additionals):
        """Set the flavors

        Parameters
        ----------
        additionals : list of Flavors
        """
        temp_additionals = []
        for additional in additionals:
            if not temp_additionals.count(additional):
                temp_additionals.append(additional)
        self.__additionals__ = temp_additionals

    def add_additional(self, additional):
        """Add a singular flavor

        Parameters
        ----------
        additional : Flavors
        """
        if not self.__additionals__.count(additional):
            self.__additionals__.append(additional)




