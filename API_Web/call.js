
export async function getItem(type='') {

    let link = 'http://127.0.0.1:5000/items'

    if (type != ''){
        link += '/' + type
    }

    try {
        const response = await fetch(link, {
        method: 'GET', // or 'POST', 'PUT', 'DELETE'
        headers: {
            'Content-Type': 'application/json',
            // Add any other headers as needed
        },
        // If it is a POST/PUT request, add body
        // body: JSON.stringify({ key: 'value' }),
        });

        if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();
        console.log(data);
        return data;
    } catch (error) {
        console.error('Error fetching data:', error);
        throw error;
    }
}

export async function postItem(formData, asFormData=false) {

    let link = 'http://127.0.0.1:5000/item'

    var object = {};
    formData.forEach((value, key) => {
        // Reflect.has in favor of: object.hasOwnProperty(key)
        if(!Reflect.has(object, key)){
            object[key] = value;
            return;
        }
        if(!Array.isArray(object[key])){
            object[key] = [object[key]];    
        }
        object[key].push(value);
    });
    var json = JSON.stringify(object);



    let jsonData = JSON.stringify(formData)

    try {
        const response = await fetch(link, {
        method: 'POST', // or 'POST', 'PUT', 'DELETE'
        headers: {
            'Content-Type': 'application/json',
            // Add any other headers as needed
        },
        body: json,
        // If it is a POST/PUT request, add body
        // body: JSON.stringify({ key: 'value' }),
        });

        if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();
        console.log(data);
        return data;
    } catch (error) {
        console.error('Error fetching data:', error);
        throw error;
    }
}





