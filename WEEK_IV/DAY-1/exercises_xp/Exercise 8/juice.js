// Part II version with nested functions and ingredient accumulation
function makeJuice(size) {
    const ingredients = [];

    function addIngredients(ing1, ing2, ing3) {
        ingredients.push(ing1, ing2, ing3);
    }

    function displayJuice() {
        const outputDiv = document.getElementById('juiceOutput');
        outputDiv.textContent = `The client wants a ${size} juice, containing ${ingredients.join(', ')}.`;
    }

    // Add ingredients twice
    addIngredients('apple', 'banana', 'orange');
    addIngredients('strawberry', 'kiwi', 'mango');

    // Display the final juice
    displayJuice();
}

// Invoke the outer function
makeJuice('large');
