from flask import Flask, request
from pydoc import locate
import package.basics
import package.items as IT
from package.items import Bases

import sys

def str_to_class(class_name):
    return getattr(IT, class_name)

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

    item_size = IT.DrinkSizes[info.get('size')]

    item_class = str_to_class(info.get('class'))

    item_flavors = None

    if item_class is IT.Drink:
        item_base = IT.Bases[info.get('base')]
        item_flavors =  info.getlist('flavors[]')
        flavors = []
        for flavor in item_flavors:
            flavors.append(IT.Flavors[flavor])
        item = IT.Drink(item_name, base=item_base, size=item_size)
        item.set_flavors(flavors)
        return {
            'name': item.get_name,
            'base': item.get_base.value,
            'size': item.get_size.value,
            'flavors': item_flavors,
            'price': str(item.get_price)
        }
    elif item_class is IT.Food:
        item_food_choice = IT.Foods(info.get('food_choice'))
        item_toppings = info.getlist('toppings[]')
        toppings = []
        for topping in item_toppings:
            toppings.append(IT.Toppings[topping])
        item = IT.Food(item_name, item_size, food_choice=item_food_choice)
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
