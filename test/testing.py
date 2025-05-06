import package.items as items
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
    items.Drink
        Created drink
    """
    if flavors is None:
        flavors = []
    drink = items.Drink(name, base, size)
    drink.set_flavors(flavors)
    return drink

def create_food(name="", food_choice=items.Foods.Hotdog, size=items.FoodSizes.Small, toppings=None):
    """Create a drink

    Parameters
    ----------
    name : string, optional
        name of drink
    size : items.FoodSizes, optional
    food_choice : items.Foods, optional
    toppings :  list of Toppings, optional


    Returns
    ----------
    items.Food
        Created Food object
    """
    if toppings is None:
        toppings = []
    drink = items.Food(name, size, food_choice)
    drink.set_toppings(toppings)
    return drink


