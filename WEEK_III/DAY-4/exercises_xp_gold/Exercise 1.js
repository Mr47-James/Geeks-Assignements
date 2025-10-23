// Get the select element
const select = document.getElementById("genres");

// Display the currently selected value
console.log(select.value);

// Create a new option
const newOption = document.createElement("option");
newOption.value = "classic";
newOption.textContent = "Classic";
newOption.selected = true;

// Append the new option to the select
select.appendChild(newOption);

// Display the updated selected value
console.log(select.value);
