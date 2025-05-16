getItem = async(type) => {

    const { getItem } = await import("./call.js");

    return getItem(type)

}

postItem = async(data) => {

    formData = new FormData(data)

    formData.delete('size')

    formData.append('size', currentSize_elem.value)

    const { postItem } = await import("./call.js");

    return postItem(formData, asFormData=true)

}

itemInfo = null

selectType_elem = document.getElementById('select_type')
sizes_elem = document.getElementById('sizes')

form = document.getElementById('itemForm')

form.addEventListener("submit", (event) => {
    event.preventDefault();
    console.log(postItem(event.target));
});

// Base Elements
// Drink
base_elem = document.getElementById('base')
flavors_elem = document.getElementById('flavors_body')
drinkSizes_elem = undefined

// Food

foodChoice_elem = document.getElementById('food_choice')
toppings_elem = document.getElementById('toppings_body')
foodSizes_elem = undefined

// Ice Cream

ic_flavors_elem = document.getElementById('ic_flavors_body')
additionals_elem = document.getElementById('additionals_body')
iceCreamSizes_elem = undefined

currentSize_elem = undefined

createItem_btn = document.getElementById('createItem')

class_elem = undefined

current_type = undefined

window.onload = async() => {

    // Set all item information
    itemInfo = await getItem('')

    // Creating Selections


    create = (parent, json, name, asTd = true) => {

        result = makeInputSelection(json, name)

        if (asTd){

            cell = document.createElement('td')

            appendChildren(cell, result)

            parent.appendChild(cell)

        }
        else{
            appendChildren(parent, result)
        }

        return result

    }

    // Drink

    create(base_elem, itemInfo.drink.bases, 'base', false)

    create(flavors_elem, itemInfo.drink.flavors, 'flavors')

    drinkSizes_elem = create(sizes_elem, itemInfo.drink.size, 'size', false)[0]

    drinkSizes_elem.disabled = true

    // Food

    create(foodChoice_elem, itemInfo.food.food_choice, 'food_choice', false)

    create(toppings_elem, itemInfo.food.toppings, 'toppings')

    foodSizes_elem = create(sizes_elem, itemInfo.food.size, 'size', false)[0]

    foodSizes_elem.disabled = true


    // Ice Cream

    create(ic_flavors_elem, itemInfo.ice_cream.flavors, 'ic_flavors')

    create(additionals_elem, itemInfo.ice_cream.additionals, 'additionals')

    iceCreamSizes_elem = create(sizes_elem, itemInfo.ice_cream.size, 'size', false)[0]

    iceCreamSizes_elem.disabled = true

    // Create Item Button

    createItem_btn.onclick = (e) => {
        
    }

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
    drinkSizes_elem.style.display = type
    if (type == 'none'){
        drinkSizes_elem.disabled = true
    } else {
        drinkSizes_elem.disabled = false
        currentSize_elem = drinkSizes_elem
    }
}

function set_food_visibility(type){
    foodChoice_elem.style.display = type
    toppings_elem.style.display = type
    foodSizes_elem.style.display = type
    if (type == 'none'){
        foodSizes_elem.disabled = true
    } else {
        foodSizes_elem.disabled = false
        currentSize_elem = drinkSizes_elem
    }
}

function set_ic_visibility(type){
    ic_flavors_elem.style.display = type
    additionals_elem.style.display = type
    iceCreamSizes_elem.style.display = type
    if (type == 'none'){
        iceCreamSizes_elem.disabled = true
    } else {
        iceCreamSizes_elem.disabled = false
        currentSize_elem = drinkSizes_elem
    }
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





