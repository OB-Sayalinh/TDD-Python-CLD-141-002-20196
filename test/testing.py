from package.drink import Bases, DrinkSizes, Drink, Flavors
from package.food import Food, FoodSizes, Foods
from package.ice_cream import IceCream, IceCreamSizes, Additionals
from package.ice_cream import Flavors as ICFlavors

def create_drink(name="", base=Bases.Water, flavors=None, size=DrinkSizes.Small):
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
    drink = Drink(name, base, size)
    drink.set_flavors(flavors)
    return drink

def create_food(name="", food_choice=Foods.Hotdog, size=FoodSizes.Small, toppings=None):
    """Create a food

    Parameters
    ----------
    name : string, optional
        name of food
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
    food = Food(name, size, food_choice)
    food.set_toppings(toppings)
    return food

def create_ice_cream(name="", size=IceCreamSizes.Scoop, flavors=None, additionals=None):
    """Create an ice cream

    Parameters
    ----------
    name : string, default ""
        name of ice cream
    size : IceCreamSizes, default IceCreamSizes.Scoop
    flavors : list of ICFlavors, default [ICFlavors.Banana]
    additionals :  list of Additionals, optional


    Returns
    ----------
    items.Food
        Created Food object
    """
    if flavors is None:
        flavors = []
    if additionals is None:
        additionals = []
    ice_cream = IceCream(name, size, flavors)
    ice_cream.set_additionals(additionals)
    return ice_cream



