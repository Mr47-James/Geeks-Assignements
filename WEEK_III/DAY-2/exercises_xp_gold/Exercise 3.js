// ==========================
// EXERCISE 3 - SWAPCASE
// ==========================
function swapCase(str) {
    let result = "";
    for (let char of str) {
        if (char === char.toUpperCase()) {
            result += char.toLowerCase();
        } else {
            result += char.toUpperCase();
        }
    }
    return result;
}

// Test case
console.log(swapCase('The Quick Brown Fox')); // 'tHE qUICK bROWN fOX'
