// ==========================
// EXERCISE 1 - RANDOM NUMBER
// ==========================

// Generate a random number between 1 and 100
let randomNumber = Math.floor(Math.random() * 100) + 1;
console.log("Random number:", randomNumber);

// Log all even numbers from 0 to the random number
for (let i = 0; i <= randomNumber; i++) {
    if (i % 2 === 0) {
        console.log(i);
    }
}

---
---

// =============================
// EXERCISE 2 - CAPITALIZED LETTERS
// =============================

function capitalize(str) {
    let evenCaps = "";
    let oddCaps = "";

    for (let i = 0; i < str.length; i++) {
        if (i % 2 === 0) {
            evenCaps += str[i].toUpperCase();
            oddCaps += str[i];
        } else {
            evenCaps += str[i];
            oddCaps += str[i].toUpperCase();
        }
    }

    return [evenCaps, oddCaps];
}

// Example
console.log(capitalize("abcdef")); // ➞ ['AbCdEf', 'aBcDeF']

---
---

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

---
---

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

---
---

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

---
---

// =============================
// EXERCISE 6 - CALENDAR
// =============================

function createCalendar(year, month) {
    // Month in JS Date is 0-indexed (0=Jan, 1=Feb,...)
    const firstDay = new Date(year, month - 1, 1);
    const lastDay = new Date(year, month, 0); // last day of the month
    const totalDays = lastDay.getDate();

    // Weekday names starting with Monday
    const weekdays = ['MO', 'TU', 'WE', 'TH', 'FR', 'SA', 'SU'];

    // Create table
    const table = document.createElement('table');
    table.border = '1';
    table.style.borderCollapse = 'collapse';

    // Create table header
    const thead = document.createElement('thead');
    const headerRow = document.createElement('tr');
    weekdays.forEach(day => {
        const th = document.createElement('th');
        th.textContent = day;
        th.style.padding = '5px';
        headerRow.appendChild(th);
    });
    thead.appendChild(headerRow);
    table.appendChild(thead);

    // Create table body
    const tbody = document.createElement('tbody');
    let row = document.createElement('tr');

    // JS getDay(): Sunday=0, Monday=1,... Saturday=6
    // Adjust so that Monday=0,...Sunday=6
    let startDay = firstDay.getDay() - 1;
    if (startDay === -1) startDay = 6; // Sunday adjustment

    // Fill initial empty cells
    for (let i = 0; i < startDay; i++) {
        const emptyCell = document.createElement('td');
        row.appendChild(emptyCell);
    }

    // Fill days
    for (let day = 1; day <= totalDays; day++) {
        const td = document.createElement('td');
        td.textContent = day;
        td.style.padding = '5px';
        row.appendChild(td);

        // Check if end of week
        if ((row.children.length) % 7 === 0) {
            tbody.appendChild(row);
            row = document.createElement('tr');
        }
    }

    // Append remaining cells if any
    if (row.children.length > 0) {
        tbody.appendChild(row);
    }

    table.appendChild(tbody);

    // Append table to body
    document.body.appendChild(table);
}

// Example usage
createCalendar(2012, 9);
