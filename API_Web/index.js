
selectType_elem = undefined

// Drink
base_elem = undefined
flavors_elem = undefined

// Food
foodChoice_elem = undefined
toppings_elem = undefined

// Ice Cream
ic_flavors_elem = undefined
additionals_elem = undefined
all_ic_flavors = [''] 

class_elem = undefined

current_type = undefined

window.onload = () => {
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

    ic_flavors_elem

    class_elem = document.getElementById('class')

    selectType_elem.onchange = (e) => {
        current_type = e.target.value
        set_type(current_type)
    }    
    current_type = selectType_elem.value
    set_type(current_type)

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




