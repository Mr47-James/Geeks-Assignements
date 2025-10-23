// =============================
// EXERCISE 3 - IS PALINDROME?
// =============================

function isPalindrome(str) {
    // Remove spaces and convert to lowercase for consistent comparison
    str = str.toLowerCase().replace(/\s+/g, '');

    // Reverse the string
    let reversed = '';
    for (let i = str.length - 1; i >= 0; i--) {
        reversed += str[i];
    }

    // Check if the original and reversed strings are equal
    return str === reversed;
}

// Examples
console.log(isPalindrome("madam"));   // ➞ true
console.log(isPalindrome("kayak"));   // ➞ true
console.log(isPalindrome("bob"));     // ➞ true
console.log(isPalindrome("hello"));   // ➞ false
console.log(isPalindrome("race car")); // ➞ true
