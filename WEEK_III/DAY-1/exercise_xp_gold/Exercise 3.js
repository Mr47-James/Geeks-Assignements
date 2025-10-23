// ==========================
// EXERCISE 3 - PLAYING WITH NUMBERS
// ==========================
let age = [20, 5, 12, 43, 98, 55];

// 1. Sum of all numbers
let sum = 0;
for (let i = 0; i < age.length; i++) {
    sum += age[i];
}
console.log("Sum of ages:", sum);

// 2. Highest age
let maxAge = age[0];
for (let i = 1; i < age.length; i++) {
    if (age[i] > maxAge) {
        maxAge = age[i];
    }
}
console.log("Highest age:", maxAge);
