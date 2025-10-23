// ==========================
// EXERCISE 4 - OMNIPRESENT VALUE
// ==========================
function isOmnipresent(arr, val) {
    return arr.every(subArr => subArr.includes(val));
}

// Test cases
console.log(isOmnipresent([[1, 1], [1, 3], [5, 1], [6, 1]], 1)); // true
console.log(isOmnipresent([[1, 1], [1, 3], [5, 1], [6, 1]], 6)); // false
