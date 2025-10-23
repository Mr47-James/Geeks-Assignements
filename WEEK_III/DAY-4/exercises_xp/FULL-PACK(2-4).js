// 1. Retrieve the form and console.log it
const form = document.querySelector('form');
console.log(form);

// 2. Retrieve inputs by their ID and console.log them
const firstNameInput = document.getElementById('fname');
const lastNameInput = document.getElementById('lname');
console.log(firstNameInput, lastNameInput);

// 3. Retrieve inputs by their name attribute and console.log them
const firstNameByName = document.querySelector('input[name="firstname"]');
const lastNameByName = document.querySelector('input[name="lastname"]');
console.log(firstNameByName, lastNameByName);

// 4. Handle form submission
form.addEventListener('submit', function(event) {
    event.preventDefault(); // prevents page reload

    const firstName = firstNameInput.value.trim();
    const last


---
---

// Global variable to store all bold items
let allBoldItems;

// Function to collect all bold elements inside the paragraph
function getBoldItems() {
    allBoldItems = document.querySelectorAll('p strong');
}

// Function to highlight all bold elements (change color to blue)
function highlight() {
    allBoldItems.forEach(item => item.style.color = 'blue');
}

// Function to return all bold elements to default color (black)
function returnItemsToDefault() {
    allBoldItems.forEach(item => item.style.color = 'black');
}

// Call getBoldItems to initialize the allBoldItems variable
getBoldItems();

// Get the paragraph
const paragraph = document.querySelector('p');

// Add event listeners for mouseover and mouseout
paragraph.addEventListener('mouseover', highlight);
paragraph.addEventListener('mouseout', returnItemsToDefault);

---
---

// Select the form
const form = document.getElementById('MyForm');

// Add submit event listener
form.addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent form from submitting/reloading the page

    // Get the radius value from the input
    const radiusInput = document.getElementById('radius');
    const radius = parseFloat(radiusInput.value);

    if (isNaN(radius) || radius <= 0) {
        alert("Please enter a valid positive number for the radius.");
        return;
    }

    // Calculate the volume of the sphere: (4/3) * π * r^3
    const volume = (4/3) * Math.PI * Math.pow(radius, 3);

    // Display the volume in the 'volume' input field
    document.getElementById('volume').value = volume.toFixed(2);
});


 
