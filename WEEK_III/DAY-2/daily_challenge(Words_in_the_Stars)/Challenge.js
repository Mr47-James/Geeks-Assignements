// Prompt user for words separated by commas
const input = prompt("Enter several words, separated by commas:");

// Convert input into an array, trimming extra spaces
const words = input.split(",").map(word => word.trim());

// Find the length of the longest word
const maxLength = words.reduce((max, word) => Math.max(max, word.length), 0);

// Create top and bottom borders
const border = "*".repeat(maxLength + 4);

console.log(border);

// Display each word with padding
words.forEach(word => {
    const padding = " ".repeat(maxLength - word.length);
    console.log(`* ${word}${padding} *`);
});

console.log(border);
