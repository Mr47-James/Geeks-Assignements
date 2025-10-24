// ------1------
const fruits = ["apple", "orange"];
const vegetables = ["carrot", "potato"];

const result = ['bread', ...vegetables, 'chicken', ...fruits];
console.log(result);
// Expected output:
// ['bread', 'carrot', 'potato', 'chicken', 'apple', 'orange']
// Explanation: The spread operator (...) expands the arrays into individual elements.

// ------2------
const country = "USA";
console.log([...country]);
// Expected output:
// ['U', 'S', 'A']
// Explanation: The spread operator spreads the string into individual characters.

// ------Bonus------
let newArray = [...[,,]];
console.log(newArray);
// Expected output:
// [undefined, undefined]
// Explanation: The spread operator expands an array with two empty slots into two undefined elements.
