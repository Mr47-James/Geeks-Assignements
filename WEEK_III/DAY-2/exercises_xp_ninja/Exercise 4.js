// =============================
// EXERCISE 4 - BIGGEST NUMBER
// =============================

function biggestNumberInArray(arrayNumber) {
    // If the array is empty, return 0
    if (arrayNumber.length === 0) return 0;

    // Initialize max number to the smallest possible value
    let max = Number.NEGATIVE_INFINITY;

    // Loop through each element in the array
    for (let i = 0; i < arrayNumber.length; i++) {
        // Check if the current value is a number
        if (typeof arrayNumber[i] === 'number' && !isNaN(arrayNumber[i])) {
            if (arrayNumber[i] > max) {
                max = arrayNumber[i];
            }
        }
    }

    // If no number was found, return 0
    return max === Number.NEGATIVE_INFINITY ? 0 : max;
}

// Examples
const array = [-1, 0, 3, 100, 99, 2, 99];
const array2 = ['a', 3, 4, 2];
const array3 = [];

console.log(biggestNumberInArray(array));  // ➞ 100
console.log(biggestNumberInArray(array2)); // ➞ 4
console.log(biggestNumberInArray(array3)); // ➞ 0
