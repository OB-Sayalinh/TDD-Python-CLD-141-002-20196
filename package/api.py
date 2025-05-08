from flask import Flask, request
from pydoc import locate
import package.basics
import package.items as IT
from package.items import Bases

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

    item_class = locate(info.get('class'))

    item_flavors = None

    if type(item_class) is IT.Drink or True:
        item_base = IT.Bases[info.get('base')]
        item_flavors = info.get('flavors')
        item = IT.Drink(item_name, base=item_base, size=item_size)
        item.set_flavors(item_flavors)
    elif item_class is IT.Food:
        item_food_choice = info.get('food_choice')
        item_toppings = info.get('toppings')
        item = IT.Food(item_name, item_size, food_choice=item_food_choice)
        item.set_toppings(item_toppings)

    return {
        'name' : item.get_name,
        'base' : item.get_base.value,
        'size' : item.get_size.value,
        'flavors' : item_flavors,
        'price' : str(item.get_price)
    }
