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
