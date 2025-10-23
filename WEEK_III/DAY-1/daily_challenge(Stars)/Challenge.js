// ==========================
// EXERCISE - PATTERN
// ==========================

// Pattern example (assuming a triangle of asterisks):
// *
// **
// ***
// ****
// *****

const rows = 5;

// --------------------------
// 1. Using one loop
// --------------------------
let pattern = "";
for (let i = 1; i <= rows; i++) {
    pattern += "*".repeat(i) + "\n";
}
console.log("Pattern using one loop:\n" + pattern);

// --------------------------
// 2. Using nested loops
// --------------------------
console.log("Pattern using nested loops:");
for (let i = 1; i <= rows; i++) {
    let line = "";
    for (let j = 1; j <= i; j++) {
        line += "*";
    }
    console.log(line);
}
