// ==========================
// EXERCISE 3 - REPEAT THE QUESTION
// ==========================

// Prompt the user for a number
let userInput = Number(prompt("Enter a number:"));

// Keep asking while the number is smaller than 10
while (userInput < 10) {
    userInput = Number(prompt("The number is smaller than 10. Enter a new number:"));
}

console.log("You entered:", userInput);
