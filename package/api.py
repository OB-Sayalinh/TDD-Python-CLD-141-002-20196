from flask import Flask, request
from flask_cors import CORS, cross_origin
import package.basics as basics
import package.drink as drink
import package.food as food
import package.ice_cream as ic

item_packages = (drink, food, ic)

def str_to_class(class_name):
    cls = None
    for package in item_packages:
        result = getattr(package, class_name, 0)
        if result != 0:
            cls = result
            break
    return cls

app = Flask(__name__.split('.')[0])
cors = CORS(app, resources={r"/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
def hello_world():
    return '<p>Hello, World!</p>'

@app.route('/get-message')
def new():
    return '<p>Wow! New Message</p>'

# Get Items

@app.get('/items')
def get_item():
    return {
        'food' : get_food(),
        'drink' : get_drink(),
        'ice_cream' : get_ice_cream()
    }

@app.get('/items/food')
def get_food():
    topping = food.Toppings.Cherry
    food_choice = food.Foods.Hotdog
    size = food.FoodSizes.Small
    return {
        'toppings' : topping.get_dict(),
        'food_choice': food_choice.get_dict(),
        'size': size.get_dict()
    }

@app.get('/items/drink')
def get_drink():
    flavor = drink.Flavors.Cherry
    base = drink.Bases.Water
    size = drink.DrinkSizes.Small
    return {
        'flavors': flavor.get_dict(),
        'bases': base.get_dict(),
        'size': size.get_dict()
    }

@app.get('/items/ice-cream')
def get_ice_cream():
    additionals = ic.Additionals.Cherry
    flavor = ic.Flavors.Banana
    size = ic.IceCreamSizes.Scoop
    return {
        'additionals': additionals.get_dict(),
        'flavors': flavor.get_dict(),
        'size': size.get_dict()
    }

@app.route('/item', methods=['GET', 'POST'])
def make_item():

    item = {}

    info = request.get_json()

    item_name = info['name']

    item_class = str_to_class(info['class'])

    item_flavors = None

    if item_class is drink.Drink:
        item_base = drink.Bases[info['base']]
        item_flavors = info['flavors']
        flavors = []
        if type(item_flavors) is list:
            for flavor in item_flavors:
                flavors.append(drink.Flavors[flavor])
        else:
            flavors = [drink.Flavors[item_flavors]]
        item_size = drink.DrinkSizes[info['size']]

        item = drink.Drink(item_name, base=item_base, size=item_size)
        item.set_flavors(flavors)

        return {
            'name': item.get_name,
            'base': item.get_base.value,
            'size': item.get_size.value,
            'flavors': item_flavors,
            'price': str(item.get_price)
        }
    elif item_class is food.Food:
        item_food_choice = food.Foods(info.get('food_choice'))
        item_toppings = info['toppings']
        toppings = []
        if type(item_toppings) is list:
            for topping in item_toppings:
                toppings.append(food.Toppings[topping])
        else:
            toppings = [food.Toppings[item_toppings]]
        item_size = food.FoodSizes[info['size']]

        item = food.Food(item_name, item_size, food_choice=item_food_choice)
        item.set_toppings(toppings)
        str_toppings = []
        for topping in item.get_toppings:
            str_toppings.append(topping.value)

        return {
            'name': item.get_name,
            'food_choice': item.get_food_choice.value,
            'size': item.get_size.value,
            'toppings': str_toppings,
            'price': str(item.get_price)
        }
    elif item_class is ic.IceCream:
        data_flavors = info['ic_flavors']
        flavors = []
        if type(data_flavors) is list:
            for flavor in data_flavors:
                flavors.append(ic.Flavors[flavor])
        else:
            flavors = [ic.Flavors[data_flavors]]
        data_additionals = info['additionals']
        additionals = []
        if type(data_additionals) is list:
            for additional in data_additionals:
                additionals.append(ic.Additionals[additional])
        else:
            additionals = [ic.Additionals[data_additionals]]
        size = ic.IceCreamSizes[info['size']]

        item = ic.IceCream(name=item_name, size=size, flavors=flavors)
        item.set_additionals(additionals)

        str_flavors = []
        for flavor in item.get_flavors:
            str_flavors.append(flavor.value)
        str_additionals = []
        for additional in item.get_additionals:
            str_additionals.append(additional.value)

        return {
            'name': item.get_name,
            'flavors': str_flavors,
            'size': item.get_size.value,
            'additionals': str_additionals,
            'price': str(item.get_price)
        }





