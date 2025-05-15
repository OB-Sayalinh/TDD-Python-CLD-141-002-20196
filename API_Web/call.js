
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

export async function postItem(data) {

    let link = 'http://127.0.0.1:5000/item'

    try {
        const response = await fetch(link, {
        method: 'POST', // or 'POST', 'PUT', 'DELETE'
        headers: {
            'Content-Type': 'application/json',
            // Add any other headers as needed
        },
        body: data,
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





