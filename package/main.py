"""Create Orders"""
from package.food import Toppings
from test.testing import create_drink, create_food, create_ice_cream
from food import Foods, Toppings
from drink import Flavors
import ice_cream as IC
from order import Order

if __name__ == '__main__':
    order = Order()

    drink1 = create_drink(name="Baja Blast", flavors=[Flavors.Lime, Flavors.Lemon])

    drink2 = create_drink(name="Sparkles", flavors=[Flavors.Cherry, Flavors.Blueberry, Flavors.Strawberry])

    order.add_item(drink1)

    order.add_item(drink2)

    print(order.get_receipt)

    food1 = create_food(name="Hotdog", food_choice=Foods.Hotdog,
                        toppings=[Toppings.Chili, Toppings.Mustard])

    food2 = create_food(name="Bacon Split", food_choice= Foods.IceCream,
                        toppings=[Toppings.Cherry, Toppings.CaramelSauce, Toppings.BaconBits])

    order.add_item(food1)

    order.add_item(food2)

    print(order.get_receipt)

    ice_cream1 = create_ice_cream(name="Banana Split", flavors=
                        [IC.Flavors.Banana, IC.Flavors.Chocolate],
                        additionals=[IC.Additionals.WhippedCream, IC.Additionals.Cherry],
                        size=IC.IceCreamSizes.Sundae)

    ice_cream2 = create_ice_cream(name="Smore Delight", flavors=
                        [IC.Flavors.Smore, IC.Flavors.VanillaBean, IC.Flavors.Smore],
                        additionals=[IC.Additionals.WhippedCream, IC.Additionals.Cherry],
                        size=IC.IceCreamSizes.TripleScoop)

    order.add_item(ice_cream1)

    order.add_item(ice_cream2)

    print(order.get_receipt)




