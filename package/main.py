"""Create Orders"""
from package.items import Toppings
from test.testing import create_drink, create_food
from items import Flavors, Foods, Toppings
from order import Order

if __name__ == '__main__':
    order = Order()

    drink1 = create_drink(name="Baja Blast", flavors=[Flavors.Lime, Flavors.Lemon])

    drink2 = create_drink(name="Sparkles", flavors=[Flavors.Cherry, Flavors.Blueberry, Flavors.Strawberry])

    order.add_item(drink1)

    order.add_item(drink2)

    # print(drink1)

    print(order.get_receipt)

    food1 = create_food(name="Hotdog", food_choice=Foods.Hotdog,
                        toppings=[Toppings.Chili, Toppings.Mustard])

    food2 = create_food(name="Bacon Split", food_choice= Foods.IceCream,
                        toppings=[Toppings.Cherry, Toppings.CaramelSauce, Toppings.BaconBits])

    order.add_item(food1)

    order.add_item(food2)

    # print(food1)

    print(order.get_receipt)




