from flask import Flask, request
import package.basics as basics
import package.drink as drink
import package.food as food
import package.ice_cream as ic

item_packages = (drink, food, ic)

import sys

def str_to_class(class_name):
    cls = None
    for package in item_packages:
        result = getattr(package, class_name, 0)
        if result != 0:
            cls = result
            break
    return cls

app = Flask(__name__.split('.')[0])

@app.route('/')
def hello_world():
    return '<p>Hello, World!</p>'

@app.route('/get-message')
def new():
    return '<p>Wow! New Message</p>'

@app.get('/item')
def get_item():
    return '<p>Up and running!</p>'

@app.post('/item')
def make_item():

    item = {}

    info = request.form

    item_name = info.get('name')

    item_class = str_to_class(info.get('class'))

    item_flavors = None

    if item_class is drink.Drink:
        item_base = drink.Bases[info.get('base')]
        item_flavors =  info.getlist('flavors[]')
        flavors = []
        for flavor in item_flavors:
            flavors.append(drink.Flavors[flavor])
        item_size = drink.DrinkSizes[info.get('size')]

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
        item_toppings = info.getlist('toppings[]')
        toppings = []
        for topping in item_toppings:
            toppings.append(food.Toppings[topping])
        item_size = food.FoodSizes[info.get('size')]

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
        data_flavors = info.getlist('ic_flavors')
        flavors = []
        for flavor in data_flavors:
            flavors.append(ic.Flavors[flavor])
        data_additionals = info.getlist('additionals')
        additionals = []
        for additional in data_additionals:
            additionals.append(ic.Additionals[additional])
        size = ic.IceCreamSizes[info.get('size')]

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







