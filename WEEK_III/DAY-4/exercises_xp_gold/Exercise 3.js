// Reference to the root div
const root = document.getElementById("root");

// Shopping list array
let shoppingList = [];

// Create form
const form = document.createElement("form");

// Create input field
const input = document.createElement("input");
input.type = "text";
input.placeholder = "Enter item";
form.appendChild(input);

// Create AddItem button
const addBtn = document.createElement("button");
addBtn.type = "button";
addBtn.textContent = "AddItem";
form.appendChild(addBtn);

// Create ClearAll button
const clearBtn = document.createElement("button");
clearBtn.type = "button";
clearBtn.textContent = "ClearAll";
form.appendChild(clearBtn);

// Append form to root
root.appendChild(form);

// Create ul to display items
const ul = document.createElement("ul");
root.appendChild(ul);

// Function to render shopping list
function renderList() {
    ul.innerHTML = ""; // Clear previous items
    shoppingList.forEach(item => {
        const li = document.createElement("li");
        li.textContent = item;
        ul.appendChild(li);
    });
}

// Function to add item
function addItem() {
    const value = input.value.trim();
    if (value) {
        shoppingList.push(value);
        input.value = "";
        renderList();
    }
}

// Function to clear all items
function clearAll() {
    shoppingList = [];
    renderList();
}

// Event listeners
addBtn.addEventListener("click", addItem);
clearBtn.addEventListener("click", clearAll);
