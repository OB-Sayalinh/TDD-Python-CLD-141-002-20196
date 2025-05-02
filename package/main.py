"""Creates Orders"""

from test.testing import create_drink
from items import Flavors
from order import Order

if __name__ == '__main__':
    order = Order()

    drink1 = create_drink(name="Baja Blast", flavors=[Flavors.Lime, Flavors.Lemon])

    drink2 = create_drink(name="Sparkles", flavors=[Flavors.Cherry, Flavors.Blueberry, Flavors.Strawberry])

    order.add_item(drink1)

    order.add_item(drink2)

    print(drink1)

    print(order.get_receipt)
