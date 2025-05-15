getItem = async(type) => {

    const { getItem } = await import("./call.js");

    return getItem(type)

}

postItem = async(data) => {

    const { postItem } = await import("./call.js");

    return postItem(data)

}

itemInfo = null


selectType_elem = document.getElementById('select_type')

// Drink
base_elem = document.getElementById('base')
flavors_elem = document.getElementById('flavors_body')

// Food

foodChoice_elem = document.getElementById('food_choice')
toppings_elem = document.getElementById('toppings_body')

// Ice Cream

ic_flavors_elem = document.getElementById('ic_flavors_body')
additionals_elem = document.getElementById('additionals_body')


class_elem = undefined

current_type = undefined

window.onload = async() => {

    // Set all item information
    itemInfo = await getItem('')

    create = (parent, json, name, asTd = true) => {
        cell = document.createElement('td')

        result = makeInputSelection(json, name)

        if (asTd){

            appendChildren(cell, result)

            parent.appendChild(cell)

        }
        else{
            appendChildren(parent, result)
        }
    }

    // Drink

    create(base_elem, itemInfo.drink.bases, 'base', false)

    create(flavors_elem, itemInfo.drink.flavors, 'flavors')

    // Food

    create(foodChoice_elem, itemInfo.food.food_choice, 'food_choice', false)

    create(toppings_elem, itemInfo.food.toppings, 'toppings')


    // Ice Cream

    create(ic_flavors_elem, itemInfo.ice_cream.flavors, 'ic_flavors')

    create(additionals_elem, itemInfo.ice_cream.additionals, 'additionals')

    // Classes

    class_elem = document.getElementById('class')

    selectType_elem.onchange = (e) => {
        current_type = e.target.value
        set_type(current_type)
    }    
    current_type = selectType_elem.value
    set_type(current_type)

}

makeInputSelection = (json, formName) => {
    
    keys = Object.keys(json)

    select = document.createElement('select')
    for(x = 0; x < keys.length; x++){
        var name = keys[x]
        text = json[name].name
        option = create_option(name, text)
        select.appendChild(option)
    }

    input = document.createElement('input')
    input.type = 'hidden'
    input.name = formName

    input.value = select.value 

    select.onchange = (e) => {
        input.value = e.target.value 
    }    

    return [input, select]

}


function set_type(type){
    if (type == "Food"){
        set_drink_visibility('none')
        set_food_visibility('')
        set_ic_visibility('none')
    }
    else if(type == "Drink"){
        set_drink_visibility('')
        set_food_visibility('none')
        set_ic_visibility('none')
    }
    else if(type == "IceCream"){
        set_drink_visibility('none')
        set_food_visibility('none')
        set_ic_visibility('')
    }
    class_elem.value = type
}

// Visibility

function set_drink_visibility(type){
    flavors_elem.style.display = type
    base_elem.style.display = type
}

function set_food_visibility(type){
    foodChoice_elem.style.display = type
    toppings_elem.style.display = type
}

function set_ic_visibility(type){
    ic_flavors_elem.style.display = type
    additionals_elem.style.display = type
}

function create_option(value, text){
    option = document.createElement('option')
    option.value = value
    option.textContent = text
    return option
}

appendChildren = (node, elements) => {
    for (x = 0; x < elements.length; x++){
        node.appendChild(elements[x])
    }
}





