// ==========================
// COLORS ARRAY
// ==========================
const colors = ["blue", "red", "green", "yellow", "purple"];

// Loop and log with numbers
for (let i = 0; i < colors.length; i++) {
    console.log(`My #${i + 1} choice is ${colors[i]}`);
}

// Bonus: correct suffixes
const suffixes = ["st", "nd", "rd", "th", "th"];

for (let i = 0; i < colors.length; i++) {
    console.log(`My ${i + 1}${suffixes[i]} choice is ${colors[i]}`);
}
