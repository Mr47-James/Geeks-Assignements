// ==========================
// EXERCISE 1 - IS_BLANK
// ==========================
function isBlank(str) {
    return str === "";
}

// Test cases
console.log(isBlank(''));     // true
console.log(isBlank('abc'));  // false

---
---
// ==========================
// EXERCISE 2 - ABBREV_NAME
// ==========================
function abbrevName(name) {
    const parts = name.split(" ");
    if (parts.length < 2) return name;
    return `${parts[0]} ${parts[1][0]}.`;
}

// Test case
console.log(abbrevName("Robin Singh")); // "Robin S."

---
---
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

---
---
// ==========================
// EXERCISE 4 - OMNIPRESENT VALUE
// ==========================
function isOmnipresent(arr, val) {
    return arr.every(subArr => subArr.includes(val));
}

// Test cases
console.log(isOmnipresent([[1, 1], [1, 3], [5, 1], [6, 1]], 1)); // true
console.log(isOmnipresent([[1, 1], [1, 3], [5, 1], [6, 1]], 6)); // false

---
---

// ==========================
// EXERCISE 5 - RED TABLE DIAGONAL
// ==========================
let table = document.body.querySelector("table");

for (let i = 0; i < table.rows.length; i++) {
    table.rows[i].cells[i].style.backgroundColor = "red";
}
