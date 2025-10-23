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
