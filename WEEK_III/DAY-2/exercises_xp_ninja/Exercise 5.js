// =============================
// EXERCISE 5 - UNIQUE ELEMENTS
// =============================

function getUniqueElements(arr) {
    // Using a Set automatically removes duplicates
    return [...new Set(arr)];
}

// Example usage:
const list = [1, 2, 3, 3, 3, 3, 4, 5];
const newList = getUniqueElements(list);

console.log(newList); // ➞ [1, 2, 3, 4, 5]
