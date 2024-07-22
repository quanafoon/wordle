// Define the API URL
const apiUrl = 'https://wordle-hwug.onrender.com';

// Function to get user data from the API
async function getUserData() {
    const response = await fetch(`${apiUrl}users`);
    if (!response.ok) {
        throw new Error('Network response was not ok');
    }
    return response.json();
}

// Function to load user data into the table
function loadTable(users) {
    const table = document.querySelector('#result');
    table.innerHTML = ''; // Clear any existing data
    for (let user of users) {
        table.innerHTML += `<tr>
            <td>${user.id}</td>
            <td>${user.username}</td>
        </tr>`;
    }
}

// Main function to initialize the page
async function main() {
    try {
        const users = await getUserData();
        loadTable(users);
    } catch (error) {
        console.error('Error fetching user data:', error);
    }
}

// Run the main function
main();