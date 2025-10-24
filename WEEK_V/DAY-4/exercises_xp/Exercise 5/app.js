// app.js

const _ = require('lodash'); // Lodash library
const math = require('./math'); // Custom math module

// Using math module functions
const sum = math.add(5, 10);          // 5 + 10 = 15
const product = math.multiply(5, 10); // 5 * 10 = 50

console.log('Sum:', sum);
console.log('Product:', product);

// Using lodash utility functions
const numbers = [1, 2, 3, 4, 5, 6];
const shuffled = _.shuffle(numbers); // shuffle the array
const maxNumber = _.max(numbers);    // find the max number
const minNumber = _.min(numbers);    // find the min number

console.log('Original array:', numbers);
console.log('Shuffled array:', shuffled);
console.log('Max number:', maxNumber);
console.log('Min number:', minNumber);

// Combining math module and lodash
const doubled = _.map(numbers, n => math.multiply(n, 2));
console.log('Doubled numbers using math.multiply:', doubled);
