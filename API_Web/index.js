

selectType_elem = undefined

// Drink
base_elem = undefined
flavors_elem = undefined

// Food
foodChoice_elem = undefined
toppings_elem = undefined

class_elem = undefined

current_type = undefined


window.onload = () => {
    selectType_elem = document.getElementById('select_type')

    base_elem = document.getElementById('base')
    flavors_elem = document.getElementById('flavors_body')

    foodChoice_elem = document.getElementById('food_choice')
    toppings_elem = document.getElementById('toppings_body')

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
        flavors_elem.style.display = 'none'
        base_elem.style.display = 'none'
        foodChoice_elem.style.display = ''
        toppings_elem.style.display = ''
    }
    else if(type == "Drink"){
        flavors_elem.style.display = ''
        base_elem.style.display = ''
        foodChoice_elem.style.display = 'none'
        toppings_elem.style.display = 'none'
    }
    class_elem.value = type
}





