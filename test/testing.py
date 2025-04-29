import items
import unittest

def create_drink(name="", base=items.Bases.Water, flavors=None, size=items.DrinkSizes.Small):
    """Create a drink

    Parameters
    ----------
    name : string, optional
        name of drink
    base : items.Bases, optional
        choice of base
    flavors :  list of Flavors, optional
    size : items.DrinkSizes

    Returns
    ----------
    Drink
        Created drink
    """
    if flavors is None:
        flavors = []
    drink = items.Drink(name, base, size)
    drink.set_flavors(flavors)
    return drink




